import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CORS 미들웨어 학습 서버")

# [핵심 학습 포인트] 환경에 따른 오리진(Origin) 분리 설정
# 서버가 실행되는 환경 변수를 읽어옵니다. (기본값은 'development')
ENVIRONMENT = os.getenv("ENV", "development")

if ENVIRONMENT == "development":
    # 1. 개발 환경: 프론트엔드 개발자의 편의를 위해 모든 도메인(*) 접근을 허용합니다.
    allowed_origins = ["*"]
else:
    # 2. 운영 환경 (안티 패턴 극복): 실제 서비스 배포 시에는 반드시 허락된 도메인만 명시해야 합니다.
    allowed_origins = [
        "https://my-real-website.com",       # 실제 서비스할 프론트엔드 도메인
        "https://admin.my-real-website.com"  # 사내 관리자용 프론트엔드 도메인
    ]

# 앱 객체에 CORS 미들웨어를 추가(부착)합니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins, # 접근을 허용할 도메인 목록 (가장 중요)
    allow_credentials=True,        # 쿠키, 인증 헤더 등의 자격 증명(Credentials) 포함 허용 여부
    allow_methods=["*"],           # 허용할 HTTP 메서드 (GET, POST, PUT, DELETE, OPTIONS 등)
    allow_headers=["*"],           # 허용할 HTTP 요청 헤더 (Authorization, Content-Type 등)
)

@app.get("/")
def read_root():
    """어떤 프론트엔드에서 호출하든 CORS 정책에 따라 응답이 제어됩니다."""
    return {"message": "CORS 보안 설정이 안전하게 적용된 서버입니다."}