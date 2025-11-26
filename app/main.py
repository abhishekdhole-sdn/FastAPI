"""
Main entry file for FastAPI application.
Integrates global send_response() for consistent API responses.
Includes global CORS configuration.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.utils.response import send_response
from app.api.v1.routes import router as api_router

# ---------------------------
# Initialize FastAPI App
# ---------------------------
app = FastAPI(
    title="My API",
    version="1.0",
    description="A sample FastAPI project using standardized responses."
)

# ---------------------------
# Global CORS configuration
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Register all versioned API routes
# ---------------------------
app.include_router(api_router, prefix="/api/v1")


# ---------------------------
# Global Validation Error Handler
# ---------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {err['loc'][-1]: err['msg'] for err in exc.errors()}
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation error",
            "errors": errors,
            "data": None
        }
    )


# ---------------------------
# Health Check API
# ---------------------------
@app.get("/health-check")
def health_check():
    return send_response(
        success=True,
        message="Server is running successfully.",
        data={"status": "ok"}
    )
