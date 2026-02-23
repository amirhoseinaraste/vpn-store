# import from files
from src.modules.config_module.config_controller import ConfigController
from src.api.schemas.config.create_schema import CreateConfigSchema, ResponseCreateConfigSchema
from src.api.schemas.config.getone_schema import ResponseGetOneConfigSchema
from src.api.schemas.config.getall_schema import ResponseGetAllConfigsSchema

from src.DB.database import sessionlocal

# import from packages
from fastapi import APIRouter, HTTPException, status


class config_router:
    def __init__(self):
        self.router = APIRouter(tags=['Config API'])
        self.config_controller = ConfigController(DB=sessionlocal)
        
        @self.router.post('/config', response_model=ResponseCreateConfigSchema)
        async def create_config(config: CreateConfigSchema):
            try:
                new_config = await self.config_controller.create_config(product_id=config.product_id, value=config.value)
                return ResponseCreateConfigSchema(id=new_config.id, status="success", created_at=str(new_config.created_at))
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            
        @self.router.get('/config/{id}', response_model=ResponseGetOneConfigSchema)
        async def get_config(id: int):
            config = await self.config_controller.get_config_by_id(id)
            if not config:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
            return ResponseGetOneConfigSchema(id=config.id, product_id=config.product_id, value=config.value, created_at=config.created_at, updated_at=config.updated_at)    
        
        @self.router.get('/configs', response_model=list[ResponseGetAllConfigsSchema])
        async def get_all_configs():
            configs = await self.config_controller.get_all_configs()
            return [ResponseGetAllConfigsSchema(id=config.id, product_id=config.product_id, value=config.value) for config in configs]
        
        @self.router.put('/config/{id}', response_model=ResponseGetOneConfigSchema)
        async def update_config(id: int, config: CreateConfigSchema):
            try:
                updated_config = await self.config_controller.update_config(config_id=id, value=config.value)
                if not updated_config:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
                return ResponseGetOneConfigSchema(id=updated_config.id, product_id=updated_config.product_id, value=updated_config.value, created_at=updated_config.created_at, updated_at=updated_config.updated_at)
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
        @self.router.delete('/config/{id}')
        async def delete_config(id: int):
            try:
                deleted_config = await self.config_controller.delete_config(config_id=id)
                if not deleted_config:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
                return {"status": "success", "message": f"Config with id {id} deleted successfully"}
            except HTTPException as e:
                raise e
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
            
        