# from files
from src.modules.product_module.product_service import ProductService
from src.modules.category_module.category_controller import CategoryController
from src.DB.database import sessionlocal


# from packages


class ProductHandler:
    def __init__(self):
        self.product_service = ProductService(DB=sessionlocal)
        self.category_controller = CategoryController(DB=sessionlocal)

    async def get_products_by_category(self, category_id: int):
        try:
            
        except ValueError as e:
            raise ValueError(f"Error fetching products: {e}")
