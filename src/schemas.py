from datetime import date
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    lastname: str = Field(max_length=30)
    email: EmailStr
    phone: str = Field(max_length=15)
    birthday: date
    additional_info: str = Field(max_length=300)


class ResponseContact(BaseModel):
    id: int
    name: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: date
    additional_info: str

    class Config:
        orm_mode = True


