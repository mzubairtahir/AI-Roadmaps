from app.repositories.user_repository import UserRepository
from fastapi import Depends
from app.models.session import Session
from fastapi import Request
from app.settings import SESSION_COOKIE_NAME
from app.services.service_exception import ServiceException
from app.repositories.session_repository import SessionRepository
from app.utils.oauth_data import get_user_detail


class AuthService:
    def __init__(self, db) -> None:
        """
        Initializes the AuthService class with user and session repositories.

        Args:
            db: Database session dependency.
        """
        self.user_repository = UserRepository(db)
        self.session_repository = SessionRepository(db)

    async def login(self, access_token: str, response) -> dict:
        """
        Logs in a user by verifying the access token, checking if the user exists,
        and creating a session for the user.

        Args:
            access_token (str): The access token to authenticate the user.
            response: The response object to set the session cookie.

        Returns:
            dict: The user object.

        Raises:
            ServiceException: If the access token is invalid or cannot be processed.
        """
        # Get user info from Google using the access token
        user_data = await get_user_detail(access_token=access_token)

        if user_data:
            # Check if the user already exists
            user = self.user_repository.check_user_exists(user_data=user_data)

            if user:
                # If user exists, create a session and set a cookie
                user_session = self.session_repository.create_session(user_id=user.id)
                response.set_cookie(
                    key=SESSION_COOKIE_NAME,
                    value=user_session.session_key,
                    max_age=3600,
                    httponly=True,
                    
                )

                return user

            # If user does not exist, create a new user and session
            user = self.user_repository.create_user(user_data)
            user_session = self.session_repository.create_session(user_id=user.id)

            response.set_cookie(
                key=SESSION_COOKIE_NAME,
                value=user_session.session_key,
                max_age=3600,
                httponly=True,
            )

            return user

        # Raise an exception if the access token is invalid
        raise ServiceException(status_code=401, message="Invalid access token")

    async def logout(self, session: Session, request: Request) -> None:
        """
        Logs out a user by deleting their session and clearing the session cookie.

        Args:
            session (Session): The current user session.
            request (Request): The request object to clear the cookies.
        """
        self.session_repository.delete_session(session.session_key)
        request.cookies.clear()
