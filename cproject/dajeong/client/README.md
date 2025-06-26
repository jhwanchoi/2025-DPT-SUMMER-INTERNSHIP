# KPI 프로젝트 실행 방법

## 1. PostgreSQL 컨테이너 실행
```bash
cd pipeline
docker-compose up -d
```

## 2. FastAPI 서버 실행 (로컬)
```bash
cd pipeline
python -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 3. Client 컨테이너 실행
```bash
cd cproject/dajeong/client
docker-compose up
```

> **Tip:** Client 입력은 터미널에서만 가능합니다.  
> Docker Desktop GUI에서는 입력이 안 됩니다!