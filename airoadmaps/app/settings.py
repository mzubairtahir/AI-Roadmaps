from dotenv import load_dotenv
import os
load_dotenv()


SESSION_COOKIE_NAME = "sessionid"  # cookie name used to set cookie

DATABASE_URL = os.environ.get("DATABASE_URL")

OPENAI_MODEL = os.environ.get("OPENAI_MODEL_NAME")
