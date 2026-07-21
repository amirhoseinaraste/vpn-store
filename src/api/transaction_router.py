from src.modules.transaction_module.transaction_controller import TransactionController
from src.api.schemas.transaction.get_all_transaction import ResponseGetAllTransactionsSchema
from src.DB.database import sessionlocal


from fastapi import APIRouter, HTTPException, status


class  tansaction_router:
    def __init__(self):
        self.router = APIRouter(tags=['Transaction_API'])
        self.transaction_controller = TransactionController(DB= sessionlocal)

        @self.router.get('/transactions', response_model=list[ResponseGetAllTransactionsSchema])
        async def get_transactions():
            transactions = await self.transaction_controller.get_transactions()
            return [ResponseGetAllTransactionsSchema(id=transaction.id, order_id=transaction.order_id, photo_file_id=transaction.photo_file_id, archive_message_id=transaction.archive_message_id, status=transaction.status) for transaction in transactions]
