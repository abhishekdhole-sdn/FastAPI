from fastapi import APIRouter
from .user_routes import router as user_router

router = APIRouter()

# Register all route groups here
router.include_router(user_router, prefix="/user", tags=["User"])
