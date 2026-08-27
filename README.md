# HUMAN_AI_2026

> 천안 데이터·AI 교육과정에서 학습한 데이터 엔지니어링, 머신러닝, 딥러닝, 응용 AI, MLOps 실습을 정리한 저장소입니다.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep_Learning-FF6F00?logo=tensorflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Model_API-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-MLOps-2496ED?logo=docker&logoColor=white)

## 과정 소개

이 저장소는 단순한 예제 코드 모음이 아니라, 데이터를 수집하고 저장한 뒤 분석·학습하고 API와 컨테이너로 서비스하는 전체 흐름을 실습한 기록입니다.

**데이터 수집·통신 → 저장·처리 → 분석·시각화 → 머신러닝 → 딥러닝 → 응용 AI → API 배포 → Docker·CI/CD**

스마트팩토리 관점에서는 센서·설비 데이터를 받아 이상을 탐지하고, 학습된 모델을 실제 서비스로 운영하는 과정과 연결됩니다.

## 전체 학습 과정

| 단계 | 학습·실습 내용 | 주요 기술 |
|---|---|---|
| 1. 개발 환경 | Python 가상환경, Anaconda, Jupyter Notebook, PyCharm | Python, Conda, pip |
| 2. 데이터 수집·통신 | 실시간 메시지 송수신, 서버·클라이언트 통신, 멀티스레드 처리 | Kafka, TCP/IP, Socket, Thread |
| 3. 데이터 저장·처리 | 문서형 DB CRUD, CSV·이미지 저장, 분산 데이터 처리 | MongoDB, pandas, PySpark |
| 4. 분석·시각화 | 데이터 전처리, 통계 확인, 그래프 작성 | NumPy, pandas, Matplotlib, Seaborn |
| 5. 머신러닝 | 회귀·분류, 앙상블, 성능 평가, 모델 해석 | LightGBM, Logistic Regression, XGBoost, SHAP |
| 6. 딥러닝 | 이진·다중 분류, 이미지·시계열 학습 | TensorFlow/Keras, CNN, RNN |
| 7. 응용 AI | 제조 이상 분류, 오토인코더 이상 탐지, 오디오 분류, 멀티태스크 학습 | Autoencoder, Conv1D, BiLSTM, Attention |
| 8. 비전 AI | 객체 탐지·추적 및 충돌 위험 분석 | YOLOv8, DeepSORT, OpenCV |
| 9. 모델 서비스 | 학습 모델을 REST API로 제공하고 클라이언트에서 호출 | FastAPI, Uvicorn |
| 10. MLOps | WSL 환경, 모델 API 컨테이너화, Compose 실행, CI/CD 흐름 | WSL2, Docker, Docker Compose, GitHub Actions |

## 주요 실습

### 데이터 엔지니어링

- Kafka Producer/Consumer를 이용한 실시간 데이터 스트리밍
- TCP/IP 서버·클라이언트 통신
- 멀티스레드 기반 동시 요청 처리
- MongoDB 데이터·CSV·이미지 저장 및 조회
- PySpark DataFrame과 병렬 처리
- FastAPI 서버 구축 및 클라이언트 요청

### 머신러닝

- **LightGBM 회귀**: California Housing 데이터의 주택 가격 예측
- **Logistic Regression**: 유방암 데이터 이진 분류
- **XGBoost**: 분류 모델 학습과 성능 평가
- **SHAP**: 모델 예측에 영향을 준 특성 해석
- **앙상블 모델**: 여러 모델의 예측을 결합해 일반화 성능 개선
- 정확도, 정밀도, 재현율, F1-score, ROC-AUC, 오차행렬 평가

### 딥러닝

- Dense 신경망을 이용한 이진 분류와 다중 클래스 분류
- CNN 기반 Fashion-MNIST 및 CIFAR-10 이미지 분류
- SimpleRNN 기반 시계열 예측
- EarlyStopping, Dropout을 이용한 과적합 방지
- 학습 모델 저장과 신규 데이터 예측

### 제조·응용 AI

- 제조 공정 품질 이상 분류
- 정상 데이터의 패턴을 학습하는 오토인코더 기반 이상 탐지
- 음원을 스펙트로그램 이미지로 변환한 악기 분류
- 고장 여부와 고장 원인을 함께 예측하는 멀티태스크 모델
- Conv1D + BiLSTM + Attention 구조를 이용한 시계열 특징 학습

### YOLO + DeepSORT

- YOLOv8 객체 탐지
- DeepSORT 객체 ID 추적
- 사람·차량·지게차 등 관심 객체 필터링
- 이동 궤적과 객체 간 거리 계산
- 제조 현장 충돌 위험 감지 응용

실행 예시:

```bash
cd C:\workspace\yolo
python DeepSort.py --source ./data/collision2.mp4
```

### MLOps

이 과정에서는 다음 흐름을 직접 실습했습니다.

1. WSL2 Ubuntu 및 Python 가상환경 구성
2. 머신러닝 모델 생성·저장
3. FastAPI 예측 API 작성
4. Docker 이미지 빌드
5. Docker Compose로 API 컨테이너 실행
6. GitHub 기반 버전 관리와 CI/CD 흐름 학습

```bash
docker build -t mlops/api:v1 .
docker compose up --build
```

> Kubernetes, Kubeflow, 운영 모니터링, 데이터·개념 드리프트 감지와 자동 재학습은 전체 MLOps 구조에서 학습한 개념 범위이며, 저장소의 핵심 실습 범위는 Docker 기반 모델 서비스와 CI/CD까지입니다.

## 저장소 구조

```text
HUMAN_AI_2026/
├─ README.md
├─ MEMO/                         # 일차별 복습용 Word 실습 매뉴얼
└─ workspace/
   ├─ MongoDB/                   # MongoDB 기본 및 AI 모델 연동
   ├─ PyCharm/
   │  ├─ AI/
   │  │  ├─ ML 기본 실습/
   │  │  ├─ DL 기본 실습/
   │  │  └─ 응용 실습/
   │  └─ workspace/
   │     ├─ FAST_API/
   │     ├─ Kafka/
   │     ├─ TCP_IP/
   │     └─ yolo/
   ├─ jupyter_notebook/          # 데이터 분석·PySpark·AI 노트북 및 데이터
   ├─ _Docker,MLOps/             # Docker·MLOps 실습 파일
   ├─ _image/                    # 실습 이미지
   └─ 설치법/                    # 환경 및 도구별 설치 기록
```

## 자료 바로가기

- [일차별 실습 매뉴얼](./MEMO)
- [머신러닝·딥러닝·응용 AI](./workspace/PyCharm/AI)
- [Kafka·FastAPI·TCP/IP 실습](./workspace/PyCharm/workspace)
- [MongoDB 실습](./workspace/MongoDB)
- [Jupyter Notebook 실습](./workspace/jupyter_notebook)
- [Docker·MLOps 실습](./workspace/_Docker%2CMLOps)
- [설치 방법](./workspace/설치법)

## 실행 환경 준비

### 저장소 받기

```bash
git clone https://github.com/Jkeonshin/HUMAN_AI_2026.git
cd HUMAN_AI_2026
```

### Conda 가상환경 예시

```bash
conda create -n ai python=3.10
conda activate ai
python -m pip install --upgrade pip
```

실습별로 필요한 패키지와 실행 방식이 다르므로 [설치법 폴더](./workspace/설치법)의 안내를 먼저 확인하세요. 대용량 데이터나 일부 외부 데이터셋은 별도 다운로드가 필요할 수 있습니다.

## 학습 결과

이 과정을 통해 다음과 같은 하나의 AI 서비스 흐름을 경험했습니다.

```text
문제 정의
  → 데이터 수집·저장
  → 전처리·시각화
  → 모델 학습·평가
  → 모델 해석
  → FastAPI 서비스
  → Docker 컨테이너
  → CI/CD
  → 운영 모니터링·재학습 개념
```

최종적으로 모델 정확도만 확인하는 데서 끝나지 않고, **데이터가 들어오는 구조부터 모델을 서비스하고 운영하는 단계까지** 전체 AI 개발 생명주기를 학습하는 것을 목표로 했습니다.

## 참고

- 본 저장소는 교육 및 복습 목적으로 작성되었습니다.
- 실행 환경과 라이브러리 버전에 따라 일부 코드 수정이 필요할 수 있습니다.
- 데이터셋과 모델 파일을 사용할 때는 각 원본의 라이선스를 확인해야 합니다.
