-- PostgreSQL 초기화 스크립트
-- Docker 컨테이너 시작 시 자동으로 실행됩니다.

-- 기본 사용자 및 데이터베이스는 docker-compose.yml에서 생성됩니다.
-- 여기서는 추가 설정이나 초기 데이터를 넣을 수 있습니다.

-- 예시: 인덱스 생성 (Day 2에서 테이블 생성 후 필요시 사용)
-- CREATE INDEX IF NOT EXISTS idx_kpi_logs_timestamp ON kpi_logs(timestamp);
-- CREATE INDEX IF NOT EXISTS idx_kpi_logs_user_id ON kpi_logs(user_id);
-- CREATE INDEX IF NOT EXISTS idx_kpi_logs_created_at ON kpi_logs(created_at);

-- 예시: 분석 결과 테이블 (Day 3에서 사용)
-- CREATE TABLE IF NOT EXISTS kpi_analysis_results (
--     id SERIAL PRIMARY KEY,
--     analysis_time TIMESTAMP NOT NULL,
--     period_start TIMESTAMP NOT NULL,
--     period_end TIMESTAMP NOT NULL,
--     result_data JSONB NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- 초기 설정 완료 메시지
SELECT 'PostgreSQL 초기화 완료' as message; 