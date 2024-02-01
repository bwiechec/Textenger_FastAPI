from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from typing import List, Optional
from config.database import collection
from models.User import OptionalUser, User
from schema.User import individual_serial, list_serial
from bson import ObjectId
from pymongo import ASCENDING, DESCENDING

router = APIRouter()

#GET ALL USERS
@router.get("/api/users", tags=["Users"])
async def get_users(filter: OptionalUser = Depends(), order_by: Optional[str] = None, order: Optional[str] = 'asc'):
    # Create a filter if filter_field and filter_value are provided
    query_filter = {k: v for k, v in filter.model_dump().items() if v is not None}

    # Determine the sort order
    sort_order = ASCENDING if order == 'asc' else DESCENDING

    # Query the collection with filter and sort
    users = collection.user.find(query_filter).sort(order_by, sort_order) if order_by else collection.user.find(query_filter)

    return list_serial(users)

#GET SINGLE USER
@router.get("/api/users/{id}", tags=["Users"])
async def get_user(id: str):
    users = collection.user.find({"_id": ObjectId(id)})
    return list_serial(users)

#Post request method
@router.post("/api/users", tags=["Users"])
async def add_user(user: User):
    try:
        user = dict(user)
        name = user["name"]
        lastChangeTimestamp = user["lastChangeTimestamp"]

        if (len(name) == 0 or isinstance(lastChangeTimestamp, int) == 0):
            raise HTTPException(status_code=400, detail="All fields must be filled")

        result = collection.user.insert_one(user)

        new_user = collection.user.find_one({"_id": result.inserted_id})
        return individual_serial(new_user)

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    
#patch request method
@router.patch("/api/users/{id}", tags=["Users"])
async def update_user(id: str, user: User):
    try:
        user = dict(user)  
        user_non_null_fields = {k: v for k, v in user.items() if v is not None}
        
        result = collection.user.update_one({"_id": ObjectId(id)}, {"$set": user_non_null_fields})

        if result.modified_count == 1:
            updated_user = collection.user.find_one({"_id": ObjectId(id)})
            return individual_serial(updated_user)

        else:
            raise HTTPException(status_code=404, detail="User not found")

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    
#delete request method
@router.delete("/api/users/{id}", tags=["Users"])
async def delete_user(id: str):
    try:
        result = collection.user.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 1:
            return Response(status_code=status.HTTP_200_OK)

        else:
            raise HTTPException(status_code=404, detail="User not found")

    except HTTPException as e:
        raise HTTPException(status_code=500, detail=e.detail)
    