#include <iostream>

#include "test_lib.hpp"

bool test_lib() {
    // Implemented some algorithm
    // 간단한 정렬 알고리즘 구현 (버블 정렬)
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    std::cout << "정렬 전 배열: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    // 버블 정렬 알고리즘
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // 두 요소 교환
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    
    std::cout << "정렬 후 배열: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    // 최대값 찾기
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    std::cout << "최대값: " << max << std::endl;

    std::cout << "called test_lib()" << std::endl;

    return true;
}
