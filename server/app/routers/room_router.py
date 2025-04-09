from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session # Assuming SQLAlchemy usage

from ..models.room import Room # Import the response model
from ..services.room_service import get_living_rooms # Import the service function
# Assuming you have a dependency function to get the DB session
# from ..dependencies import get_db # Example import for DB session dependency

# Placeholder for the database dependency function
# Replace this with your actual dependency injection logic
def get_db_placeholder():
    print("Getting DB session (placeholder)...")
    # In a real app, this would yield a SQLAlchemy Session
    # For example:
    # from ..database import SessionLocal # Assuming SessionLocal is your session factory
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
    yield None # Placeholder yield

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"], # Tag for Swagger UI grouping
    responses={404: {"description": "Not found"}}, # Default response for not found
)

@router.get("/living", response_model=List[Room])
async def read_living_rooms(db: Session = Depends(get_db_placeholder)):
    """
    Retrieve all rooms currently in 'living' status.
    """
    living_rooms = get_living_rooms(db) # Call the service function
    return living_rooms 