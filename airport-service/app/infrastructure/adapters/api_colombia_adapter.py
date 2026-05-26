from app.domain.models.airport import Airport
from app.domain.ports.airport_provider import AirportProvider
from app.infrastructure.clients.api_colombia_client import ApiColombiaClient

class ApiColombiaAdapter(AirportProvider):

    def __init__(self):
        self.client = ApiColombiaClient()

    def adapt(self, data):
        return Airport(
            id=data["id"],
            name=data["name"],
            latitude=data["latitude"],
            longitude=data["longitude"]
        )

    def get_airports(self):
        data = self.client.get_airports()
        return [self.adapt(item) for item in data]

    def get_airport_by_id(self, airport_id: int):
        data = self.client.get_airport_by_id(airport_id)

        if not data:
            return None

        return self.adapt(data)
