from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")



client = AsyncIOMotorClient(MONGO_URL)
database = client.product_reviews
review_collection = database.get_collection("review_analyses")
