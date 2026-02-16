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
    async def create_product(self, name: str, price: int, description: str):
        # Create a new product
        async with self.db() as session:
            new_product = Product(
                name=name,
                price=price,
                description=description
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

    async def update_product(self, id: int, name: str, price: int, description: str):
        # update one product
        async with self.db() as session:
            result = await session.execute(select(Product).where(Product.id == id))
            product = result.scalars().first()
            if product:
                product.name = name
                product.price = price
                product.description = description
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
        
    
    
