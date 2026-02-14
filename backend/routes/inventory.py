from fastapi import APIRouter, HTTPException
from models import Inventory
from database import inventory_collection
from automation import check_inventory_alert
from bson import ObjectId

router = APIRouter()

@router.post("/inventory")
async def add_inventory_item(item: Inventory):
    item_dict = item.dict()
    result = await inventory_collection.insert_one(item_dict)
    
    # Check for alerts
    check_inventory_alert(item.item_name, item.quantity, item.min_threshold)
    
    return {
        "success": True,
        "id": str(result.inserted_id),
        "message": "Inventory item added"
    }

@router.get("/inventory")
async def get_inventory():
    items = []
    async for item in inventory_collection.find():
        item["_id"] = str(item["_id"])
        items.append(item)
    return {"inventory": items}

@router.get("/inventory/alerts")
async def get_inventory_alerts():
    alerts = []
    async for item in inventory_collection.find():
        if item["quantity"] < item["min_threshold"]:
            alerts.append({
                "item": item["item_name"],
                "category": item["category"],
                "current": item["quantity"],
                "threshold": item["min_threshold"],
                "deficit": item["min_threshold"] - item["quantity"]
            })
    return {"alerts": alerts, "count": len(alerts)}

@router.put("/inventory/{item_id}")
async def update_inventory(item_id: str, quantity: int):
    item = await inventory_collection.find_one({"_id": ObjectId(item_id)})
    
    result = await inventory_collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"quantity": quantity}}
    )
    
    # Check for alerts after update
    if item:
        check_inventory_alert(item["item_name"], quantity, item["min_threshold"])
    
    return {"success": True, "message": "Inventory updated"}