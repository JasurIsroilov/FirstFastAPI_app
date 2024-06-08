import re

from fastapi import HTTPException

from users.errors import UsersErrors


class UserManager:

    __email_re_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    __phone_re_pattern = r'Depends on country'

    @classmethod
    def _on_register(cls):
        pass

    @classmethod
    def validate_email(cls, email: str):
        if not re.match(cls.__email_re_pattern, email):
            raise HTTPException(status_code=422, detail=UsersErrors.invalid_email)
        return

    @classmethod
    def validate_phone(cls, phone: str):
        if not re.match(cls.__phone_re_pattern, phone):
            raise HTTPException(status_code=422, detail=UsersErrors.invalid_phone)
        return
