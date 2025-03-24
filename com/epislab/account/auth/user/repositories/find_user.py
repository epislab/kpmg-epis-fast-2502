from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func 
from com.epislab.account.auth.user.models.user_entity import UserEntity

async def login(**kwargs):
    
    user_id = kwargs.get("user_id")
    password = kwargs.get("password")
    
    return select(UserEntity).where(
        UserEntity.user_id == user_id,
        UserEntity.password == password
    )

async def logout(**kwargs):
    pass
