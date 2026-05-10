from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str

    APP_HOST: str
    APP_PORT: int

    DEBUG: bool = False

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REDIS_URL: str

    OLLAMA_BASE_URL: str
    OLLAMA_MODEL: str

    STORAGE_TYPE: str
    LOCAL_STORAGE_PATH: str

    class Config:
        env_file = ".env"


settings = Settings()