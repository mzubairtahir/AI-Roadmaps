from typing import List, Literal
from pydantic import BaseModel



class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class Chat(BaseModel):
    messages: List[Message]
