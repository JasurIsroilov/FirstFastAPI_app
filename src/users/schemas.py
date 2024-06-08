from pydantic import BaseModel

from roles import RolesEnum


class UsersDTO(BaseModel):
    email: str
    username: str
    phone_number: str

    role: RolesEnum

    class Config:
        from_attributes = True
        use_enum_values = True


class UsersReadDTO(BaseModel):
    id: int
    email: str
    username: str
    phone_number: str

    class Config:
        from_attributes = True
        use_enum_values = True


class UsersAddDTO(UsersDTO):
    password: str


class UsersActionDTO(BaseModel):
    id: int
