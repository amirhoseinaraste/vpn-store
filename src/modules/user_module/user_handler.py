# import from files
from src.modules.user_module.user_controller import UserController
from src.DB.database import sessionlocal
from src.modules.user_module.user_keyboard import UserKeyboard
from src.modules.category_module.category_handler import CategoryHandler

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
        self.category_handler = CategoryHandler()


        
        # GET PRODUCT LIST 
        @self.router.callback_query(lambda c: c.data == "buy_config")
        async def handle_buy_config(callback_query):
            await callback_query.message.answer("Please select a category:")
            await self.category_handler.get_categories_handler(callback_query.message)

    async def start_handler(self, message: Message):
        # sing in user
        telegram_id = message.from_user.id
        print(type(telegram_id))
        username = message.from_user.username or ''
        first_name = message.from_user.first_name or ''
        last_name = message.from_user.last_name or ''


        sign_in = await self.user_controller.sign_in_user(telegram_id, username, first_name, last_name)

        await message.answer(f"Welcome, {sign_in.first_name} {sign_in.last_name}!")         
        await message.answer("Use the menu below to navigate through the bot's features.", reply_markup=UserKeyboard.main_menu_keyboard())
        


