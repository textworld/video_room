from typing import List, Optional
from sqlalchemy.orm import Session # Assuming SQLAlchemy usage
from ..models.room import Room # Import the Room model
from ..models.database_models import RoomDB
# Assuming you have a database model representation, e.g., DB Room model
# from ..db_models.room import Room as DBRoom # Example database model import

def get_living_rooms(db: Session) -> List[Room]:
    """
    获取所有状态为"living"的房间。

    Args:
        db: 数据库会话。

    Returns:
        状态为"living"的Room对象列表。
    """
    # 使用SQLAlchemy查询数据库
    living_rooms_db = db.query(RoomDB).filter(RoomDB.status == "living").all()
    
    # 将数据库对象转换为Pydantic模型
    living_rooms = [
        Room(
            room_id=room_db.room_id,
            name=room_db.name,
            status=room_db.status
        ) for room_db in living_rooms_db
    ]

    return living_rooms

def get_room_by_id(db: Session, room_id: str) -> Optional[Room]:
    """
    通过ID获取特定房间。

    Args:
        db: 数据库会话。
        room_id: 房间ID。

    Returns:
        找到的Room对象，如果不存在则返回None。
    """
    room_db = db.query(RoomDB).filter(RoomDB.room_id == room_id).first()
    if not room_db:
        return None
        
    return Room(
        room_id=room_db.room_id,
        name=room_db.name,
        status=room_db.status
    ) 