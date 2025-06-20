"""
KPI API용 Pydantic 스키마 정의
Day 2에서 API 요청/응답 데이터 검증을 위해 사용됩니다.
"""

# TODO Day 2: Pydantic 임포트
# from pydantic import BaseModel, Field
# from datetime import datetime
# from typing import List, Dict, Any, Optional

# TODO Day 2: 위치 정보 스키마
# class Position(BaseModel):
#     """객체의 3D 위치 정보"""
#     x: float = Field(..., description="X 좌표")
#     y: float = Field(..., description="Y 좌표")
#     z: float = Field(..., description="Z 좌표")

# TODO Day 2: 탐지된 객체 스키마
# class DetectedObject(BaseModel):
#     """탐지된 객체 정보"""
#     id: int = Field(..., description="객체 ID")
#     type: str = Field(..., description="객체 타입 (car, person, etc.)")
#     position: Position = Field(..., description="객체 위치")

# TODO Day 2: KPI 로그 요청 스키마
# class KPILogRequest(BaseModel):
#     """KPI 로그 데이터 저장 요청"""
#     timestamp: datetime = Field(..., description="KPI 데이터 생성 시각")
#     user_id: int = Field(..., description="사용자 ID")
#     task_id: int = Field(..., description="작업 ID")
#     frame_id: int = Field(..., description="프레임 ID")
#     objects: List[DetectedObject] = Field(..., description="탐지된 객체 목록")
#
#     class Config:
#         # JSON 예시
#         schema_extra = {
#             "example": {
#                 "timestamp": "2025-05-28T10:56:37.043Z",
#                 "user_id": 1,
#                 "task_id": 1,
#                 "frame_id": 2,
#                 "objects": [
#                     {
#                         "id": 1,
#                         "type": "car",
#                         "position": {"x": 0.1, "y": 0.2, "z": 0.6}
#                     },
#                     {
#                         "id": 2,
#                         "type": "person",
#                         "position": {"x": 0.5, "y": 0.3, "z": 0.0}
#                     }
#                 ]
#             }
#         }

# TODO Day 2: KPI 로그 응답 스키마
# class KPILogResponse(BaseModel):
#     """KPI 로그 데이터 조회 응답"""
#     id: int
#     timestamp: datetime
#     user_id: int
#     task_id: int
#     frame_id: int
#     objects: List[Dict[str, Any]]  # JSON 형태로 저장된 객체들
#     created_at: datetime
#     updated_at: datetime
#
#     class Config:
#         from_attributes = True  # SQLAlchemy 모델에서 변환 가능

# TODO Day 2: 통계 정보 응답 스키마
# class KPIStatsResponse(BaseModel):
#     """KPI 통계 정보 응답"""
#     total_logs: int = Field(..., description="전체 로그 수")
#     total_objects: int = Field(..., description="전체 탐지 객체 수")
#     object_types: Dict[str, int] = Field(..., description="객체 타입별 개수")
#     latest_log_time: Optional[datetime] = Field(None, description="최근 로그 시간")

# Day 2 실습 가이드:
# 1. 위의 주석 처리된 스키마들을 활성화
# 2. Pydantic 모델의 유효성 검증 기능 확인
# 3. Field를 사용한 상세 설명 및 제약조건 설정
# 4. Config 클래스로 예시 데이터 및 SQLAlchemy 연동 설정
