#==============================================================
'''
FastAPI 서버
- 학생 정보를 가지고 있음
- 기준 점수 이상인 학생 정보를 반환
'''
#==============================================================

from fastapi import FastAPI, Query
import uvicorn

## 1. FastAPI 웹 인스턴스 생성
app = FastAPI(title="학생 점수 조회 서버")

## 2. 학생 데이터
students = [
    {"id": 1, "name": "홍길동", "score": 85},
    {"id": 2, "name": "김철수", "score": 72},
    {"id": 3, "name": "이영희", "score": 95},
    {"id": 4, "name": "박민수", "score": 60}
]

## 3. 기준 점수 이상 학생 조회 API
# GET /students/search?min_score=80
@app.get("/students/search")
async def search_students(min_score: int = Query(...)):
    result = [student for student in students if student["score"] >= min_score]
    return result

## 4. 서버 실행부
if __name__ == "__main__":
    uvicorn.run(app, host="192.168.133.107", port=8000)