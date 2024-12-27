from sqlalchemy import Column, Integer, String,  Text, DateTime, ForeignKey
import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class Session(Base):

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    session_key = Column(String(40), unique=True, index=True)
    session_data = Column(Text, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="sessions")
    user_id =  Column(Integer, ForeignKey('users.id'), nullable=False)

    def is_expired(self):

        current_time = datetime.datetime.now(datetime.timezone.utc)

        if self.expires_at < current_time:
            return True

        return False
