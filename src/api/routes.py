# import frpm packages
from fastapi import APIRouter

# import from files
from .webhook.webhook_api import webhook

# TODO: init main router
class main_router:
    def __init__(self):
        self.router = APIRouter()
        self.config_routes()

    def config_routes(self):
        self.router.include_router(webhook().router)



    