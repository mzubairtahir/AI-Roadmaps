
from app.models import Session, User


class RequestUser:

    def __init__(self, session: Session, user: User) -> None:
        self.session = session
        self.user = user
