# import from files
from src.modules.user_module.user_controller import UserController
from src.api.schemas.user.create_schema import CreateUserSchema, responseCreateUserSchema
from src.api.schemas.user.getone_schema import GetUserSchema
from src.api.schemas.user.getall_schema import GetAllUsersSchema

from src.DB.database import sessionlocal


# import from necessary packages
from fastapi import APIRouter, HTTPException, status


# this not force => in refatory sesion we will change this to class based router
class user_router:
    def __init__(self):
        self.router = APIRouter(tags=['User API'])
        self.user_controller = UserController(DB=sessionlocal)

        # sign in user route
        @self.router.post('/user/signin', response_model=GetUserSchema)
        async def sign_in_user(user: CreateUserSchema):
            created_user = await self.user_controller.sign_in_user(
                telegram_id=user.telegram_id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            if not created_user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User could not be created")
            return created_user
        
        # get user by id route
        @self.router.get('/user/{id}', response_model=GetUserSchema)
        async def get_user(id: int):
            user = await self.user_controller.get_user(id)
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            return user
        
        # get all users route
        @self.router.get('/users', response_model=list[GetAllUsersSchema])
        async def get_all_users():
            users = await self.user_controller.get_all_users()
            return users
        


