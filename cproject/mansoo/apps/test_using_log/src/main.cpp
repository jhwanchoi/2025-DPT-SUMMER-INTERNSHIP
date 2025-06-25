#include <iostream>
#include <spdlog/spdlog.h>
#include <spdlog/sinks/basic_file_sink.h>
#include <spdlog/sinks/stdout_color_sinks.h>

int main() {
    std::cout << "spdlog 테스트 프로그램 시작" << std::endl;
    
    // 기본 로거 설정
    spdlog::info("기본 로거로 정보 메시지 출력");
    spdlog::warn("경고 메시지 출력");
    spdlog::error("에러 메시지 출력");
    
    // 색상 콘솔 로거 생성
    auto console_logger = spdlog::stdout_color_mt("console_logger");
    console_logger->info("색상 콘솔 로거로 정보 메시지");
    console_logger->warn("색상 콘솔 로거로 경고 메시지");
    console_logger->error("색상 콘솔 로거로 에러 메시지");
    
    // 파일 로거 생성
    auto file_logger = spdlog::basic_logger_mt("file_logger", "logs/test_using_log.txt");
    file_logger->info("파일 로거로 정보 메시지");
    file_logger->warn("파일 로거로 경고 메시지");
    file_logger->error("파일 로거로 에러 메시지");
    
    // 로그 레벨 설정
    spdlog::set_level(spdlog::level::debug);
    spdlog::debug("디버그 레벨 메시지 (기본 로거)");
    
    console_logger->set_level(spdlog::level::debug);
    console_logger->debug("디버그 레벨 메시지 (콘솔 로거)");
    
    file_logger->set_level(spdlog::level::debug);
    file_logger->debug("디버그 레벨 메시지 (파일 로거)");
    
    // 포맷팅 예제
    int number = 42;
    std::string text = "Hello World";
    spdlog::info("숫자: {}, 텍스트: {}", number, text);
    
    // 구조화된 로깅
    spdlog::info("사용자 정보 - ID: {}, 이름: {}, 나이: {}", 12345, "홍길동", 30);
    
    std::cout << "spdlog 테스트 프로그램 완료" << std::endl;
    std::cout << "로그 파일은 logs/test_using_log.txt에 저장되었습니다." << std::endl;
    
    return 0;
}
