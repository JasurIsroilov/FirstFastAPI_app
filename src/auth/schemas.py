from pydantic import BaseModel


class RegisterSchema(BaseModel):

    email: str
    username: str
    phone_number: str
    password: str

    class Config:
        from_attributes = True
