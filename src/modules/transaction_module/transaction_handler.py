# from files
from src.modules.transaction_module.transaction_controller import TransactionController
from src.modules.transaction_module.transaction_service import TransactionService

from src.DB.database import sessionlocal

# from packages
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




class TransactionHandler:
    def __init__(self):
        self.router = Router()
        self.transaction_controller = TransactionController(DB = sessionlocal)
        
        @self.router.callback_query(lambda c: c.data.startswith('approve_'))
        async def approve_transaction(callback_query):
            
            transactoin_id = int(callback_query.data.split('_')[1])
            print('approve')

            
