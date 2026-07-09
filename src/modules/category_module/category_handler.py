# from files
from src.model.product import Product
from src.modules.category_module.category_keyboard import CategoryKeyboard
from src.DB.database import sessionlocal
from src.modules.category_module.category_controller import CategoryController
from src.modules.product_module.product_handler import ProductHandler


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
        self.product_handler = ProductHandler()

        # # get limited categories
        # @self.router.callback_query(lambda c: c.data == "limited")
        # async def get_limited_categories_handler(callback_query):
            
        #     await callback_query.message.answer("Please select a product:")
        #     products_list = await self.product_handler.get_products_by_category(category_id=2)  # Example category_id, replace with actual logic to get the selected category ID    
        #     print(products_list)
        #     await callback_query.message.answer("Here are the available products:", reply_markup=products_list[1])  # Assuming products_list is a tuple with the second element being the keyboard

        #  # get unlimited categories
        # @self.router.callback_query(lambda c: c.data == "Unlimited")
        # async def get_unlimited_categories_handler(callback_query):
          
        #     await callback_query.answer("Please select a product:")
        #     products_list = await self.product_handler.get_products_by_category(category_id=1)  # Example category_id, replace with actual logic to get the selected category ID
        #     print(products_list)
        #     await callback_query.message.answer("Here are the available products:", reply_markup=products_list[1])  # Assuming products_list is a tuple with the second element being the keyboard

        #  get category with id
        @self.router.callback_query(lambda c: c.data.startswith("category_"))
        async def get_category_handler(callback_query):
            category_id = int(callback_query.data.split("_")[1])
            products_list, keyboard = await self.product_handler.get_products_by_category(category_id=category_id)
            await callback_query.message.answer("Here are the available products:", reply_markup=keyboard)
            return 

    async def get_categories_handler(self, message: Message):
        # get all categories
        categories = await self.category_controller.get_categories()
        keyboard = CategoryKeyboard().categories_keyboard(categories)
        await message.answer("Here are the available categories:", reply_markup=keyboard)

        



