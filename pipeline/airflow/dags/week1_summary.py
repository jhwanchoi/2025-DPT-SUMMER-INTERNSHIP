from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def summarize_day1():
    print("Day 1 (6/23) - 개발 환경 세팅 & FastAPI 맛보기")
    print("- VS Code, Docker 등 개발 환경 구축")
    print("- Git 워크플로우 실습 (clone → branch → PR)")
    print("- FastAPI 기초: /ping, /echo API 구현")
    print("- 결과: 개인 브랜치 PR 요청 및 팀 리뷰")

def summarize_day2():
    print("Day 2 (6/24) - FastAPI 기반 KPI API 실습")
    print("- FastAPI + PostgreSQL 연동 (SQLAlchemy)")
    print("- /log POST API로 KPI 수신 및 저장")
    print("- DB 구조 설계 및 FastAPI 구조 정리")
    print("- 결과: API 동작 캡처 및 README 작성")

def summarize_day3():
    print("Day 3 (6/25) - CMake 기초")
    print("- C++ 빌드 시스템 학습")
    print("- CMake를 이용한 프로젝트 빌드 실습")

def summarize_day4():
    print("Day 4 (6/26) - Airflow DAG 연동")
    print("- Airflow 개념 학습 (DAG, Task, Operator)")
    print("- Docker Compose로 서비스 구성")
    print("- BashOperator 활용 데이터 처리 DAG 작성")
    print("- 결과: DAG 실행 흐름 확인 및 설명")

dag = DAG(
    dag_id="week1_summary",
    start_date=datetime(2025, 6, 26),
    schedule_interval=None,
    catchup=False,
    tags=["learning", "summary"],
)

with dag:
    task_day1 = PythonOperator(
        task_id="summarize_day1",
        python_callable=summarize_day1,
    )

    task_day2 = PythonOperator(
        task_id="summarize_day2",
        python_callable=summarize_day2,
    )

    task_day3 = PythonOperator(
        task_id="summarize_day3",
        python_callable=summarize_day3,
    )

    task_day4 = PythonOperator(
        task_id="summarize_day4",
        python_callable=summarize_day4,
    )

    task_day1 >> task_day2 >> task_day3 >> task_day4

globals()["dag"] = dag