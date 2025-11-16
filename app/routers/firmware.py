# app/routers/firmware.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Firmware"])
def firmware_info():
    return {
        "message": "Firmware endpoint placeholder — ready for ML integration."
    }