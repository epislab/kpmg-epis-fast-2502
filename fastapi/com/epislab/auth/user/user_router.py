from fastapi import APIRouter
from com.epislab.auth.user.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/")
def hello():
    return user_service.hello()

def add_user(self, user):
    print(f"컨트롤러➕사용자 추가: {user}")
    return UserService().add_user(user)


def get_user(self, user):
    print(f"컨트롤러✍️사용자 조회: {user}")
    return user

def update_user(self, user):
    print(f"컨트롤러🌻사용자 수정: {user}")
    return user


def delete_user(self, user):    
    print(f"컨트롤러😈사용자 삭제: {user}")
    return "Success"