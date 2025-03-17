from enum import Enum

class CustomerAction(Enum):
    CREATE_CUSTOMER = "create_customer"
    DELETE_CUSTOMER = "delete_customer"
    REMOVE_CUSTOMER = "remove_customer"

    GET_ALL = "get_all"
    GET_DETAIL = "get_detail"
    FULL_UPDATE = "full_update"
    PARTIAL_UPDATE = "partial_update"
    
    UPDATE_CUSTOMER = "update_customer"
    GET_ALL_CUSTOMER = "get_all_customer"
    GET_DETAIL_CUSTOMER = "get_detail_customer"

    

