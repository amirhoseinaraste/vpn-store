# import from files
from src.modules.category_module.category_service import CategoryService
# import from packages
from fastapi import HTTPException


class category_controller:
    def __init__(self, DB):
        self.category_service = CategoryService(DB)

    async def get_categories(self):
        try:
            categories = await self.category_service.get_all_categories()
            return categories
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching categories: {e}")
        
    async def get_category(self, id: int):
        try:
            category = await self.category_service.get_category_by_id(id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            return category
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching category: {e}")
        
    async def create_category(self, name: str):
        try:
            new_category = await self.category_service.create_category(name)
            return new_category
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error creating category: {e}")
    async def update_category(self, id: int, name: str):
        try:
            updated_category = await self.category_service.update_category(id, name)
            if not updated_category:
                raise HTTPException(status_code=404, detail="Category not found")
            return updated_category
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error updating category: {e}")
    async def delete_category(self, id: int):
        try:
            deleted_category = await self.category_service.delete_category_by_id(id)
            if not deleted_category:
                raise HTTPException(status_code=404, detail="Category not found")
            return deleted_category
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error deleting category: {e}")
        

