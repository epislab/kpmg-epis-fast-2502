from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.utils.creational.abstract.abstract_service import AbstractService
from com.epislab.account.auth.user.models.user_schema import UserSchema
from com.epislab.account.auth.user.repositories.mutate_user import create_new_user


class CreateNewUser(AbstractService):
    
    async def handle(self, **kwargs):
        try:
            return "success"
        except Exception as e:
            return "fail"
        

