# import from files
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# import from packages
from src.model.config import Config

class ConfigService:
    def __init__(self, Db: AsyncSession):

        self.db = Db

    async def create_config(self, product_id: int, value: str):
        async with self.db() as session:
            new_config = Config(
                product_id=product_id,
                value=value
            )
            session.add(new_config)
            await session.commit()
            await session.refresh(new_config)
            return new_config
        
    async def get_configs_by_product_id(self, product_id: int):
        async with self.db() as session:
            stmt = select(Config).where(Config.product_id == product_id)
            result = await session.execute(stmt)
            return result.scalars().all()
        
    async def get_config_by_id(self, config_id: int):
        async with self.db() as session:
            stmt = select(Config).where(Config.id == config_id)
            result = await session.execute(stmt)
            return result.scalars().first()
        
    async def get_all_configs(self):
        async with self.db() as session:
            stmt = select(Config)
            result = await session.execute(stmt)
            return result.scalars().all()
    
        
    async def update_config(self, config_id: int, value: str):
        async with self.db() as session:
            stmt = select(Config).where(Config.id == config_id)
            result = await session.execute(stmt)
            config = result.scalars().first()
            if not config:
                raise ValueError("Config not found")
            
            config.value = value
            await session.commit()
            await session.refresh(config)
            return config
        
    async def delete_config(self, config_id: int):
        async with self.db() as session:
            stmt = select(Config).where(Config.id == config_id)
            result = await session.execute(stmt)
            config = result.scalars().first()
            if not config:
                raise ValueError("Config not found")
            
            await session.delete(config)
            await session.commit()
            return True
