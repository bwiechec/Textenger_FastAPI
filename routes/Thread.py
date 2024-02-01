from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi import Response
from typing import List, Optional
from models.Thread import Thread, OptionalThread, OptionalThreadGet
from config.database import collection  
from schema.Thread import individual_serial, list_serial
from bson import ObjectId
from pymongo import ASCENDING, DESCENDING

router = APIRouter()

#GET ALL THREADS
@router.get("/api/threads", tags=["Threads"])
async def get_threads(filter: OptionalThreadGet = Depends(), participant: Optional[str] = None,order_by: Optional[str] = None, order: Optional[str] = 'asc', limit: Optional[int] = None, offset: Optional[int] = None):
    # Create a filter if filter_field and filter_value are provided
    query_filter = {k: v for k, v in filter.model_dump().items() if v is not None and k != "participants"}
    if participant:
        query_filter["participants"] = {"$in": participant.split(",")}

    # Determine the sort order
    sort_order = ASCENDING if order == 'asc' else DESCENDING

    limit = limit if limit else 0
    offset = offset if offset else 0

    # Query the collection with filter and sort
    threads = collection.thread.find(query_filter).sort(order_by, sort_order).limit(limit).skip(offset) if order_by else collection.thread.find(query_filter)

    return list_serial(threads)

#GET SINGLE THREAD
@router.get("/api/threads/{id}", tags=["Threads"])
async def get_thread(id: str):
    threads = collection.thread.find({"_id": ObjectId(id)})
    return list_serial(threads)

#Post request method
@router.post("/api/threads", tags=["Threads"])
async def add_thread(thread: Thread):
    try:
        thread = dict(thread)
        name = thread["name"]
        emoji = thread["emoji"]
        color_sent = thread["color_sent"]
        color_received = thread["color_received"]
        participants = thread["participants"]

        if (len(name) == 0 or len(emoji) == 0 or len(color_sent) == 0 or len(color_received) == 0 or len(participants) == 0):
            raise HTTPException(status_code=400, detail="All fields must be filled")

        result = collection.thread.insert_one(thread)

        new_thread = collection.thread.find_one({"_id": result.inserted_id})
        return individual_serial(new_thread)

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    
#patch request method
@router.patch("/api/threads/{id}", tags=["Threads"])
async def update_thread(id: str, thread: Thread):
    try:
        thread = dict(thread)  
        thread_non_null_fields = {k: v for k, v in thread.items() if v is not None}
        
        collection.thread.update_one({"_id": ObjectId(id)}, {"$set": thread_non_null_fields})

        updated_thread = collection.thread.find_one({"_id": ObjectId(id)})
        return individual_serial(updated_thread)

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    
#delete request method
@router.delete("/api/threads/{id}", tags=["Threads"])
async def delete_thread(id: str):
    try:
        result = collection.thread.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 1:
            return Response(status_code=status.HTTP_200_OK)

        else:
            raise HTTPException(status_code=404, detail="Thread not found")

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
