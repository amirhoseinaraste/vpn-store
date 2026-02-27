# import from files     
from src.DB.database import Base


# import from packages
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

import datetime

# NOTE: ProductStatus enum defined in product model; category doesn't need its own copy.

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tag = Column(String, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime,  default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    parent = relationship('Category', remote_side=[id], backref='children')

    # inverse side of Product.category_rel relationship
    products = relationship("Product", back_populates="category_rel")