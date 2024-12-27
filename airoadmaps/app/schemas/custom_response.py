from typing import List, Literal , Optional
from pydantic import BaseModel



class CustomResponse(BaseModel):
    created: bool
    message: Optional[str]
    course_id:Optional[int]