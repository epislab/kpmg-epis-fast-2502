from fastapi import APIRouter
from com.epislab.account.auth.user.api.user_router import router as user_router
from com.epislab.account.guest.customer.api.customer_router import router as customer_router

router = APIRouter()

router.include_router(user_router, prefix="/user")
router.include_router(customer_router, prefix="/customer")