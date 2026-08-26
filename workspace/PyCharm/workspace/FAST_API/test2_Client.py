#============================================================================
'''
학생 성적 등급 조회 클라이언트
- 사용자에게 학생 이름을 입력받음
- 서버에 GET 요청을 전송
- 학생 이름, 점수, 등급을 출력
'''
#============================================================================

import requests
import json

## 1. 서버 접속 정보
SERVER_URL = "http://192.168.133.107:8000/students/grade"
print("학생 성적 등급 조회 클라이언트 시작(종료 = exit)\n")

## 2. 사용자 입력
while True:
    student_name = input("학생 이름 입력: ").strip()

    if student_name.lower() == "exit":
        print("클라이언트 종료")
        break

    ## 3. GET 요청 전송
    try:
        response = requests.get(SERVER_URL, params={"name": student_name})
    except requests.exceptions.RequestException as e:
        print(f"서버 연결 오류: {e}\n")
        continue

    ## 4. 서버 응답 처리
    if response.status_code == 200:
        result = response.json()
        print(f"\n서버 응답:\n{json.dumps(result, ensure_ascii=False, indent=2)}\n")
    else:
        print(f"오류 발생: {response.status_code}, {response.text}\n")