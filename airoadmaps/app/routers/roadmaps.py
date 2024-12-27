from fastapi import APIRouter, Depends
from app.core.request_user import RequestUser
from app.dependencies import get_db, authenticate_user
from app.services.roadmaps_service import RoadmapsService
from app.utils.docs import error_response_schema
from app.utils.openai_utils import Roadmap
from app.core.exceptions import CustomHttpException
# Initialize the API router with a prefix for roadmap endpoints
router = APIRouter(prefix="/api/roadmap")


@router.get(
    "/list",
    responses={
        200: {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "title": {"type": "string"}
                            }
                        }
                    }
                }
            }
        },
        401: error_response_schema(),
    },
)
async def get_roadmaps(
    request_user: RequestUser = Depends(authenticate_user), db=Depends(get_db)
):
    """
    Retrieve a list of roadmaps.
    """
    # Initialize the RoadmapsService with the database session
    roadmap_service = RoadmapsService(db=db)

    # Fetch roadmaps for the authenticated user
    data = roadmap_service.get_roadmaps(request_user=request_user)

    # Return the fetched data
    return data


@router.delete(
    "/{id}",
    responses={
        200: {
            "content": {
                "application/json": {
                    "schema": {"type": "null"}
                }
            }
        },
        401: error_response_schema(),
    },
)
async def delete_roadmap(
    id: int, request_user: RequestUser = Depends(authenticate_user), db=Depends(get_db)
):
    """
    Delete a specific roadmap by ID.
    """
    # Initialize the RoadmapsService with the database session
    roadmap_service = RoadmapsService(db=db)

    # Delete the roadmap by ID for the authenticated user
    roadmap_service.delete_roadmap(request_user=request_user, roadmap_id=id)

    # Return no content as the response for successful deletion
    return


@router.get(
    "/{id}",
    responses={
        200: {"model": Roadmap},
        401: error_response_schema(),
    },
)
async def get_roadmap(
    id: int, request_user: RequestUser = Depends(authenticate_user), db=Depends(get_db)
):
    """
    Retrieve a specific roadmap by ID.
    """
    # Initialize the RoadmapsService with the database session
    roadmap_service = RoadmapsService(db=db)

    # Fetch the specific roadmap by ID for the authenticated user
    data = roadmap_service.get_roadmap(request_user=request_user, roadmap_id=id)

    # Return the fetched roadmap data
    return data
