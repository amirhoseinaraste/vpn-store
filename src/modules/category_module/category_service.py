# import from packages
from ast import stmt
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


import datetime

# import from files
from src.model.category import Category


class CategoryService:
    def __init__(self, DB: AsyncSession):
        # inject database
        self.db = DB

    async def create_category(self, name: str, tag: str, description: str = None, parent_id: int = None):
        async with self.db() as session:   
            # create new category
            new_category = Category(
                name=name,
                tag=tag,
                description=description,
                parent_id= parent_id if parent_id and parent_id > 0 else None,
                created_at=datetime.datetime.now()
            )
            session.add(new_category)
            await session.commit()
            await session.refresh(new_category)
            return new_category
        
    async def get_category_by_name(self, name: str):
        async with self.db() as session:
            stmt = select(Category).where(Category.name == name)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        
    async def get_all_categories(self):
        async with self.db() as session:
            stmt = select(Category)
            result = await session.execute(stmt)
            return result.scalars().all()
        
    async def get_category_by_id(self, id: int):
        async with self.db() as session:
            stmt = select(Category).where(Category.id == id)
            result = await session.execute(stmt)
            return result.scalars().first()
        
    async def update_category(self, id: int, name: str = None, tag: str = None, description: str = None, parent_id: int = None):    
        async with self.db() as session:
            stmt = select(Category).where(Category.id == id)
            result = await session.execute(stmt)
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
            
            await session.commit()
            await session.refresh(category)
            return category
        
        async def delete_category_by_id(self, id: int):
            async with self.db() as session:
                stmt = select(Category).where(Category.id == id)
                result = await session.execute(stmt)
                category = result.scalars().first()
                if not category:
                    raise ValueError("Category not found")
                
                  
                await session.delete(category)
                await session.commit()
                return True