# import packages
from fastapi import FastAPI
from api.routes import main_router
from bot.bot import tel_bot
import asyncio
# import files
from DB.database import DB
from utils.logger import setup_logger

from  DB.model import *
# config app log
logger = setup_logger('app')

""" explain App:
        class based

"""

# TODO: Init App

class App:
    def __init__(self):

        logger.info('app init')
        # config app
        self.app = FastAPI(swagger_ui_parameters={'syntaxHighlight': False})


        # config db
        self.db = DB()
        self.db.Base.metadata.create_all(bind=self.db.Engine)
        
        # configurate api 
        self.app.include_router(main_router().router)
        





        
        
 


    

    

    