from datetime import date
from pydantic import BaseModel


class UserRegister(BaseModel):
    first_name: str
    second_name: str
    birthdate: date
    biography: str | None = None
    city: str | None = None
    password: str


class UserOut(BaseModel):
    id: int
    first_name: str
    second_name: str
    birthdate: date
    biography: str | None
    city: str | None
