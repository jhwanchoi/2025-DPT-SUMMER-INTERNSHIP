cmake_minimum_required(VERSION 3.10)
project(CClient LANGUAGES C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# libcurl
find_package(CURL REQUIRED)

# pkg‐config and cJSON
find_package(PkgConfig REQUIRED)
pkg_check_modules(CJSON REQUIRED libcjson)

# 바이너리
add_executable(client
  main.c
  client.c
)

# cJSON 헤더 경로
target_include_directories(client PRIVATE
  ${CJSON_INCLUDE_DIRS}
)

# cJSON 컴파일 옵션 (ifdef 등 추가 플래그가 있을 때 필요)
target_compile_options(client PRIVATE
  ${CJSON_CFLAGS_OTHER}
)

# 링크
target_link_libraries(client PRIVATE
  CURL::libcurl
  ${CJSON_LIBRARIES}
)