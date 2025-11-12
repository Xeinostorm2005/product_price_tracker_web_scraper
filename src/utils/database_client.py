# Imports necessary modules
from pymongo import MongoClient
import os

# Gets the Database information
MONGO_URI = os.getenv("DATABASE_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Create a single MongoDB client instance
client = MongoClient(MONGO_URI)

# Select the specific database
db = client[f"{DATABASE_NAME}"]
