from pydantic import BaseModel, Field
from typing import Optional

class Room(BaseModel):
    """
    Represents a live streaming room.
    """
    room_id: str = Field(..., max_length=12, description="Unique identifier for the room (12 characters)")
    name: str = Field(..., max_length=30, description="Name of the live room (up to 30 characters)")
    status: str = Field(..., max_length=10, description="Current status of the room (e.g., 'live', 'offline', 'waiting')")

    class Config:
        orm_mode = True # If you plan to use this with an ORM like SQLAlchemy
        schema_extra = {
            "example": {
                "room_id": "ABC123XYZ789",
                "name": "My Awesome Live Stream",
                "status": "live"
            }
        } 