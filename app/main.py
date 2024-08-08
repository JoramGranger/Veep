# app/main.py
from fastapi import FastAPI
from app.routers import venue, user, payment

app = FastAPI()

app.include_router(venue.router, prefix="/v1/venues")
app.include_router(user.router, prefix="/v1/users")
app.include_router(payment.router, prefix="/v1/payments")
