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
            return self.product_service.get_product(id)
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))      
    
    async def get_all_product(self):
        try:
            return self.product_service.get_all_products()
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
        
    async def create_new_product(self):
        try:            
            return self.product_service.create_product()
        except Exception as e:
            raise exception_handlers.HTTPException(status_code=500, detail=str(e))
        
