from fastapi import Depends, Request
from app.core.request_user import RequestUser
from app.repositories.session_repository import SessionRepository
from app.settings import SESSION_COOKIE_NAME
from app.database import SessionFactory
from sqlalchemy.orm import Session
from app.core.exceptions import CustomHttpException
import traceback


def get_db():
    """
    Creates and manages the database session lifecycle.

    Yields:
        session: A SQLAlchemy session for database interactions.
    
    Raises:
        CustomHttpException: In case of any exceptions during DB operations.
    """
    session = SessionFactory()

    try:
        yield session
    except Exception as e:
        traceback.print_exc()  # For logging purposes, ideally this should be replaced with a proper logging mechanism
        session.rollback()

        if isinstance(e, CustomHttpException):
            raise e

        raise CustomHttpException(status=500, message="Error occurred at our end")
    finally:
        session.close()


def authenticate_user(request: Request, db: Session = Depends(get_db)):
    """
    Authenticates the user based on the session cookie.

    Args:
        request (Request): The incoming HTTP request containing the session cookie.
        db (Session): The database session dependency.

    Returns:
        RequestUser: The authenticated user object.

    Raises:
        CustomHttpException: If authentication fails or session is invalid.
    """
    sessionid = request.cookies.get(SESSION_COOKIE_NAME)

    if not sessionid:
        raise CustomHttpException(
            status=401, message="Authentication required. Please provide valid credentials."
        )

    session_repository = SessionRepository(db)
    session = session_repository.get_session(session_key=sessionid)

    if not session:
        raise CustomHttpException(
            status=401, message="Authentication required. Please provide valid credentials."
        )

    user = session.user if session else None
    request_user = RequestUser(session=session, user=user)

    return request_user
