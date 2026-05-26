from fastapi import FastAPI
from app.api.routes.airport_routes import router

app = FastAPI(title="Airport Service", version="1.0")

app.include_router(router)
