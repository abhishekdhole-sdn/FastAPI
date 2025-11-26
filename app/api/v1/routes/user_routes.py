from fastapi import APIRouter
from app.utils.response import send_response

router = APIRouter()

@router.get("/health-check")
def user_route_health_check():
    """
    Basic health checker for User routes.
    """
    return send_response(
        success=True,
        message="User route is working fine.",
        data=None
    )
