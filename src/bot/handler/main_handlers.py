# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# import from files
from .user_handler import UserHandler


class Handler:
    def __init__(self):
        self.router = Router()

        self.router.include_router(UserHandler().router)
        # configurate all handller
        self.config_all_handler()
        
    def config_all_handler(self):
        self.router.include_router(UserHandler().router)
