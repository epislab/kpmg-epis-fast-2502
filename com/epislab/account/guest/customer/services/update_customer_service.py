

from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from com.epislab.utils.creational.abstract.abstract_service import AbstractService


class UpdateCustomer(AbstractService):

    async def handle(self, db: AsyncSession, update_customer: CustomerSchema):
        pass

class PatchCustomer(AbstractService):

    async def handle(self, db: AsyncSession, update_customer: CustomerSchema):
        pass
