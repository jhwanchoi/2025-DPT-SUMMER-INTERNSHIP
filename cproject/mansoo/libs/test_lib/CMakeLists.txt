cmake_minimum_required(VERSION 3.10)

# 프로젝트 이름 설정
project(test_lib)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 헤더 파일 경로 추가
include_directories(include)

# 소스 파일들
set(SOURCES
    src/test_lib.cpp
)

# 정적 라이브러리 생성
add_library(test_lib STATIC ${SOURCES})

# 라이브러리 타겟 속성 설정
# set_target_properties(test_lib PROPERTIES
#     OUTPUT_NAME "test_lib"
#     VERSION 1.0.0
#     SOVERSION 1
# )
