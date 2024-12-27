from app.core.exceptions import CustomHttpException


class ServiceException(Exception):
    """
    Custom exception class for service-related errors, encapsulating status code and message.
    """

    def __init__(self, status_code, message) -> None:
        """
        Initialize the ServiceException instance.

        Args:
            status_code: The HTTP status code representing the error.
            message: A detailed error message describing the exception.
        """
        self.status_code = status_code
        self.message = message

    def to_http_exception(self):
        """
        Convert the ServiceException to a CustomHttpException for FastAPI.

        Returns:
            CustomHttpException: The exception to be raised in FastAPI.
        """
        return CustomHttpException(status=self.status_code, message=self.message)
