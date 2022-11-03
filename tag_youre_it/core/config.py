from typing import Any, Dict, Optional

from pydantic import BaseSettings, Field, PostgresDsn, validator


class Settings(BaseSettings):
    CLIENT_ID: str = Field(default="", env="CLIENT_ID")
    CLIENT_SECRET: str = Field(default="", env="CLIENT_SECRET")
    USERNAME: str = Field(default="", env="USERNAME")
    PASSWORD: str = Field(default="", env="PASSWORD")

    BOT_NAME: str = Field(default="", env="BOT_NAME")
    VERSION: str = Field(default="", env="VERSION")
    DEVELOPER: str = Field(default="", env="DEVELOPER")

    POSTGRES_USER: str = Field(default="", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(default="", env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(default="", env="POSTGRES_HOST")
    POSTGRES_PORT: str = Field(default="", env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(default="", env="POSTGRES_DB")

    DB_POOL_SIZE: int = Field(default=83, env="DB_POOL_SIZE")
    WEB_CONCURRENCY: int = Field(default=9, env="WEB_CONCURRENCY")
    POOL_SIZE: Optional[int]
    POSTGRES_URL: Optional[str]

    @validator("POOL_SIZE", pre=True)
    def build_pool(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, int):
            return v

        return max(values.get("DB_POOL_SIZE") // values.get("WEB_CONCURRENCY"), 5)

    @validator("POSTGRES_URL", pre=True)
    def build_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=str(values.get("POSTGRES_PORT")),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


settings = Settings()
