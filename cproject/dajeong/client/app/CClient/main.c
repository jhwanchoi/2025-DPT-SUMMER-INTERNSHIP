#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include "client.h"

// 메뉴 출력
static void menu() {
    puts("==== KPI 데이터 관리 메뉴 ====");
    puts("1) KPI 로그 생성");
    puts("2) 사용자별 KPI 로그 조회");
    puts("3) KPI 로그 수정");
    puts("4) KPI 로그 삭제");
    puts("0) 종료");
    printf("선택> ");
}

int main(void) {
    int choice;
    int user_id, task_id, frame_id, log_id;
    // 수정·삭제에 쓸 변수 미리 선언
    int log_count, *log_ids, sel, chosen_id;
    int new_task_id, new_frame_id;

    curl_global_init(CURL_GLOBAL_ALL);

    do {
        menu();
        if (scanf("%d%*c", &choice) != 1) break;

        switch (choice) {
            case 1:
                printf("User ID 입력> ");
                scanf("%d%*c", &user_id);
                printf("Task ID 입력> ");
                scanf("%d%*c", &task_id);
                printf("Frame ID 입력> ");
                scanf("%d%*c", &frame_id);
                create_kpi_log(user_id, task_id, frame_id);
                break;
            case 2:
                log_count = get_kpi_logs_by_user(user_id);

                if (log_count == 0) {
                    printf("해당 사용자의 로그가 없습니다.\n");
                    break;
                }

                break;
            case 3:   // 수정
                log_count = get_kpi_logs_by_user(0);  // 전체 로그 출력
                if (log_count == 0) {
                    printf("수정할 로그가 없습니다.\n");
                    break;
                }

                int chosen_id, new_task_id, new_frame_id;

                printf("수정할 Log ID 입력> ");
                scanf("%d%*c", &chosen_id);

                printf("새 Task ID> ");
                scanf("%d%*c", &new_task_id);
                printf("새 Frame ID> ");
                scanf("%d%*c", &new_frame_id);

                update_kpi_log(chosen_id, new_task_id, new_frame_id);
                printf("Log ID %d가 수정되었습니다.\n", chosen_id);
                break;
            case 4: 
                log_count = get_kpi_logs_by_user(0);  // user_id는 의미 없으니 0
                if (log_count == 0) {
                    printf("삭제할 로그가 없습니다.\n");
                    break;
                }

                int log_id;
                printf("삭제할 Log ID 입력> ");
                scanf("%d%*c", &log_id);

                delete_kpi_log(log_id);
                printf("Log ID %d 삭제 완료\n", log_id);
                break;
            case 0:
                puts("프로그램을 종료합니다.");
                break;
            default:
                puts("잘못된 선택입니다.");
        }
        puts("");
    } while (choice != 0);

    curl_global_cleanup();
    return 0;
}