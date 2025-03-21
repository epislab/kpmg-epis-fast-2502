from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.account.auth.user.models.user_entity import UserEntity
from com.epislab.account.auth.user.models.user_schema import UserSchema




def refresh_access_token(self, db: AsyncSession, refresh_token: str):
        pass

def login(self, db: AsyncSession, user_id: str):
        pass

def logout(self, db: AsyncSession, user_id: str):
        pass