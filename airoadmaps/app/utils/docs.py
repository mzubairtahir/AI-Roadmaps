def error_response_schema(description: str = None):
    """
    Generates a standardized error response schema.

    Args:
        description (str, optional): A description of the error response. Defaults to None.

    Returns:
        dict: The error response schema in JSON format.
    """
    return {
        "description": description,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "object",
                            "properties": {
                                "status": {"type": "integer"},
                                "message": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }
