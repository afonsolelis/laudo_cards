from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
from bson import ObjectId
import uuid
import json
import os

from models import CardModel, GraderModel
from database import cards_collection, graders_collection
from storage import upload_file_to_minio

app = FastAPI(title="Laudo Cards")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

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
    if grade >= 9: return 'bg-success'
    if grade >= 8: return 'bg-warning text-dark'
    return 'bg-secondary'

templates.env.globals['get_grade_badge_color'] = get_grade_badge_color

# HTML Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Buscar todas as cartas para listar na home
    cards_cursor = cards_collection.find()
    cards_list = await cards_cursor.to_list(1000)
    
    graders = await cards_collection.distinct("grading_company")
    
    return templates.TemplateResponse(
        request=request, name="index.html", context={"cards": cards_list, "graders": graders}
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
async def admin_page(request: Request):
    managed_graders = await graders_collection.find().to_list(100)
    return templates.TemplateResponse(
        request=request, name="admin.html", context={"graders": managed_graders}
    )

# API Routes
@app.get("/api/graders", response_model=List[GraderModel])
async def list_graders():
    graders = await graders_collection.find().to_list(100)
    return graders

@app.post("/api/graders", response_model=GraderModel)
async def create_grader(grader: GraderModel):
    new_grader = await graders_collection.insert_one(grader.model_dump(by_alias=True, exclude=["id"]))
    created_grader = await graders_collection.find_one({"_id": new_grader.inserted_id})
    return created_grader

@app.delete("/api/graders/{grader_id}")
async def delete_grader(grader_id: str):
    if not ObjectId.is_valid(grader_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await graders_collection.delete_one({"_id": ObjectId(grader_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Grader not found")
    return {"message": "Deleted successfully"}
@app.post("/api/cards", response_model=CardModel)
async def create_card(card: CardModel):
    new_card = await cards_collection.insert_one(card.model_dump(by_alias=True, exclude=["id"]))
    created_card = await cards_collection.find_one({"_id": new_card.inserted_id})
    return created_card

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    
    url = await upload_file_to_minio(file, filename)
    if not url:
        raise HTTPException(status_code=500, detail="Failed to upload image")
    
    return {"url": url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
