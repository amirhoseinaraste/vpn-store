

# from packages
from concurrent.futures import wait
from email.mime import message

from aiogram import Router

# from files
from src.DB.database import sessionlocal
from src.modules.product_module.product_service import ProductService
from src.model.order import Order
from src.model.product import Product
from src.modules.order_module.order_controller import OrderController
from src.modules.product_module.product_service import ProductService
from src.modules.category_module.category_controller import CategoryController
from src.modules.product_module.product_controller import ProductController
from src.modules.product_module.product_keyboard import ProductKeyboard
from src.modules.order_module.order_keyboard import OrderKeyboard






class ProductHandler:
    def __init__(self):
        self.router = Router()
        self.product_service = ProductService(DB=sessionlocal)
        self.category_controller = CategoryController(DB=sessionlocal)
        self.product_contorller = ProductController(DB=sessionlocal)

        self.order_controller = OrderController(DB=sessionlocal)

        # select product by id
        @self.router.callback_query(lambda c: c.data.startswith("product_"))
        async def get_product_handler(callback_query):
            product_id = int(callback_query.data.split("_")[1])

            product = await self.product_contorller.get_product_by_id(product_id)
            user = callback_query.from_user
            print(user.id)
            print(product.name)
            order = {
                "user_id":user.id,
                "product_id":product.id,
                "quantity":int(1),
                "total_price":product.price
                
            }
            
            
            invoice = await self.order_controller.create_order(order)

            print(invoice)

            if product:
                
                await callback_query.message.answer(
                    f"""
                🧾 پیش‌فاکتور سفارش

                سلام {user.first_name} عزیز 🌹

                سفارش شما ثبت شد.

                ━━━━━━━━━━━━━━
                📦 محصول: {product.name}
                💰 مبلغ: {product.price:,} ریال
                🔢 تعداد: {invoice.quantity}
                🆔 شماره سفارش: {invoice.id}
                📌 وضعیت: در انتظار تایید
                ━━━━━━━━━━━━━━

                لطفاً سفارش خود را تایید یا لغو کنید.
                """,
                    reply_markup=OrderKeyboard.confirm_order(order_id=invoice.id))
            else:
                await callback_query.answer("Product not found.")


    async def get_products_by_category(self, category_id: int):
        try:
            
            # check if category exists
            category = await self.category_controller.get_category(category_id)
            if category is None:
                raise ValueError(f"Category with id {category_id} does not exist")

            product_list = await self.product_contorller.get_products_by_category_id(category_id)
            if not product_list:
                raise ValueError(f"No products found for category with id {category_id}")
            keyboard = ProductKeyboard().products_keyboard(product_list)

            

            return product_list, keyboard
        
        except ValueError as e:
            raise ValueError(f"Error fetching products: {e}")
