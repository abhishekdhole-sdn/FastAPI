from fastapi.responses import JSONResponse

def send_response(
    success: bool,
    message: str,
    data=None,
    errors=None,
    status_code: int = 200
):
    """
    Standardized API response wrapper.

    Args:
        success (bool): Operation status
        message (str): Status message
        data (any, optional): Response payload
        errors (dict/list/str, optional): Error details
        status_code (int): HTTP status code

    Returns:
        JSONResponse
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": success,
            "message": message,
            "data": data,
            "errors": errors
        }
    )
