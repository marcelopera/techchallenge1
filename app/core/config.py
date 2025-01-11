from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "TECH_CHALLENGE_1"
    VERSION: str = "0.0.1-SNAPSHOT"
    API_V1_STR: str = "/api/v1"
    pythondontwritebytecode: str = "1"
    pythonunbuffered: str = "1"
    
    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()