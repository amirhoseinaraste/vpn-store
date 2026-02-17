# import from packages
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


# import from file
from src.model.product import Product

# TODO: implement product service
class ProductService:

    def __init__(self, DB: AsyncSession):
        # Inject database
        self.db = DB
    
    async def check_product_exists(self, name: str, category: str, volume: int, price: int, duration: int):
        # check if product already exists in database
        async with self.db() as session:
            result = await session.execute(select(Product).filter(
                Product.name == name,
                Product.category == category,
                Product.volume == volume,
                Product.price == price,
                Product.duration == duration
            ))
            return result.scalars().first()
    async def create_product(self, name: str, category: str, volume: int, price: int, duration: int):
        # Create a new product
        async with self.db() as session:
            new_product = Product(
                name=name,
                category=category,
                volume=volume,
                price=price,
                duration=duration
            )
            session.add(new_product)
            await session.commit()
            await session.refresh(new_product)
            return new_product
    
    async def get_all_products(self):
        # get all products
        async with self.db() as session:
            result = await session.execute(select(Product))
            return result.scalars().all()
        
    async def get_product(self, id: int):
        # get one product by id
        async with self.db() as session:
            result = await session.execute(select(Product).where(Product.id == id))
            return result.scalars().first()

    async def update_product(self, id: int, name: str, price: int, duration: int):
        # update one product
        async with self.db() as session:
            result = await session.execute(select(Product).where(Product.id == id))
            product = result.scalars().first()
            if product:
                product.name = name
                product.price = price
                product.duration = duration
                await session.commit()
                await session.refresh(product)
                return product
            return None
        
    async def delete_product(self, id: int):
        # delete product by id
        async with self.db() as session:
            result = await session.execute(select(Product).where(Product.id == id))
            product = result.scalars().first()
            if product:
                await session.delete(product)
                await session.commit()
                return True
            return False
        
    
    
