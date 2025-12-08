# import packages
from fastapi import FastAPI
from api.routes import main_router
from bot.bot import tel_bot
# import files
from DB.database import DB
from utils.logger import setup_logger

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
        self.config_db()

        # configurate api 
        self.app.include_router(main_router().router)
        

    # configurate db in app module
    def config_db(self):
        logger.info('db config')

        # init db
        self.db = DB()

        # connect app to db
        self.db.connect_to_db()





        
        
 


    

    

    