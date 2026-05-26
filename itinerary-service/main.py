from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.itinerary_routes import router
from app.infrastructure.database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Itinerary Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
