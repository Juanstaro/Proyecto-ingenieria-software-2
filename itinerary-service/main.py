from fastapi import FastAPI
from app.api.routes.itinerary_routes import router

app = FastAPI(title="Itinerary Service", version="1.0")

app.include_router(router)
