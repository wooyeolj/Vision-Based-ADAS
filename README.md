# 비전 기반 지능형 주행 보조 시스템 

### Vision-Based-ADAS

> 센서 없이 **OpenCV**와 **YOLOv5** 로 구현한 지능형 주행 보조 시스템
> </div>
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

<br><br>
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

## 🎯 프로젝트 소개

### 📚 2024 한이음 ICT 멘토링 프로그램

본 프로젝트는 **2024년 한이음 ICT 멘토링 프로그램**의 일환으로 진행되었습니다.

- **프로그램**: 한국정보산업연합회 주관 산학 협력 프로젝트
- **프로젝트 기간**: 2024년 3월 ~ 11월 (9개월)
- **멘토**: 김신형
- **팀 구성**: 4인 (전자공학과 졸업생)

---

### 🚨 배경 및 필요성

#### 교통사고의 심각성
ADAS 기술은 운전자의 안전과 편의성 측면에서 중요한 요소로 부상하고 있다. 통계상 교통사고로 인해 약 25초에 1명씩 사람이 사망하고 있는데, 첨단 운전자 보조 시스템(ADAS, Advanced Driver Assistance Systems)을 통해 운전자를 보조하여 안전뿐만 아니라 경제적인 이익을 가져와 줄 것으로 예상된다.

#### ADAS 기술의 중요성

ADAS는 센서와 카메라를 통해 운전 중 발생할 수 있는 위험을 사전에 감지하고 운전자가 대처할 수 있도록 돕는 안전장치입니다. 이는 단순히 사고를 예방하는 것을 넘어:

- ✅ 운전자의 집중력 향상
- ✅ 자율주행 기술 발전의 기반
- ✅ 사회 전반적인 경제적 이익 창출

#### 기존 ADAS의 한계

기존 ADAS 시스템은 다음과 같은 문제점을 가지고 있습니다:

| 한계점 | 설명 |
|:---:|---|
| **💰 높은 비용** | 라이다, 초음파 센서 등 고가의 센서 다수 사용 |
| **🔧 복잡한 구조** | 여러 센서의 융합 및 캘리브레이션 필요 |
| **⚙️ 유지보수 어려움** | 센서 고장 시 높은 수리 비용 |

---

### 🎯 프로젝트 목표

본 프로젝트는 기존 ADAS의 한계를 극복하고자 다음과 같은 목표를 설정했습니다:

#### 1️⃣ 비전 기반 저비용 ADAS 구현

**라이다, 초음파 센서 없이 오직 카메라만**으로 핵심 ADAS 기능을 구현하여 경제성을 확보합니다.

#### 2️⃣ 차선 인식 + 객체 탐지 통합 시스템

- **차선 탐지**: Canny Edge Detection + Hough Transform
- **객체 인식**: YOLOv5 커스텀 학습 (8개 클래스)
- **통합 제어**: 실시간 상황 판단 및 자동 주행 제어

#### 3️⃣ 날씨 정보를 고려한 지능형 주행

통계적으로 우천, 안개, 눈 등의 기상 상태에서 교통사고 사망률이 높게 나타나는 점을 고려하여, 실시간 날씨 정보를 수집하고 이를 주행 제어에 반영합니다.

---

### 💡 프로젝트 차별점

#### 🔹 센서리스 접근 방식
```
기존 ADAS: 라이다 + 초음파 센서 + 레이더 + 카메라 (수백만원)
           ↓
본 프로젝트: 카메라 단일 센서 (~10만원)
```

**장점:**
- ✅ **90% 이상 비용 절감**
- ✅ 간단한 하드웨어 구성
- ✅ 유지보수 용이

#### 🔹 비전 기반 복합 기능 구현

하나의 카메라로 다음 기능을 모두 수행:

| 기능 | 기술 | 결과 |
|:---:|---|---|
| 🛣️ **차선 인식** | Canny + Hough | 차선 이탈 방지 |
| 🚦 **객체 탐지** | YOLOv5 (8 classes) | 충돌 회피 |
| 📏 **거리 측정** | 기하학적 삼각측량 | 안전거리 유지 |
| 🌦️ **날씨 대응** | API 크롤링 | 상황별 제어 |

#### 🔹 실시간 외부 데이터 통합

단순히 영상 처리에 그치지 않고, **OpenWeather API**를 통해 실시간 날씨 정보를 수집하여 주행 제어에 반영합니다.

**예시:**
```
맑음 → PWM 200 (정상 속도)
강우 → PWM 190 (감속, -10)
```

---

### 🚀 프로젝트의 의의

본 프로젝트는 다음과 같은 의의를 갖습니다:

1. **경제적 ADAS 솔루션 제시**: 고가의 센서 없이도 핵심 기능 구현 가능성 입증
2. **비전 기술의 활용 가능성 확대**: Computer Vision + Deep Learning의 실용적 응용
3. **실시간 데이터 통합 사례**: 외부 API와 임베디드 시스템의 융합
4. **교육적 가치**: AI/ML 분야 학습자를 위한 실전 프로젝트 사례

---

### 🎓 학습 목표

프로젝트를 통해 다음 기술을 습득하고 활용했습니다:

- **Computer Vision**: OpenCV, 영상 전처리, Edge Detection, Line Detection
- **Deep Learning**: YOLOv5 모델 학습, 커스텀 데이터셋 제작
- **Embedded Systems**: Raspberry Pi, Arduino, UART 통신
- **System Integration**: 하드웨어-소프트웨어 통합, 실시간 제어
- **Web Crawling**: REST API 활용, 외부 데이터 수집

---



