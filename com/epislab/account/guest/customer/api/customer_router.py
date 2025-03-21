from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from com.epislab.account.employee.customer.models.customer_schema import CustomerSchema
from com.epislab.account.employee.customer.api.customer_controller import CustomerController
from com.epislab.utils.config.db_config import get_db



router = APIRouter()
controller = CustomerController()

@router.post(path="/create")
async def create_customer(new_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    print("🎉🎉 create_customer 로 진입함")
    print("new_customer : ",new_customer)
    return await controller.create_customer(db=db, new_customer=new_customer)

@router.get(path="/detail")
async def get_customer_by_id(user_id: str, db: AsyncSession = Depends(get_db)):
    return await controller.get_customer_by_id(db=db, user_id=user_id)


# 응답 구조를 정의하는 모델
class CustomerListResponse(BaseModel):
    customer_list: List[CustomerSchema]


@router.get("/list", response_model=CustomerListResponse)
async def get_all_customers( db: AsyncSession = Depends(get_db)):
    print("🎉🎉 get_customers 로 진입함")
    customers = await controller.get_all_customers(db=db)
    return {
        "customer_list": customers
    }

    
@router.put(path="/update")
async def update_customer(update_customer: CustomerSchema, db: AsyncSession = Depends(get_db)):
    return await controller.update_customer(db=db, update_customer=update_customer)

@router.delete(path="/delete")
async def delete_customer(user_id: str, db: AsyncSession = Depends(get_db)):
    return await controller.delete_customer(db=db, user_id=user_id)
