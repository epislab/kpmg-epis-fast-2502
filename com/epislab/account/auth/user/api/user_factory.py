from com.epislab.auth.user.models.user_action import UserAction


class UserFactory:
    
    _strategy_map = {    
    UserAction.LOGIN: Login(),
    UserAction.LOGOUT: Logout(),
        
    AuthAction.GET_STORED_REFRESH_TOKEN: GetStoredRefreshToken(),
    AuthAction.REFRESH_ACCESS_TOKEN: RefreshAccessToken(),

  

    }

    @staticmethod
    def create(strategy, **kwargs):
        instance = AuthFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.create(**kwargs)