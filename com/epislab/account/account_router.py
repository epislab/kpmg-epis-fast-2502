from fastapi import APIRouter
from com.epislab.account.auth.user.api.user_router import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/user")