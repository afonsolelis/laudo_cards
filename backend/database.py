import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "laudo_cards")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
cards_collection = db.get_collection("cards")
graders_collection = db.get_collection("graders")
users_collection = db.get_collection("users")
sessions_collection = db.get_collection("sessions")
