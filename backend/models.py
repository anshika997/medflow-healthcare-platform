from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Appointment(BaseModel):
    patient_name: str
    phone: str
    email: str
    appointment_type: str
    date: str
    time: str
    doctor: str
    status: str = "scheduled"
    created_at: Optional[datetime] = None

class Patient(BaseModel):
    name: str
    phone: str
    email: str
    message: str
    status: str = "new"
    created_at: Optional[datetime] = None

class Inventory(BaseModel):
    item_name: str
    quantity: int
    category: str
    min_threshold: int = 10

class Staff(BaseModel):
    name: str
    role: str
    email: str
    phone: str

class ClinicSettings(BaseModel):
    clinic_name: str
    services: list
    working_hours: str
    is_active: bool = False