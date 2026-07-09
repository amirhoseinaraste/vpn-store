# from files
from src.modules.product_module.product_service import ProductService

# from packages
from sqlalchemy.ext.asyncio import AsyncSession

class OrderService:
    def __init__(self, DB: AsyncSession):
        self.db = DB

        self.product_service = ProductService(DB=self.db)

    async def create_order(self, order_data):
        # Implement order creation logic here
        # For example, you might want to check if the product exists before creating an order
        product = await self.product_service.get_product(order_data.product_id)
        if not product:
            raise ValueError(f"Product with id {order_data.product_id} does not exist")
        
        # Proceed with order creation logic
        # ...