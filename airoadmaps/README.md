# AI Roadmaps Backend

This directory is backend service for the **AI Roadmaps** project, enabling functionalities like user authentication, roadmap management, and agent interaction through chat. 

---

## Features

- **User Authentication**:
  - Google login
  - Session validation
  - Logout functionality
- **Chatbot**:
  - Chat with an AI-powered agent
- **Roadmap Management**:
  - Retrieve roadmap details
  - List all roadmaps for a user
  - Delete roadmaps
- **API Documentation**:
  - Swagger documentation available at `/docs`

---

## Prerequisites

Ensure the following are installed on your system:

- Python `>= 3.11`
- SQLite (default database) or another database of your choice
- Virtual environment setup (optional but recommended)

Environment variables setup:
- **`OPENAI_API_KEY`**: API key for OpenAI integration
- **`DATABASE_URL`**: URL for the database connection
- **`OPENAI_MODEL_NAME`**: Name of OpenAI model that you want to use as agent. **Example:** "gpt-4o-mini"


---

## How to setup

1. Open the terminal in this directory:

2. Create a virtual environment named `venv`:
   ```bash
   python -m venv venv
   source act-env.sh
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file:
   - Create a `.env` file in the root directory.
   - Add the following environment variables:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     DATABASE_URL=your_database_url
     OPENAI_MODEL_NAME=model_name
     ```

5. Install the database driver (if using a database other than SQLite). For example:
   ```bash
   pip install psycopg2-binary  # PostgreSQL driver
   ```

6. Apply database migrations:
   ```bash
   source makemigrations.sh <migration_message>
   source migrate.sh
   ```

---

## Usage

### Running the application
Start the backend service:
```bash
source runapp.sh
```

The application will run on `http://127.0.0.1:8000/` by default.

---

## Project Structure

- **`app/`**: Core application directory containing all the backend components.  

- **`app/settings.py`**: Configuration file for the project.

- **`app/main.py`**: Entry point of the application, initializing the FastAPI app object and setting up routes.

## Design of the app
The design of the app follows a layered architecture to ensure modularity, maintainability, and clear separation of concerns:

1. **Repository Layer**:  
   - Acts as an abstraction over the database, providing methods for querying and persisting data.  
   - Ensures that the database logic is encapsulated and reusable across the application.  
   - Examples: Fetching user records, saving new roadmaps, and deleting data.

2. **Service Layer**:  
   - Contains the core business logic of the application.  
   - Implements the rules and processes for application functionality, such as validating session tokens, managing roadmaps, and handling AI-based chatbot requests.  
   - This layer ensures clean separation between data handling (Repository) and API interaction.

3. **API Layer**:  
   - Defines the API endpoints exposed to the client.  
   - Connects incoming requests to the appropriate service methods.  
   - Example routes include:
     - `/api/auth/` for user authentication
     - `api/roadmap/` for roadmap management
     - `/api/chat/` for chatbot interactions  


## Technologies Used

- **Framework**: FastAPI
- **Database**: SQLite (default) or any database supported by SQLAlchemy
- **ORM**: SQLAlchemy with Alembic for migrations
- **AI Integration**: LangChain, OpenAI

---

## API Documentation

Interactive API documentation is available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)