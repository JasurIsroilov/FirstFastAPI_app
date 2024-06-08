import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    CONFIG_URL = os.getenv("CONFIG_URL")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    SECRET_SALT = os.getenv("SECRET_SALT")

    @classmethod
    def async_db_url(cls):
        return f"postgresql+asyncpg://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
