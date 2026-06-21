import json
import os
import uuid
from typing import List, Optional

import bcrypt
from bson import ObjectId
from database import (cards_collection, graders_collection,
                      sessions_collection, users_collection)
from fastapi import (Depends, FastAPI, File, Form, HTTPException, Request,
                     UploadFile)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import CardModel, GraderModel
from storage import upload_file_to_cloudinary

app = FastAPI(title="Laudo Cards")

# Mount static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount(
    "/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static"
)

# Templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# CORS (more relevant for API, but good to keep)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Helper para cor do badge de nota no Jinja
def get_grade_badge_color(grade: float) -> str:
    if grade >= 9:
        return "bg-success"
    if grade >= 8:
        return "bg-warning text-dark"
    return "bg-secondary"


templates.env.globals["get_grade_badge_color"] = get_grade_badge_color


# Evento de startup (Health Check + Seeding)
@app.on_event("startup")
async def startup_event():
    # 1. Health Check do MongoDB
    try:
        from database import client

        await client.admin.command("ping")
        print("INFO: Conexao com o MongoDB estabelecida com sucesso!")
    except Exception as e:
        print(f"CRITICAL ERROR: Nao foi possivel conectar ao MongoDB: {e}")
        raise e

    # 2. Auto-Seeding do usuario admin
    admin = await users_collection.find_one({"username": "afonsolelis"})
    if not admin:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw("080909".encode("utf-8"), salt)
        await users_collection.insert_one(
            {"username": "afonsolelis", "password_hash": hashed.decode("utf-8")}
        )
        print("INFO: Usuario administrador 'afonsolelis' criado com sucesso.")


# Autenticacao e Sessoes
class RedirectToLoginException(Exception):
    pass


@app.exception_handler(RedirectToLoginException)
async def redirect_to_login_handler(request: Request, exc: RedirectToLoginException):
    return RedirectResponse(url="/login", status_code=303)


async def get_current_user_optional(request: Request) -> Optional[dict]:
    session_id = request.cookies.get("session_id")
    if not session_id:
        return None
    session = await sessions_collection.find_one({"session_id": session_id})
    if not session:
        return None
    user = await users_collection.find_one({"username": session["username"]})
    return user


async def get_current_user(request: Request) -> dict:
    user = await get_current_user_optional(request)
    if not user:
        raise RedirectToLoginException()
    return user


async def get_current_user_api(request: Request) -> dict:
    user = await get_current_user_optional(request)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user


# Rotas de Autenticacao
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, error: Optional[str] = None):
    user = await get_current_user_optional(request)
    if user:
        return RedirectResponse(url="/admin", status_code=303)
    return templates.TemplateResponse(
        request=request, name="login.html", context={"error": error}
    )


@app.post("/login")
async def login_submit(
    request: Request, username: str = Form(...), password: str = Form(...)
):
    user = await users_collection.find_one({"username": username})
    if not user:
        return RedirectResponse(
            url="/login?error=Usuario ou senha incorretos", status_code=303
        )

    password_hash = user.get("password_hash")
    if not password_hash or not bcrypt.checkpw(
        password.encode("utf-8"), password_hash.encode("utf-8")
    ):
        return RedirectResponse(
            url="/login?error=Usuario ou senha incorretos", status_code=303
        )

    # Criar Sessao
    session_id = uuid.uuid4().hex
    await sessions_collection.insert_one(
        {"session_id": session_id, "username": username}
    )

    response = RedirectResponse(url="/admin", status_code=303)
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        max_age=30 * 24 * 60 * 60,  # 30 dias
        samesite="lax",
        secure=False,  # localhost amigavel
    )
    return response


@app.get("/logout")
async def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id:
        await sessions_collection.delete_one({"session_id": session_id})
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie(key="session_id")
    return response


# HTML Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Buscar todas as cartas para listar na home
    cards_cursor = cards_collection.find()
    cards_list = await cards_cursor.to_list(1000)

    graders = await graders_collection.find().to_list(100)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"cards": cards_list, "graders": graders},
    )


@app.get("/laudo/{card_id}", response_class=HTMLResponse)
async def view_laudo(request: Request, card_id: str):
    if not ObjectId.is_valid(card_id):
        raise HTTPException(status_code=400, detail="Invalid ID")

    card = await cards_collection.find_one({"_id": ObjectId(card_id)})
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    return templates.TemplateResponse(
        request=request, name="laudo.html", context={"card": card}
    )


@app.get("/admin", response_class=HTMLResponse)
async def admin_page(
    request: Request, edit_id: str = None, user: dict = Depends(get_current_user)
):
    # Retrieve managed graders
    managed_graders = await graders_collection.find().to_list(100)

    # Retrieve all cards to list in admin panel
    cards_cursor = cards_collection.find()
    cards_list = await cards_cursor.to_list(1000)
    for c in cards_list:
        c["_id"] = str(c["_id"])

    card = None
    if edit_id:
        try:
            card = await cards_collection.find_one({"_id": ObjectId(edit_id)})
            if card:
                card["_id"] = str(card["_id"])
        except Exception:
            pass  # nosec

    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"graders": managed_graders, "card": card, "cards": cards_list},
    )


# API Routes
@app.get("/api/graders", response_model=List[GraderModel])
async def list_graders():
    graders = await graders_collection.find().to_list(100)
    return graders


@app.post("/api/graders", response_model=GraderModel)
async def create_grader(
    grader: GraderModel, user: dict = Depends(get_current_user_api)
):
    new_grader = await graders_collection.insert_one(
        grader.model_dump(by_alias=True, exclude=["id"])
    )
    created_grader = await graders_collection.find_one({"_id": new_grader.inserted_id})
    return created_grader


@app.delete("/api/graders/{grader_id}")
async def delete_grader(grader_id: str, user: dict = Depends(get_current_user_api)):
    if not ObjectId.is_valid(grader_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await graders_collection.delete_one({"_id": ObjectId(grader_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Grader not found")
    return {"message": "Deleted successfully"}


@app.post("/api/cards", response_model=CardModel)
async def create_card(card: CardModel, user: dict = Depends(get_current_user_api)):
    new_card = await cards_collection.insert_one(
        card.model_dump(by_alias=True, exclude=["id"])
    )
    created_card = await cards_collection.find_one({"_id": new_card.inserted_id})
    return created_card


@app.put("/api/cards/{card_id}")
async def update_card(
    card_id: str, card: CardModel, user: dict = Depends(get_current_user_api)
):
    try:
        existing_card = await cards_collection.find_one({"_id": ObjectId(card_id)})
        if not existing_card:
            raise HTTPException(status_code=404, detail="Card not found")

        update_data = card.model_dump(by_alias=True, exclude=["id"])

        await cards_collection.update_one(
            {"_id": ObjectId(card_id)}, {"$set": update_data}
        )
        return {"message": "Card updated successfully", "card_id": card_id}
    except Exception as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/cards/{card_id}")
async def delete_card(card_id: str, user: dict = Depends(get_current_user_api)):
    if not ObjectId.is_valid(card_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await cards_collection.delete_one({"_id": ObjectId(card_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"message": "Card deleted successfully"}


@app.post("/api/upload")
async def upload_image(
    file: UploadFile = File(...), user: dict = Depends(get_current_user_api)
):
    url = await upload_file_to_cloudinary(file)
    if not url:
        raise HTTPException(status_code=500, detail="Failed to upload image")

    return {"url": url}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)  # nosec
