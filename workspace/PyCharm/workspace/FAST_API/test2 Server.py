#==============================================================
'''
퀴즈2) 성적 등급 계산 API 구현
--> GET /students/grade
--> 응답
{
    "name":"홍길동",
    "score":85,
    "grade":"B"
}

등급기준
90이상 - A
80이상 - B
70이상 - C
60이상 - D
60미만 - F

'''
#==============================================================

from fastapi import FastAPI, Query
import uvicorn

## 1. FastAPI 웹 인스턴스 생성
app = FastAPI(title="학생 성적 등급 조회 서버")

## 2. 학생 데이터
students = [
    {"id": 1, "name": "홍길동", "score": 85},
    {"id": 2, "name": "김철수", "score": 72},
    {"id": 3, "name": "이영희", "score": 95},
    {"id": 4, "name": "박민수", "score": 60}
]

## 3. 학생 이름으로 성적 등급 조회
# GET /students/grade?name=홍길동
@app.get("/students/grade")
async def get_student_grade(name: str = Query(...)):
    student = next((student for student in students if student["name"] == name), None)

    if student is None:
        return {"error": "학생을 찾을 수 없습니다."}

    score = student["score"]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    result = {
        "name": student["name"],
        "score": score,
        "grade": grade
    }

    return result

## 4. 서버 실행부
if __name__ == "__main__":
    uvicorn.run(app, host="192.168.133.107", port=8000)