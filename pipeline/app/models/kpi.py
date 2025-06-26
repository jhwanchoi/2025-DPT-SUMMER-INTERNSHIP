"""
KPI 데이터 모델 정의
Day 2에서 PostgreSQL 테이블 구조를 정의합니다.
"""

# TODO Day 2: SQLAlchemy 임포트
from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

# TODO Day 2: KPI 로그 모델 정의
class KPILog(Base):
    """
    KPI 로그 데이터를 저장하는 테이블

    Attributes:
        id: 기본 키 (자동 증가)
        timestamp: KPI 데이터 생성 시각
        user_id: 사용자 ID
        task_id: 작업 ID
        frame_id: 프레임 ID
        created_at: 데이터베이스 저장 시각
        updated_at: 데이터 수정 시각
    """
    __tablename__ = "kpi_logs"

    # TODO Day 2: 테이블 컬럼 정의
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False, comment="KPI 데이터 생성 시각")
    user_id = Column(Integer, nullable=False, comment="사용자 ID")
    task_id = Column(Integer, nullable=False, comment="작업 ID")
    frame_id = Column(Integer, nullable=False, comment="프레임 ID")
    objects_id = Column(JSON, nullable=True, server_default="[]")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    objects = relationship("KPIObject", back_populates="log", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<KPILog(id={self.id}, user_id={self.user_id}, task_id={self.task_id})>"

class KPIObject(Base):
    __tablename__ = "kpi_objects"
    object_id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    log_id = Column(Integer, ForeignKey("kpi_logs.id", ondelete="CASCADE"), nullable=False)
    type = Column(String, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)

    log = relationship("KPILog", back_populates="objects")




# Day 2 실습 가이드:
# 1. 위의 주석 처리된 임포트 및 클래스 정의를 활성화
# 2. 각 컬럼의 타입과 제약조건 확인
# 3. JSON 컬럼으로 객체 탐지 결과 저장 구조 이해
# 4. created_at, updated_at 자동 시간 기록 확인
