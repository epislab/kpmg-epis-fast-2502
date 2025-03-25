from com.epislab.account.auth.user.models.user_action import UserAction
from com.epislab.account.auth.user.services.user_mutation import CreateNewUser


class UserFactory:
    
    _strategy_map = {
        

    UserAction.CREATE_NEW_USER: CreateNewUser(),

    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = UserFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.create(**kwargs)