# impoort from files

# import from packages

from http.client import HTTPException

from src.modules.config_module.config_service import ConfigService


class ConfigController:
    def __init__(self, DB):
        self.config_service = ConfigService(DB)

    # create config controller
    async def create_config(self, product_id: int, value: str):
        try:
            check_configs = await self.config_service.get_configs_by_product_id(product_id) 
            if len(check_configs) >= 5:
                raise ValueError("Maximum of 5 configs per product allowed")
            new_config = await self.config_service.create_config(product_id, value)
            return new_config
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error creating config: {e}")
        
    async def get_configs_by_product_id(self, product_id: int):
        try:
            configs = await self.config_service.get_configs_by_product_id(product_id)
            return configs
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching configs: {e}")
        
    async def get_config_by_id(self, config_id: int):
        try:
            config = await self.config_service.get_config_by_id(config_id)
            if not config:
                raise HTTPException(status_code=404, detail="Config not found")
            return config
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching config: {e}")
        
    async def get_configs(self):
        try:
            configs = await self.config_service.get_all_configs()
            return configs
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error fetching configs: {e}")
        
        
    async def update_config(self, config_id: int, value: str):
        try:
            updated_config = await self.config_service.update_config(config_id, value)
            if not updated_config:
                raise HTTPException(status_code=404, detail="Config not found")
            return updated_config
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error updating config: {e}")
        
    async def delete_config(self, config_id: int):
        try:
            deleted_config = await self.config_service.delete_config(config_id)
            if not deleted_config:
                raise HTTPException(status_code=404, detail="Config not found")
            return deleted_config
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error deleting config: {e}")
        
