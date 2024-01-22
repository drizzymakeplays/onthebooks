from fastapi import FastAPI
from authenticator import authenticator
from routers import accounts, appointments, profiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.include_router(authenticator.router, tags=["Auth"])
app.include_router(accounts.router, tags=["Accounts"])
app.include_router(profiles.router, tags=["Profiles"])
app.include_router(appointments.router, tags=["Appointments"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
