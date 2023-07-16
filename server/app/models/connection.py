from pymongo import MongoClient
from utils.config import MONGO_URL

try:
    client = MongoClient(MONGO_URL)
    db = client.get_database()
    print("Successfully connected to database")
except Exception as e:
    print("Error occured while connecting to database", e)
