from sqlalchemy import select, func, text          # ✅ SQL 함수만 가져오고
from sqlalchemy.engine import Result   
from com.epislab.account.auth.user.repositories.find_user import get_check_user_id_stmt, get_login_stmt
from com.epislab.utils.creational.abstract.abstract_service import AbstractService


class Login(AbstractService):
    async def handle(self, **kwargs):
        print("😁😁😁😁Login 진입함")
        user_schema = kwargs.get("user_schema")
        db = kwargs.get("db")
        print("🐍🐍🐍🐍user_schema : ", user_schema)
         # user_schema는 dict 또는 객체라고 가정
        # user_schema는 dict 또는 Pydantic 모델
        user_dict = user_schema if isinstance(user_schema, dict) else user_schema.dict()

        user_id = user_dict.get("user_id")
        password = user_dict.get("password")

        # 1단계: user_id 존재 여부 확인
        check_stmt, check_params = get_check_user_id_stmt(user_id)
        check_result: Result = await db.execute(check_stmt, check_params)

        if check_result.fetchone() is None:
            return {
                "message": "고객에서 등록된 ID가 없습니다",
                "data": {}
            }

        # 2단계: user_id + password 검사
        login_stmt, login_params = get_login_stmt(user_id, password)
        login_result: Result = await db.execute(login_stmt, login_params)

        row = login_result.fetchone()

        if row is None:
            return {
                "message": "비밀번호가 일치하지 않습니다",
                "data": {}
            }

        # 3단계: 로그인 성공
        return {
            "message": "로그인에 성공했습니다",
            "data": dict(row._mapping)
        }



        

