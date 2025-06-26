#include "client.h"
#include <curl/curl.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <cjson/cJSON.h>

static size_t write_cb(void *ptr, size_t size, size_t nmemb, void *userdata) {
    fwrite(ptr, size, nmemb, stdout);
    return size * nmemb;
}

static size_t string_write_cb(void *ptr, size_t size, size_t nmemb, void *userdata) {
    char **str_ptr = (char**)userdata;
    size_t total_size = size * nmemb;
    
    if (*str_ptr == NULL) {
        *str_ptr = malloc(total_size + 1);
        if (!*str_ptr) return 0;
        (*str_ptr)[0] = '\0';
    } else {
        size_t old_len = strlen(*str_ptr);
        char *new_buf = realloc(*str_ptr, old_len + total_size + 1);
        if (!new_buf) return 0;
        *str_ptr = new_buf;
    }

    size_t current_len = strlen(*str_ptr);
    memcpy(*str_ptr + current_len, ptr, total_size);
    (*str_ptr)[current_len + total_size] = '\0';
    
    return total_size;
}

static void perform_request(const char *method,
                            const char *url,
                            const char *json_payload) {
    CURL *curl = curl_easy_init();
    if (!curl) {
        fprintf(stderr, "curl init failed\n");
        return;
    }

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "Content-Type: application/json");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, method);
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);

    if (json_payload) {
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_payload);
    }

    CURLcode res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
        fprintf(stderr, "Request failed: %s\n",
                curl_easy_strerror(res));
    }

    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);
}

static char* perform_request_string(const char *method, const char *url) {
    CURL *curl = curl_easy_init();
    char *response = NULL;

    if (!curl) {
        fprintf(stderr, "curl init failed\n");
        return NULL;
    }

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "Content-Type: application/json");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, method);
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, string_write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    CURLcode res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
        fprintf(stderr, "Request failed: %s\n", curl_easy_strerror(res));
        free(response);
        response = NULL;
    } 

    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);
    return response;
}

// 간단한 사용자 ID 파싱 (실제로는 JSON 파서 사용 권장)
int* get_existing_users(int *count) {
    char url[256];
    snprintf(url, sizeof(url),
             "http://host.docker.internal:8000/api/v1/logs?skip=0&limit=100");
    char *response = perform_request_string("GET", url);

    if (!response) {
        *count = 0;
        return NULL;
    }
    
    // 간단한 파싱 (실제 구현에서는 JSON 라이브러리 사용 권장)
    int users[100]; // 최대 100개 사용자
    *count = 0;
    
    char *token = strtok(response, "{}[],\"");
    while (token != NULL && *count < 100) {
        if (strstr(token, "user_id") != NULL) {
            token = strtok(NULL, "{}[],\"");
            if (token != NULL) {
                int user_id = atoi(token);
                // 중복 체크
                int found = 0;
                for (int i = 0; i < *count; i++) {
                    if (users[i] == user_id) {
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    users[*count] = user_id;
                    (*count)++;
                }
            }
        }
        token = strtok(NULL, "{}[],\"");
    }
    
    free(response);
    
    // 정렬
    for (int i = 0; i < *count - 1; i++) {
        for (int j = i + 1; j < *count; j++) {
            if (users[i] > users[j]) {
                int temp = users[i];
                users[i] = users[j];
                users[j] = temp;
            }
        }
    }
    
    // 동적 할당으로 복사
    int *result = malloc(*count * sizeof(int));
    if (result) {
        memcpy(result, users, *count * sizeof(int));
    }
    
    return result;
}

int select_user(void) {
    int count;
    int *existing_users = get_existing_users(&count);
    
    printf("사용자 선택:\n");
    
    // 기존 사용자들 표시
    for (int i = 0; i < count; i++) {
        printf("%d) User %d\n", i + 1, existing_users[i]);
    }
    
    // 새 사용자 추가 옵션
    int next_option = count + 1;
    printf("%d) 새 사용자 추가\n", next_option);
    
    int choice;
    while (1) {
        printf("선택 (1-%d)> ", next_option);
        if (scanf("%d", &choice) == 1) {
            if (choice >= 1 && choice <= count) {
                int user_id = existing_users[choice - 1];
                free(existing_users);
                return user_id;
            } else if (choice == next_option) {
                // 새 사용자 ID 입력
                int new_user_id;
                while (1) {
                    printf("새 User ID 입력> ");
                    if (scanf("%d", &new_user_id) == 1) {
                        if (new_user_id > 0) {
                            free(existing_users);
                            return new_user_id;
                        } else {
                            printf("양수를 입력해주세요.\n");
                        }
                    } else {
                        printf("숫자를 입력해주세요.\n");
                        while (getchar() != '\n');
                    }
                }
            } else {
                printf("1-%d 사이의 숫자를 입력해주세요.\n", next_option);
            }
        } else {
            printf("숫자를 입력해주세요.\n");
            while (getchar() != '\n');
        }
    }
}

// user_id 기준으로 logs를 가져와서 ID 배열과 개수를 리턴
int* get_log_ids_by_user(int user_id, int *out_count) {
    char url[256];
    snprintf(url, sizeof(url),
             "http://host.docker.internal:8000/api/v1/logs?skip=0&limit=100&user_id=%d",
             user_id);

    char *resp = perform_request_string("GET", url);
    if (!resp) {
        *out_count = 0;
        return NULL;
    }

    cJSON *root = cJSON_Parse(resp);
    free(resp);
    if (!cJSON_IsArray(root)) {
        cJSON_Delete(root);
        *out_count = 0;
        return NULL;
    }

    int len = cJSON_GetArraySize(root);
    int *ids = malloc(len * sizeof(int));
    for (int i = 0; i < len; i++) {
        cJSON *item = cJSON_GetArrayItem(root, i);
        ids[i] = cJSON_GetObjectItem(item, "id")->valueint;
    }
    cJSON_Delete(root);
    *out_count = len;
    return ids;
}


void create_kpi_log(int user_id, int task_id, int frame_id) {
    char url[256], json[512];
    time_t now = time(NULL);
    struct tm *tm_info = gmtime(&now);
    char timestamp[30];
    strftime(timestamp, sizeof(timestamp), "%Y-%m-%dT%H:%M:%S.000Z", tm_info);
    
    snprintf(url, sizeof(url), "http://host.docker.internal:8000/api/v1/log");
    snprintf(json, sizeof(json),
        "{"
        "\"timestamp\":\"%s\","
        "\"user_id\":%d,"
        "\"task_id\":%d,"
        "\"frame_id\":%d,"
        "\"objects\":["
            "{"
            // "id":1,      ← 이 줄을 빼세요
            "\"type\":\"car\","
            "\"position\":{\"x\":0.1,\"y\":0.2,\"z\":0.6}"
            "},"
            "{"
            // "id":2,      ← 이 줄도 빼세요
            "\"type\":\"person\","
            "\"position\":{\"x\":0.5,\"y\":0.3,\"z\":0.0}"
            "}"
        "]"
        "}",
        timestamp, user_id, task_id, frame_id
    );
    
    perform_request("POST", url, json);
}


int get_kpi_logs_by_user(int user_id) {
    char url[256];
    snprintf(url, sizeof(url),
             "http://host.docker.internal:8000/api/v1/logs?skip=0&limit=100");

    // 1) JSON 전체를 문자열로 받아온다
    char *response = perform_request_string("GET", url);
    if (!response) {
        printf("KPI 로그 조회 실패 (user_id=%d)\n", user_id);
        return 0;
    }

    // 2) cJSON 으로 예쁘게 파싱·출력
    cJSON *root = cJSON_Parse(response);
    if (!cJSON_IsArray(root)) {
        printf("로그 데이터가 배열 형식이 아닙니다.\n");
        cJSON_Delete(root);
        free(response);
        return 0;
    }

    int len = cJSON_GetArraySize(root);
    for (int i = 0; i < len; i++) {
        cJSON *item    = cJSON_GetArrayItem(root, i);
        int    id      = cJSON_GetObjectItem(item, "id")->valueint;
        const char *ts = cJSON_GetObjectItem(item, "timestamp")->valuestring;
        int    uid     = cJSON_GetObjectItem(item, "user_id")->valueint;
        int    tid     = cJSON_GetObjectItem(item, "task_id")->valueint;
        int    fid     = cJSON_GetObjectItem(item, "frame_id")->valueint;
        cJSON *objs    = cJSON_GetObjectItem(item, "objects_id");
        int    oc      = cJSON_GetArraySize(objs);

        printf("── Log %d ──────────────────────\n", id);
        printf(" Timestamp : %s\n", ts);
        printf(" User ID   : %d\n", uid);
        printf(" Task ID   : %d\n", tid);
        printf(" Frame ID  : %d\n", fid);
        printf(" #Objects  : %d [", oc);
        for (int j = 0; j < oc; j++) {
            printf("%d%s",
                cJSON_GetArrayItem(objs, j)->valueint,
                j < oc - 1 ? ", " : "");
        }
        printf("]\n\n");
    }

    cJSON_Delete(root);
    free(response);
    return len;  // 조회된 로그 건수 리턴
}

void update_kpi_log(int log_id, int new_task_id, int new_frame_id) {
    char url[256], json[256];
    snprintf(url, sizeof(url), "http://host.docker.internal:8000/api/v1/logs/%d", log_id);
    snprintf(json, sizeof(json),
        "{\"task_id\":%d,\"frame_id\":%d}",
        new_task_id, new_frame_id);

    perform_request("PUT", url, json);
}

void delete_kpi_log(int log_id) {
    char url[256];
    snprintf(url, sizeof(url),
             "http://host.docker.internal:8000/api/v1/logs/%d",
             log_id);
    perform_request("DELETE", url, NULL);
}