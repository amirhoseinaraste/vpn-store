# import from packages
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import datetime


# import from file
from src.model.category import Category
from src.model.product import Product
from src.modules.category_module.category_service import CategoryService

# TODO: implement product service
class ProductService:

    def __init__(self, DB: AsyncSession):
        # Inject database
        self.db = DB
        
        # inject category service
        self.category_services = CategoryService(self.db)
    
    async def check_product_exists(self, product):
        """Check if a product with the same attributes already exists.

        The controller passes the full Pydantic model so we can compare all
        relevant fields (name, category, volume, price, duration).
        """
        async with self.db() as session:
            result = await session.execute(select(Product).filter(
                Product.name == product.name,
                Product.category_id == product.category,
                Product.volume == product.volume,
                Product.price == product.price,
                Product.duration == product.duration
            ))
            return result.scalars().first()
    async def create_product(self, product):
        # Create a new product
        async with self.db() as session:
            print("!")
            category = await self.category_services.get_category_by_id(id = product.category)
            if not category:
                # caller should handle a bad request
                raise ValueError(f"Category with id {product.category} does not exist")
            new_product = Product(
                name=product.name,
                category_id=category.id,
                volume=product.volume,
                price=product.price,
                duration=product.duration,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
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

    async def update_product(self, product_id: int, product):
        """Update the given product's attributes.

        We accept the full Pydantic model so all mutable fields can be applied.
        """
        async with self.db() as session:
            result = await session.execute(select(Product).where(Product.id == product_id))
            existing = result.scalars().first()
            if existing:
                # validate category existence
                if product.category is not None:
                    category = await self.category_services.get_category_by_id(id=product.category)
                    if not category:
                        raise ValueError(f"Category with id {product.category} does not exist")
                    existing.category_id = category.id
                existing.name = product.name
                existing.price = product.price
                existing.duration = product.duration
                existing.volume = product.volume
                await session.commit()
                await session.refresh(existing)
                return existing
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
        
    
    
