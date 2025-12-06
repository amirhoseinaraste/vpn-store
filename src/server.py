# import from files
from utils.env_loader import env_loader
from utils.logger import setup_logger
from app import App

# import from packages 
import uvicorn


# config server log
logger = setup_logger('server')

# TODO : Init server

class Server:
    HOST = str(env_loader('HOST'))
    PORT = int(env_loader('PORT'))

    def __init__(self):
        self.server = App()

    # run server method
    def run(self):
        logger.info('server running')

        uvicorn.run(self.server.app, host= self.HOST, port=self.PORT, log_level='info')

if __name__ == '__main__':
    app = Server()
    app.run()
