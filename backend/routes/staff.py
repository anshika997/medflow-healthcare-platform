from fastapi import APIRouter
from models import Staff
from database import staff_collection

router = APIRouter()

@router.post("/staff")
async def add_staff(staff: Staff):
    staff_dict = staff.dict()
    result = await staff_collection.insert_one(staff_dict)
    return {"success": True, "id": str(result.inserted_id)}

@router.get("/staff")
async def get_staff():
    staff_list = []
    async for staff in staff_collection.find():
        staff["_id"] = str(staff["_id"])
        staff_list.append(staff)
    return {"staff": staff_list}