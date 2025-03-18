from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema
from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.storages.create_customer_command import create_customer
from com.epislab.utils.creational.abstract.abstract_service import AbstractService


class CreateCustomer(AbstractService):

    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        new_customer: CustomerSchema = kwargs.get("new_customer")
        try:
            customer = await create_customer(new_customer)
            db.add(customer)
            await db.commit()
            await db.refresh(customer)
            return customer
        except Exception as e:
            print(f"[ERROR] CustomerCreate failed: {e}")
            await db.rollback()
            raise e

