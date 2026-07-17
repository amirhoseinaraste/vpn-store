# import from files
from src.DB.database import Base

# import from packages
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, Float
from sqlalchemy.orm import relationship
import datetime
import enum

class ProductStatus(enum.Enum):
    available = "available"
    inactive = "inactive"
    out_of_stock = "out_of_stock"


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    volume = Column(Integer)
    duration = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    status = Column(Enum(ProductStatus), default=ProductStatus.available)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    category = relationship("Category", back_populates="products")
    # configs = relationship('Config', back_populates='product', cascade='all, delete-orphan')
    # transactions = relationship('Transaction', back_populates='product', cascade='all, delete-orphan')








