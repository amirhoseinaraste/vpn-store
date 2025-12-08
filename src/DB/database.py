# import from packages
from pymongo import MongoClient
from utils.logger import setup_logger

# import from files
from utils.env_loader import env_loader

logger = setup_logger('DB')

class DB:
    DB_URI = str(env_loader('DB_URI'))
    DB_NAME = str(env_loader('DB_NAME'))
    def __init__(self):
        self.client = MongoClient(self.DB_URI)
        self.database = self.client[self.DB_NAME]

    # connect to db
    def connect_to_db(self):
        if self.client:
            logger.info(f"Connected to MongoDB  ✅ (Database: {self.database.name})")
        else:
            logger.info("Failed to connect to MongoDB  ❌")

    # disconnect db
    async def disconnect_db(self):
        self.client.close() 
        logger.info(f"Disconnected from MongoDB  ❌ (Database: {self.database.name})")

    async def collection(self, collection_name: str):
        collection = self.database.get_collection(collection_name)
        return collection