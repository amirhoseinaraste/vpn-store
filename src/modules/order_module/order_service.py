# from files
from src.modules.product_module.product_service import ProductService
from src.model.order import Order
# from packages
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

from sqlalchemy import select


class OrderService:
    def __init__(self, DB: AsyncSession):
        self.db = DB

        self.product_service = ProductService(DB=self.db)

    async def create_order(self, order):
        print(order)
        order_data = Order(
            **order,
            status="pending"
        )   
        async with self.db() as session:
            session.add(order_data)
            await session.commit()
            await session.refresh(order_data)
            return order_data
        
    async def get_all_orders(self):
        async with self.db() as session:
            stmt = select(Order)
            result = await session.execute(stmt)
            return result.scalars().all()
        
    async def get_order_by_id(self, id: int):
        async with self.db() as session:
            result = await session.execute(select(Order).where(Order.id==id))
            order = result.scalars().first()
            return order
    
        