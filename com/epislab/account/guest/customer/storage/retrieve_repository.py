from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from com.epislab.account.employee.customer.models.customer_entity import CustomerEntity
from com.epislab.account.employee.customer.models.customer_schema import CustomerSchema
from com.epislab.account.employee.customer.service.retrieve_service import RetrieveService


class GetAllRepository(RetrieveService):

    async def retrieve(self, db: AsyncSession, **kwargs):
        print("💯🌈 GetAllRepository 로 진입함:")
        query = text("SELECT * FROM member")
        try:
            async with db.begin():  # 🔥 트랜잭션 자동 관리
                result = await db.execute(query)
                records = result.fetchall()
                print("💯🌈 데이터 조회 결과:", records)
                return [dict(record._mapping) for record in records]
        except SQLAlchemyError as e:
            print("⚠️ 데이터 조회 중 오류 발생:", str(e))
            await db.rollback()  # 🔥 오류 발생 시 `rollback()` 수행
            return {"error": "데이터 조회 중 오류가 발생했습니다."}
  

class GetDetailRepository(RetrieveService):

    async def retrieve(self, db: AsyncSession, user_id: str):
        pass


  