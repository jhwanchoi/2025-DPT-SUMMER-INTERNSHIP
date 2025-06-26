# 🚀 KPI 데이터 수집 및 분석 시스템

이 프로젝트는 C 언어로 작성된 클라이언트가 **FastAPI 기반의 REST API 서버**에 KPI 데이터를 전송하고,  
그 데이터를 **PostgreSQL** 데이터베이스에 저장·조회하는 **컨테이너 기반 시스템**입니다.

---

## 📦 구성 요소

- **C Client (libcurl + cJSON)**: 터미널 기반 사용자 인터페이스, REST API 호출  
- **FastAPI Server**: KPI 로그 및 통계 API 제공  
- **PostgreSQL**: KPI 데이터 저장소  
- **Docker**: 모든 구성 요소를 컨테이너로 실행  

---

## 🧱 프로젝트 구조

<details>
<summary>📁 디렉토리 구조 보기</summary>

```bash
.
├── app/
│   └── CClient/
│       ├── client.c
│       ├── main.c
│       ├── CMakeLists.txt
│       └── build/
├── docker-compose.yml
├── client.Dockerfile
├── server/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── database.py
│   └── requirements.txt
```

</details>

---

## ✅ 실행 방법 가이드

아래 순서를 따라 KPI 프로젝트를 실행할 수 있습니다.  
전체 실행은 Docker 기반으로 이루어지며, C 클라이언트는 별도 컨테이너에서 빌드됩니다.

---

### 1️⃣ Docker 네트워크 생성

```bash
docker network create kpi_network
```

---

### 2️⃣ FastAPI 서버 및 PostgreSQL 실행

```bash
docker-compose up -d fastapi postgres
```

FastAPI는 `http://localhost:8000`에서 실행되며,  
`http://localhost:8000/docs`에서 API 문서를 확인할 수 있습니다.

---

### 3️⃣ C 클라이언트 컨테이너 실행

```bash
docker run -it --rm \
  -v "$(pwd)":/workspace \
  -w /workspace/app/CClient/build \
  pipeline-client:latest \
  bash
```

---

### 4️⃣ CMake로 C 클라이언트 빌드 및 실행

```bash
apt-get update && apt-get install -y \
  cmake build-essential pkg-config libcjson-dev

cmake ..
make
./client
```

---

### 🎉 실행 완료

`./client` 실행 후 터미널에서 메뉴를 선택하면  
FastAPI 서버에 요청을 보내고 KPI 로그를 생성하거나 조회할 수 있습니다.

---

## 📦 Docker 이미지 빌드 (처음 한 번만 필요)

```bash
docker build -t pipeline-client:latest -f client.Dockerfile .
```

---

## 🙋‍♀️ 문의

프로젝트에 대한 질문이나 피드백은 이슈 또는 PR로 남겨주세요. 감사합니다!