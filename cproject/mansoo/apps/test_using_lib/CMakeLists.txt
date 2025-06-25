cmake_minimum_required(VERSION 3.10)

# 프로젝트 이름 설정
project(test_using_lib)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 헤더 파일 경로 추가
include_directories(src)
include_directories(${CMAKE_SOURCE_DIR}/libs/test_lib/include)

# 소스 파일들
set(SOURCES
    src/main.cpp
)

# 실행 파일 생성
add_executable(test_using_lib ${SOURCES})

# test_lib 라이브러리 링크
target_link_libraries(test_using_lib test_lib)
