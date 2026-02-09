from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Mini REST API")
app.include_router(router)
