from typing import List
from sqlalchemy.orm import Session # Assuming SQLAlchemy usage
from ..models.room import Room # Import the Room model
# Assuming you have a database model representation, e.g., DB Room model
# from ..db_models.room import Room as DBRoom # Example database model import

def get_living_rooms(db: Session) -> List[Room]:
    """
    Retrieves all rooms from the database that have the status 'living'.

    Args:
        db: The database session.

    Returns:
        A list of Room objects with status 'living'.
    """
    # This is a placeholder implementation.
    # Replace this with your actual database query logic.
    # For example, if using SQLAlchemy:
    # living_rooms_db = db.query(DBRoom).filter(DBRoom.status == 'living').all()
    # Convert DB objects to Pydantic models if necessary
    # living_rooms = [Room.from_orm(room_db) for room_db in living_rooms_db]

    # Placeholder data for demonstration:
    print("Fetching living rooms (placeholder implementation)...")
    # Replace with actual DB query
    all_rooms = [
        {"room_id": "LIVE123XYZ01", "name": "Live Coding Session", "status": "living"},
        {"room_id": "OFF456ABC02", "name": "Gaming Stream", "status": "offline"},
        {"room_id": "LIVE789DEF03", "name": "Music Production Live", "status": "living"},
    ]
    living_rooms = [Room(**room_data) for room_data in all_rooms if room_data["status"] == "living"]

    return living_rooms 