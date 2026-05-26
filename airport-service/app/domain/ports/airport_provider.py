from abc import ABC, abstractmethod

class AirportProvider(ABC):

    @abstractmethod
    def get_airports(self):
        pass

    @abstractmethod
    def get_airport_by_id(self, airport_id: int):
        pass
