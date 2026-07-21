from enum import Enum

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship

from src.DB.database import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    photo_file_id = Column(String, nullable=False)

    archive_message_id = Column(Integer, nullable=False)

    status = Column(
        String,
        nullable=True,
        default='pending'
    )

    orders = relationship('Order', back_populates='transaction')

