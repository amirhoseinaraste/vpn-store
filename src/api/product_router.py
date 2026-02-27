# import from files
from src.modules.product_module.product_controller import ProductController
from src.api.schemas.product.create_schema import CreateProduct, responseCreateProductSchema
from src.api.schemas.product.getone_schema import ResponseGetOneProductSchema
from src.api.schemas.product.getall_schema import ResponseGetAllProductsSchema

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
                print(product)
                new_product = await self.product_controller.create_new_product(product)
                return responseCreateProductSchema(id=new_product.id, status="success", created_at=str(new_product.created_at))
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            
        # get product by id route
        @self.router.get('/product/{id}', response_model=ResponseGetOneProductSchema)
        async def get_product(id: int):
            product = await self.product_controller.get_product_by_id(id)
            if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
            return ResponseGetOneProductSchema(id=product.id, name=product.name, category=product.category_id, price=product.price, volume=product.volume, duration=product.duration, status=product.status, created_at=product.created_at, updated_at=product.updated_at)    
        # get all products route
        @self.router.get('/products', response_model=list[ResponseGetAllProductsSchema])
        async def get_all_products():
            products = await self.product_controller.get_all_products()
            return [ResponseGetAllProductsSchema(id=product.id, name=product.name, category=product.category_id, price=product.price, volume=product.volume, duration=product.duration, status=product.status) for product in products]
    
        @self.router.put('/product/{id}', response_model=ResponseGetOneProductSchema)
        async def update_product(id: int, product: CreateProduct):
            try:
                updated_product = await self.product_controller.update_product(product_id=id, product=product)
                if not updated_product:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
                return ResponseGetOneProductSchema(id=updated_product.id, name=updated_product.name, category=updated_product.category_id, price=updated_product.price, volume=updated_product.volume, duration=updated_product.duration, status=updated_product.status, created_at=updated_product.created_at, updated_at=updated_product.updated_at)
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            
        @self.router.delete('/product/{id}')
        async def delete_product(id: int):
            try:
                deleted_product = await self.product_controller.delete_product(product_id=id)
                if not deleted_product:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
                return {"status": "success", "message": f"Product with id {id} deleted successfully"}
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            