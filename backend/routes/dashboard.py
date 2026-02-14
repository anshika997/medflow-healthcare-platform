from fastapi import APIRouter
from database import (
    appointments_collection, 
    patients_collection, 
    inventory_collection,
    settings_collection
)
from datetime import datetime, date

router = APIRouter()

@router.get("/dashboard/stats")
async def get_dashboard_stats():
    # Today's appointments
    today = date.today().isoformat()
    today_appointments = await appointments_collection.count_documents({"date": today})
    
    # New patient inquiries
    new_patients = await patients_collection.count_documents({"status": "new"})
    
    # Pending appointments
    pending_appointments = await appointments_collection.count_documents({"status": "scheduled"})
    
    # Inventory alerts count
    alerts_count = 0
    async for item in inventory_collection.find():
        if item["quantity"] < item["min_threshold"]:
            alerts_count += 1
    
    # Total appointments this month
    current_month = datetime.now().strftime("%Y-%m")
    total_appointments = 0
    async for appt in appointments_collection.find():
        if appt["date"].startswith(current_month):
            total_appointments += 1
    
    return {
        "today_appointments": today_appointments,
        "new_patients": new_patients,
        "pending_appointments": pending_appointments,
        "inventory_alerts": alerts_count,
        "total_appointments_month": total_appointments
    }

@router.get("/dashboard/recent-activity")
async def get_recent_activity():
    activities = []
    
    # Recent appointments
    async for appt in appointments_collection.find().sort("created_at", -1).limit(5):
        activities.append({
            "type": "appointment",
            "message": f"New appointment: {appt['patient_name']} - {appt['appointment_type']}",
            "time": appt.get("created_at", datetime.now()).isoformat()
        })
    
    # Recent patient inquiries
    async for patient in patients_collection.find().sort("created_at", -1).limit(3):
        activities.append({
            "type": "inquiry",
            "message": f"New inquiry from {patient['name']}",
            "time": patient.get("created_at", datetime.now()).isoformat()
        })
    
    return {"activities": sorted(activities, key=lambda x: x["time"], reverse=True)[:10]}

@router.post("/setup")
async def setup_clinic(settings: dict):
    # Check if setup already exists
    existing = await settings_collection.find_one({"type": "clinic_settings"})
    
    if existing:
        return {"success": False, "message": "Clinic already setup"}
    
    settings_doc = {
        "type": "clinic_settings",
        "clinic_name": settings.get("clinic_name"),
        "services": settings.get("services", []),
        "working_hours": settings.get("working_hours"),
        "is_active": True,
        "setup_date": datetime.now()
    }
    
    await settings_collection.insert_one(settings_doc)
    
    return {
        "success": True,
        "message": "Clinic setup completed",
        "automation": "System activated"
    }

@router.get("/setup/status")
async def get_setup_status():
    settings = await settings_collection.find_one({"type": "clinic_settings"})
    
    if settings:
        return {
            "is_setup": True,
            "clinic_name": settings.get("clinic_name"),
            "services": settings.get("services", [])
        }
    
    return {"is_setup": False}