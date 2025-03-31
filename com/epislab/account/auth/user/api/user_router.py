import os
from fastapi.security import OAuth2PasswordBearer
from jose import ExpiredSignatureError, JWTError, jwt
from fastapi import Depends, APIRouter, Body, HTTPException, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from typing import Annotated
from fastapi.responses import JSONResponse
from com.epislab.account.auth.user.api.user_controller import UserController
from com.epislab.account.auth.user.models.user_schema import UserLoginSchema, UserSchema
from com.epislab.utils.config.db_config import get_db
from com.epislab.utils.config.security.redis_config import redis_client

router = APIRouter()
controller = UserController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")


@router.get("/refresh", response_model=UserSchema)
async def refresh_token(request: Request, db: AsyncSession = Depends(get_db)):

    # 1. 쿠키 또는 헤더에서 토큰 꺼내기 (여기선 쿠키 예시)
    incoming_token = request.cookies.get("refresh_token")
    print("🎯🎯🎯🎯incoming_token : ", incoming_token)
    if not incoming_token:
        raise HTTPException(status_code=400, detail="💥💥💥💥Refresh token is missing")

    try:
        payload = jwt.decode(incoming_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="💥💥💥💥Invalid token payload")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="💥💥💥💥Refresh token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="💥💥💥💥Invalid refresh token")

    # 2. Redis에서 토큰 검증
    stored_token = await redis_client.get(f"refresh_token:{user_id}")
    print("🎯🎯🎯🎯stored_token : ", stored_token)
    if stored_token != incoming_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")




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


