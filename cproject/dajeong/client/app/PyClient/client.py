#!/usr/bin/env python3
import requests
import json
from datetime import datetime

BASE_URL = "http://host.docker.internal:8000"

def create_kpi_log(user_id, task_id, frame_id):
    """KPI 로그 생성"""
    kpi_data = {
        "timestamp": datetime.now().isoformat() + "Z",
        "user_id": user_id,
        "task_id": task_id,
        "frame_id": frame_id,
        "objects": [
            {
                "id": 1,
                "type": "car",
                "position": {"x": 0.1, "y": 0.2, "z": 0.6}
            },
            {
                "id": 2,
                "type": "person", 
                "position": {"x": 0.5, "y": 0.3, "z": 0.0}
            }
        ]
    }
    
    r = requests.post(f"{BASE_URL}/kpi/log", json=kpi_data)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.json()}")

def get_kpi_logs_by_user(user_id):
    """특정 사용자의 KPI 로그 조회"""
    r = requests.get(f"{BASE_URL}/kpi/logs")
    if r.status_code == 200:
        logs = r.json()
        # user_id로 필터링
        user_logs = [log for log in logs if log.get('user_id') == user_id]
        print(f"User {user_id}의 KPI 로그 {len(user_logs)}개:")
        for log in user_logs:
            print(f"  - Log ID: {log['id']}, Task: {log['task_id']}, Frame: {log['frame_id']}")
            print(f"    Objects: {len(log.get('objects_id', []))}개")
    else:
        print(f"Error: {r.status_code}")

def get_kpi_stats():
    """KPI 통계 조회"""
    r = requests.get(f"{BASE_URL}/kpi/stats")
    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        stats = r.json()
        print(f"전체 로그: {stats['total_logs']}개")
        print(f"전체 객체: {stats['total_objects']}개")
        print(f"객체 타입별: {stats['object_types']}")

def delete_kpi_log(log_id):
    """KPI 로그 삭제 (현재 API에 없으므로 메시지만 출력)"""
    print(f"Log ID {log_id} 삭제 기능은 현재 API에 구현되지 않았습니다.")

def get_existing_users():
    """저장된 사용자 목록 조회"""
    r = requests.get(f"{BASE_URL}/kpi/logs")
    if r.status_code == 200:
        logs = r.json()
        # 중복 제거하고 정렬
        users = sorted(list(set(log.get('user_id') for log in logs if log.get('user_id') is not None)))
        return users
    return []

def select_user():
    """사용자 선택 메뉴 (동적 생성)"""
    existing_users = get_existing_users()
    
    print("사용자 선택:")
    
    # 기존 사용자들 표시
    for i, user_id in enumerate(existing_users, 1):
        print(f"{i}) User {user_id}")
    
    # 새 사용자 추가 옵션
    next_option = len(existing_users) + 1
    print(f"{next_option}) 새 사용자 추가")
    
    while True:
        try:
            choice = int(input(f"선택 (1-{next_option})> ").strip())
            if 1 <= choice <= len(existing_users):
                return existing_users[choice - 1]
            elif choice == next_option:
                # 새 사용자 ID 입력
                while True:
                    try:
                        new_user_id = int(input("새 User ID 입력> ").strip())
                        if new_user_id > 0:
                            return new_user_id
                        else:
                            print("양수를 입력해주세요.")
                    except ValueError:
                        print("숫자를 입력해주세요.")
            else:
                print(f"1-{next_option} 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

def menu():
    print("==== KPI 데이터 관리 메뉴 ====")
    print("1) KPI 로그 생성")
    print("2) 사용자별 KPI 로그 조회")
    print("3) KPI 통계 조회")
    print("4) KPI 로그 삭제")
    print("0) 종료")
    return input("선택> ")

def main():
    while True:
        choice = menu().strip()
        if choice == '1':
            try:
                user_id = select_user()
                task_id = int(input("Task ID 입력> ").strip())
                frame_id = int(input("Frame ID 입력> ").strip())
                create_kpi_log(user_id, task_id, frame_id)
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == '2':
            try:
                user_id = select_user()
                get_kpi_logs_by_user(user_id)
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == '3':
            get_kpi_stats()
        elif choice == '4':
            try:
                log_id = int(input("삭제할 Log ID> ").strip())
                delete_kpi_log(log_id)
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == '0':
            print("종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")
        print()

if __name__ == "__main__":
    main()