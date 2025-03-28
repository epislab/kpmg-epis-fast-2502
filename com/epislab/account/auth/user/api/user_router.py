from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, APIRouter, Body, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from typing import Annotated
from fastapi.responses import JSONResponse
from com.epislab.account.auth.user.api.user_controller import UserController
from com.epislab.account.auth.user.models.user_schema import UserLoginSchema, UserSchema
from com.epislab.utils.config.db_config import get_db


router = APIRouter()
controller = UserController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login", response_model=UserSchema)
async def handle_user(
    response: Response,
    user_schema: UserLoginSchema = Body(...), 
    db: AsyncSession = Depends(get_db)):

    content = await controller.login(user_schema=user_schema, db=db)

    print("🎯🎯🎯🎯content : ", content)
    access_token = content["access_token"]
    refresh_token = content["refresh_token"]
    # ✅ HttpOnly Refresh Token 쿠키로 설정
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,             # HTTPS 환경에서만 사용되도록
        samesite="Lax",          # 또는 'Strict', 'None'
        max_age=60 * 60 * 24 * 7,  # 7일
        path="/",                # 모든 경로에서 유효
    )

    return JSONResponse(content={
        "message": content["message"],
        "access_token": access_token,
        "logged_in_user": content["logged_in_user"]
    })


