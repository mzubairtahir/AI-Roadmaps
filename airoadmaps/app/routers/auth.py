from app.services.auth_service import AuthService
from fastapi import Request, APIRouter, Depends, Response
from app.utils.docs import error_response_schema
from sqlalchemy.orm import Session
from app.core.request_user import RequestUser
from app.services.service_exception import ServiceException
from app.schemas.auth import LoginData
from app.dependencies import get_db, authenticate_user

# Initialize the API router with a prefix for authentication endpoints
router = APIRouter(prefix="/api/auth")


@router.post(
    "/login",
    responses={
        200: {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "user": {"type": "integer"}
                        }
                    }
                }
            }
        },
        401: error_response_schema(description="Invalid token"),
    },
)
async def login(data: LoginData, response: Response, db: Session = Depends(get_db)):
    """
    Handle user login using Google auth access token.
    """
    auth_service = AuthService(db=db)

    try:
        user = await auth_service.login(access_token=data.access_token, response=response)
        return {"user": user.id}
    except ServiceException as e:
        raise e.to_htpp_exception()


@router.post(
    "/logout",
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
async def logout(
    request: Request,
    request_user: RequestUser = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Handle user logout by invalidating the session.
    """
    auth_service = AuthService(db=db)
    await auth_service.logout(session=request_user.session, request=request)
    return


@router.get(
    "/session",
    description="Validate user session and retrieve user details.",
    responses={
        200: {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "user": {"type": "integer"}
                        }
                    }
                }
            }
        },
        401: error_response_schema(),
    },
)
async def session(request_user: RequestUser = Depends(authenticate_user)):
    """
    Validate the current session and fetch user details.
    """
    return {"user": request_user.user.id}
