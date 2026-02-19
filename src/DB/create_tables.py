# import from packages
import asyncio

# from files
from src.DB.database import Base, engine
from src.model.user import User  
from src.model.category import Category
from src.model.product import Product


# note: this file is for create tables in database if not exist, we run this file one time after we add new model to create new table in database, and we can delete this file after that, because we will use alembic for database migration in future
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(create_tables())