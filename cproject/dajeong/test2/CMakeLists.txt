cmake_minimum_required(VERSION 3.10)
project(mylib LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 정적 라이브러리 타겟
add_library(mylib STATIC
  mylib.cpp
)

# 헤더 검색 경로 (애플리케이션에서 include)
target_include_directories(mylib PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}
)