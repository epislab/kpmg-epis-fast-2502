from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.employee.customer.models.customer_entity import CustomerEntity
from com.epislab.account.employee.customer.models.customer_schema import CustomerSchema
from com.epislab.account.employee.customer.service.delete_service import DeleteService


class SoftDeleteRepository(DeleteService):

    async def delete(self,  db: AsyncSession, user_id: str):
        print("🚀🤖DeleteRepository user_id 정보 : ", user_id)
       
        return None

class HardDeleteRepository(DeleteService):

    async def delete(self, db: AsyncSession, user_id: str):
        pass
