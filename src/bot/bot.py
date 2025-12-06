# import from files
from utils.env_loader import env_loader
from utils.logger import setup_logger
from .handler.main_handlers import Handler

# import from packages
from aiogram import Bot, Dispatcher, Router
from aiogram.types import FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage

# config bot logger
logger = setup_logger('Bot')

# TODO: Init bot

class tel_bot:
    TOKEN = str(env_loader('BOT_TOKEN'))
    WEBHOOK_URL = str(env_loader('WEBHOOK_URL'))
    BOT_USERNAME = str(env_loader('BOT_USERNAME'))

    def __init__(self):
        self.bot = Bot(token=self.TOKEN)
        self.dp = Dispatcher(storage=MemoryStorage())
        self.router = Router()
        
    
    # update data process
    async def update_data(self, data):
        logger.info(f'Processed:{data.update_id}')
        await self.dp._process_update(self.bot, update=data)

    # set webhook
    async def set_webhook(self):
        try:
            # cert key for production
            cert = ''

            # delete last webhook
            await self.bot.delete_webhook()
            webhook_info = await self.bot.set_webhook(url= self.WEBHOOK_URL)


            # check webhook conection
            if webhook_info:
                logger.info('webhook set succsesfuly')
                self.config_handler()
            else:
                raise Exception('webhook is not set')
        except Exception as e:
            logger.info(str(e))

    
    # config bot handler
    def config_handler(self):
        logger.info('config bot handlers')
        self.router.include_routers(Handler().router)
