from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.storages.create_customer import DefaultCreateRepository
from com.epislab.utils.creational.abstract.abstract_service import AbstractService


class CustomerCreate(AbstractService):

    async def handle(self, db: AsyncSession, new_customer: CustomerSchema):
        customer_repo = DefaultCreateRepository()
        return await customer_repo.create(db, new_customer)

