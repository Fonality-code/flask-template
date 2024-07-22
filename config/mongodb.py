
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from beanie import init_beanie
import os




# documents

documents = [

]



async def init_db():
    MONGODB_URL = os.environ.get("MONGODB_URL")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    # Create a new client and connect to the server
    client = AsyncIOMotorClient(MONGODB_URL, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    database = client[DATABASE_NAME]
    try:
        await init_beanie(database=database, document_models=documents)
        client.admin.command('ping')
        print("You successfully connected to Database!")
    except Exception as e:
        print(e)
        print("Database Not Connected!")

