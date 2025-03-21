from com.epislab.account.auth.user.models.user_action import UserAction
from com.epislab.account.auth.user.api.user_factory import UserFactory

class UserController:
    def __init__(self):
        pass

    def get_stored_refresh_token(self, **kwargs):
        return UserFactory.create(UserAction.GET_STORED_REFRESH_TOKEN, **kwargs)
    
    
    def refresh_access_token(self, **kwargs):
        return UserFactory.create(UserAction.REFRESH_ACCESS_TOKEN, **kwargs)