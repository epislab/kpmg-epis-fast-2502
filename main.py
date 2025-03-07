from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
import os
from fastapi import FastAPI
from com.epislab.design_pattern.creational.builder.db_builder import get_db

app = FastAPI()

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

    
@app.get("/users")
async def get_users(db=Depends(get_db)):
    print("🎉🎉 get_users 로 진입함")
    query = "SELECT * FROM member"
    try:
        results = await db.fetch(query)
        print("💯🌈 데이터 조회 결과:", results)
        # JSON 형태로 반환
        return {"users": [dict(record) for record in results]}
    except Exception as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        return {"error": "데이터 조회 중 오류가 발생했습니다."}
