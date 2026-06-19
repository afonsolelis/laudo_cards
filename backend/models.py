from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type, _handler
    ):
        from pydantic_core import core_schema
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ])
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class GraderModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str

class CardGrade(BaseModel):
    centering: Optional[float] = None
    corners: Optional[float] = None
    edges: Optional[float] = None
    surface: Optional[float] = None
    final: float
    description: str # ex: Gem Mint

class CardLinks(BaseModel):
    tcg_player: Optional[str] = None
    price_charting: Optional[str] = None
    liga_pokemon: Optional[str] = None
    myp_cards: Optional[str] = None

class CardModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    number: str
    full_name: str
    set_name: str
    year: int
    rarity: str
    pokemon_type: str
    language: str
    illustrator_name: str
    
    # Graduação
    grading_company: str
    certificate_number: str
    grading_year: int
    cert_link: str
    
    # Imagens
    image_front_url: Optional[str] = None
    image_back_url: Optional[str] = None
    
    # Notas
    grade: CardGrade
    
    # Links
    links: CardLinks
    
    # Histórico (opcional, pode ser uma string grande de markdown ou lista)
    history_markdown: Optional[str] = None
    
    # Notas da Graduadora (opcional)
    grader_notes_markdown: Optional[str] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
