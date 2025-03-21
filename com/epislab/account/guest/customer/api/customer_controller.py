from com.epislab.account.employee.customer.api.customer_factory import CustomerFactory
from com.epislab.account.employee.customer.models.customer_action import CustomerAction

class CustomerController:

    def __init__(self):
        pass

    async def create_customer(self, **kwargs):
        print("🍔🍔🍔🍔 CustomerController -> create_customer 로 진입함")
        return await CustomerFactory.create(strategy=CustomerAction.CREATE_CUSTOMER, **kwargs)

    async def get_customer_by_id(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.GET_CUSTOMER_BY_ID, **kwargs)

    async def get_all_customers(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.GET_ALL_CUSTOMERS, **kwargs)

    async def update_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.UPDATE_CUSTOMER, **kwargs)

    async def delete_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.DELETE_CUSTOMER, **kwargs)


