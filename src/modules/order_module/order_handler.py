# from files

# from packages

from src.modules.order_module.order_service import OrderService
from src.modules.product_module.product_service import ProductService


class OrderHandler:
    def __init__(self):
        self.order_service = OrderService(DB=self.db)
        self.product_service = ProductService(DB=self.db)