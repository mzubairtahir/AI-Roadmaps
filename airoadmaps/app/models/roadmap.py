from app.database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship


# roadmap


class LearningOutcome(Base):
    __tablename__ = "learning_outcomes"

    id = Column(Integer, primary_key=True)

    outcome = Column(String(300), nullable=False)
    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'))
    roadmap = relationship("Roadmap", back_populates="learning_outcomes")


class Prerequisite(Base):

    __tablename__ = "prerequisites"

    id = Column(Integer, primary_key=True)

    requirement = Column(String(300), nullable=False)

    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'))

    roadmap = relationship("Roadmap", back_populates="prerequisites")


class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="roadmaps")

    title = Column(String(100), nullable=False)

    description = Column(String(500), nullable=False)

    project = Column(String(400), nullable=False)

    learning_outcomes = relationship(
        "LearningOutcome", back_populates="roadmap", cascade="all, delete-orphan")

    prerequisites = relationship(
        "Prerequisite", back_populates="roadmap", cascade="all, delete-orphan")

    modules = relationship(
        "Module", back_populates="roadmap", cascade="all, delete-orphan")

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "project": self.project,
            "learning_outcomes": [learning_outcome.outcome for learning_outcome in self.learning_outcomes],
            "prerequisites": [prerequisite.requirement for prerequisite in self.prerequisites],
            "modules": [module.to_dict() for module in self.modules]

        }


# modules of roadmap

class Objective(Base):

    __tablename__ = "objectives"

    id = Column(Integer, primary_key=True)
    module_id = Column(Integer, ForeignKey('modules.id'))
    module = relationship("Module", back_populates="objectives")
    objective = Column(String(200), nullable=False)


class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    project = Column(String(300), nullable=False)
    description = Column(String(200), nullable=False)

    objectives = relationship(
        "Objective", back_populates="module", cascade="all, delete-orphan")

    subtopics = relationship(
        "Subtopic", back_populates="module", cascade="all, delete-orphan")

    roadmap_id = Column(Integer, ForeignKey('roadmaps.id'))
    roadmap = relationship("Roadmap", back_populates="modules")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "subtopics": [subtopic.to_dict() for subtopic in self.subtopics],
            "project": self.project,
            "objectives": [objective.objective for objective in self.objectives]
        }


# subtopics of modules

class Activity(Base):

    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    subtopic_id = Column(Integer, ForeignKey('subtopics.id'))
    subtopic = relationship("Subtopic", back_populates="activities")
    activity = Column(String(200), nullable=False)


class Subtopic(Base):
    __tablename__ = "subtopics"

    id = Column(Integer, primary_key=True)

    title = Column(String(100), nullable=False)

    query = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    module_id = Column(Integer, ForeignKey('modules.id'))
    module = relationship("Module", back_populates="subtopics")

    activities = relationship(
        "Activity", back_populates="subtopic", cascade="all, delete-orphan")

    def to_dict(self):

        return {
            "title": self.title,
            "description": self.description,
            "activities": [activity.activity for activity in self.activities],
            "query": self.query
        }
