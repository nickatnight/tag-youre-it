from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CLIENT_ID: str = Field(default="", env="CLIENT_ID")
    CLIENT_SECRET: str = Field(default="", env="CLIENT_SECRET")
    USERNAME: str = Field(default="", env="USERNAME")
    PASSWORD: str = Field(default="", env="PASSWORD")

    BOT_NAME: str = Field(default="", env="BOT_NAME")
    VERSION: str = Field(default="", env="VERSION")
    DEVELOPER: str = Field(default="", env="DEVELOPER")


settings = Settings()
