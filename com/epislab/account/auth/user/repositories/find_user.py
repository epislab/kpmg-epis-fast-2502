from sqlalchemy import  text          # ✅ SQL 함수만 가져오고

def get_check_user_id_stmt(user_id: str):
    return text("""
        SELECT 1 FROM users
        WHERE user_id = :user_id
        LIMIT 1
    """), {"user_id": user_id}


def get_login_stmt(user_id: str, password: str):
    return text("""
        SELECT * FROM users
        WHERE user_id = :user_id AND password = :password
        LIMIT 1
    """), {
        "user_id": user_id,
        "password": password
    }
