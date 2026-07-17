from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

class TransactionKeyboard:
    @staticmethod
    def checking_transaction(id: int):
        
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ تایید پرداخت",
                        callback_data=f"approve_{id}"
                    ),
                    InlineKeyboardButton(
                        text="❌ رد پرداخت",
                        callback_data=f"reject_{id}"
                    ),
                ]
                ]
            )
        return keyboard