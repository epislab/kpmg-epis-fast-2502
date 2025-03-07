from pydantic import BaseModel, EmailStr

class MemberBase(BaseModel):
    user_id: str
    email: EmailStr
    name: str

class MemberCreate(MemberBase):
    password: str  # 회원가입 시 사용

class MemberResponse(MemberBase):
    class Config:
        from_attributes = True  # ✅ Pydantic v2에서는 orm_mode 대신 from_attributes 사용
