# import for files

# import from packages

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class UserKeyboard:

    @staticmethod
    def main_menu_keyboard() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="🛍 خرید کانفیگ", callback_data="buy_config")
        builder.button(text="👤 حساب کاربری", callback_data="profile")
        builder.button(text="📞 پشتیبانی", callback_data="support")

        builder.adjust(1)

        return builder.as_markup()