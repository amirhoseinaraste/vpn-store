# import from files     
from src.DB.database import Base

# import from packages
from sqlalchemy import Column, Integer, String, BigInteger, Date


class Product(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    prduct_id = Column(Integer, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(String, unique=True, index=True)
    price = Column(String)
    stock = Column(String)
    status = Column(String, default='active')
    created_at = Column(Date)
    updated_at = Column(Date)