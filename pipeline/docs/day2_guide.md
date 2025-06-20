 # Day 2 실습 가이드: FastAPI 기반 KPI API 실습

## 학습 목표
- FastAPI와 PostgreSQL 연동 방법 이해
- SQLAlchemy ORM을 사용한 데이터베이스 작업
- KPI 데이터 수신 및 저장 API 구현
- FastAPI 프로젝트 구조 정리 (레이어 분리)

## 실습 내용

### 1단계: PostgreSQL 연동 설정 (90분)

#### Docker로 PostgreSQL 실행
```bash
# PostgreSQL 컨테이너 실행
docker-compose up -d postgres

# 컨테이너 상태 확인
docker ps | grep postgres

# 데이터베이스 접속 테스트
psql -h localhost -p 5432 -U kpi_user -d kpi_db
# 비밀번호: kpi_password

# 접속 후 기본 명령어
\l        # 데이터베이스 목록
\dt       # 테이블 목록  
\q        # 종료
```

#### 환경 변수 설정
```bash
# env.example을 .env로 복사
cp env.example .env

# .env 파일 내용 확인 및 수정
cat .env
```

#### SQLAlchemy 설정 활성화
`app/database.py` 파일에서 주석 처리된 코드들을 활성화:

```python
# 주석 해제할 코드들:
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 2단계: KPI 모델 및 스키마 정의 (60분)

#### SQLAlchemy 모델 구현
`app/models/kpi.py` 파일 구현:

```python
# 주석 해제하고 구현:
from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class KPILog(Base):
    __tablename__ = "kpi_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)
    task_id = Column(Integer, nullable=False)
    frame_id = Column(Integer, nullable=False)
    objects = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
```

#### Pydantic 스키마 구현
`app/schemas/kpi.py` 파일 구현:

```python
# 주석 해제하고 구현:
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Any, Optional

class Position(BaseModel):
    x: float = Field(..., description="X 좌표")
    y: float = Field(..., description="Y 좌표") 
    z: float = Field(..., description="Z 좌표")

class DetectedObject(BaseModel):
    id: int = Field(..., description="객체 ID")
    type: str = Field(..., description="객체 타입")
    position: Position = Field(..., description="객체 위치")

class KPILogRequest(BaseModel):
    timestamp: datetime = Field(..., description="KPI 데이터 생성 시각")
    user_id: int = Field(..., description="사용자 ID")
    task_id: int = Field(..., description="작업 ID")
    frame_id: int = Field(..., description="프레임 ID")
    objects: List[DetectedObject] = Field(..., description="탐지된 객체 목록")
```

### 3단계: KPI 서비스 구현 (90분)

#### 비즈니스 로직 구현
`app/services/kpi_service.py` 파일 구현:

**핵심 메서드들:**
1. `create_log()` - KPI 데이터 저장
2. `get_logs()` - KPI 데이터 목록 조회
3. `get_log_by_id()` - 특정 로그 조회
4. `get_statistics()` - 통계 정보 생성

**구현 예시:**
```python
def create_log(self, kpi_data: KPILogRequest) -> int:
    db_log = KPILog(
        timestamp=kpi_data.timestamp,
        user_id=kpi_data.user_id,
        task_id=kpi_data.task_id,
        frame_id=kpi_data.frame_id,
        objects=[obj.dict() for obj in kpi_data.objects]
    )
    
    self.db.add(db_log)
    self.db.commit()
    self.db.refresh(db_log)
    
    return db_log.id
```

### 4단계: API 라우터 구현 (90분)

#### KPI API 엔드포인트 구현
`app/routers/kpi.py` 파일 구현:

**구현할 API들:**
1. `POST /api/v1/log` - KPI 데이터 저장
2. `GET /api/v1/logs` - KPI 데이터 목록 조회
3. `GET /api/v1/logs/{log_id}` - 특정 로그 조회  
4. `GET /api/v1/stats` - 통계 정보 조회

#### 메인 애플리케이션 수정
`app/main.py` 파일에서 주석 해제:

```python
# 데이터베이스 연동 코드 활성화
from app.database import engine, Base
from app.models import kpi

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

# 라우터 등록 코드 활성화  
from app.routers import kpi
app.include_router(kpi.router, prefix="/api/v1", tags=["KPI"])
```

### 5단계: 테스트 및 검증 (60분)

#### 서버 실행 및 기본 테스트
```bash
# 서버 실행
uvicorn app.main:app --reload --port 8000

# 테이블 생성 확인 (DBeaver에서)
# localhost:5432 / kpi_db 접속
# kpi_logs 테이블 확인
```

#### API 테스트
```bash
# 1. KPI 데이터 저장 테스트
curl -X POST http://localhost:8000/api/v1/log \
  -H "Content-Type: application/json" \
  -d @data/sample_kpi_data.json

# 2. 저장된 데이터 조회
curl http://localhost:8000/api/v1/logs

# 3. 통계 정보 조회
curl http://localhost:8000/api/v1/stats
```

#### DBeaver로 데이터 확인
1. **연결 설정:**
   - 호스트: localhost
   - 포트: 5432
   - 데이터베이스: kpi_db
   - 사용자: kpi_user
   - 비밀번호: kpi_password

2. **테이블 확인:**
   ```sql
   SELECT * FROM kpi_logs ORDER BY created_at DESC LIMIT 5;
   
   -- JSON 컬럼 쿼리 예시
   SELECT 
       id, 
       user_id, 
       task_id,
       jsonb_array_length(objects) as object_count,
       objects
   FROM kpi_logs;
   ```

## 숙제
1. **KPI 저장 API 완성**: `/log` POST API 정상 동작 구현
2. **동작 화면 캡처**: API 테스트 결과 스크린샷
3. **README 작성**: 구현한 API 설명 및 사용법 정리
4. **PR 생성**: 구현한 코드를 개인 브랜치에서 PR 요청

## 트러블슈팅

### 자주 발생하는 문제들

1. **데이터베이스 연결 오류**
   ```bash
   # PostgreSQL 컨테이너 상태 확인
   docker ps
   docker logs kpi_postgres
   ```

2. **테이블 생성 안됨**
   ```python
   # main.py에서 모델 import 확인
   from app.models import kpi  # 이 줄이 있어야 함
   ```

3. **JSON 데이터 오류**
   ```bash
   # 샘플 데이터 유효성 확인
   cat data/sample_kpi_data.json | python -m json.tool
   ```

## 🔗 참고 자료

### SQLAlchemy
- [SQLAlchemy 공식 문서](https://docs.sqlalchemy.org/)
- [FastAPI Database 가이드](https://fastapi.tiangolo.com/tutorial/sql-databases/)

### PostgreSQL
- [PostgreSQL JSON 함수](https://www.postgresql.org/docs/current/functions-json.html)
- [DBeaver 사용법](https://dbeaver.io/docs/)

### API 설계
- [REST API 설계 원칙](https://restfulapi.net/)
- [HTTP 상태 코드 가이드](https://httpstatuses.com/)