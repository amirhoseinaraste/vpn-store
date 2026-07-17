# import from packages
from requests import Session
from sqlalchemy import Transaction
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

# import from file
from src.model.transaction import Transaction 



class TransactionService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_transaction(self, transaction: Transaction):
        async with self.db() as session:
            session.add(transaction)
            await session.commit()
            await session.refresh(transaction)
            return transaction
    
    async def get_transaction_by_id(self, transaction_id: int):
        async with self.db() as session:
            result = await session.execute(select(Transaction).filter(Transaction.id == transaction_id))
            return result.scalars().first()
        
    async def get_transactions_by_user_id(self, user_id: int):
        async with self.db() as session:
            result = await session.execute(select(Transaction).filter(Transaction.user_id == user_id))
            return result.scalars().all()
    
    async def update_transaction_status(self, transaction_id: int, status: str):
        async with self.db() as session:
            transaction = await self.get_transaction_by_id(transaction_id)
            if transaction:
                transaction.status = status
                if status == "approved":
                    transaction.approved_at = datetime.datetime.utcnow()
                await session.commit()
                await session.refresh(transaction)
                return transaction
            return None
        
    async def delete_transaction(self, transaction_id: int):
        async with self.db() as session:
            transaction = await self.get_transaction_by_id(transaction_id)
            if transaction:
                await session.delete(transaction)
                await session.commit()
                return True
            return False
    
    async def get_all_transactions(self):
        async with self.db() as session:
            result = await session.execute(select(Transaction))
            return result.scalars().all()
        
    async def get_transactions_by_status(self, status: str):
        async with self.db() as session:
            result = await session.execute(select(Transaction).filter(Transaction.status == status))
            return result.scalars().all()
        
