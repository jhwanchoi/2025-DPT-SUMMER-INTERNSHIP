cmake_minimum_required(VERSION 3.10)

# 프로젝트 이름 설정
project(mansoo)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 출력 디렉토리 설정
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Build Libraries
add_subdirectory(3rdparty/spdlog)
add_subdirectory(libs/test_lib)

# Build Applications
add_subdirectory(apps/test_using_lib)
add_subdirectory(apps/test_using_log)
