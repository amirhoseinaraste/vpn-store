# Import from files
from src.modules.user_module.user_service import UserService


# import from packages
from fastapi import HTTPException

# todo: implement user controller

class UserController:
    
    def __init__(self, DB):
        self.user_service = UserService(DB)

    #/signinuser => test controller 
    async def sign_in_user(self, telegram_id: int, username: str, first_name: str, last_name: str):
        try:
            # check if user already exists
            existing_user = await self.user_service.get_user(telegram_id)
            if existing_user:
                return existing_user
            
            new_user = await self.user_service.create_user(telegram_id, username, first_name, last_name)
            return new_user
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error creating user: {e}")
        
    # get user by id
    async def get_user(self, id: int):
        try:
            user = await self.user_service.get_user(id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching user: {e}")
        
    # get all user contoller
    async def get_all_users(self):
        try:
            users = await self.user_service.get_all_users()
            return users
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching users: {e}")
        