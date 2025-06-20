"""
KPI 데이터 분석 DAG
Day 3에서 저장된 KPI 데이터를 분석하여 결과를 저장합니다.
"""

# TODO Day 3: Airflow 모듈 임포트
# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.operators.bash import BashOperator

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
#     'analyze_kpi_data',
#     default_args=default_args,
#     description='KPI 데이터를 분석하여 통계 정보를 생성',
#     schedule_interval=timedelta(hours=1),  # 1시간마다 실행
#     catchup=False,
#     tags=['kpi', 'analysis', 'intern_tutorial']
# )

# TODO Day 3: KPI 분석 함수
# def analyze_kpi_data():
#     """
#     KPI 데이터를 분석하는 Python 함수
#     """
#     import pandas as pd
#     import psycopg2
#     import json
#     from datetime import datetime, timedelta
#
#     # 데이터베이스 연결 설정
#     conn_params = {
#         'host': 'localhost',
#         'port': 5432,
#         'database': 'kpi_db',
#         'user': 'kpi_user',
#         'password': 'kpi_password'
#     }
#
#     try:
#         # 데이터베이스 연결
#         conn = psycopg2.connect(**conn_params)
#
#         # 최근 1시간 데이터 조회
#         one_hour_ago = datetime.now() - timedelta(hours=1)
#         query = """
#         SELECT id, timestamp, user_id, task_id, frame_id, objects, created_at
#         FROM kpi_logs
#         WHERE created_at >= %s
#         ORDER BY created_at DESC
#         """
#
#         # Pandas DataFrame으로 로드
#         df = pd.read_sql_query(query, conn, params=[one_hour_ago])
#
#         if df.empty:
#             print("분석할 데이터가 없습니다.")
#             return
#
#         # 분석 수행
#         analysis_result = {
#             'analysis_time': datetime.now().isoformat(),
#             'period_start': one_hour_ago.isoformat(),
#             'period_end': datetime.now().isoformat(),
#             'total_logs': len(df),
#             'unique_users': df['user_id'].nunique(),
#             'unique_tasks': df['task_id'].nunique(),
#             'avg_objects_per_frame': 0,
#             'object_type_distribution': {},
#             'user_activity': {}
#         }
#
#         # 객체 분석
#         total_objects = 0
#         object_types = {}
#
#         for _, row in df.iterrows():
#             objects = row['objects']
#             if isinstance(objects, str):
#                 objects = json.loads(objects)
#
#             total_objects += len(objects)
#
#             for obj in objects:
#                 obj_type = obj.get('type', 'unknown')
#                 object_types[obj_type] = object_types.get(obj_type, 0) + 1
#
#         analysis_result['avg_objects_per_frame'] = round(total_objects / len(df), 2) if len(df) > 0 else 0
#         analysis_result['object_type_distribution'] = object_types
#
#         # 사용자별 활동 분석
#         user_activity = df.groupby('user_id').agg({
#             'id': 'count',
#             'timestamp': ['min', 'max']
#         }).reset_index()
#
#         user_activity.columns = ['user_id', 'log_count', 'first_activity', 'last_activity']
#         analysis_result['user_activity'] = user_activity.to_dict('records')
#
#         # 분석 결과를 별도 테이블에 저장 (선택사항)
#         # create_analysis_result_table(conn)
#         # save_analysis_result(conn, analysis_result)
#
#         print(f"분석 완료: {json.dumps(analysis_result, indent=2)}")
#
#         conn.close()
#
#     except Exception as e:
#         print(f"분석 중 오류 발생: {str(e)}")

# TODO Day 3: 분석 결과 테이블 생성 함수
# def create_analysis_result_table(conn):
#     """분석 결과를 저장할 테이블 생성"""
#     cursor = conn.cursor()
#
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS kpi_analysis_results (
#         id SERIAL PRIMARY KEY,
#         analysis_time TIMESTAMP NOT NULL,
#         period_start TIMESTAMP NOT NULL,
#         period_end TIMESTAMP NOT NULL,
#         result_data JSONB NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
#     """
#
#     cursor.execute(create_table_query)
#     conn.commit()
#     cursor.close()

# TODO Day 3: 분석 결과 저장 함수
# def save_analysis_result(conn, analysis_result):
#     """분석 결과를 데이터베이스에 저장"""
#     cursor = conn.cursor()
#
#     insert_query = """
#     INSERT INTO kpi_analysis_results (analysis_time, period_start, period_end, result_data)
#     VALUES (%s, %s, %s, %s)
#     """
#
#     cursor.execute(insert_query, [
#         analysis_result['analysis_time'],
#         analysis_result['period_start'],
#         analysis_result['period_end'],
#         json.dumps(analysis_result)
#     ])
#
#     conn.commit()
#     cursor.close()

# TODO Day 3: Task 정의
# # KPI 데이터 분석 태스크
# analyze_task = PythonOperator(
#     task_id='analyze_kpi_data',
#     python_callable=analyze_kpi_data,
#     dag=dag
# )

# # 외부 스크립트 실행 방식 (대안)
# analyze_script_task = BashOperator(
#     task_id='run_analysis_script',
#     bash_command='python /opt/airflow/scripts/analyze_kpi_data.py',
#     dag=dag
# )

# TODO Day 3: Task 실행
# analyze_task

# Day 3 실습 가이드:
# 1. 위의 주석 처리된 코드들을 활성화
# 2. 데이터베이스 연결 및 쿼리 실행 방법 학습
# 3. Pandas를 사용한 데이터 분석 기법 적용
# 4. JSON 데이터 처리 및 집계 방법 이해
# 5. 분석 결과를 다시 데이터베이스에 저장하는 패턴 학습
# 6. Airflow UI에서 DAG 실행 및 로그 확인
