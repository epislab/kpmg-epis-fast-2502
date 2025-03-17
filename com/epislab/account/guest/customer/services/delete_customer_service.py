from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from com.epislab.account.guest.customer.service.delete_service import DeleteService

class SoftDeleteStrategy(DeleteService):

    async def delete(self, db: AsyncSession, user_id: str):
        pass

class HardDeleteStrategy(DeleteService):

    async def delete(self, db: AsyncSession, user_id: str):
        pass
