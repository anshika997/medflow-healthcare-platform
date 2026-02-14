from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import appointments, patients, inventory, staff, dashboard

app = FastAPI(
    title="MedFlow - Healthcare Operations Platform",
    description="Unified platform for managing clinic operations",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(appointments.router, prefix="/api", tags=["Appointments"])
app.include_router(patients.router, prefix="/api", tags=["Patients"])
app.include_router(inventory.router, prefix="/api", tags=["Inventory"])
app.include_router(staff.router, prefix="/api", tags=["Staff"])
app.include_router(dashboard.router, prefix="/api", tags=["Dashboard"])

@app.get("/")
async def root():
    return {
        "message": "MedFlow API - Healthcare Operations Platform",
        "version": "1.0.0",
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)