
from pydantic import BaseModel


class LoginData(BaseModel):
    access_token:str


