from fastapi import APIRouter, Depends
from app.dependencies import get_db, authenticate_user
from app.schemas.roadmaps import Chat
from app.utils.docs import error_response_schema
from app.schemas.custom_response import CustomResponse
from app.services.chat_service import ChatService

# Initialize the API router with a prefix for chat endpoints
router = APIRouter(prefix="/api/chat")


@router.post(
    "",
    responses={
        200: {"model": CustomResponse},
        401: error_response_schema(),
    },
)
async def chat(data: Chat, request_user=Depends(authenticate_user), db=Depends(get_db)):
    """
    Handle chat interactions.
    """
    # Extract chat messages from the payload
    messages = data

    # Initialize the ChatService with the database session
    chat_service = ChatService(db=db)

    # Process the chat messages using the service
    response_data = await chat_service.chat(request_user=request_user, messages=messages)

    # Return the processed response
    return response_data
