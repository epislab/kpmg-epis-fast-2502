
from app.utils.creational.factory.password_factory import PasswordFactory
from sqlalchemy.sql import delete
from sqlalchemy.ext.asyncio import AsyncSession
password_factory = PasswordFactory()

async def create_new_user(new_user: UserSchema):
    
    hashed_password = password_factory.create(new_user.password)

    return UserEntity(
        user_id=new_user.user_id,
        personal_id=new_user.personal_id,
        survey_id=new_user.survey_id,
        member_number=new_user.member_number,
        roles=new_user.roles,
        fullname=new_user.fullname,
        nickname=new_user.nickname,
        gender=new_user.gender,
        birth_date=new_user.birth_date,
        email=new_user.email,
        phone=new_user.phone,
        street=new_user.street,
        suburb=new_user.suburb,
        postcode=new_user.postcode,
        profile_image=new_user.profile_image,
        password=hashed_password,  # 해싱된 비밀번호 저장
    )
    
async def delete_user_by_id(user_id: str):

    return delete(UserEntity).where(UserEntity.user_id == user_id)



async def remove_user_by_id(db: AsyncSession, user_id: str):
    the_user = db.query(UserEntity).filter(UserEntity.user_id == user_id).first()
    if the_user:
        db.delete(the_user)
        db.commit()
    return the_user