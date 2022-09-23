from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CLIENT_ID: str = Field(..., env="CLIENT_ID")
    CLIENT_SECRET: str = Field(..., env="CLIENT_SECRET")
    USERNAME: str = Field(..., env="USERNAME")
    PASSWORD: str = Field(..., env="PASSWORD")

    BOT_NAME: str = Field(..., env="BOT_NAME")
    VERSION: str = Field(..., env="VERSION")
    DEVELOPER: str = Field(..., env="DEVELOPER")


settings = Settings()
