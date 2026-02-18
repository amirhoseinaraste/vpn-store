# import from packages
from fastapi import exception_handlers

# # import from files
from src.modules.product_module.product_service import ProductService

class ProductController:
    def __init__(self, DB):
        # inject user service
        self.product_service = ProductService(DB)

    async def get_product_by_id(self, id: int):
        try:
            return await self.product_service.get_product(id)
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))      
    
    async def get_all_products(self):
        try:
            return await self.product_service.get_all_products()
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
        
    async def create_new_product(self, name: str, category: str, volume: int, price: int, duration: int):
        try:          
            check_product = await self.product_service.check_product_exists(name=name, category=category, volume=volume, price=price, duration=duration)
            if check_product:
                raise exception_handlers.HTTPException(status_code=400, detail="Product already exists")
            return await self.product_service.create_product(name=name, category=category, volume=volume, price=price, duration=duration)
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
        
