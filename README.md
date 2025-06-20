# 2025 DPT Summer Internship

## 프로젝트 개요

본 프로젝트는 DPT 팀의 2025년 여름 인턴십 프로그램으로, 데이터 파이프라인과 센서 데이터 처리에 관한 실무 경험을 제공합니다.

## 프로젝트 구조

```
2025-dpt-summer-internship/
├── pipeline/           # 데이터 분석 & 백엔드 파이프라인 프레임워크 학습
└── sensing/            # 센서 데이터 처리를 위한 C++ 학습
```

### Pipeline 프로젝트
- **목적**: 데이터 분석과 백엔드 파이프라인 프레임워크 학습
- **주요 기술스택**: FastAPI, PostgreSQL, Airflow, Docker
- **내용**: KPI 데이터 수집 API 구현 및 자동화 파이프라인 구축

### Sensing 프로젝트
- **목적**: 센서 데이터 처리를 위한 C++ 지식 학습
- **주요 기술스택**: C++, CMake
- **내용**: 센서 데이터 처리 및 빌드 시스템 학습

## 인턴십 학습 일정 (2025년 6월)

### Day 1 (6/23) - 개발 환경 세팅 & Git / FastAPI 맛보기
- **시간**: 14:00 – 18:00 (KST)
- **내용**:
  - 개발 환경 구축 (VS Code, Docker, 필수 확장 프로그램)
  - Git 워크플로우 실습 (clone → branch → PR)
  - FastAPI 기초 실습 (GET /ping, POST /echo API 구현)
- **결과물**: 개인 브랜치 PR 요청 + 팀원 리뷰

### Day 2 (6/24) - FastAPI 기반 KPI API 실습
- **목표**: KPI 데이터를 저장하는 REST API 구현
- **내용**:
  - FastAPI + PostgreSQL 연동 (SQLAlchemy 기반)
  - `/log` POST API 구현 (KPI 데이터 수신 및 저장)
  - DB 구조 설계 및 FastAPI 구조 정리
- **결과물**: KPI 저장 API 동작 캡처 + README 작성

### Day 3 (6/25) - CMake 기초
- **목표**: C++ 빌드 시스템 학습
- **내용**: CMake를 이용한 C++ 프로젝트 빌드 실습

### Day 4 (6/26) - Airflow DAG 연동
- **목표**: KPI 분석 로직 자동화
- **내용**:
  - Airflow 핵심 개념 학습 (DAG, Task, Operator)
  - Docker Compose를 통한 Airflow 서비스 구성
  - BashOperator를 이용한 데이터 처리 DAG 구성
- **결과물**: DAG 정의 코드 + 실행 결과 + 전체 흐름 설명

### Day 5 (6/27) - 리뷰 · Q&A · 발표
- **내용**:
  - 코드 리뷰 및 리팩터링 포인트 피드백
  - Airflow DAG 확장 아이디어 브레인스토밍
  - 개인별 5분 발표

## 시작하기

### 필수 도구
- VS Code + 확장 프로그램 (Python, Docker, YAML)
- Git CLI
- Docker & Docker Compose
- DBeaver (DB 관리 도구)
- Postman (API 테스트 도구)

### 프로젝트 실행
각 프로젝트 폴더의 README.md를 참고하여 실행하세요.

## 협업 규칙

### Git 워크플로우
1. 개인 브랜치 생성
2. 기능 개발 및 커밋
3. Pull Request 생성
4. 팀원 리뷰 후 머지

### Commit Message Convention
- feat: 새로운 기능 추가
- fix: 버그 수정
- docs: 문서 수정
- style: 코드 포맷팅
- refactor: 코드 리팩터링
- test: 테스트 추가/수정

## 학습 목표

1. **백엔드 개발**: FastAPI를 이용한 REST API 개발
2. **데이터베이스**: PostgreSQL과 SQLAlchemy를 이용한 데이터 관리
3. **데이터 파이프라인**: Airflow를 이용한 자동화 시스템 구축
4. **C++ 개발**: CMake를 이용한 빌드 시스템 및 센서 데이터 처리
5. **협업**: Git 워크플로우 및 코드 리뷰 프로세스

---

**Happy Coding! 🎉**
