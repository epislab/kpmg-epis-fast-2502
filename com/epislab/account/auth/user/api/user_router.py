from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, APIRouter, Body
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from typing import Annotated

from com.epislab.account.auth.user.api.user_controller import UserController
from com.epislab.account.auth.user.models.user_schema import UserLoginSchema, UserSchema
from com.epislab.utils.config.db_config import get_db


router = APIRouter()
controller = UserController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login", response_model=UserSchema)
async def handle_user(
    user_schema: UserLoginSchema = Body(...), 
    db: AsyncSession = Depends(get_db)):

    result = await controller.login(user_schema=user_schema, db=db)

    print("🎯🎯🎯🎯result : ", result)

    return JSONResponse(content={"message": result.message, "data": result.data})


