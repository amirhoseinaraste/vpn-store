# import from fiels
from src.modules.category_module.category_controller import category_controller
from src.api.schemas.category.create_schema import CreateCategorySchema, responseCreateCategorySchema
from src.DB.database import sessionlocal

# from packages
from fastapi import APIRouter, HTTPException


class category_router:
    def __init__(self):
        self.router = APIRouter(tags=['Category API'])
        self.category_controller = category_controller(DB=sessionlocal)
        
        @self.router.post('/category', response_model=responseCreateCategorySchema)
        async def create_category(category: CreateCategorySchema):
            try:
                new_category = await self.category_controller.create_category(name=category.name)
                return responseCreateCategorySchema(id=new_category.id, status="success", created_at=str(new_category.created_at))
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        @self.router.get('/categories')
        async def get_categories():
            try:
                categories = await self.category_controller.get_categories()
                return categories
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
            
        @self.router.get('/category/{id}')
        async def get_category(id: int):
            try:
                category = await self.category_controller.get_category(id)
                return category
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
