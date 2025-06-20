"""
더미 KPI 데이터 생성 DAG
Day 3에서 Airflow를 사용하여 더미 데이터를 주기적으로 생성합니다.
"""

# TODO Day 3: Airflow 모듈 임포트
# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.bash import BashOperator
# from airflow.operators.python import PythonOperator

# TODO Day 3: DAG 기본 설정
# default_args = {
#     'owner': 'intern',
#     'depends_on_past': False,
#     'start_date': datetime(2025, 1, 20),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5)
# }

# TODO Day 3: DAG 정의
# dag = DAG(
#     'insert_dummy_kpi_data',
#     default_args=default_args,
#     description='더미 KPI 데이터를 주기적으로 생성하여 데이터베이스에 저장',
#     schedule_interval=timedelta(minutes=10),  # 10분마다 실행
#     catchup=False,
#     tags=['kpi', 'dummy_data', 'intern_tutorial']
# )

# TODO Day 3: 더미 데이터 생성 Python 함수
# def generate_dummy_kpi_data():
#     """
#     더미 KPI 데이터를 생성하는 Python 함수
#     """
#     import requests
#     import json
#     import random
#     from datetime import datetime
#
#     # 더미 데이터 생성
#     dummy_data = {
#         "timestamp": datetime.now().isoformat(),
#         "user_id": random.randint(1, 10),
#         "task_id": random.randint(1, 5),
#         "frame_id": random.randint(1, 1000),
#         "objects": []
#     }
#
#     # 랜덤한 객체들 생성
#     object_types = ["car", "person", "truck", "bicycle", "motorcycle"]
#     num_objects = random.randint(1, 5)
#
#     for i in range(num_objects):
#         obj = {
#             "id": i + 1,
#             "type": random.choice(object_types),
#             "position": {
#                 "x": round(random.uniform(-1.0, 1.0), 3),
#                 "y": round(random.uniform(-1.0, 1.0), 3),
#                 "z": round(random.uniform(0.0, 2.0), 3)
#             }
#         }
#         dummy_data["objects"].append(obj)
#
#     # FastAPI 서버로 데이터 전송
#     try:
#         response = requests.post(
#             "http://localhost:8000/api/v1/log",
#             json=dummy_data,
#             headers={"Content-Type": "application/json"}
#         )
#
#         if response.status_code == 200:
#             print(f"더미 데이터 저장 성공: {response.json()}")
#         else:
#             print(f"데이터 저장 실패: {response.status_code} - {response.text}")
#
#     except Exception as e:
#         print(f"API 호출 중 오류 발생: {str(e)}")

# TODO Day 3: Task 정의
# # Task 1: 더미 데이터 생성 및 전송
# generate_data_task = PythonOperator(
#     task_id='generate_dummy_kpi_data',
#     python_callable=generate_dummy_kpi_data,
#     dag=dag
# )

# # Task 2: 스크립트 실행 방식 (대안)
# # BashOperator를 사용하여 외부 Python 스크립트 실행
# run_script_task = BashOperator(
#     task_id='run_dummy_data_script',
#     bash_command='python /opt/airflow/scripts/generate_dummy_data.py',
#     dag=dag
# )

# TODO Day 3: Task 의존성 설정
# # 단순한 경우 (하나의 task만 실행)
# # generate_data_task

# # 두 가지 방식을 순차 실행하려면:
# # generate_data_task >> run_script_task

# Day 3 실습 가이드:
# 1. 위의 주석 처리된 코드들을 활성화
# 2. DAG의 구조와 설정 이해
# 3. PythonOperator와 BashOperator의 차이점 학습
# 4. Airflow UI에서 DAG 확인 및 실행
# 5. 더미 데이터가 데이터베이스에 정상 저장되는지 확인
# 6. schedule_interval 조정하여 실행 주기 변경 실습
