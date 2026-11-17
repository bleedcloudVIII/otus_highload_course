from datetime import date
from pydantic import BaseModel


class UserRegister(BaseModel):
    first_name: str
    second_name: str
    birthdate: str
    biography: str | None = None
    city: str
    password: str


class UserOut(BaseModel):
    id: int
    first_name: str
    second_name: str
    birthdate: date | None
    biography: str
    city: str
