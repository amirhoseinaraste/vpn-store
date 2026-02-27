# import from packages
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

# import from files
from src.utils.env_loader import env_loader
from src.utils.logger import setup_logger

logger = setup_logger('database')
logger.info('database init')

# init database
database_URI = str(env_loader('DB_URI'))
engine = create_async_engine(database_URI, echo=True)
sessionlocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


