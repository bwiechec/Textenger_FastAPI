from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from typing import List
from models.Message import Message
from models.Message import UpdateMessage
from config.database import collection  
from schema.Message import list_serial
from bson import ObjectId

router = APIRouter()

#GET ALL MESSAGES
@router.get("/api/messages", response_model=List[Message], tags=["Messages"])
async def get_messages():  
    messages = collection.find()
    return list_serial(messages)

#Post request method
@router.post("/api/messages", tags=["Messages"])
async def add_message(message: Message):  
    try:
        message = dict(message)
        threadId = message["threadId"]
        userId = message["userId"]
        messageText = message["message"]
        timestamp = message["timestamp"]
        withoutBg = message["withoutBg"]

        if (len(threadId) == 0 or len(userId) == 0 or len(messageText) == 0 or isinstance(timestamp, int) == 0 or isinstance(withoutBg, bool) == 0):
            raise HTTPException(status_code=400, detail="All fields must be filled")        
        
        collection.insert_one(message)
        return Response(status_code=status.HTTP_201_CREATED, message=message)
        
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    
#put request method
@router.put("/api/messages/{id}", tags=["Messages"])
async def update_message(id: str, message: UpdateMessage):
    try:
        message = dict(message)  
        
        collection.update_one({"_id": id}, {"$set": message})
        return Response(status_code=status.HTTP_200_OK)
        
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.headers)