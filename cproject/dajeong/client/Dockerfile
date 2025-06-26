FROM python:3.9-slim

WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    cmake \
    build-essential \
    curl \                  
    libcurl4-openssl-dev \
    pkg-config \
    libcjson-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
RUN pip install --no-cache-dir requests

# 애플리케이션 코드 복사
COPY . .

# 기본적으로 Python 클라이언트 실행
CMD ["python", "app/PyClient/client.py"] 