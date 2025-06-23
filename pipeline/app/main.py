"""
KPI 데이터 수집 및 분석 시스템 - FastAPI 메인 애플리케이션

이 파일은 4일간 점진적으로 완성해나가는 프로젝트의 진입점입니다.
각 날짜별 TODO 주석을 참고하여 단계적으로 구현하세요.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Day 1: 기본 FastAPI 설정
app = FastAPI(
    title="KPI 데이터 수집 및 분석 시스템",
    description="인턴십 첫 주 커리큘럼: FastAPI + PostgreSQL + Airflow",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS 설정 (개발용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO Day 2: 데이터베이스 연동 및 테이블 생성
# from app.database import engine, Base
# from app.models import kpi  # KPI 모델 import

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # 애플리케이션 시작 시 데이터베이스 테이블 생성
#     Base.metadata.create_all(bind=engine)
#     yield
#     # 종료 시 정리 작업 (필요한 경우)

# app = FastAPI(..., lifespan=lifespan)

# TODO Day 2: KPI 라우터 등록
# from app.routers import kpi
# app.include_router(kpi.router, prefix="/api/v1", tags=["KPI"])


# Day 1: 기본 엔드포인트들
@app.get("/")
async def root():
    """
    루트 엔드포인트 - 프로젝트 정보 반환
    Day 1에서 구현
    """
    return {
        "message": "KPI 데이터 수집 및 분석 시스템에 오신 것을 환영합니다!",
        "project": "인턴십 첫 주 커리큘럼",
        "current_day": "Day 1 - FastAPI 기초",
        "next_steps": [
            "Day 1: /ping, /echo API 구현",
            "Day 2: PostgreSQL 연동 및 KPI API 구현",
            "Day 3: Airflow DAG 연동",
            "Day 4: 리뷰 및 발표",
        ],
        "available_endpoints": [
            "GET / - 프로젝트 정보",
            "GET /ping - 서버 상태 확인 (Day 1 TODO)",
            "POST /echo - 메시지 에코 (Day 1 TODO)",
            "POST /api/v1/log - KPI 데이터 저장 (Day 2 TODO)",
            "GET /api/v1/logs - KPI 데이터 조회 (Day 2 TODO)",
            "GET /docs - API 문서 (Swagger UI)",
            "GET /redoc - API 문서 (ReDoc)",
        ],
    }


# TODO Day 1: ping API 구현
# 요구사항:
# - GET /ping
# - 응답: {"message": "pong"}
@app.get("/ping")
async def ping():
    """
    서버 상태 확인용 ping API

    Day 1 실습: 이 함수를 구현하세요

    Returns:
        dict: {"message": "pong"}
    """
    # TODO: {"message": "pong"} 응답 반환하는 코드 작성
    return {"message": "pong"}


# TODO Day 1: echo API 구현
# 요구사항:
# - POST /echo
# - 입력: {"message": "안녕하세요"}
# - 응답: {"echo": "안녕하세요"}
from pydantic import BaseModel


class EchoRequest(BaseModel):
    """Echo API 요청 모델"""

    message: str


class EchoResponse(BaseModel):
    """Echo API 응답 모델"""

    echo: str


@app.post("/echo", response_model=EchoResponse)
async def echo(request: EchoRequest):
    """
    입력받은 메시지를 그대로 반환하는 echo API

    Day 1 실습: 이 함수를 구현하세요

    Args:
        request (EchoRequest): 메시지가 포함된 요청

    Returns:
        EchoResponse: echo 필드에 입력 메시지 반환
    """
    # TODO: 입력받은 메시지를 echo 필드에 담아서 반환
    return {"echo": request.message}


# Day 1 추가 실습: 현재 시간 반환 API
@app.get("/time")
async def current_time():
    """
    현재 시간을 반환하는 API
    Day 1 추가 실습용
    """
    from datetime import datetime

    return {"current_time": datetime.now().isoformat(), "timezone": "UTC"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
