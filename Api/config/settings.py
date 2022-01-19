from pydantic import BaseSettings
from functools import lru_cache


@lru_cache()
class Settings(BaseSettings):
    app_name: str
    mongo_url: str
    
    class Config:
        env_file = ".env"