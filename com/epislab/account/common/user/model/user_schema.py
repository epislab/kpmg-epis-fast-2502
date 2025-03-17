from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    password: str  # 회원가입 시 사용
    class Config:
       from_attributes = True

# class MemberCreate(MemberBase):
#     password: str  # 회원가입 시 사용

# class MemberResponse(MemberBase):
#     class Config:
#         from_attributes = True  # ✅ Pydantic v2에서는 orm_mode 대신 from_attributes 사용
