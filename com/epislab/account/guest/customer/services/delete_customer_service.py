from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.employee.customer.models.customer_schema import CustomerSchema
from com.epislab.utils.creational.abstract.abstract_service import AbstractService

class DeleteCustomer(AbstractService):

    async def handle(self, db: AsyncSession, user_id: str):
        pass

class RemoveCustomer(AbstractService):

    async def handle(self, db: AsyncSession, user_id: str):
        pass
