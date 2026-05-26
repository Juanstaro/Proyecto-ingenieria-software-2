from app.infrastructure.adapters.api_colombia_adapter import ApiColombiaAdapter

class AirportService:

    def __init__(self):
        self.provider = ApiColombiaAdapter()

    def get_airports(self):
        return self.provider.get_airports()

    def get_airport_by_id(self, airport_id):
        return self.provider.get_airport_by_id(airport_id)
