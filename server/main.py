from fastapi import FastAPI
import uvicorn # To run the FastAPI app

# Adjust the import path based on your project structure if necessary
try:
    # If main.py is run directly from the server directory
    from app.routers import room_router
except ImportError:
    # If main.py is run from the workspace root (e.g., python server/main.py)
    from server.app.routers import room_router


app = FastAPI(
    title="Video Room API",
    description="API for managing video rooms.",
    version="0.1.0",
)

# Include the room router
# The prefix "/rooms" is already defined in room_router.py
app.include_router(room_router.router)

@app.get("/", tags=["Default"])
async def root():
    """
    Root endpoint providing a welcome message.
    """
    return {"message": "Welcome to the Video Room API"}

# --- Running the App (Example using uvicorn) ---
# This part allows running the server directly using `python server/main.py`
# You might run it differently (e.g., `uvicorn server.main:app --reload`)

def start_server():
    """Starts the FastAPI server using uvicorn."""
    print("Starting FastAPI server...")
    uvicorn.run(
        "server.main:app", # Path to the FastAPI app instance
        host="0.0.0.0",    # Listen on all available network interfaces
        port=8000,         # Port to listen on
        reload=True        # Enable auto-reload for development
                           # Set reload=False in production
    )

if __name__ == "__main__":
    # Note: Running uvicorn directly like this might behave differently
    # than running from the command line, especially with reload.
    # Recommended way for development: uvicorn server.main:app --reload
    start_server()
