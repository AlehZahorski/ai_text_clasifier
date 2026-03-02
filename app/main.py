from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Ai Text Clasifier")

app.include_router(router)