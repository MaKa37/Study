import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI(title="SQLite DB 연동 학습 서버")

# 실무 팁: 하드코딩을 피하기 위해 DB 파일 경로를 상수로 분리합니다.
DB_FILE = "DB/Python/todo_app.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # users 테이블이 없다면 생성해라! (id, name, age 칸 만들기)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                       todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT)
        """)
        conn.commit()

init_db()

# [READ] 조건에 맞는 데이터 읽기 (전체 조회)
@app.get("todos/")
def read_all_todos():
    """데이터베이스에 저장된 모든 할 일 목록을 반환합니다."""

    # 1. 커넥션 자원 관리 (with 문)
    with sqlite3.connect(DB_FILE) as conn:
        # 2. 데이터 직렬화 편의성
        # 기본적으로 SQLite는 결과를 (1, "장보기") 같은 튜플로 반환합니다.
        # 이를 {"id": 1, "title": "장보기"} 같은 딕셔너리 형태로 쉽게 변환하기 위해 row_factory를 설정합니다.
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos")

        # fetchall()로 가져온 데이터를 dict 리스트로 변환하여 반환하면 FastAPI가 자동으로 JSON 응답으로 만듭니다.
        return [dict(row) for row in cursor.fetchall]
    
@app.post("/todos/post/")
def create_user(user: UserCreate):
    # 1. user 변수에 데이터가 담겨서 들어옵니다. (아직 메모리에만 있음)
    
    # 2. 반드시 데이터베이스(SQLite 등)를 열고 INSERT 문을 실행해 하드디스크에 기록해야 합니다.
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todos (name, age) VALUES (?, ?)", (user.name, user.age))
        conn.commit()

    return {"message": f"{user.name}님의 정보가 DB에 저장되었습니다!", "path": DB_PATH}
    
# [UPDATE] 기존 데이터 덮어쓰기 (단일 수정)
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str):
    """특정 ID를 가진 할 일의 제목을 수정합니다."""

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # 3. Parameterized Query (보안 및 매핑)
        cursor.execute(
            "UPDATE todos SET title = ? WHERE id = ?",
            (title, todo_id)
        )

        # 데이터가 '조회'가 아닌 '변경(생성, 수정, 삭제)'될 때는 반드시 디스크에 기록하라는 명령(commit)을 내려야 합니다.
        conn.commit()

        # 4. 방어적 프로그래밍 (정확한 HTTP 상태 코드 반환)
        # 만약 클라이언트가 존재하지 않는 ID(예: 999번)를 수정하려고 하면, SQL 구문 자체는 문법적 오류가 없으므로 에러가 나지 않습니다.
        # 따라서 '실제로 변경된 행(row)의 개수'가 0인지 확인하여 404 에러를 인위적으로 발생시켜야 합니다.
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="수정할 아이템을 찾을 수 없습니다.")
        return {"message": f"{todo_id}번 아이템이 '{title}'(으)로 수정되었습니다."}