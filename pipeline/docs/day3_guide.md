# Day 3 실습 가이드: Airflow DAG 연동

## 학습 목표
- Apache Airflow 핵심 개념 이해
- DAG를 사용한 데이터 파이프라인 구축
- KPI 데이터 자동 생성 및 분석 워크플로우 구현

## 실습 내용

### 1단계: Airflow 환경 구축
```bash
# Airflow 컨테이너 실행
docker-compose up -d airflow-webserver airflow-scheduler

# Airflow UI 접속
# http://localhost:8080
# 사용자: admin / 비밀번호: admin
```

### 2단계: 더미 데이터 생성 DAG 구현
- `airflow/dags/insert_dummy_kpi.py` 파일 활성화
- PythonOperator로 더미 데이터 생성
- 10분마다 실행되는 스케줄 설정

### 3단계: 데이터 분석 DAG 구현  
- `airflow/dags/analyze_kpi.py` 파일 활성화
- Pandas를 사용한 데이터 분석
- 1시간마다 실행되는 분석 작업

### 4단계: DAG 실행 및 모니터링
- Airflow UI에서 DAG 활성화
- 실행 로그 확인
- 데이터베이스에서 결과 검증

## 숙제
1. DAG 정의 코드 완성
2. 실행 결과 캡처
3. 전체 흐름 설명 README 작성
4. PR 생성