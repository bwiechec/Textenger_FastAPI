from pydantic import BaseModel
from typing import Optional

class User(BaseModel):    
    name: str
    lastChangeTimestamp: int

class OptionalUser(BaseModel):   
    name: Optional[str] = None
    lastChangeTimestamp: Optional[int] = None