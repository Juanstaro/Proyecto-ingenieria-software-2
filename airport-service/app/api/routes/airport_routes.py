from fastapi import APIRouter, HTTPException
from app.application.services.airport_service import AirportService

router = APIRouter()
service = AirportService()

@router.get("/airports")
def get_airports():
    return service.get_airports()

@router.get("/airports/{airport_id}")
def get_airport_by_id(airport_id: int):

    airport = service.get_airport_by_id(airport_id)

    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")

    return airport

@router.get("/airports/plotly/data")
def get_plotly_data():

    airports = service.get_airports()

    return {
        "latitudes": [a.latitude for a in airports],
        "longitudes": [a.longitude for a in airports],
        "names": [a.name for a in airports]
    }
