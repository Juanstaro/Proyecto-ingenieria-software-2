import requests
from fastapi import HTTPException

AIRPORT_SERVICE_URL = "http://airport-service:8000/airports"

class AirportValidator:

    @staticmethod
    def validate_airport(airport_id: int):

        response = requests.get(f"{AIRPORT_SERVICE_URL}/{airport_id}")

        if response.status_code != 200:
            raise HTTPException(
                status_code=404,
                detail=f"Airport {airport_id} does not exist"
            )
