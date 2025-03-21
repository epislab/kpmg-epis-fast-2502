from fastapi import APIRouter
from com.epislab.account.employee.customer.api.customer_router import router as customer_router

router = APIRouter()

router.include_router(customer_router, prefix="/customer")