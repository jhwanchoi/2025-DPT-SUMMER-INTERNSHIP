"""
KPI 서비스 - 비즈니스 로직 구현
Day 2에서 KPI 데이터 처리 관련 비즈니스 로직을 구현합니다.
"""

# TODO Day 2: 필요한 모듈 임포트
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional, Dict, Any
from datetime import datetime

# TODO Day 2: 로컬 모듈 임포트
from app.models.kpi import KPILog
from app.schemas.kpi import KPILogRequest, KPILogResponse, KPIStatsResponse

# TODO Day 2: KPI 서비스 클래스 정의
class KPIService:
    """KPI 데이터 처리를 담당하는 서비스 클래스"""

    def __init__(self, db: Session):
        """
        서비스 초기화

        Args:
            db: 데이터베이스 세션
        """
        self.db = db

    def create_log(self, kpi_data: KPILogRequest) -> int:
        """
        KPI 로그 데이터를 데이터베이스에 저장

        Args:
            kpi_data: 저장할 KPI 데이터

        Returns:
            int: 생성된 로그의 ID
        """
        # TODO Day 2: KPILog 모델 인스턴스 생성 및 저장
        db_log = KPILog(
            timestamp=kpi_data.timestamp,
            user_id=kpi_data.user_id,
            task_id=kpi_data.task_id,
            frame_id=kpi_data.frame_id,
            objects=[obj.dict() for obj in kpi_data.objects]  # Pydantic -> dict 변환
        )

        self.db.add(db_log)
        self.db.commit()
        self.db.refresh(db_log)

        return db_log.id

    def get_logs(self, skip: int = 0, limit: int = 100) -> List[KPILogResponse]:
        """
        KPI 로그 목록을 조회

        Args:
            skip: 건너뛸 레코드 수
            limit: 조회할 최대 레코드 수

        Returns:
            List[KPILogResponse]: KPI 로그 목록
        """
        # TODO Day 2: 데이터베이스에서 로그 조회
        logs = self.db.query(KPILog).offset(skip).limit(limit).all()
        return [KPILogResponse.from_orm(log) for log in logs]

    def get_log_by_id(self, log_id: int) -> Optional[KPILogResponse]:
        """
        특정 ID의 KPI 로그를 조회

        Args:
            log_id: 조회할 로그 ID

        Returns:
            Optional[KPILogResponse]: KPI 로그 또는 None
        """
        # TODO Day 2: 특정 ID로 로그 조회
        log = self.db.query(KPILog).filter(KPILog.id == log_id).first()
        return KPILogResponse.from_orm(log) if log else None

    def get_statistics(self) -> KPIStatsResponse:
        """
        KPI 데이터 통계 정보를 조회

        Returns:
            KPIStatsResponse: 통계 정보
        """
        # TODO Day 2: 통계 정보 계산
        total_logs = self.db.query(KPILog).count()

        # 전체 객체 수 계산 (JSON 배열 길이 합계)
        total_objects = self.db.query(
            func.sum(func.json_array_length(KPILog.objects))
        ).scalar() or 0

        # 객체 타입별 개수 계산 (복잡한 JSON 쿼리)
        object_types = self._calculate_object_types()

        # 최근 로그 시간
        latest_log = self.db.query(KPILog).order_by(KPILog.created_at.desc()).first()
        latest_log_time = latest_log.created_at if latest_log else None

        return KPIStatsResponse(
            total_logs=total_logs,
            total_objects=total_objects,
            object_types=object_types,
            latest_log_time=latest_log_time
        )

    def _calculate_object_types(self) -> Dict[str, int]:
        """
        객체 타입별 개수를 계산하는 헬퍼 메서드

        Returns:
            Dict[str, int]: 객체 타입별 개수
        """
        # TODO Day 2: JSON 데이터에서 객체 타입별 개수 계산
        # 복잡한 PostgreSQL JSON 쿼리가 필요합니다.
        # 간단한 구현을 위해 Python에서 처리할 수도 있습니다.

        logs = self.db.query(KPILog).all()
        object_types = {}

        for log in logs:
            for obj in log.objects:
                obj_type = obj.get('type', 'unknown')
                object_types[obj_type] = object_types.get(obj_type, 0) + 1

        return object_types

# Day 2 실습 가이드:
# 1. 위의 주석 처리된 메서드들을 단계별로 구현
# 2. SQLAlchemy ORM을 사용한 CRUD 작업 패턴 학습
# 3. Pydantic 모델과 SQLAlchemy 모델 간 변환 처리
# 4. JSON 컬럼을 다루는 방법 이해
# 5. 복잡한 통계 쿼리 작성 경험
