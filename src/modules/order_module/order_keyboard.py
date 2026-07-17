
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class OrderKeyboard:

    @staticmethod
    def confirm_order(order_id: int):

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ تایید سفارش",
                        callback_data=f"order_{order_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="❌ لغو سفارش",
                        callback_data=f"cancel_order_{order_id}"
                    )
                ]
            ]
        )

        return keyboard