from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Pydantic 유효성 검증 학습 서버")

# [핵심 학습 포인트] 단순 타입을 넘어선 엄격한 조건 부여
class TodoCreate(BaseModel):
    # Field(..., )에서 '...'은 이 필드가 필수값(Required)임을 의미합니다.
    # 클라이언트가 빈 문자열("")이나 너무 긴 텍스트를 보내면 DB 에러가 나기 전에 Pydantic이 쳐냅니다.
    title: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="할 일의 제목 (2~50자 이내)"
    )

    # | None을 사용해 선택적(Optional) 데이터임을 명시합니다. 
    # 기본값(default=None)을 주면 클라이언트가 이 필드를 아예 안 보내도 에러가 나지 않습니다.
    description: str | None = Field(
        default=None,
        max_length=200,
        description="상세 설명(최대 200자)"
    )

# API 엔드포인트에서 위에서 정의한 Pydantic 모델을 인자로 받습니다.
@app.post("/todos/")
def create_todo(todo: TodoCreate):
    """
    클라이언트가 보낸 JSON 데이터가 TodoCreate 규칙을 통과해야만 이 함수가 실행됩니다.
    만약 규칙에 어긋나면 함수 내부로 진입조차 하지 못하고 422 에러가 즉시 반환됩니다.
    """
    
    # 이 줄에 도달했다면, todo.title은 무조건 안전한 문자열(str)이며, 
    # 길이는 2자 이상 50자 이하임이 '수학적으로 보장'됩니다.
    # 따라서 안심하고 DB 저장 로직으로 넘길 수 있습니다.
    
    return {
        "message": "안전하게 데이터가 검증되었습니다.",
        "received_data": {
            "title": todo.title,
            "description": todo.description
        }
    }