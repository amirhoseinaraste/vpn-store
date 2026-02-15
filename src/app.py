# import packages
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

# import files
from api.routes import main_router
from src.api.schemas.error_schema import ErrorResponse
from utils.logger import setup_logger

# config app log
logger = setup_logger('app')

# TODO: Init App

class App:
    def __init__(self):

        logger.info('app init')

        # config app
        self.app = FastAPI(swagger_ui_parameters={'syntaxHighlight': False})

        # configurate api 
        self.app.include_router(main_router().router)
        
        # error handeling
        @self.app.exception_handler(HTTPException)
        async def global_exception_handler(request: Request, exc: HTTPException):
            return JSONResponse(
                status_code=exc.status_code,
                content=ErrorResponse(code=exc.status_code, message=exc.detail).model_dump()
            )
        







        
        
 


    

    

    