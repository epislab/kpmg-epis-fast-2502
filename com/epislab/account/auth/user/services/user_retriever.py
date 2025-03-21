from sqlalchemy.ext.asyncio import AsyncSession
from app.account.common.user.models.user_entity import UserEntity
from app.utils.creational.abstract.abstract_service import AbstractService

def get_refresh_token(self, db: AsyncSession, refresh_token: str):
        pass


