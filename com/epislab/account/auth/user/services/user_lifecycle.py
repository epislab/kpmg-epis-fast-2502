from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.utils.creational.abstract.abstract_service import AbstractService
from com.epislab.account.auth.user.models.user_schema import UserSchema
from com.epislab.account.auth.user.repositories.create_user import create_new_user


class CreateNewUser(AbstractService):
    
    async def handle(self, db: AsyncSession, new_user: UserSchema):
        try:
            user_entity = await create_new_user(new_user)
            db.add(user_entity) # 비동기 I/O 작업(DB 접근)이 아니므로 await를 붙일 필요가 없음
            await db.commit()
            return "success"
        except Exception as e:
            print(e)
            await db.rollback()
            return "fail"
        
class LoginUser(AbstractService):
    async def handle(self, db: AsyncSession, user_id: str):
        pass

class LogoutUser(AbstractService):
    async def handle(self, db: AsyncSession, user_id: str):
        pass
        
class DeleteUserById(AbstractService):
    
    async def handle(self, db: AsyncSession, user_id: str):
        try:
            # 삭제할 사용자 조회
            result = await db.execute(await get_user_by_id(user_id))
            user_to_delete = result.scalars().first()

            if not user_to_delete:
                return {"message": "User not found", "status": "failed"}

            # 사용자 삭제 실행
            await db.execute(delete_user_by_id(user_id))
            await db.commit()  # 트랜잭션 반영

            return {"message": "User deleted successfully", "status": "success", "user": user_to_delete}

        except Exception as e:
            print(f"[ERROR] User deletion failed: {e}")
            await db.rollback()
            raise e



class RemoveUser(AbstractService):
    
    async def handle(self, db: AsyncSession, user_id: str):
        the_user = await remove_user(db=db, user_id=user_id)
        if the_user:
            db.delete(the_user)
            db.commit()
        return the_user