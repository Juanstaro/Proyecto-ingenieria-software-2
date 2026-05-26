from pydantic import BaseModel

class Airport(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
