# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


class Handler:
    def __init__(self):
        self.router = Router()

        # configurate all handller
        self.router.include_router()