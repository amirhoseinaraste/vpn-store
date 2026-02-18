# import from packages
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import datetime

# import from files
from src.model.category import Category


class CategoryService:
    def __init__(self, DB: AsyncSession):
        # inject database
        self.db = DB

    async def create_category(self, name: str, tag: str, description: str = None, parent_id: int = None):
        async with self.db() as session:   
            # check if category exists
            stmt = select(Category).where(Category.name == name)
            result = await self.db.execute(stmt)
            existing_category = result.scalars().first()
            if existing_category:
                raise ValueError("Category already exists")

            # create new category
            new_category = Category(
                name=name,
                tag=tag,
                description=description,
                parent_id=parent_id,
                created_at=datetime.datetime.now()
            )
            self.db.add(new_category)
            await self.db.commit()
            await self.db.refresh(new_category)
            return new_category
        
    async def get_all_categories(self):
        async with self.db() as session:
            stmt = select(Category)
            result = await self.db.execute(stmt)
            return result.scalars().all()
        
    async def get_category(self, id: int):
        async with self.db() as session:
            stmt = select(Category).where(Category.id == id)
            result = await self.db.execute(stmt)
            return result.scalars().first()
        
    async def update_category(self, id: int, name: str = None, tag: str = None, description: str = None, parent_id: int = None):    
        async with self.v() as session:
            stmt = select(Category).where(Category.id == id)
            result = await self.DB.execute(stmt)
            category = result.scalars().first()
            if not category:
                raise ValueError("Category not found")
            
            if name:
                category.name = name
            if tag:
                category.tag = tag
            if description:
                category.description = description
            if parent_id is not None:
                category.parent_id = parent_id
            
            await self.DB.commit()
            await self.DB.refresh(category)
            return category
        
        async def delete_category(self, id: int):
            async with self.DB.() as session:
                stmt = select(Category).where(Category.id == id)
                result = await self.DB.execute(stmt)
                category = result.scalars().first()
                if not category:
                    raise ValueError("Category not found")
                
                await self.DB.delete(category)
                await self.DB.commit()
                return True