from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
database = client.medflow_db

# Collections
appointments_collection = database.get_collection("appointments")
patients_collection = database.get_collection("patients")
inventory_collection = database.get_collection("inventory")
staff_collection = database.get_collection("staff")
settings_collection = database.get_collection("settings")