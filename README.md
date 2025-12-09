# 비전 기반 지능형 주행 보조 시스템 

### Vision-Based-ADAS

> 센서 없이 **OpenCV**와 **YOLOv5** 로 구현한 지능형 주행 보조 시스템
> Advanced Driver Assistance System



<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-Custom-00FFFF?style=flat)](https://github.com/ultralytics/yolov5)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-C51A4A?style=flat&logo=raspberry-pi&logoColor=white)](https://www.raspberrypi.com/)
[![Arduino](https://img.shields.io/badge/Arduino-UNO-00979D?style=flat&logo=arduino&logoColor=white)](https://www.arduino.cc/)

</div>

<div align="center">

### 프로젝트 데모
![Image](https://github.com/user-attachments/assets/e2915de3-207e-4805-91f9-c9e6f4306fb0)

![Image](https://github.com/user-attachments/assets/99476136-0403-4d5e-a7f2-a1ca7cbcbdb1)

![Image](https://github.com/user-attachments/assets/8a53ab16-71b0-41cc-8774-b417bead44fd)

</div>



## 목차
1. [프로젝트 소개](#프로젝트-소개)
2. [주요 기능](#주요-기능)
3. [시스템 아키텍처](#시스템-아키텍처)
4. [기술 스택](#기술-스택)
5. [핵심 알고리즘](#핵심-알고리즘)
6. [설치 및 실행](#설치-및-실행)
7. [프로젝트 결과](#프로젝트-결과)
8. [기술적 도전과 해결](#기술적-도전과-해결)
9. [향후 개선 방향](#향후-개선-방향)
10. [팀 및 기여](#팀-및-기여)
11. [라이선스](#라이선스)


## 프로젝트 소개


### 📚 2024 한이음 ICT 멘토링 프로그램

본 프로젝트는 **2024년 한이음 ICT 멘토링 프로그램**의 일환으로 진행되었습니다.

- **프로그램**: 한국정보산업연합회 주관 산학 협력 프로젝트
- **프로젝트 기간**: 2024년 3월 ~ 11월 (9개월)
- **멘토**: 김신형
- **팀 구성**: 4인 (전자공학과 졸업생)

---

### 🚨 배경 및 필요성

#### 교통사고의 심각성
ADAS 기술은 운전자의 안전과 편의성 측면에서 중요한 요소로 부상하고 있다. 통계상 교통사고로 인해 약 25초에 1명씩 사람이 사망하고 있는데, 첨단 운전자 보조 시스템(ADAS, Advanced Driver Assistance Systems)을 활용하면 운전자를 보조하여 안전뿐만 아니라 경제적인 이익을 가져와 줄 것으로 예상된다.

#### 기존 ADAS의 한계

기존 ADAS 시스템은 다음과 같은 문제점을 가지고 있다.

| 한계점 | 설명 |
|:---:|---|
| **💰 높은 비용** | 라이다, 초음파 센서 등 고가의 센서 다수 사용 |
| **🔧 복잡한 구조** | 여러 센서의 융합 및 캘리브레이션 필요 |
| **⚙️ 유지보수 어려움** | 센서 고장 시 높은 수리 비용 |

---

### 🎯 프로젝트 목표

본 프로젝트는 고가의 센서 기반 ADAS 장비 없이, 단일 카메라 기반의 비전 기술만으로 ADAS 시스템을 구현하는 것을 목표로 한다.

#### 1️⃣ 비전 기반 저비용 ADAS 구현

라이다, 초음파 센서 없이 오직 **카메라만**으로 핵심 ADAS 기능을 구현하여 경제성을 확보

#### 2️⃣ 차선 인식 + 객체 탐지 통합 시스템

- **차선 탐지**: Canny Edge Detection + Hough Transform
- **객체 인식**: YOLOv5 커스텀 학습 (9개 클래스)
- **통합 제어**: 실시간 상황 판단 및 자동 주행 제어

#### 3️⃣ 날씨 정보를 고려한 지능형 주행

우천, 안개, 눈 등의 기상 상태에서 교통사고 사망률이 높게 나타나는 점을 고려하여, 
실시간 날씨 정보를 수집하고 이를 주행 제어에 반영

---

### 💡 프로젝트 차별점

#### 🔹 비전 기반 복합 기능 구현

하나의 카메라로 다음 기능을 모두 수행:

| 기능 | 기술 | 결과 |
|:---:|---|---|
| 🛣️ **차선 인식** | Canny + Hough | 차선 이탈 방지 |
| 🚦 **객체 탐지** | YOLOv5 (9 classes) | 충돌 회피 |
| 📏 **거리 측정** | 기하학적 삼각측량 | 안전거리 유지 |
| 🌦️ **날씨 대응** | API 크롤링 | 상황별 제어 |

---
### 🎓 학습 목표

프로젝트를 통해 다음 기술을 습득하고 활용

- **Computer Vision**: OpenCV, 영상 전처리, Edge Detection, Line Detection
- **Deep Learning**: YOLOv5 모델 학습, 커스텀 데이터셋 제작
- **Embedded Systems**: Raspberry Pi, Arduino, UART 통신
- **System Integration**: 하드웨어-소프트웨어 통합, 실시간 제어
- **Web Crawling**: API 활용, 외부 데이터 수집

---

## 주요 기능

본 프로젝트는 3가지 핵심 기능으로 자율주행을 구현

### 1.차선 탐지 

#### 🎯 핵심 기능

Canny Edge Detection + Hough Transform 기반 컴퓨터 비전 기법으로 차선을 인식

| 기능 | 설명 | 기술 |
|:---:|---|---|
| **실시간 차선 인식** | 직선 및 곡선 차선 검출 | Canny Edge  |
| **차선 이탈 방지** | 차선 중심 유지 주행 | Hough Transform |
| **조명 적응** | 다양한 조명 환경 대응 | HSV 색공간 튜닝 |
| **노이즈 제거** | 안정적인 차선 검출 | Gaussian Blur  |

#### 🔧 제어 로직

**알고리즘**
```
카메라 입력 → RoI 마스킹 → HSV 변환 → 이진화 (흰색/노란색)
→ Gaussian Blur → Canny Edge Detection → Hough Transform
→ 중심점 거리 계산 → PWM 제어 명령
```

**중심점 거리 기반 차등 PWM 제어**
```python
# 차선 중심과 RC카 중심 간 거리 계산
offset = detected_line_x - center_x

# 거리 기반 회전 제어
if offset > 80:  # 차선이 오른쪽에 있음
    turn_right(left_pwm=10, right_pwm=220)  # 급격한 우회전
elif offset < -80:  # 차선이 왼쪽에 있음
    turn_left(left_pwm=220, right_pwm=10)   # 급격한 좌회전
else:
    move_forward(pwm=70)  # 직진
```

#### 📊 주요 특징

- ✅ **HSV 색공간 튜닝**: 조명 변화에 강건한 차선 검출
- ✅ **RoI 마스킹**: 불필요한 영역 제거로 연산량 최적화
- ✅ **프레임 스킵**: 6프레임마다 처리하여 안정성 보장

---

### 2. 🚦 객체 탐지 및 충돌 회피 
YOLOv5 기반 다중 객체 실시간 탐지 및 거리 측정

#### 📌 딥러닝 모델



## 시스템 아키텍처

### 🔧 H/W 구성도

<table> <tr> <td align="center"><b>회로도</b><br> <img src="https://github.com/user-attachments/assets/99de63d4-4cb2-4124-a659-c363e90f96dc" width="95%"> </td> <td align="center"><b>L298N 20W 모터 드라이버</b><br> <img src="https://github.com/user-attachments/assets/05219c48-c05b-43e3-8f69-fc064e20c0f3" width="75%"> </td> </tr> </table>

---

### 💻 S/W 구성도

<table> <tr> <td align="center"><b>Lane Tracer</b><br> <img src="https://github.com/user-attachments/assets/74170473-170c-4459-b603-592b28dcac8d" width="95%"> </td> <td align="center"><b>Object Detection</b><br> <img src="https://github.com/user-attachments/assets/98e23368-5f04-496e-bb8f-f49ace3d1aad" width="95%"> </td> </tr> </table>

---

### 🔄 서비스 흐름도
<table> <tr> <td align="center"><b>Lane Tracer Flow</b><br> <img src="https://github.com/user-attachments/assets/d38f02bc-a475-4e9b-9c9f-18462ce3cd0a" width="95%"> </td> <td align="center"><b>Object Detection Flow</b><br> <img src="https://github.com/user-attachments/assets/cdeba528-5189-44a0-8d4a-a699b834f74e" width="95%"> </td> </tr> </table>

---

## 기술 스택


### 🔧 Hardware Stack
|   구성품   | 모델                  | 사양         | 역할                         |
| :-----: | ------------------- | ---------- | -------------------------- |
|   SBC   | **Raspberry Pi 5**  | 4GB RAM    | 비전 처리, 객체 탐지, 차선 처리, 통합 제어 |
|   MCU   | **Arduino UNO**     | ATmega328 | 모터 PWM 제어     |
| 모터 드라이버 | **L298N 2채널**     | 20W 출력  | 좌/우 바퀴 모터 제어               |
|   카메라   | **USB WebCam**      | 720p | 도로 영상 입력                   |
|    모터   | **DC Motor x4**     | 6~12V     | 차량 구동                      |
|    전원   | **AA Battery Pack** | 6×1.5V     | 모터 및 드라이버 전원 공급            |


---
### 💻 Software Stack
|        분류        | 기술                         |   버전 | 용도                             |
| :--------------: | -------------------------- | ---: | ------------------------------ |
|     프로그래밍 언어     | **Python**                 | 3.9+ | 전체 시스템 구현      |
|      컴퓨터 비전      | **OpenCV**                 |  4.8 | 영상 처리, 차선 탐지, 전처리              |
|     딥러닝 프레임워크    | **PyTorch**                |  2.0 | YOLOv5 모델 학습 및 추론              |
|     객체탐지           | **YOLOv5 (Custom)**        |    - | 9개 클래스 객체 탐지 모델                |
|      데이터 파싱      | **XML Parsing** |    -          | WeatherAPI 기상 데이터 수집           |
|       직렬 통신      | **pySerial**               |    - | Raspberry Pi ↔ Arduino UART 제어 |

---
### ⭐ 배지(Badges)

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-Custom-00FFFF?style=flat)](https://github.com/ultralytics/yolov5)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-C51A4A?style=flat&logo=raspberry-pi&logoColor=white)](https://www.raspberrypi.com/)
[![Arduino](https://img.shields.io/badge/Arduino-UNO-00979D?style=flat&logo=arduino&logoColor=white)](https://www.arduino.cc/)

</div>

---


## 핵심 알고리즘
## 설치 및 실행
## 프로젝트 결과
## 기술적 도전과 해결
## 향후 개선 방향
## 팀 및 기여
## 라이선스



