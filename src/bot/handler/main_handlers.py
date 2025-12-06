# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# import from files
from .user_handler import userHandler

class Handler:
    def __init__(self):
        self.router = Router()

        # configurate all handller
        self.router.include_router(userHandler().router)