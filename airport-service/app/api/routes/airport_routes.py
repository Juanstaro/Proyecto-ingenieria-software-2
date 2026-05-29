from fastapi import APIRouter, HTTPException
from app.application.services.airport_service import AirportService

router = APIRouter()

service = AirportService()

@router.get("/airports")
def get_airports():
    return service.get_airports()

# Aplicamos la corrección documentando el 404 en las respuestas de este endpoint
@router.get(
    "/airports/{airport_id}",
    responses={
        404: {"description": "Airport not found"}
    }
)
def get_airport_by_id(airport_id: int):

    airport = service.get_airport_by_id(airport_id)

    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")

    return airport