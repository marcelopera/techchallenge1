from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "MyAPI"
    VERSION: str = "0.0.1-SNAPSHOT"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()