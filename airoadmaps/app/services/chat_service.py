from app.schemas.custom_response import CustomResponse
from app.utils.openai_utils import create_learning_roadmap
from app.schemas.roadmaps import Chat
from app.services.roadmaps_service import RoadmapsService


class ChatService:
    """
    Service class for handling chat interactions and generating learning roadmaps.
    """

    def __init__(self, db) -> None:
        """
        Initialize the ChatService instance.

        Args:
            db: Database session used for interacting with the database.
        """
        self.db = db

    async def chat(self, request_user, messages: Chat):
        """
        Handle the chat interaction and generate a learning roadmap.

        Args:
            request_user: The authenticated user making the request.
            messages: The chat message payload containing the user's input.

        Returns:
            dict: A dictionary representing the response, including the creation status
                  and roadmap information (if generated).
        """
        # Call to the utility function to create a learning roadmap based on the input messages
        model_response_result = await create_learning_roadmap(messages=messages)

        # Extract the generated roadmap from the model response
        roadmap = model_response_result.roadmap
        
        if roadmap:
            # If a roadmap was generated, create a new roadmap entry in the database
            roadmap_service = RoadmapsService(self.db)
            roadmap_id = roadmap_service.create_roadmap(request_user.user, roadmap.model_dump())
            
            # Return a successful response with the roadmap ID
            return CustomResponse(
                created=True, message=None, course_id=roadmap_id
            ).model_dump()
        else:
            # If no roadmap was generated, return a failure response with an error message
            return CustomResponse(
                created=False, message=model_response_result.message, course_id=None
            ).model_dump()
