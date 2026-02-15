# import from packages
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import datetime

# import from file
from src.model.user import User

# TODO: implement user service
class UserService:

    def __init__(self, DB: AsyncSession):
        # Inject database
        self.db = DB
    
    async def get_user(self, telegram_id: int):
        async with self.db() as session:
            # find user by telegram_id
            result = await session.execute(select(User).where(User.telegram_id == telegram_id))
            user = result.scalars().first()
            return user
    
    async def get_all_users(self):
        async with self.db() as session:
            # find all users from db
            result = await session.execute(select(User))
            return result.scalars().all()

    async def create_user(self, telegram_id: int, username: str, first_name: str, last_name: str):
        async with self.db() as session:
            # create object of user model
            new_user = User(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )

            # add user to database
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)

            return new_user

    # need to develop after create product and order module  
    def update_user(self, telegram_id: str, status: str):
        pass
    
    # need to test
    async def delete_user(self, telegram_id: str):
        async with self.db() as session:
            result = await session.execute(select(User).where(User.telegram_id == int(telegram_id)))
            user = result.scalars().first()
            if user:
                await session.delete(user)
                await session.commit()
                return True
            return False

