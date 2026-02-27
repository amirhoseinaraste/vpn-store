# from files
from src.modules.category_module.category_keyboard import CategoryKeyboard
from src.DB.database import sessionlocal
from src.modules.category_module.category_controller import CategoryController


# from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# todo: implement category Handler

class CategoryHandler:
    
    def __init__(self):
        self.router = Router()
        self.router.message.register(self.get_categories_handler, Command("categories"))
        self.category_controller = CategoryController(DB=sessionlocal)


    async def get_categories_handler(self, message: Message):
        # get all categories
        categories = await self.category_controller.get_categories()
        print(categories)
        keyboard = CategoryKeyboard().categories_keyboard(categories)
        await message.answer("Here are the available categories:", reply_markup=keyboard)

        



