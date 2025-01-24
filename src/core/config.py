from typing import Dict

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)  # обязательно pydantic_settings a не pydantic!
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(main_dir, '.env')

""" Идем в главную директорию и забираем env"""


class DatabaseConfig(BaseModel):
    convention: Dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    DB_HOST: str  # указываем тип переменных
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    dbconfig: DatabaseConfig = DatabaseConfig()

    @property
    def DATABASE_URL(self):
        """Создаем свойство класса с помощью декоратора property кото
        рый при первом вызове(и при любом другом когда написано property,а не .setter) будет get,то есть будет отдавать нам этот URL
        """
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        # pydantic сам берет переменные из env файла

    model_config = SettingsConfigDict(env_file=file_path)


settings = Settings()
