from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.models.customer_entity import CustomerEntity
from com.epislab.account.guest.customer.models.customer_schema import CustomerSchema


async def create_customer(new_customer: CustomerSchema):

    return CustomerEntity(
        user_id = new_customer.user_id,
        name = new_customer.name,
        email = new_customer.email,
        password = new_customer.password
    )


