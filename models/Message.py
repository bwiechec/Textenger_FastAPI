from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
  threadId: str;
  userId: str;
  message: str;
  timestamp: int;
  withoutBg: bool;

class UpdateMessage(BaseModel):
  threadId: Optional[str]
  userId: Optional[str]
  message: Optional[str]
  timestamp: Optional[int]
  withoutBg: Optional[bool]