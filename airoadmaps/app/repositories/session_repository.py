import pickle
import base64
from datetime import datetime, timedelta
import secrets

from app.models.session import Session
from .base import BaseRepository
from sqlalchemy import select


class SessionRepository(BaseRepository):
    """
    Repository class for managing user sessions, including encoding/decoding session data,
    creating, retrieving, and deleting sessions.
    """

    def __init__(self, db) -> None:
        """
        Initialize the SessionRepository instance.

        Args:
            db: Database session used for interacting with the database.
        """
        super().__init__(db)

    def __encode_data(self, data):
        """
        Encode session data by pickling and base64 encoding it.

        Args:
            data: The data to encode.

        Returns:
            bytes: The base64-encoded pickled data.
        """
        pickled_dict = pickle.dumps(data)
        encoded_dict = base64.b64encode(pickled_dict)

        return encoded_dict

    def __decode_data(self, encoded_data):
        """
        Decode base64-encoded session data and unpickle it back into a dictionary.

        Args:
            encoded_data: The base64-encoded session data.

        Returns:
            dict: The decoded and unpickled session data.
        """
        decoded_bytes = base64.b64decode(encoded_data)
        unpickled_dict = pickle.loads(decoded_bytes)

        return unpickled_dict

    def create_session(self, user_id):
        """
        Create a new session for a user.

        Args:
            user_id: The ID of the user for whom the session is created.

        Returns:
            Session: The created session object.
        """
        session_key = secrets.token_urlsafe(30)  # Generate a secure random session key
        current_dt = datetime.now()  # Current timestamp
        delta = timedelta(hours=1)  # Session expiration time (1 hour from now)
        expires_at = current_dt + delta  # Calculate expiration timestamp

        # Encode session data (user ID)
        session_data = self.__encode_data(data={"uid": user_id})

        # Create the session object
        user_session = Session(
            session_key=session_key,
            expires_at=expires_at,
            session_data=session_data,
            user_id=user_id
        )

        # Commit the session to the database
        self.db.add(user_session)
        self.db.commit()

        return user_session

    def get_session(self, session_key):
        """
        Retrieve a session by its session key.

        Args:
            session_key: The session key to look up.

        Returns:
            Session or None: The session object if found, else None.
        """
        session = self.db.execute(select(Session).where(
            Session.session_key == session_key)).scalar_one_or_none()

        return session

    def delete_session(self, session_key):
        """
        Delete a session by its session key.

        Args:
            session_key: The session key of the session to delete.
        """
        session = self.get_session(session_key)
        if session:
            # Delete the session from the database
            self.db.delete(session)
            self.db.commit()
