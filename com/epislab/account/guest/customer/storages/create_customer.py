from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.models.customer_entity import CustomerEntity
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from com.epislab.account.guest.customer.service.create_service import CreateService


class DefaultCreateRepository(CreateService):

    async def create(self, new_customer: CustomerSchema, db: AsyncSession):
        print("🚀🤖Repository new_customer 정보 : ", new_customer)
        db.add(CustomerEntity(
            user_id = new_customer.user_id,
            name = new_customer.name,
            email = new_customer.email,
            password = new_customer.password
        ))
        db.commit()
        db.refresh(new_customer)
        return new_customer

class ValidatedCreateRepository(CreateService):

    async def create(self, db: AsyncSession, new_customer: CustomerSchema):
        pass
