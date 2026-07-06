# from files


from email.mime import message

from src.model.product import Product
from src.modules.product_module.product_service import ProductService
from src.modules.category_module.category_controller import CategoryController
from src.modules.product_module.product_controller import ProductController
from src.modules.product_module.product_keyboard import ProductKeyboard
from src.DB.database import sessionlocal


# from packages


class ProductHandler:
    def __init__(self):
        self.product_service = ProductService(DB=sessionlocal)
        self.category_controller = CategoryController(DB=sessionlocal)
        self.product_contorller = ProductController(DB=sessionlocal)

    async def get_products_by_category(self, category_id: int):
        try:
            
            # check if category exists
            category = await self.category_controller.get_category(category_id)
            if category is None:
                raise ValueError(f"Category with id {category_id} does not exist")

            product_list = await self.product_contorller.get_products_by_category_id(category_id)
            if not product_list:
                raise ValueError(f"No products found for category with id {category_id}")
            keyboard = ProductKeyboard().products_keyboard(product_list)

            

            return product_list, keyboard
        
        except ValueError as e:
            raise ValueError(f"Error fetching products: {e}")
