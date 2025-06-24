"""
데이터베이스 연결 설정
Day 2에서 PostgreSQL과 SQLAlchemy 연동에 사용됩니다.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# TODO Day 2: 데이터베이스 URL 설정
# 환경변수에서 읽어오거나 기본값 사용
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://kpi_user:kpi_password@localhost:5432/kpi_db"
)

# TODO Day 2: SQLAlchemy 엔진 생성
# 주석 해제하고 사용하세요
engine = create_engine(DATABASE_URL)

# TODO Day 2: 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# TODO Day 2: Base 클래스 생성 (모델 정의용)
Base = declarative_base()


# TODO Day 2: 데이터베이스 세션 의존성 함수
def get_db():
    """
    데이터베이스 세션을 생성하고 종료하는 의존성 함수
    FastAPI의 Depends에서 사용

    Day 2 실습에서 주석을 해제하고 구현하세요:

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    """
    # TODO Day 2: 데이터베이스 세션 생성 및 반환 로직 구현
    pass


# Day 2 실습 가이드:
# 1. 위의 주석 처리된 코드들을 해제
# 2. PostgreSQL 컨테이너 실행: docker-compose up -d postgres
# 3. DBeaver로 데이터베이스 연결 확인
# 4. get_db() 함수 구현
