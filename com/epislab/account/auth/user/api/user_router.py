from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, APIRouter, Body, Query
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from typing import Annotated

from com.epislab.account.auth.user.api.user_controller import UserController
from com.epislab.account.auth.user.models.user_schema import UserSchema
from com.epislab.utils.config.db_config import get_db


router = APIRouter()
controller = UserController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/", response_model=UserSchema)
async def handle_user(
    op: str = Query(default="create"),
    user_schema: UserSchema = Body(UserSchema()), 
    db: AsyncSession = Depends(get_db)):
    
    if op == "login":
        pass
            

    return JSONResponse(content={"message": "", "result": ""})


@router.delete("/")
async def delete_user_by_id(
    op: str = Query(default="delete"),
    db: AsyncSession = Depends(get_db)):
        
    if op == "logout":
        print("User logout successfully") 
            
    return JSONResponse(content={"message": ""})
