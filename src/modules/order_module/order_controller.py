# import from files
from http.client import HTTPException

from src.modules.order_module.order_service import OrderService

# import from packages
from sqlalchemy.ext.asyncio import AsyncSession


class OrderController:
    def __init__(self, DB: AsyncSession):
        self.order_service = OrderService(DB)

    async def create_order(self, data):
        try:
            # create order data
            new_order = await self.order_service.create_order(data)
            
            return new_order
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error creating order: {e}")
        
    async def get_orders(self):
        try:
            orders = await self.order_service.get_all_orders() 
            return orders
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching orders: {e}")
    async def get_order(self, id: int):
        try:
            order = await self.order_service.get_order_by_id(id)
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
            return order
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching order: {e}")
    async def get_orders_by_user_id(self, user_id: str):
        try:
            orders = await self.order_service.get_orders_by_user_id(user_id)
            return orders
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching orders by user id: {e}")
    async def get_orders_by_status(self, status: str):
        try:
            orders = await self.order_service.get_orders_by_status(status)
            return orders
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching orders by status: {e}")
        
    async def update_order(self, id: int, data):
        try:
            updated_order = await self.order_service.update_order(id, data)
            if not updated_order:
                raise HTTPException(status_code=404, detail="Order not found")
            return updated_order
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error updating order: {e}")
        
        
    async def delete_order(self, id: int):
        try:
            deleted_order = await self.order_service.delete_order_by_id(id)
            if not deleted_order:
                raise HTTPException(status_code=404, detail="Order not found")
            return deleted_order
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error deleting order: {e}")
        