from config import DATABASE
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient(DATABASE.MONGO_DB_URI)

db = mongo.SPAM
