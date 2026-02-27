# import from files 
from src import DB

# import from packages

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class CategoryKeyboard():
    @staticmethod
    def categories_keyboard(categories_list) -> InlineKeyboardMarkup:
        # for category 
        builder = InlineKeyboardBuilder()
        for category in categories_list :
            builder.button(text=category.name, callback_data=category.name)


        builder.adjust(1)

        return builder.as_markup()
    