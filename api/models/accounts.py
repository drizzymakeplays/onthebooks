from pydantic import BaseModel, validator
from jwtdown_fastapi.authentication import Token
from datetime import datetime


class DuplicateAccountError(ValueError):
    pass


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    birthday: str
    email: str
    password: str
    role: str

    @validator("birthday")
    def parse_dob(cls, v):
        return datetime.strptime(v, "%m-%d-%Y").date()


class AccountOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    birthday: str
    email: str
    role: str


class AccountOutWithHashedPassword(AccountOut):
    hashed_password: str


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut
