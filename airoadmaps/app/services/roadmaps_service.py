from app.repositories.roadmaps_repository import RoadmapsRepository
from app.schemas.custom_response import CustomResponse
from app.core.exceptions import CustomHttpException


class RoadmapsService:
    """
    Service class for handling operations related to roadmaps, such as retrieving,
    creating, and deleting roadmaps.
    """

    def __init__(self, db) -> None:
        """
        Initialize the RoadmapsService instance.

        Args:
            db: Database session used for interacting with the roadmap repository.
        """
        self.roadmap_repository = RoadmapsRepository(db)

    def get_roadmap(self, request_user, roadmap_id):
        """
        Retrieve a specific roadmap by its ID, ensuring that the user has access.

        Args:
            request_user: The authenticated user making the request.
            roadmap_id: The ID of the roadmap to retrieve.

        Returns:
            dict: The roadmap data as a dictionary.

        Raises:
            CustomHttpException: If no roadmap is found or the user doesn't own it.
        """
        roadmap = self.roadmap_repository.get_roadmap(id=roadmap_id)

        # Check if the roadmap exists and if the user has permission to access it
        if roadmap and roadmap.user_id == request_user.user.id:
            return roadmap.to_dict()

        # Raise an exception if the roadmap is not found or the user doesn't have access
        raise CustomHttpException(
            status=404, message="No roadmap found for this identifier")

    def get_roadmaps(self, request_user):
        """
        Retrieve all roadmaps for a specific user.

        Args:
            request_user: The authenticated user making the request.

        Returns:
            list: A list of roadmaps owned by the user.
        """
        roadmaps = self.roadmap_repository.get_roadmaps(request_user.user)

        # If roadmaps exist, return them
        if roadmaps:
            return roadmaps

        return []

    def create_roadmap(self, user, roadmap_data):
        """
        Create a new roadmap for a user.

        Args:
            user: The user who owns the new roadmap.
            roadmap_data: The data for the new roadmap.

        Returns:
            dict: The created roadmap's data.
        """
        return self.roadmap_repository.create_roadmap(user=user, data=roadmap_data)

    def delete_roadmap(self, request_user, roadmap_id):
        """
        Delete a specific roadmap for a user.

        Args:
            request_user: The authenticated user making the request.
            roadmap_id: The ID of the roadmap to delete.
        """
        self.roadmap_repository.delete_roadmap(
            request_user.user, id=roadmap_id)
