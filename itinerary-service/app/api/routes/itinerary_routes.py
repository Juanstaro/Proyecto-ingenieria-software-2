from fastapi import APIRouter
from app.domain.models.itinerary import ItineraryCreate
from app.application.services.itinerary_service import AirportValidator

router = APIRouter()

fake_db = []

@router.post("/itineraries")
def create_itinerary(itinerary: ItineraryCreate):

    AirportValidator.validate_airport(itinerary.departure_airport)
    AirportValidator.validate_airport(itinerary.arrival_airport)

    fake_db.append(itinerary)

    return {
        "message": "Itinerary created successfully",
        "data": itinerary
    }

@router.get("/itineraries")
def get_itineraries():
    return fake_db
