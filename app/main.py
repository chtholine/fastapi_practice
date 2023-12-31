from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.router import router

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "0.0.0.0:8000",
    "127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
