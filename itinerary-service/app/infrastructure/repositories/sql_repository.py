from sqlalchemy import Column, Integer, String, Date
from app.infrastructure.database.db import Base

class ItineraryDB(Base):

    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    departure_airport = Column(Integer)
    arrival_airport = Column(Integer)
    travel_date = Column(Date)
    duration_minutes = Column(Integer)
