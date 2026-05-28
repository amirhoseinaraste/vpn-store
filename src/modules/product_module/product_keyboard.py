# import from fiels

# import from packages
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup    

class ProductKeyboard():

    @staticmethod
    def products_keyboard(products_list):
        # for category 
        builder = InlineKeyboardBuilder()
        for product in products_list :
            builder.button(text=product.name, callback_data=product.name)


        builder.adjust(1)

        return builder.as_markup()