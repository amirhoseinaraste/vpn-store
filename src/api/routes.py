# import frpm packages
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

# import from files
from src.api.webhook.webhook_api import webhook_router as webhook
from src.api.user_router import user_router as user
from src.api.product_router import product_router as product
from src.api.category_router import category_router as category
from src.api.config_router import config_router as config
from src.api.schemas.error_schema import ErrorResponse

# TODO: init main router
class main_router:
    def __init__(self):
        self.router = APIRouter()
        self.routes_configurate()
        
    def routes_configurate(self):
        self.router.include_router(webhook().router)
        self.router.include_router(user().router)
        self.router.include_router(product().router)
        self.router.include_router(category().router)
        self.router.include_router(config().router)
        



    