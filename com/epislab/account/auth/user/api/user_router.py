from fastapi import Query, Depends, HTTPException, APIRouter, Body
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.auth.web.auth_controller import AuthController
from app.auth.web.auth_service import create_jwt
from app.utils.creational.builder.db_builder import get_db
from app.utils.creational.factory.token_factory import oauth2_scheme

router = APIRouter()
controller = UserController()


@router.post("/user/refresh")
async def refresh_access_token(
    refresh_token: Annotated[str, Depends(oauth2_scheme)],
    action: str = Query(default="refresh"),
    db: AsyncSession = Depends(get_db),):
    
    if action == "refresh":
        # ✅ DB 또는 Redis에서 refresh_token 검증
        stored_token = await controller.get_stored_refresh_token(db, refresh_token)
        if not stored_token:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    
        # ✅ 새로운 access_token 발급
        new_access_token = await controller.refresh_access_token(refresh_token)

    return JSONResponse(content={"message": "Success", "new_access_token": new_access_token})


# ✅ FastAPI 라우터 추가 (임시 토큰 발급용)
router = APIRouter()

@router.get("/user/token")
def get_test_token():
    """테스트용 JWT 토큰 생성"""
    token = create_jwt({"user_id": "test-user"})
    return {"access_token": token, "token_type": "bearer"}