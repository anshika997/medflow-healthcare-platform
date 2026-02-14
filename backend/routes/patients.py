from fastapi import APIRouter
from models import Patient
from database import patients_collection
from automation import send_welcome_message
from datetime import datetime

router = APIRouter()

@router.post("/patients")
async def create_patient_inquiry(patient: Patient):
    patient_dict = patient.dict()
    patient_dict["created_at"] = datetime.now()
    
    result = await patients_collection.insert_one(patient_dict)
    
    # Trigger automation
    send_welcome_message(patient_dict)
    
    return {
        "success": True,
        "message": "Message received successfully",
        "id": str(result.inserted_id),
        "automation": "Welcome email sent"
    }

@router.get("/patients")
async def get_patients():
    patients = []
    async for patient in patients_collection.find().sort("created_at", -1):
        patient["_id"] = str(patient["_id"])
        patients.append(patient)
    return {"patients": patients}

@router.put("/patients/{patient_id}/status")
async def update_patient_status(patient_id: str, status: str):
    from bson import ObjectId
    result = await patients_collection.update_one(
        {"_id": ObjectId(patient_id)},
        {"$set": {"status": status}}
    )
    return {"success": True, "message": "Status updated"}