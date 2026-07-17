# from files
from src.modules.order_module.order_state import PaymentState
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from src.modules.order_module.order_controller import OrderController
from src.modules.product_module.product_service import ProductService
from src.modules.transaction_module.transaction_keyboard import TransactionKeyboard
from src.DB.database import sessionlocal

# from packages
from aiogram import Router, F


class OrderHandler:
    def __init__(self):
        self.router = Router()
        self.order_controller = OrderController(DB=sessionlocal)
        self.product_service = ProductService(DB=sessionlocal)
    
        @self.router.callback_query(lambda c: c.data.startswith("order_"))
        async def get_order_handler(callback_query, state: FSMContext ):
            order_id = int(callback_query.data.split("_")[1])
            order = await self.order_controller.get_order(id = order_id)

            await callback_query.message.answer('لطفا عکس فیش پرداخت رو ارسال کنید')

            await state.set_state(PaymentState.waiting_for_receipt)

        @self.router.message(PaymentState.waiting_for_receipt, F.photo)
        async def recive_receipt(message, state: FSMContext):

            file_id = message.photo[-1].file_id

            archive_message = await message.bot.send_photo(
                chat_id ='@transactionfastvpn',
                photo = file_id,
                caption = f'''رسید پرداخت''',
                reply_markup = TransactionKeyboard.checking_transaction(1)
            )

            await message.answer(
                "رسید دریافت شد، در حال بررسی..."
            )

            