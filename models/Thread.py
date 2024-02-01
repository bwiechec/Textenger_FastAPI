from pydantic import BaseModel
from typing import Optional

class Thread(BaseModel):
    name: str
    emoji: str
    color_sent: Optional[str] = "bg-blue-500"
    color_received: Optional[str] = "bg-gray-700"
    participants: list[str]

class OptionalThread(BaseModel):
    name: Optional[str] = None
    emoji: Optional[str] = None
    color_sent: Optional[str] = None
    color_received: Optional[str] = None
    participants: Optional[list[str]] = None

class OptionalThreadGet(BaseModel):
    name: Optional[str] = None
    emoji: Optional[str] = None
    color_sent: Optional[str] = None
    color_received: Optional[str] = None
