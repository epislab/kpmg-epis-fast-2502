from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from com.epislab.utils.config.db_config import init_db, engine
from com.epislab.app_router import router as app_router

# ✅ FastAPI 애플리케이션 생성
app = FastAPI()

# ✅ 애플리케이션 시작 시 `init_db()` 실행
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀🚀🚀🚀 FastAPI 앱이 시작됩니다. 데이터베이스 초기화 중...")
    await init_db()  # ✅ DB 초기화 실행
    print("✅ 데이터베이스 초기화 완료!")
    yield  # 애플리케이션이 실행되는 동안 유지
    print("🛑 FastAPI 앱이 종료됩니다.")
    await engine.dispose()  # 🔥 모든 커넥션 정리
    print("✅ DB 연결이 정상적으로 종료되었습니다.")

# ✅ 라우터 등록
app.include_router(app_router)

def current_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
    <h2>{current_time()}</h2>
</div>
</body>
""")

    

