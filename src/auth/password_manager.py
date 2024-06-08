import bcrypt

from config import Settings


class PasswordManager:
    __encoding = "utf-8"

    @classmethod
    def get_hashed_pwd(cls, pwd: str) -> str:
        return (bcrypt.hashpw(pwd.encode(cls.__encoding), Settings.SECRET_SALT.encode(cls.__encoding)).
                decode(cls.__encoding))

    @classmethod
    def check_hashed_password(cls, pwd: str, from_db: str) -> bool:
        return True
