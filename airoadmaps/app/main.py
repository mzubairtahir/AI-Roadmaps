from fastapi import FastAPI
from app.core.exceptions import CustomHttpException
from app.core.exception_handler import custom_http_exception_handler
from app.routers import auth, roadmaps, chat


app = FastAPI()

app.include_router(roadmaps.router)
app.include_router(auth.router)
app.include_router(chat.router)

app.add_exception_handler(CustomHttpException, custom_http_exception_handler)
