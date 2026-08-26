#============================================================================
'''
퀴즈1) 80점 이상의 학생정보를 서버로 부터 받아오는 API 구현
--> GET /students/search?min_score=80
--> 응답
{
    {"id":1, "name":"홍길동","score":85},
    {"id":3, "name":"이영희","score":95}
}

    등급기준
    90이상 - A
    80이상 - B
    70이상 - C
    60이상 - D
    60미만 - F

'''
#============================================================================

import requests
import json

## 1. 서버 접속 정보
SERVER_URL = "http://192.168.133.107:8000/students/search"
print("학생 점수 조회 클라이언트 시작(종료 = exit)\n")

## 2. 사용자 입력
while True:
    min_score = input("기준 점수 입력: ").strip()

    # exit 입력 시 종료
    if min_score.lower() == "exit":
        print("클라이언트 종료")
        break

    ## 3. GET 요청 전송
    try:
        response = requests.get(SERVER_URL, params={"min_score": min_score})
    except requests.exceptions.RequestException as e:
        print(f"서버 연결 오류: {e}\n")
        continue

    ## 4. 서버 응답 처리
    if response.status_code == 200:
        result = response.json()
        print(f"\n서버 응답:\n{json.dumps(result, ensure_ascii=False, indent=2)}\n")
    else:
        print(f"오류 발생: {response.status_code}, {response.text}\n")