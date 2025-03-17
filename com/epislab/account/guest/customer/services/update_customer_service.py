

from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from com.epislab.account.guest.customer.service.update_service import UpdateService


class FullUpdateStrategy(UpdateService):

    async def update(self, db: AsyncSession, update_customer: CustomerSchema):
        pass

class PartialdUpdateStrategy(UpdateService):

    async def update(self, db: AsyncSession, update_customer: CustomerSchema):
        pass
