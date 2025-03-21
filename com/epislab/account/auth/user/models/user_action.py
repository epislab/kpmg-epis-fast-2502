from enum import Enum

class UserAction(Enum):
    
    # auth_service
    GET_STORED_REFRESH_TOKEN = "get_stored_refresh_token"
    REFRESH_ACCESS_TOKEN = "refresh_access_token"

    # user_service
    LOGIN = "login"
    LOGOUT = "logout"
    
