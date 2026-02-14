from fastapi import APIRouter, HTTPException
from models import Appointment
from database import appointments_collection
from automation import (
    send_appointment_confirmation, 
    send_appointment_reminder,
    notify_staff_new_appointment
)
from datetime import datetime
from bson import ObjectId

router = APIRouter()

@router.post("/appointments")
async def create_appointment(appointment: Appointment):
    appointment_dict = appointment.dict()
    appointment_dict["created_at"] = datetime.now()
    
    result = await appointments_collection.insert_one(appointment_dict)
    
    # Trigger automations
    send_appointment_confirmation(appointment_dict)
    send_appointment_reminder(appointment_dict)
    notify_staff_new_appointment(appointment_dict)
    
    return {
        "success": True,
        "message": "Appointment booked successfully",
        "id": str(result.inserted_id),
        "automation": "Confirmation email sent"
    }

@router.get("/appointments")
async def get_appointments():
    appointments = []
    async for appointment in appointments_collection.find().sort("created_at", -1):
        appointment["_id"] = str(appointment["_id"])
        appointments.append(appointment)
    return {"appointments": appointments}

@router.get("/appointments/today")
async def get_today_appointments():
    from datetime import date
    today = date.today().isoformat()
    
    appointments = []
    async for appointment in appointments_collection.find({"date": today}):
        appointment["_id"] = str(appointment["_id"])
        appointments.append(appointment)
    return {"appointments": appointments}

@router.put("/appointments/{appointment_id}/complete")
async def complete_appointment(appointment_id: str):
    result = await appointments_collection.update_one(
        {"_id": ObjectId(appointment_id)},
        {"$set": {"status": "completed"}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, message="Appointment not found")
    
    return {"success": True, "message": "Appointment marked as completed"}

@router.put("/appointments/{appointment_id}/cancel")
async def cancel_appointment(appointment_id: str):
    result = await appointments_collection.update_one(
        {"_id": ObjectId(appointment_id)},
        {"$set": {"status": "cancelled"}}
    )
    return {"success": True, "message": "Appointment cancelled"}