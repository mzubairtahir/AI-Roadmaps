from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.roadmaps import Chat
# Import necessary Langchain modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from app.settings import OPENAI_MODEL


# Define TypedDicts for structured output

class Subtopic(BaseModel):
    title: str = Field(..., description="The title of the subtopic")
    description: str = Field(
        ..., description="A brief description that explains the content and scope of the subtopic"
    )
    query: str = Field(..., description="Search term or keyword to find relevant resources such as YouTube videos or articles on the web")
    activities: List[str] = Field(
        ..., description="Hands-on exercises the user can perform to apply the knowledge from this subtopic"
    )


class Module(BaseModel):
    title: str = Field(..., description="The title of the module")
    description: str = Field(
        ..., description="A brief description outlining the purpose and scope of the module"
    )
    subtopics: List[Subtopic] = Field(
        ..., description="A list of subtopics within this module, detailing smaller units of knowledge within the module's scope"
    )
    project: str = Field(..., description="A practical project or task based on the content of the module to solidify learning")
    objectives: List[str] = Field(
        ..., description="A clear list of specific learning objectives the user should achieve after completing this module"
    )


class Roadmap(BaseModel):
    title: str = Field(..., description="The title of the course")
    description: str = Field(
        ..., description="A brief description providing an overview of the course, its focus, its purpose, and its target audience"
    )
    learning_outcomes: List[str] = Field(
        ..., description="A list of skills, knowledge, or competencies that the user will gain upon completing the course"
    )
    modules: List[Module] = Field(
        ..., description="A list of modules, each containing relevant subtopics and projects, building a structured learning journey"
    )
    prerequisites: List[str] = Field(
        ..., description="A list of required knowledge, skills, or previous courses that the user should have before starting this course"
    )
    project: str = Field(..., description="Detail of a final project that synthesizes all the learning from the course, offering a practical demonstration of the user's new skills")


class Result(BaseModel):
    valid_query: bool = Field(
        ..., description="Indicates whether the query is valid (related to learning roadmaps).")
    enough_info: bool = Field(
        ..., description="Indicates if the user provided sufficient information (skill level and end goals).")
    roadmap: Optional[Roadmap] = Field(
        None,
        description="The roadmap information will be displayed only if both valid_query and enough_info are true",
    )
    message: Optional[str] = Field(
        None,
        description="A prompt to engage with the user"
        # description="A prompt used to ask for missing information or guide the user when necessary."
    )


async def create_learning_roadmap(messages: Chat) -> Result:
    """
    Generate a personalized learning roadmap based on the user's skill level and end goal.

    Args:
        messages (Chat): The conversation containing details about the user's learning goals.

    Returns:
        Result: A structured learning roadmap or a message prompting for missing information.
    """
    # Initialize OpenAI model
    model = ChatOpenAI(model=OPENAI_MODEL, temperature=0.4)

    # Define the system message template
    system_template = """
    You are a friendly AI assistant created for designing learning roadmaps. Your goal is to engage with the user in a friendly, motivated, and encouraging way to help them create a personalized learning plan.

    ## Instructions:
    1. **Analyze the conversation**: Review the conversation between the user and yourself.
    2. **Identify required information**:
       - **Skill level** (beginner, intermediate, advanced).
       - **End goal** (what the user wants to be able to do by the end after learning, e.g., web development, data science).
    3. **If enough information is provided**:
       - Generate a personalized learning roadmap based on the skill level and goal.
    4. **If enough information is missing**:
       - Create a friendly, engaging message that prompts the user to provide the missing details (e.g., skill level or goal).
       - Keep the tone encouraging and motivating, helping the user feel confident in their learning journey.
       - Continue the conversation until both skill level and end goal are clearly stated.
    """

    # Define the prompt template for chat messages
    messages = messages.model_dump()
    previous_messages = [(i.get("role"), i.get("content"))
                         for i in messages.get("messages")]

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template)] + previous_messages
    )

    input_messages = await prompt_template.ainvoke({})
    structured_llm = model.with_structured_output(Result)

    model_response = await structured_llm.ainvoke(input_messages.to_messages())

    # with open("sampledata.json") as file:
    #     model_response = json.load(file)

    return model_response
