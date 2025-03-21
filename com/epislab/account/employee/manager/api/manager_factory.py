from com.epislab.account.employee.manager.models.manager_action import ManagerAction



class ManagerFactory:
    
    _strategy_map = {
        
    ManagerAction.DELETE_USER: DeleteManager(),
    ManagerAction.CREATE_NEW_USER: CreateNewManager(),

    ManagerAction.GET_USER_ID: GetManagerId(),

    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = ManagerFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.create(**kwargs)