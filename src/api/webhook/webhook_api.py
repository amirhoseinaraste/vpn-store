# import from packages
from fastapi import APIRouter, Request
from aiogram.types import Update

# import from files
from bot.bot import tel_bot

# TODO: init webhook

class webhook_router:
    def __init__(self):
        self.router = APIRouter(tags=['Webhook API'])
        self.bot = tel_bot()

        # update webhook router
        @self.router.post('/webhook')
        async def update_webhook(req: Request):
            data = await req.json()
            update_Data = Update(**data)
            await self.bot.update_data(update_Data)

            return {'status': 'ok'}
        
        # set webhook router
        @self.router.get('/set_webhook')
        async def set_webhook():
            await self.bot.set_webhook()
            return {'status': 'ok'}