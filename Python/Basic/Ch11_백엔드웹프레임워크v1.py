import time, sqlite3, os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. 현재 파이썬 파일이 있는 폴더의 절대 경로를 알아냅니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. 그 폴더 안에 my_database.db를 만들도록 경로를 하나로 합칩니다.
DB_PATH = os.path.join(BASE_DIR, "my_database.db")

app = FastAPI(title="Path Parameter Tutorial")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # users 테이블이 없다면 생성해라! (id, name, age 칸 만들기)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       age INTEGER)
        """)
        conn.commit()

init_db()

class UserCreate(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "FastAPI 서버가 정상 실행되었습니다."}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    특정 사용자의 정보를 조회하는 단일 데이터 조회 API입니다.
    - **user_id**: URL 경로에서 추출되는 변수입니다.
    - 파이썬 타입 힌트(int)를 명시했으므로, FastAPI가 내부적으로 문자열 URL을 정수로 자동 변환(Casting)합니다.
    """

    # [동작 원리 예시]
    # 요청: GET http://localhost:8000/users/3
    # 결과: user_id 변수에는 정수 3이 안전하게 할당됩니다.
    return{
        "user_id": user_id,
        "status": "active",
        "message": f"성공적으로 {user_id}번 유저의 데이터를 가져왔습니다."
    }

@app.get("/files/{file_name}")
def download_file(file_name: str):
    return {"message": f"{file_name} 다운로드 시작"}

@app.get("/files/{upload_guide}")
def get_upload_guide():
    return {"message": "파일 업로드 가이드 문서"}

@app.post("/users")
def create_user(user: UserCreate):
    # 1. user 변수에 데이터가 담겨서 들어옵니다. (아직 메모리에만 있음)
    
    # 2. 반드시 데이터베이스(SQLite 등)를 열고 INSERT 문을 실행해 하드디스크에 기록해야 합니다.
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))
        conn.commit()

    return {"message": f"{user.name}님의 정보가 DB에 저장되었습니다!", "path": DB_PATH}

@app.get("/users/name/{user_name}")
def get_user_name(user_name: str):
    """
    URL 마지막에 입력된 문자열(이름)을 받아 DB에서 검색합니다.
    예: GET /users/name/홍길동
    """

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # 1. Parameterized Query 적용 (SQL 인젝션 방어)
        cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,))

        # 2. 결과 중 첫 번째 데이터 한 건만 가져오기
        user_info = cursor.fetchone()

        # 3. 데이터가 존재하지 않을 때의 방어 로직
        if user_info is None:
            raise HTTPException(status_code=404, detail=f"'{user_name}'(으)로 등록된 유저는 찾을 수 없습니다.")
        
        return dict(user_info) # JSON 응답을 위해 딕셔너리로 변환

