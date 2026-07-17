# from files
from src.modules.transaction_module.transaction_service import TransactionService


# from packages
from http.client import HTTPException


class TransactionController:
    def __init__(self):
        self.transaction_service = TransactionService


    async def create_transaction(self, data):
        try:
            # create 
            new_transaction = await self.transaction_service.create_transaction(data)

            return new_transaction
        except ValueError as e:
            raise  HTTPException(status_code=400, detail= f'Error creating  transaction: {e}')
        
    async def get_transactions(self):
        try:
            transaction = await self.transaction_service.get_all_transactions()
            if not transaction:
                raise HTTPException(status_code=404, detail= 'not found transaction') 
        except ValueError as e:
            raise HTTPException(status_code=400, detail= f'Error fetching transaction: {e}')
        
        
    async def get_transaction(self, id: int):
        try:
            transaction = await self.transaction_service.get_transaction_by_id(id)
            if not transaction:
                raise HTTPException(status_code=404, detail='not found transaction')
            
        except ValueError as e:
            HTTPException(status_code=400, detail = f'Error fetching transaction: {e}')