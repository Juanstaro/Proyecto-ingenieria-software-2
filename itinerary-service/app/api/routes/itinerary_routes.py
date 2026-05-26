from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.models.itinerary import ItineraryCreate

from app.application.services.itinerary_service import AirportValidator

from app.infrastructure.database.db import SessionLocal

from app.infrastructure.repositories.sql_repository import ItineraryDB

router = APIRouter()

@router.post("/itineraries")
def create_itinerary(itinerary: ItineraryCreate):

    AirportValidator.validate_airport(
        itinerary.departure_airport
    )

    AirportValidator.validate_airport(
        itinerary.arrival_airport
    )

    db = SessionLocal()

    new_itinerary = ItineraryDB(
        user_name=itinerary.user_name,
        departure_airport=itinerary.departure_airport,
        arrival_airport=itinerary.arrival_airport,
        travel_date=itinerary.travel_date,
        duration_minutes=itinerary.duration_minutes
    )

    db.add(new_itinerary)

    db.commit()

    db.refresh(new_itinerary)

    return new_itinerary

@router.get("/itineraries")
def get_itineraries():

    db = SessionLocal()

    itineraries = db.query(ItineraryDB).all()

    return itineraries

@router.get("/itineraries/{itinerary_id}")
def get_itinerary(itinerary_id: int):

    db = SessionLocal()

    itinerary = db.query(ItineraryDB).filter(
        ItineraryDB.id == itinerary_id
    ).first()

    if not itinerary:

        raise HTTPException(
            status_code=404,
            detail="Itinerary not found"
        )

    return itinerary

@router.delete("/itineraries/{itinerary_id}")
def delete_itinerary(itinerary_id: int):

    db = SessionLocal()

    itinerary = db.query(ItineraryDB).filter(
        ItineraryDB.id == itinerary_id
    ).first()

    if not itinerary:

        raise HTTPException(
            status_code=404,
            detail="Itinerary not found"
        )

    db.delete(itinerary)

    db.commit()

    return {
        "message": "Deleted successfully"
    }
