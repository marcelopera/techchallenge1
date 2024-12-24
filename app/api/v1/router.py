from fastapi import APIRouter
from app.api.v1.endpoints import hello, auth

api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello")
api_router.include_router(auth.router, prefix="/auth")