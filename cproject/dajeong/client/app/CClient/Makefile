CC      := gcc
CXX     := g++
CFLAGS  := -I../../libs/mylib/include `curl-config --cflags`
CXXFLAGS := -I../../libs/mylib/include `curl-config --cflags`
LDFLAGS := -L../../libs/mylib/mylib_build -lmylib `curl-config --libs`
SRCS    := main.c client.c
OBJS    := $(SRCS:.c=.o)
TARGET  := client

.PHONY: all clean

all: ../../libs/mylib/mylib_build/libmylib.a $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) -o $@ $^ $(LDFLAGS)

main.o: main.c client.h
	$(CC) $(CFLAGS) -c $<

client.o: client.c client.h
	$(CC) $(CFLAGS) -c $<

# libs/mylib 먼저 빌드
../../libs/mylib/mylib_build/libmylib.a:
	cd ../../libs/mylib && mkdir -p build && cd build && cmake .. && make

clean:
	rm -f $(OBJS) $(TARGET)