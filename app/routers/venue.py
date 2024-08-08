# app/routers/venue.py
from fastapi import APIRouter, Depends
from app.models.venue import venue_collection
from app.schemas.venue import Venue

router = APIRouter()

@router.get("/")
async def get_venues():
    venues = list(venue_collection.find({}))
    return venues

@router.post("/")
async def create_venue(venue: Venue):
    venue_collection.insert_one(venue.dict())
    return {"message": "Venue created successfully"}
