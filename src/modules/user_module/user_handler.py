# import from files
from src.modules.user_module.user_controller import UserController
from src.DB.database import sessionlocal

# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


# todo: implement user Handler

class UserHandler:
    
    def __init__(self):
        self.router = Router()
        self.router.message.register(self.start_handler, Command("start"))
        self.user_controller = UserController(DB=sessionlocal)

    async def start_handler(self, message: Message):
        # sing in user
        telegram_id = message.from_user.id
        print(type(telegram_id))
        username = message.from_user.username or ''
        first_name = message.from_user.first_name or ''
        last_name = message.from_user.last_name or ''


        sign_in = await self.user_controller.sign_in_user(telegram_id, username, first_name, last_name)

        await message.answer(f"Welcome, {sign_in.first_name} {sign_in.last_name}!")         


