# import from packages
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# import from files


LOG_DIR = '../logs'
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] => %(message)s',
        datefmt= '%Y-%m-%d %H:%M:%S'

    )

    file_handler = TimedRotatingFileHandler(
        filename=os.path.join(LOG_DIR, f"{name}.log"),
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
