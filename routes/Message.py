from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from typing import List, Optional
from models.Message import Message
from models.Message import OptionalMessage
from config.database import collection  
from schema.Message import individual_serial, list_serial
from bson import ObjectId
from pymongo import ASCENDING, DESCENDING

router = APIRouter()

#GET ALL MESSAGES
@router.get("/api/messages", tags=["Messages"])
async def get_messages(filter: OptionalMessage = Depends(), order_by: Optional[str] = None, order: Optional[str] = 'asc'):  
    # Create a filter if filter_field and filter_value are provided
    query_filter = {k: v for k, v in filter.model_dump().items() if v is not None}

    # Determine the sort order
    sort_order = ASCENDING if order == 'asc' else DESCENDING

    # Query the collection with filter and sort
    messages = collection.message.find(query_filter).sort(order_by, sort_order) if order_by else collection.message.find(query_filter)

    return list_serial(messages)

#GET SINGLE MESSAGE
@router.get("/api/messages/{id}", tags=["Messages"])
async def get_message(id: str):  
    messages = collection.message.find({"_id": ObjectId(id)})
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
        
        
        result = collection.message.insert_one(message)
    
        new_message = collection.message.find_one({"_id": result.inserted_id})
        return individual_serial(new_message)
        
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    
#patch request method
@router.patch("/api/messages/{id}", tags=["Messages"])
async def update_message(id: str, message: OptionalMessage):
    try:
        message = dict(message)  
        message_non_null_fields = {k: v for k, v in message.items() if v is not None}

        
        collection.message.update_one({"_id": ObjectId(id)}, {"$set": message_non_null_fields})
    
        new_message = collection.message.find_one({"_id": ObjectId(id)})
        return individual_serial(new_message)
        
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.headers)
    
#delete request method
@router.delete("/api/messages/{id}", tags=["Messages"])
async def delete_message(id: str):
    try:
        collection.message.delete_one({"_id": ObjectId(id)})
        return Response(status_code=status.HTTP_200_OK)
        
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.headers)