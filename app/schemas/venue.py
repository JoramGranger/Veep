# app/schemas/venue.py
from pydantic import BaseModel
from typing import List

class Venue(BaseModel):
    name: str
    location: str
    capacity: int
    amenities: List[str]
    price_per_hour: float
    owner_id: str

# app/models/venue.py
from app.database import db

venue_collection = db.get_collection("venues")