import requests

BASE_URL = "https://api-colombia.com/api/v1/Airport"

class ApiColombiaClient:

    def get_airports(self):
        response = requests.get(BASE_URL)
        return response.json()

    def get_airport_by_id(self, airport_id: int):
        response = requests.get(f"{BASE_URL}/{airport_id}")

        if response.status_code != 200:
            return None

        return response.json()
