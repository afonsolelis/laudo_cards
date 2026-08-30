#!/usr/bin/env python3
"""Validate and create Laudo Cards documents without exposing database secrets."""

from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_ENV_FILE = REPO_ROOT / ".env"

TOP_LEVEL_FIELDS = {
    "name",
    "number",
    "full_name",
    "set_name",
    "year",
    "rarity",
    "pokemon_type",
    "language",
    "illustrator_name",
    "acquisition_price",
    "added_date",
    "available_for_trade",
    "grading_company",
    "certificate_number",
    "grading_year",
    "cert_link",
    "image_front_url",
    "image_back_url",
    "grade",
    "links",
    "history_markdown",
    "grader_notes_markdown",
    "card_history",
}
GRADE_FIELDS = {"centering", "corners", "edges", "surface", "final", "description"}
LINK_FIELDS = {"tcg_player", "price_charting", "liga_pokemon", "myp_cards", "ebay"}
REQUIRED_STRINGS = {
    "name",
    "number",
    "full_name",
    "set_name",
    "rarity",
    "pokemon_type",
    "language",
    "illustrator_name",
    "grading_company",
    "certificate_number",
}
URL_FIELDS = {"cert_link", "image_front_url", "image_back_url"}


class CardAdminError(Exception):
    """Expected input, configuration, or integrity error."""


def load_payload(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CardAdminError(f"input file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CardAdminError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}"
        ) from exc
    if not isinstance(data, dict):
        raise CardAdminError("the JSON root must be an object")
    return data


def reject_unknown_fields(payload: dict[str, Any]) -> None:
    unknown = sorted(set(payload) - TOP_LEVEL_FIELDS)
    if unknown:
        raise CardAdminError(f"unknown top-level fields: {', '.join(unknown)}")

    grade = payload.get("grade")
    if not isinstance(grade, dict):
        raise CardAdminError("grade must be an object")
    unknown_grade = sorted(set(grade) - GRADE_FIELDS)
    if unknown_grade:
        raise CardAdminError(f"unknown grade fields: {', '.join(unknown_grade)}")

    links = payload.get("links")
    if not isinstance(links, dict):
        raise CardAdminError("links must be an object; use {} when empty")
    unknown_links = sorted(set(links) - LINK_FIELDS)
    if unknown_links:
        raise CardAdminError(f"unknown link fields: {', '.join(unknown_links)}")


def validate_values(payload: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_STRINGS - set(payload))
    if missing:
        raise CardAdminError(f"missing required fields: {', '.join(missing)}")
    for field in REQUIRED_STRINGS:
        value = payload[field]
        if not isinstance(value, str) or not value.strip():
            raise CardAdminError(f"{field} must be a non-empty string")

    for field in ("year", "grading_year"):
        value = payload.get(field)
        if not isinstance(value, int) or isinstance(value, bool):
            raise CardAdminError(f"{field} must be an integer")

    grade = payload["grade"]
    for required in ("final", "description"):
        if required not in grade:
            raise CardAdminError(f"grade.{required} is required")
    if not isinstance(grade["description"], str) or not grade["description"].strip():
        raise CardAdminError("grade.description must be a non-empty string")
    for field in ("centering", "corners", "edges", "surface", "final"):
        value = grade.get(field)
        if value is None and field != "final":
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise CardAdminError(f"grade.{field} must be numeric")
        if not 1 <= float(value) <= 10:
            raise CardAdminError(f"grade.{field} must be between 1 and 10")

    price = payload.get("acquisition_price")
    if price is not None:
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise CardAdminError("acquisition_price must be a non-negative number")

    added_date = payload.get("added_date")
    if added_date:
        try:
            date.fromisoformat(added_date)
        except (TypeError, ValueError) as exc:
            raise CardAdminError("added_date must use YYYY-MM-DD") from exc

    for field in URL_FIELDS:
        validate_url(field, payload.get(field))
    for field, value in payload["links"].items():
        validate_url(f"links.{field}", value)


def validate_url(field: str, value: Any) -> None:
    if value is None:
        return
    if not isinstance(value, str) or not value.strip():
        raise CardAdminError(f"{field} must be a URL or null")
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise CardAdminError(f"{field} must be an absolute HTTP(S) URL")


def validate_model(payload: dict[str, Any]):
    reject_unknown_fields(payload)
    validate_values(payload)
    sys.path.insert(0, str(REPO_ROOT / "backend"))
    try:
        from models import CardModel
        from pydantic import ValidationError
    except ImportError as exc:
        raise CardAdminError(
            "project dependencies are unavailable; run with "
            "uv run --with-requirements backend/requirements.txt"
        ) from exc
    try:
        return CardModel.model_validate(payload)
    except ValidationError as exc:
        raise CardAdminError(f"CardModel validation failed: {exc}") from exc


def load_environment(env_file: Path) -> None:
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise CardAdminError("python-dotenv is unavailable") from exc
    load_dotenv(env_file, override=False)
    if not os.getenv("MONGO_URL"):
        raise CardAdminError(f"MONGO_URL is missing from the environment or {env_file}")


def connect_database(env_file: Path):
    load_environment(env_file)
    try:
        from pymongo import MongoClient
    except ImportError as exc:
        raise CardAdminError("pymongo is unavailable") from exc

    client = MongoClient(os.environ["MONGO_URL"], serverSelectionTimeoutMS=10_000)
    try:
        client.admin.command("ping")
    except Exception as exc:
        client.close()
        raise CardAdminError(
            "database connection failed "
            f"({type(exc).__name__}); credentials were not printed"
        ) from exc
    database = client[os.getenv("DB_NAME", "laudo_cards")]
    return client, database


def integrity_check(database, model) -> None:
    grader = model.grading_company.strip()
    certificate = model.certificate_number.strip()
    if database.graders.find_one({"name": grader}) is None:
        accepted = sorted(doc["name"] for doc in database.graders.find({}, {"name": 1}))
        suffix = f" Accepted values: {', '.join(accepted)}" if accepted else ""
        raise CardAdminError(f"grading company is not registered: {grader}.{suffix}")

    duplicate = database.cards.find_one(
        {"grading_company": grader, "certificate_number": certificate},
        {"_id": 1, "name": 1},
    )
    if duplicate:
        raise CardAdminError(
            "duplicate card found: "
            f"id={duplicate['_id']} name={duplicate.get('name', 'unknown')}"
        )


def upload_image(path: Path) -> tuple[str, str]:
    if not path.is_file():
        raise CardAdminError(f"image file not found: {path}")
    required = (
        "CLOUDINARY_CLOUD_NAME",
        "CLOUDINARY_API_KEY",
        "CLOUDINARY_API_SECRET",
    )
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise CardAdminError(f"missing Cloudinary settings: {', '.join(missing)}")
    try:
        import cloudinary
        import cloudinary.uploader
    except ImportError as exc:
        raise CardAdminError("cloudinary is unavailable") from exc

    cloudinary.config(
        cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
        api_key=os.environ["CLOUDINARY_API_KEY"],
        api_secret=os.environ["CLOUDINARY_API_SECRET"],
        secure=True,
    )
    public_id = uuid.uuid4().hex
    try:
        result = cloudinary.uploader.upload(
            str(path),
            folder=os.getenv("CLOUDINARY_FOLDER", "laudo_cards"),
            public_id=public_id,
            resource_type="image",
            overwrite=True,
        )
    except Exception as exc:
        raise CardAdminError(f"image upload failed ({type(exc).__name__})") from exc
    secure_url = result.get("secure_url")
    uploaded_public_id = result.get("public_id")
    if not secure_url or not uploaded_public_id:
        raise CardAdminError("Cloudinary did not return secure_url and public_id")
    return secure_url, uploaded_public_id


def cleanup_uploads(public_ids: list[str]) -> None:
    if not public_ids:
        return
    try:
        import cloudinary.uploader

        for public_id in public_ids:
            cloudinary.uploader.destroy(
                public_id, resource_type="image", invalidate=True
            )
    except Exception:
        print(
            "warning: automatic Cloudinary cleanup failed; inspect recent uploads",
            file=sys.stderr,
        )


def command_list_graders(args: argparse.Namespace) -> None:
    client, database = connect_database(args.env_file)
    try:
        names = sorted(doc["name"] for doc in database.graders.find({}, {"name": 1}))
    except Exception as exc:
        raise CardAdminError(f"database read failed ({type(exc).__name__})") from exc
    finally:
        client.close()
    print(json.dumps({"graders": names}, ensure_ascii=False, indent=2))


def command_preflight(args: argparse.Namespace) -> None:
    payload = load_payload(args.input)
    model = validate_model(payload)
    client, database = connect_database(args.env_file)
    try:
        integrity_check(database, model)
    except CardAdminError:
        raise
    except Exception as exc:
        raise CardAdminError(f"database read failed ({type(exc).__name__})") from exc
    finally:
        client.close()
    print(
        json.dumps(
            {
                "status": "ready",
                "name": model.name,
                "grading_company": model.grading_company,
                "certificate_number": model.certificate_number,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def command_create(args: argparse.Namespace) -> None:
    payload = load_payload(args.input)
    model = validate_model(payload)
    client, database = connect_database(args.env_file)
    uploaded_ids: list[str] = []
    try:
        integrity_check(database, model)
        image_sources = (
            ("image_front_url", args.front_image),
            ("image_back_url", args.back_image),
        )
        for field, local_path in image_sources:
            if payload.get(field) and local_path:
                raise CardAdminError(
                    f"provide either {field} or its image file, not both"
                )
            if local_path:
                url, public_id = upload_image(local_path)
                payload[field] = url
                uploaded_ids.append(public_id)
            if not payload.get(field) and not args.allow_missing_images:
                raise CardAdminError(f"{field} or its local image file is required")

        model = validate_model(payload)
        document = model.model_dump(by_alias=True, exclude={"id"})
        if not document.get("added_date"):
            document["added_date"] = date.today().isoformat()

        result = database.cards.insert_one(document)
        created = database.cards.find_one(
            {"_id": result.inserted_id},
            {"name": 1, "grading_company": 1, "certificate_number": 1},
        )
        if created is None:
            rollback = database.cards.delete_one({"_id": result.inserted_id})
            if rollback.deleted_count != 1:
                uploaded_ids.clear()
                raise CardAdminError(
                    "read-back verification failed and database state is ambiguous; "
                    f"inspect card id={result.inserted_id} before retrying"
                )
            raise CardAdminError(
                "read-back verification failed; insertion was rolled back"
            )
    except CardAdminError:
        cleanup_uploads(uploaded_ids)
        raise
    except Exception as exc:
        cleanup_uploads(uploaded_ids)
        raise CardAdminError(f"database write failed ({type(exc).__name__})") from exc
    finally:
        client.close()

    card_id = str(created["_id"])
    print(
        json.dumps(
            {
                "status": "created",
                "id": card_id,
                "name": created["name"],
                "grading_company": created["grading_company"],
                "certificate_number": created["certificate_number"],
                "path": f"/laudo/{card_id}",
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--env-file",
        type=Path,
        default=DEFAULT_ENV_FILE,
        help="dotenv file (default: repository .env)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list-graders", help="list accepted graders")
    list_parser.set_defaults(handler=command_list_graders)

    preflight_parser = subparsers.add_parser(
        "preflight", help="validate schema, grader, and duplicate status"
    )
    preflight_parser.add_argument("--input", type=Path, required=True)
    preflight_parser.set_defaults(handler=command_preflight)

    create_parser = subparsers.add_parser(
        "create", help="upload images and create card"
    )
    create_parser.add_argument("--input", type=Path, required=True)
    create_parser.add_argument("--front-image", type=Path)
    create_parser.add_argument("--back-image", type=Path)
    create_parser.add_argument(
        "--allow-missing-images",
        action="store_true",
        help="allow an incomplete card only when the user explicitly requested it",
    )
    create_parser.set_defaults(handler=command_create)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        args.handler(args)
    except CardAdminError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
