from fastapi import FastAPI

from com.epislab.auth.user.user_router import router as user_router
from com.epislab.auth.admin.admin_router import router as admin_router

# python -m uvicorn main:app --reload

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])


@app.get("/")
def read_root():
    return {"main":"메인 라우터"}