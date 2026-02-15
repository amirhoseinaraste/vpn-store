# import from packages
from fastapi import exception_handlers

# # import from files
# from src.modules.product_module.product_service import ProductService

class ProductController:
    def __init__(self):
        pass

    async def get_product_by_id(self, id: int):
        pass

    async def get_all_product(self):
        async with self.db() as session:
            pass
    async def create_new_product(self):
        pass
