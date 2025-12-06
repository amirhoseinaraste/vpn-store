# import from package 
import os
from dotenv import load_dotenv

# TODO: create loader function
def env_loader(key: str):
    # config env
    load_dotenv()

    # return env value
    return os.getenv(key)