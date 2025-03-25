

from com.epislab.account.auth.user.repositories.find_user import login
from com.epislab.utils.creational.abstract.abstract_service import AbstractService


class Login(AbstractService):
    async def handle(self, **kwargs):
        print("😁😁😁😁Login 진입함")
        user_schema = kwargs.get("user_schema")
        db = kwargs.get("db")
        print("🐍🐍🐍🐍user_schema : ", user_schema)
         # user_schema는 dict 또는 객체라고 가정
        user_dict = user_schema if isinstance(user_schema, dict) else user_schema.dict()

        # login 호출
        result = await login(session=db, **user_dict)

        print("🎯🎯🎯🎯login result : ", result)

        return result



        

