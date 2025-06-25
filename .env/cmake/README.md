# 빌드 방법

```
cd .env/cmake
docker build -t ubuntu-cmake-cpp:22.04 .
```

# 컨테이너 실행

```
cd cproject

docker run --rm -it -v .:/workspace ubuntu-cmake-cpp:22.04
```
