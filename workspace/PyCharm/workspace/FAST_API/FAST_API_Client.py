#============================================================================
'''
AI 클라이언트 (Request 기반)
- 사용자 입력을 받아 ai 서버에 분석 요청을 전송하고
- json 응답을 받아 콘솔에 출력
'''
#============================================================================

import requests  # http 통신용
import json

from win32con import FALSE

## 1. 서버 접속 정보
SERVER_URL = "http://192.168.133.107:8000/analyze"
print("AI 서버 클라이언트 시작(종료 = exit)\n")

## 2. 사용자 입력
while True:
    # 분석 모드 선택
    mode = input("분석 모드 입력 (length / sentiment / keywords):").strip()

    # exit 입력시 종료
    if mode.lower() == "exit":
        print("클라이언트 종료")
        break

    # 분석형 문장 입력
    text = input("분석할 문장 입력 : ").strip()

    # 요청 데이터(json) 생성
    payload = {"mode":mode, "text": text}

    # POST 요청 전송
    try:
        response = requests.post(SERVER_URL, json=payload)
    except requests.exceptions.RequestException as e:
        print(f"서버 연결 오류 : {e}\n")
        continue

    ## 5. 서버 응답 처리
    ## 5. 서버 응답 처리
    if response.status_code == 200:  # 정상 동작 처리
        result = response.json()
        print(f"\n서버 응답:\n{json.dumps(result, ensure_ascii=False, indent=2)}")
    else:
        print(f"오류 발생: {response.status_code}, {response.text}\n")
