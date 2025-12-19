# import from packages
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import asyncio

# import from files
from utils.logger import setup_logger
from utils.env_loader import env_loader

# import model
from .model import *

# init logger
logger = setup_logger('database')

# TODO : init database
class DB:
    # database url
    DB_URL = str(env_loader('DB_URI'))

    # create base model
    Base = declarative_base()

    def __init__(self):

        logger.info("Initializing database engine...")

        # create engine   
        self.Engine = create_engine(self.DB_URL, echo= True, future=True)

        # Session
        self.SessionLocal = sessionmaker(
            expire_on_commit=False,
            autoflush=False,
            bind=self.Engine
        )





    

        

        
