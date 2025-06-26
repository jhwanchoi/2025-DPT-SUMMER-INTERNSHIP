#ifndef CLIENT_H
#define CLIENT_H

// 사용자 선택 함수
int select_user(void);

int* get_log_ids_by_user(int user_id, int *out_count);


// KPI CRUD 요청 함수들
void create_kpi_log(int user_id, int task_id, int frame_id);
int get_kpi_logs_by_user(int user_id);
void update_kpi_log(int log_id, int new_task_id, int new_frame_id);
void delete_kpi_log(int log_id);


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// End of include guard
#endif // CLIENT_H