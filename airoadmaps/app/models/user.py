from app.database import Base
from sqlalchemy.orm import relationship
import bcrypt
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True, nullable=False)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))

    profile_pic = Column(String(2083))

    is_verified = Column(Boolean, nullable=False, default=False)

    roadmaps = relationship(
        "Roadmap", back_populates="user", cascade="all, delete-orphan")
    
    sessions = relationship("Session", back_populates="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        return self.first_name + (f" {self.last_name}" if self.last_name else "")
