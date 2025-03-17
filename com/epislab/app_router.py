from fastapi import APIRouter
from com.epislab.account.account_router import router as account_router

router = APIRouter()

router.include_router(account_router)



