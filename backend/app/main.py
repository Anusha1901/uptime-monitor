from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from app.api.routes import router
from app.config import settings
from app.database import models
from app.database.database import Base
from app.database.database import engine
from app.scheduler.monitor import scheduler
from app.scheduler.monitor import start_scheduler

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):

    start_scheduler(settings.CHECK_INTERVAL)

    yield

    scheduler.shutdown()


app = FastAPI(
    title="Uptime Monitor API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Uptime Monitor API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }