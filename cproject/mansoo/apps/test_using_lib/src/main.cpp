#include <iostream>

#include "test_lib.hpp"

int main() {
    std::cout << "test_lib 라이브러리 테스트 시작" << std::endl;
    
    bool result = test_lib();
    
    if (result) {
        std::cout << "test_lib() 호출 성공!" << std::endl;
    } else {
        std::cout << "test_lib() 호출 실패!" << std::endl;
    }
    
    return 0;
}
