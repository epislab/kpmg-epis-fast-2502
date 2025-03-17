from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.guest.customer.models.customer_action import CustomerAction
from com.epislab.account.guest.customer.services.create_customer_service import CreateCustomer
from com.epislab.account.guest.customer.services.delete_customer_service import DeleteCustomer, RemoveCustomer
from com.epislab.account.guest.customer.services.get_customer_service import GetAllCustomers, GetCustomerById
from com.epislab.account.guest.customer.services.update_customer_service import UpdateCustomer, PatchCustomer
class CustomerFactory:

    _strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer(),
        CustomerAction.REMOVE_CUSTOMER: RemoveCustomer(),
        CustomerAction.GET_ALL_CUSTOMERS: GetAllCustomers(),
        CustomerAction.GET_CUSTOMER_BY_ID: GetCustomerById(),
        CustomerAction.UPDATE_CUSTOMER: UpdateCustomer(),
        CustomerAction.PATCH_CUSTOMER: PatchCustomer(),
    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = CustomerFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return await instance.handle(**kwargs)
    

    # 복잡한 것을 간단하게 변경함

    # @staticmethod
    # async def execute(
    #     strategy: StrategyType, 
    #     method: Literal["create", "retrieve", "update", "delete"], 
    #     db: AsyncSession,
    #     **kwargs
    # ):
    #     instance = CustomerFactory.strategy_map.get(strategy)
    #     if not instance:
    #         raise ValueError(f"Invalid strategy: {strategy}")
        
    #     if not hasattr(instance, method):
    #         raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

    #     method_to_call = getattr(instance, method)

    #     # 비동기 메서드 여부 확인 후 실행
    #     if callable(method_to_call):
    #         if method == "retrieve":  # retrieve는 비동기 실행
    #             return await method_to_call(db=db, **kwargs)
    #         else:
    #             return await method_to_call(db=db, **kwargs)
    #     else:
    #         raise TypeError(f"Method '{method}' is not callable.")
