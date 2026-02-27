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
        
    async def create_new_product(self, product):
        try:       
            # pass full product object to service for existence check
            check_product = await self.product_service.check_product_exists(product)
            if check_product:
                raise exception_handlers.HTTPException(status_code=400, detail="Product already exists")
            return await self.product_service.create_product(product)
        except ValueError as ve:
            # expected validation error from service
            raise exception_handlers.HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
         
    async def update_product(self, product_id: int, product):
        try:
            return await self.product_service.update_product(product_id, product)
        except ValueError as ve:
            raise exception_handlers.HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
    
    async def delete_product(self, product_id: int):
        try:
            return await self.product_service.delete_product(product_id)
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
        
