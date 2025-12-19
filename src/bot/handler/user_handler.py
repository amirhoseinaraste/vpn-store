# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


class UserHandler:
    def __init__(self):
        self.router = Router()

        @self.router.message(Command('start'))
        async def start_handler(message: Message):
            user = message.from_user
            await message.answer(f'Hello {user.first_name}')

