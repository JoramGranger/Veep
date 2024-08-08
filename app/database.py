# app/database.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE_URL"))
db = client.get_database("venue_marketplace")
