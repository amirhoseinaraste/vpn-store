# import from packages
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# import from files
from src.modules.product_module.product_handler import ProductHandler
from src.modules.user_module.user_handler import UserHandler
from src.modules.category_module.category_handler import CategoryHandler


class Handler:
    def __init__(self):
        self.router = Router()

        # configure all handlers
        self.router.include_router(UserHandler().router)
        self.router.include_router(CategoryHandler().router)
        self.router.include_router(ProductHandler().router)  # Include the ProductHandler router




    