from fastapi import Request
from app.core.response_format import ErrorResponseFormat
from fastapi.responses import JSONResponse
from app.core.exceptions import CustomHttpException


async def custom_http_exception_handler(request: Request, exception: CustomHttpException):

    return JSONResponse(
        status_code=exception.status,
        content=ErrorResponseFormat(status=exception.status, message=exception.message).to_dict())
