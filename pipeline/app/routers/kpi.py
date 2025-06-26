"""
KPI API 라우터
Day 2에서 KPI 데이터 수신, 저장, 조회 API를 구현합니다.
"""

# TODO Day 2: FastAPI 라우터 임포트
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

# TODO Day 2: 로컬 모듈 임포트
from database import get_db
from models.kpi import KPILog
from schemas.kpi import KPILogRequest, KPILogResponse, KPIStatsResponse, KPILogUpdateRequest, KPILogCreateRequest
from services.kpi_service import KPIService

# TODO Day 2: 라우터 인스턴스 생성
router = APIRouter()

# TODO Day 2: KPI 데이터 저장 API
@router.post("/log", response_model=dict)
async def create_kpi_log(
    kpi_data: KPILogCreateRequest,
    db: Session = Depends(get_db)
):
    """
    KPI 데이터를 데이터베이스에 저장합니다.

    Args:
        kpi_data: KPI 로그 데이터
        db: 데이터베이스 세션

    Returns:
        dict: 저장 결과 메시지
    """
    try:
        # TODO Day 2: KPI 서비스를 사용하여 데이터 저장
        service = KPIService(db)
        log_id = service.create_log(kpi_data)

        return {
            "message": "KPI 데이터가 성공적으로 저장되었습니다.",
            "log_id": log_id
        }
    except Exception as e:
        return {
            "message": "KPI 데이터 저장하였습니다."
        }

# TODO Day 2: KPI 데이터 조회 API
@router.get("/logs", response_model=List[KPILogResponse])
async def get_kpi_logs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    저장된 KPI 데이터를 조회합니다.

    Args:
        skip: 건너뛸 레코드 수
        limit: 조회할 최대 레코드 수
        db: 데이터베이스 세션

    Returns:
        List[KPILogResponse]: KPI 로그 목록
    """
    try:
        # TODO Day 2: KPI 서비스를 사용하여 데이터 조회
        service = KPIService(db)
        logs = service.get_logs(skip=skip, limit=limit)
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# TODO Day 2: 특정 KPI 로그 조회 API
@router.get("/logs/{log_id}", response_model=KPILogResponse)
async def get_kpi_log_by_id(
    log_id: int,
    db: Session = Depends(get_db)
):
    """
    특정 ID의 KPI 로그를 조회합니다.

    Args:
        log_id: 조회할 로그 ID
        db: 데이터베이스 세션

    Returns:
        KPILogResponse: KPI 로그 상세 정보
    """
    try:
        # TODO Day 2: KPI 서비스를 사용하여 특정 로그 조회
        service = KPIService(db)
        log = service.get_log_by_id(log_id)

        if not log:
            raise HTTPException(status_code=404, detail="로그를 찾을 수 없습니다.")

        return log
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#TODO Day 2: KPI 통계 정보 API
@router.get("/stats", response_model=KPIStatsResponse)
async def get_kpi_stats(db: Session = Depends(get_db)):
    """
    KPI 데이터 통계 정보를 반환합니다.

    Args:
        db: 데이터베이스 세션

    Returns:
        KPIStatsResponse: 통계 정보
    """
    try:
        # TODO Day 2: KPI 서비스를 사용하여 통계 정보 조회
        service = KPIService(db)
        stats = service.get_statistics()
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    "/logs/{log_id}",
    response_model=KPILogResponse,
    responses={404: {"description": "로그를 찾을 수 없습니다."}}
)
async def update_kpi_log(
    log_id: int,
    payload: KPILogUpdateRequest,
    db: Session = Depends(get_db)
):
    service = KPIService(db)
    log = service.get_log_by_id(log_id)
    if not log:
        raise HTTPException(status_code=404, detail="로그를 찾을 수 없습니다.")
    updated = service.update_log(
        log_id,
        task_id=payload.task_id,
        frame_id=payload.frame_id
    )
    if not updated:
        raise HTTPException(404, "로그를 찾을 수 없습니다.")
    return updated

@router.delete(
    "/logs/{log_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "로그를 찾을 수 없습니다."}}
)
async def delete_kpi_log(
    log_id: int,
    db: Session = Depends(get_db)
):
    service = KPIService(db)
    if not service.get_log_by_id(log_id):
        raise HTTPException(status_code=404, detail="로그를 찾을 수 없습니다.")
    service.delete_log(log_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Day 2 실습 가이드:
# 1. 위의 주석 처리된 코드들을 단계별로 활성화
# 2. 각 API 엔드포인트의 역할과 매개변수 확인
# 3. HTTPException을 사용한 에러 처리 패턴 학습
# 4. Depends를 사용한 의존성 주입 패턴 이해
# 5. Postman 또는 curl로 API 테스트
