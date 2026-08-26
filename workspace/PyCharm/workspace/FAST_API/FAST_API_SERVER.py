#==============================================================
'''

FastAPI 서버
- 클라이언트로부터 분석 요청을 받아
- 문장 길이, 감성, 키워드 탐지 분석 결과를 반환하는 실습
'''
#==============================================================

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline    ## 이미 학습한 결과파일을 가지고 추론을 하는
import uvicorn

## 1. 감정분석 모델 로드
# Hugging Face의 사진 학습된 모델을 사용
sentiment_analyzer = pipeline("sentiment-analysis") #모델 결과 다운로드

## 2. FastAPI 웹 인스턴스 생성
app = FastAPI(title="ai 분석 서버")

## 3. 데이터 구조 정의
class AnalysisRequest(BaseModel):
    mode: str #분석모드 (length / sentiment / keyword)
    text: str #분석할 문장

## 4. 분석 api 앤드포인트를 정의
@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    #요청한 값 읽기
    mode =request.mode.lower()
    text =request.text

    # 1) 문장 길이 분석
    if mode == "length":
        result = {
            "result" : len(text),
            "desc" : f"문장 길이는 {len(text)}자 입니다"
        }

    #2) 감성분석 (transformers 이용)
    elif mode == "sentiment":
        analyzers = sentiment_analyzer(text)[0]
        label = analyzers["label"]                #감정결과
        score = round(analyzers["score"],3)       #신뢰도 (0~1)
        result = {
            "result" : label,
            "confidence": score,
            "desc": f"감정 : {label}, 신뢰도: {score}"
        }

    # 3) 키워드 탐지
    elif mode == "keywords":
        keywords = ["ai", "press", "factory", "defect", "data", "불량"]
        found = [w for w in keywords if w.lower() in text.lower()]
        result = {
            "result": found,
            "desc": f"키워드 발견: {', '.join(found) if found else '없음'}"
        }

    # 4) 지원하지 않는 모드 처리
    else:
        result = {
            "error": f"지원하지 않는 모드입니다: {mode}"
        }

    return result  # json 결과 반환


## 5. 서버 실행부
if __name__ == "__main__":
    uvicorn.run(app, host="192.168.133.107", port=8000)