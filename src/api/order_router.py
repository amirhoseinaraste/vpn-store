# from files
from src.DB.database import sessionlocal

from src.modules.order_module.order_controller import OrderController
# from packages

from fastapi import APIRouter, HTTPException, status

class order_router:
    def __init__(self):
        self.router = APIRouter(tags=['Order API'])
        self.router_controller = OrderController(DB=sessionlocal)

        @self.router.post('/order')
        async def create_order(): 
            try:
                # Implement the logic to create a new order
                return {"message": "Order created successfully"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        @self.router.get('/order/{id}')
        async def get_order(id: int):
            try:
                # Implement the logic to get an order by ID
                return {"message": f"Order with ID {id} retrieved successfully"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        @self.router.get('/orders')
        async def get_all_orders():
            try:
                # Implement the logic to get all orders
                orders = await self.router_controller.get_orders()
                return orders
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            
        @self.router.put('/order/{id}')
        async def update_order(id: int):
            try:
                # Implement the logic to update an order by ID
                return {"message": f"Order with ID {id} updated successfully"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        @self.router.delete('/order/{id}')
        async def delete_order(id: int):
            try:
                # Implement the logic to delete an order by ID
                return {"message": f"Order with ID {id} deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))   

