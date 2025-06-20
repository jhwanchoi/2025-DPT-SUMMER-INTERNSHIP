# KPI 데이터 수집 및 분석 시스템

인턴분의 Backend 및 pipeline 프레임워크 학습을 위한 프로젝트입니다.  
4일간 점진적으로 완성해나가는 KPI 데이터 수집 및 분석 파이프라인을 구축합니다.

## 프로젝트 개요

자동차 객체 탐지 시스템에서 생성되는 KPI 데이터를 수집, 저장, 분석하는 파이프라인을 구축합니다.

### 최종 시스템 아키텍처
```
KPI 데이터 → FastAPI → PostgreSQL → Airflow → 분석 결과
```

### 예시 KPI 데이터
```json
{
  "timestamp": "2025-05-28T10:56:37.043Z",
  "user_id": 1,
  "task_id": 1,
  "frame_id": 2,
  "objects": [
    {
      "id": 1,
      "type": "car", 
      "position": {"x": 0.1, "y": 0.2, "z": 0.6}
    },
    {
      "id": 2,
      "type": "person",
      "position": {"x": 0.5, "y": 0.3, "z": 0.0}
    }
  ]
}
```

## 프로젝트 구조

```
tutorial/
├── README.md                    # 프로젝트 개요 (이 파일)
├── requirements.txt             # Python 의존성
├── docker-compose.yml           # PostgreSQL + Airflow 환경
├── .env                        # 환경 변수
│
├── app/                        # FastAPI 애플리케이션
│   ├── main.py                 # 애플리케이션 진입점
│   ├── config.py               # 설정 관리
│   ├── database.py             # 데이터베이스 연결
│   ├── models/                 # SQLAlchemy 모델
│   │   ├── __init__.py
│   │   └── kpi.py             # KPI 관련 모델
│   ├── schemas/                # Pydantic 스키마
│   │   ├── __init__.py
│   │   └── kpi.py             # KPI API 스키마
│   ├── routers/                # API 라우터
│   │   ├── __init__.py
│   │   └── kpi.py             # KPI API 엔드포인트
│   └── services/               # 비즈니스 로직
│       ├── __init__.py
│       └── kpi_service.py     # KPI 관련 서비스
│
├── airflow/                    # Airflow DAG 및 설정
│   ├── dags/                   # DAG 정의
│   │   ├── insert_dummy_kpi.py # 더미 데이터 생성
│   │   └── analyze_kpi.py     # KPI 분석
│   └── scripts/                # 스크립트
│       ├── generate_dummy_data.py
│       └── analyze_kpi_data.py
│
├── data/                       # 샘플 데이터
│   └── sample_kpi_data.json   # 테스트용 KPI 데이터
│
└── docs/                       # 문서
    ├── day1_guide.md          # Day 1 실습 가이드
    ├── day2_guide.md          # Day 2 실습 가이드
    ├── day3_guide.md          # Day 3 실습 가이드
    └── api_usage.md           # API 사용법
```

## 시작하기

### 1. 환경 설정
```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
```

### 2. 데이터베이스 실행
```bash
# PostgreSQL 컨테이너 실행
docker-compose up -d postgres
```

### 3. FastAPI 서버 실행
```bash
# 개발 서버 실행
uvicorn app.main:app --reload --port 8000
```

### 4. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 기술 스택

- **Backend**: FastAPI, SQLAlchemy, Alembic
- **Database**: PostgreSQL  
- **Workflow**: Apache Airflow
- **Containerization**: Docker, Docker Compose
- **Development**: Python 3.11+, Git

## 학습 진행 방법

1. 각 날짜별 가이드 문서 (`docs/dayX_guide.md`) 참고
2. 코드의 `TODO` 주석을 따라 단계별 구현
3. 각 날짜 종료 시 개인 브랜치에서 PR 생성
4. 팀원들과 코드 리뷰 진행

## 학습 목표

- **Git/GitHub 워크플로우** 숙달
- **FastAPI** 기반 REST API 개발
- **PostgreSQL** 데이터베이스 연동
- **Apache Airflow** 워크플로우 자동화
- **Docker** 컨테이너 환경 활용
- **코드 리뷰** 및 협업 경험 