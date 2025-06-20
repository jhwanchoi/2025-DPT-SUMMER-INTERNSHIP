# Day 1 실습 가이드: 개발 환경 세팅 & FastAPI 맛보기

## 학습 목표
- 개발 환경 구축 및 설정 완료
- Git 워크플로우 실습으로 협업 기초 이해
- FastAPI 기초 개념 학습 및 간단한 API 구현

## 실습 내용

### 1단계: 개발 환경 구축

#### 필수 도구 설치 확인
```bash
# Git 버전 확인
git --version

# Python 버전 확인 (3.11 이상 권장)
python --version

# VS Code 확장 프로그램 설치 확인
code --list-extensions | grep -E "(ms-python|ms-azuretools.vscode-docker|redhat.vscode-yaml)"
```

#### 프로젝트 환경 설정
```bash
# 1. 레포지토리 클론
git clone <repository-url>
cd dpt-2025-summer-internship/tutorial

# 2. 가상환경 생성 및 활성화
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux  
source venv/bin/activate

# 3. 패키지 설치
pip install -r requirements.txt
```

### 2단계: Git 워크플로우 실습

#### 개인 브랜치 생성 및 자기소개 작성
```bash
# 1. 새 브랜치 생성
git checkout -b feature/add-self-introduction-<your-name>

# 2. 자기소개 파일 작성
mkdir -p docs/introductions
vim docs/introductions/<your-name>.md
```

**자기소개 파일 템플릿:**
```markdown
# 자기소개 - <이름>

## 기본 정보
- **이름**: 
- **소속**: 
- **이메일**: 

## 경험 및 관심사
- **프로그래밍 경험**: 
- **관심 기술**: 
- **인턴십 목표**: 

## 인사말
인턴십 기간 동안 잘 부탁드립니다!
```

#### 커밋 및 푸시
```bash
# 3. 변경사항 스테이징
git add .

# 4. 커밋 (컨벤션 준수)
git commit -m "feat: add self introduction for <your-name>"

# 5. 원격 저장소에 푸시
git push origin feature/add-self-introduction-<your-name>
```

#### Pull Request 생성
1. GitHub 웹사이트에서 새 PR 생성
2. 제목: `[Day 1] Add self introduction - <your-name>`
3. 설명: 자기소개 내용 간단 요약
4. 다른 팀원들을 리뷰어로 지정

### 3단계: FastAPI 기초 실습

#### FastAPI 서버 실행
```bash
# 서버 시작
uvicorn app.main:app --reload --port 8000

# 브라우저에서 확인
# http://localhost:8000        (루트 페이지)
# http://localhost:8000/docs   (Swagger UI)
# http://localhost:8000/redoc  (ReDoc)
```

#### 실습 과제 1: ping API 구현
`app/main.py` 파일에서 `ping()` 함수를 완성하세요.

**요구사항:**
- GET `/ping` 엔드포인트
- 응답: `{"message": "pong"}`

**힌트:**
```python
@app.get("/ping")
async def ping():
    # TODO: {"message": "pong"} 반환
    return {"message": "pong"}
```

**테스트:**
```bash
curl http://localhost:8000/ping
# 예상 응답: {"message":"pong"}
```

#### 실습 과제 2: echo API 구현  
`app/main.py` 파일에서 `echo()` 함수를 완성하세요.

**요구사항:**
- POST `/echo` 엔드포인트
- 입력: `{"message": "hello"}`
- 응답: `{"echo": "hello"}`

**힌트:**
```python
@app.post("/echo", response_model=EchoResponse)
async def echo(request: EchoRequest):
    # TODO: 입력받은 메시지를 echo 필드에 담아서 반환
    return EchoResponse(echo=request.message)
```

**테스트:**
```bash
curl -X POST http://localhost:8000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "hello world"}'
# 예상 응답: {"echo":"hello world"}
```

## 숙제
1. **자기소개 PR 생성**: 개인 브랜치에서 자기소개 작성 후 PR 요청
2. **ping, echo API 구현**: 두 API 모두 정상 동작하도록 구현
3. **팀원 PR 리뷰**: 다른 팀원들의 자기소개 PR에 댓글 작성

## 참고 자료

### FastAPI
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Pydantic 모델 가이드](https://pydantic-docs.helpmanual.io/)
- [HTTP 상태 코드](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

### Git
- [Git 커밋 메시지 컨벤션](https://www.conventionalcommits.org/)
- [GitHub Flow 가이드](https://guides.github.com/introduction/flow/)

### 개발 도구
- [VS Code Python 확장 가이드](https://code.visualstudio.com/docs/languages/python)
- [curl 사용법](https://curl.se/docs/manual.html)