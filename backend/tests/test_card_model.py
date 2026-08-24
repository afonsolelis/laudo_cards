import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import CardModel  # noqa: E402


def test_card_accepts_unavailable_online_certificate():
    card = CardModel(
        name="Eevee ex",
        number="167/131",
        full_name="Eevee ex - Evolucoes Prismaticas",
        set_name="Evolucoes Prismaticas",
        year=2025,
        rarity="Ilustracao Rara Especial",
        pokemon_type="Colorless (Incolor)",
        language="Portugues (Portuguese)",
        illustrator_name="tono",
        grading_company="CAPY",
        certificate_number="C001090",
        grading_year=2025,
        cert_link=None,
        grade={
            "centering": 9.5,
            "corners": 9.5,
            "edges": 9,
            "surface": 8.5,
            "final": 8.5,
            "description": "Near Mint to Mint+",
        },
        links={},
    )

    assert card.cert_link is None  # nosec
