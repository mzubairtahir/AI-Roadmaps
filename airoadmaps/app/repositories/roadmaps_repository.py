from app.repositories.base import BaseRepository
from app.models.user import User
from sqlalchemy import select
from app.models.roadmap import Roadmap, Module, Subtopic, Activity, Objective, Prerequisite, LearningOutcome


class RoadmapsRepository(BaseRepository):
    """
    Repository class for interacting with the Roadmap-related data models,
    such as Roadmap, Module, Subtopic, Activity, Objective, Prerequisite, and LearningOutcome.
    """

    def __init__(self, db) -> None:
        """
        Initialize the RoadmapsRepository instance.

        Args:
            db: Database session used for interacting with the database.
        """
        super().__init__(db)

    def get_roadmaps(self, user: User):
        """
        Retrieve a list of roadmaps for a specific user.

        Args:
            user: The user for whom the roadmaps are to be retrieved.

        Returns:
            list: A list of roadmaps, with each containing the ID and title.
        """
        roadmaps = self.db.execute(select(Roadmap.id, Roadmap.title).where(
            Roadmap.user_id == user.id
        )).mappings().all()

        return roadmaps

    def get_roadmap(self, id):
        """
        Retrieve a specific roadmap by its ID.

        Args:
            id: The ID of the roadmap to retrieve.

        Returns:
            Roadmap: The roadmap object if found, or None if not.
        """
        roadmap = self.db.execute(select(Roadmap).where(
            Roadmap.id == id
        )).scalar_one_or_none()

        return roadmap

    def delete_roadmap(self, user, id):
        """
        Delete a specific roadmap if it belongs to the given user.

        Args:
            user: The authenticated user making the request.
            id: The ID of the roadmap to delete.
        """
        roadmap = self.get_roadmap(id=id)
        
        # Ensure the user owns the roadmap before deleting
        if roadmap and roadmap.user_id == user.id:
            self.db.delete(roadmap)
            self.db.commit()

    def create_roadmap(self, user: User, data):
        """
        Create a new roadmap based on the provided data.

        Args:
            user: The user who will own the new roadmap.
            data: A dictionary containing the roadmap and related data.

        Returns:
            int: The ID of the newly created roadmap.
        """
        # Create the new roadmap
        new_roadmap = Roadmap(
            title=data.get("title"), 
            user_id=user.id,
            description=data.get("description"),
            project=data.get("project"),
        )

        # Add modules to the roadmap
        for module in data.get("modules", []):
            new_module = Module(
                title=module.get("title"),
                project=module.get("project"),
                description=module.get("description"),
                roadmap=new_roadmap
            )

            # Add subtopics to the module
            for subtopic in module.get("subtopics", []):
                new_sub_topic = Subtopic(
                    title=subtopic.get("title"),
                    query=subtopic.get("query"),
                    description=subtopic.get("description"),
                    module=new_module
                )

                # Add activities to the subtopic
                activities = [Activity(activity=activity, subtopic=new_sub_topic)
                              for activity in subtopic.get("activities", [])]
                new_sub_topic.activities.extend(activities)

                # Add subtopic to the module
                new_module.subtopics.append(new_sub_topic)

            # Add objectives to the module
            objectives = [Objective(objective=objective, module=new_module)
                          for objective in module.get("objectives", [])]
            new_module.objectives.extend(objectives)

            # Add module to the roadmap
            new_roadmap.modules.append(new_module)

        # Add prerequisites and learning outcomes to the roadmap
        prerequisites = [Prerequisite(requirement=prerequisite, roadmap=new_roadmap)
                         for prerequisite in data.get("prerequisites", [])]
        learning_outcomes = [LearningOutcome(
            outcome=learning_outcome, roadmap=new_roadmap) for learning_outcome in data.get("learning_outcomes", [])]

        new_roadmap.prerequisites.extend(prerequisites)
        new_roadmap.learning_outcomes.extend(learning_outcomes)

        # Commit the new roadmap to the database
        self.db.add(new_roadmap)
        self.db.commit()

        # Refresh the roadmap object to include the database-generated ID
        self.db.refresh(new_roadmap)

        return new_roadmap.id
