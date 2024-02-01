from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
  threadId: str;
  userId: str;
  message: str;
  timestamp: int;
  withoutBg: bool;

class OptionalMessage(BaseModel):
  threadId: Optional[str] = None
  userId: Optional[str] = None
  message: Optional[str] = None
  timestamp: Optional[int] = None
  withoutBg: Optional[bool] = None