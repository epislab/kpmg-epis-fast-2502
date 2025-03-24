from com.epislab.account.auth.user.models.user_action import UserAction
from com.epislab.account.auth.user.services.user_lookup import Logout
from com.epislab.account.auth.user.services.user_mutation import CreateNewUser
from com.epislab.account.employee.manager.services.manager_lookup import Login


class UserFactory:
    
    _strategy_map = {
        

    UserAction.LOGIN: Login(),
    UserAction.CREATE_NEW_USER: CreateNewUser(),
    UserAction.LOGOUT: Logout(),

    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = UserFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.create(**kwargs)