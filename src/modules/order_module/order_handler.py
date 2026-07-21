# from files
from src.modules.order_module.order_state import PaymentState
from src.modules.order_module.order_controller import OrderController
from src.modules.product_module.product_controller import ProductController
from src.modules.transaction_module.transaction_keyboard import TransactionKeyboard
from src.modules.transaction_module.transaction_controller import TransactionController
from src.model.transaction import Transaction
from src.DB.database import sessionlocal
# from packages
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class OrderHandler:
    def __init__(self):
        self.router = Router()
        self.order_controller = OrderController(DB=sessionlocal)
        self.transaction_controller = TransactionController(DB=sessionlocal)
    
        @self.router.callback_query(lambda c: c.data.startswith("order_"))
        async def get_order_handler(callback_query, state: FSMContext ):
            order_id = int(callback_query.data.split("_")[1])
            await state.update_data(order_id = order_id)

            # change status order
            await callback_query.message.answer('لطفا عکس فیش پرداخت رو ارسال کنید')

            await state.set_state(PaymentState.waiting_for_receipt)

        @self.router.message(PaymentState.waiting_for_receipt, F.photo)
        async def recive_receipt(message, state: FSMContext):
            
            
            order_id = await state.get_data()
            file_id = message.photo[-1].file_id

            archive_message = await message.bot.send_photo(
                chat_id ='@transactionfastvpn',
                photo = file_id,
                caption = f'''رسید پرداخت''',
                reply_markup = TransactionKeyboard.checking_transaction(order_id)
            )

            Transaction = {
                'order_id' : order_id['order_id'],
                'photo_file_id' : file_id,
                'archive_message_id': archive_message.message_id
            }


            create_trx = await self.transaction_controller.create_transaction(data=Transaction)

            await message.answer(
                "رسید دریافت شد، در حال بررسی..."
            )

            
