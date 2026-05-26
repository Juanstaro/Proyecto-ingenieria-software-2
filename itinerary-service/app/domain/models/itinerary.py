from pydantic import BaseModel
from datetime import date

class ItineraryCreate(BaseModel):

    user_name: str
    departure_airport: int
    arrival_airport: int
    travel_date: date
    duration_minutes: int
