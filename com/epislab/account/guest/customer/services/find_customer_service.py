from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from com.epislab.account.guest.customer.storages.find_customer import GetAllRepository, GetDetailRepository
from com.epislab.utils.creational.abstract.abstract_service import AbstractService

class FindCustomers(AbstractService):

    async def handle(self, db: AsyncSession, **kwargs):
        retrieve_repo = GetAllRepository()
        try:
            result = await retrieve_repo.retrieve(db, **kwargs)
            return result
        except SQLAlchemyError as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            return {"error": "데이터 조회 중 오류가 발생했습니다."}