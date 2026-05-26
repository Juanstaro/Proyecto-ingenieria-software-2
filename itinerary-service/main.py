from fastapi import FastAPI

from app.api.routes.itinerary_routes import router

from app.infrastructure.database.db import Base, engine

from app.infrastructure.repositories.sql_repository import ItineraryDB

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Itinerary Service",
    version="1.0"
)

app.include_router(router)
