# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# import from files
from src.modules.user_module.user_handler import UserHandler


class Handler:
    def __init__(self):
        self.router = Router()

        # configure all handlers
        self.router.include_router(UserHandler().router)



    