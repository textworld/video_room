from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models.room import Room
from ..services.room_service import get_living_rooms, get_room_by_id
from ..database import get_db

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.get("/", response_model=List[Room])
async def get_all_living_rooms(db: Session = Depends(get_db)):
    """
    获取所有直播中的房间。
    """
    return get_living_rooms(db)

@router.get("/{room_id}", response_model=Room)
async def get_room(room_id: str, db: Session = Depends(get_db)):
    """
    通过ID获取房间信息。
    """
    room = get_room_by_id(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail=f"未找到ID为{room_id}的房间")
    return room 