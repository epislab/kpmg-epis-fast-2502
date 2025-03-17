from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from com.epislab.account.guest.customer.storages.find_customer import GetAllRepository, GetDetailRepository
from com.epislab.utils.creational.abstract.abstract_service import AbstractService

class FindCustomers(AbstractService):

    async def handle(self, db: AsyncSession, **kwargs):
        pass