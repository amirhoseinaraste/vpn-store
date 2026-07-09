# import from files     
from src.DB.database import Base

# import from packages
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime


class statusEnum:
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Transaction(Base):
    __tablename__ = 'Transaction'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=True)
    user_id = Column(Integer, nullable=False)
    config_id = Column(Integer, ForeignKey('Configs.id'), nullable=True)
    amount = Column(Integer, nullable=False)
    status = Column(String, default=statusEnum.pending)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    approved_at = Column(DateTime, nullable=True)

    
