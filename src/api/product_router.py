# import from files
from src.modules.product_module.product_controller import ProductController
from src.modules.product_module.product_controller import ProductController
from src.api.schemas.product.create_schema import CreateProduct, responseCreateProductSchema

from src.DB.database import sessionlocal


# import from necessary packages
from fastapi import APIRouter, HTTPException, status


# this not force => in refatory sesion we will change this to class based router
class product_router:
    def __init__(self):
        self.router = APIRouter(tags=['Product API'])
        self.product_controller = ProductController(DB=sessionlocal)
        
        # create new product route
        @self.router.post('/product', response_model=responseCreateProductSchema)
        async def create_product(product: CreateProduct):
            try:
                new_product = await self.product_controller.create_new_product(name=product.name, category=product.category, volume=product.volume, price=product.price, duration=product.duration)
                return responseCreateProductSchema(id=new_product.id, status="success", created_at=str(new_product.created_at))
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            


