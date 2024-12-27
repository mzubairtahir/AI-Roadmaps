from sqlalchemy import select
from app.models.user import User
from .base import BaseRepository


class UserRepository(BaseRepository):
    """
    Repository class for interacting with user-related data in the database,
    such as creating new users and checking if a user already exists.
    """

    def __init__(self, db) -> None:
        """
        Initialize the UserRepository instance.

        Args:
            db: Database session used for interacting with the database.
        """
        super().__init__(db)

    def create_user(self, user_data):
        """
        Create a new user in the database using the provided data.

        Args:
            user_data: A dictionary containing user details like email, name, etc.

        Returns:
            User: The created user object.
        """
        # Create a new User object based on the provided data
        user = User(
            email=user_data.get("email"),
            first_name=user_data.get("given_name"),
            last_name=user_data.get("family_name"),
            profile_pic=user_data.get("picture"),
            is_verified=user_data.get("email_verified"),
        )

        # Add the new user to the database and commit the transaction
        self.db.add(user)
        self.db.commit()

        return user

    def check_user_exists(self, user_data):
        """
        Check if a user with the provided email already exists in the database.

        Args:
            user_data: A dictionary containing user details, including the email.

        Returns:
            User or None: The User object if found, otherwise None.
        """
        # Check if a user with the provided email exists in the database
        user = self.db.execute(select(User).where(
            User.email == user_data.get("email"))).scalar_one_or_none()

        return user
