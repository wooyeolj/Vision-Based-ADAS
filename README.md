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
5. [설치 및 실행](#설치-및-실행)
6. [프로젝트 결과](#프로젝트-결과)
7. [기술적 도전과 해결](#기술적-도전과-해결)
8. [향후 개선 방향](#향후-개선-방향)
9. [팀 및 기여](#팀-및-기여)
10. [라이선스](#라이선스)


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

Canny Edge Detection + Hough Transform 기반 컴퓨터 비전 기법으로 차선을 인식

#### 🎯 핵심 기능

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

**중심점 거리 기반 PWM 제어**
```python
# 차선 중심과 RC카 중심 간 거리 계산
offset = detected_line_x - center_x

# 거리 기반 회전 제어
if offset > 80:  # 차선이 오른쪽에 있음
    turn_right(left_pwm=10, right_pwm=220) 
elif offset < -80:  # 차선이 왼쪽에 있음
    turn_left(left_pwm=220, right_pwm=10) 
else:
    move_forward(pwm=70)  
```

#### 📊 특징

- ✅ **HSV 색공간 튜닝**: 조명 변화에 강건한 차선 검출
- ✅ **RoI 마스킹**: 불필요한 영역 제거로 연산량 최적화
- ✅ **프레임 스킵**: 6프레임마다 처리하여 안정성 보장

---

### 2. 객체 탐지 및 충돌 회피 

YOLOv5 기반 다중 객체 실시간 탐지 및 거리 측정

#### 📝 딥러닝 모델

**YOLOv5 커스텀 학습 모델** - 한국 도로 환경에 최적화

- **프레임워크**: Ultralytics YOLOv5
- **학습 데이터**: 자체 제작 데이터셋 (직접 촬영 + 데이터셋 라벨링)
- **클래스 수**: 9개
- **Confidence Threshold**: 0.3

#### 🎯 탐지 클래스

| 번호 | 클래스 | 용도 | 안전거리 |
|:---:|:---:|---|:---:|
| 0 | 🟢 초록불 신호등 | 주행 허가 | - |
| 1 | 🔴 빨간불 신호등 | 정지 | < 0.3m |
| 2 | 🟡 노란불 신호등 | 감속  | < 0.3m |
| 3 | 🚶 보행자 | 긴급 정지 | < 0.4m |
| 4 | 🚗 차량 | 안전거리 유지 | < 0.6m |
| 5 | 🚸 30km/h 제한 | 감속 | - |
| 6 | 🚸 50km/h 제한 | 감속 | - |
| 7 | 🚶 횡단보도 표지판 | 주의 주행 | < 0.3m |
| 8 | 👶 어린이보호구역 | 서행 | < 0.3m |

#### 📏 거리 측정 알고리즘

Pinhole Camera Mode 적용

```
class_heights = {
    0: 0.01,  # green
    1: 0.01,  # red
    2: 0.01,  # yellow
    3: 0.02,  # person
    4: 0.04,  # car
    ...
}
camera_matrix = 
[[616.0, 0.0, 320.0],
 [0.0, 616.0, 240.0],
 [0.0,   0.0,   1.0]]

distance = (class_heights[int(cls)] * camera_matrix[1, 1]) / h

거리 = (class_heights에 정의된 높이 * 카메라의 초점거리) / 측정된 객체의 높이
```

#### 📊 특징
- ✅ 실시간 계산 (딥러닝 depth 모델 대비 빠름)
- ✅ 추가 학습 불필요
- ⚠️ 객체 크기 데이터베이스 필요

#### ❗ 충돌 회피 로직

**객체별 맞춤형 제어 전략**

```python
# 예시 1: 보행자 감지
if class_id == 3:  # 사람
    if distance < 0.4m:
        emergency_stop(pwm=0)      # 긴급 정지
    elif distance < 0.6m:
        slow_down(pwm=140)         # 서행
    else:
        normal_speed(pwm=200)      # 정상 주행

# 예시 2: 신호등 감지
if class_id == 1:  # 빨간불
    if distance < 0.3m:
        stop(pwm=0)                # 정지선 준수
    else:
        prepare_stop(pwm=140)      # 감속 준비
```

#### 📊 특징
- ✅ **안정화 로직**: 3프레임 연속 감지 시 제어 명령 실행 (오검출 방지)
- ✅ **다중 객체 동시 처리**: 한 프레임에서 여러 객체 실시간 탐지
- ✅ **우선순위 처리**: 가장 가까운 객체 우선 대응

---

### 3. 🌦️ 날씨 적응형 주행 (Weather-Adaptive Control)

날씨 정보 수집 및 PWM 자동 보정

#### 📌 API 연동

**WeatherAPI.com - XML 기반 실시간 기상 데이터**

```python
# API 요청
url = "http://api.weatherapi.com/v1/--"
response = requests.get(url)
xml_data = ET.fromstring(response.content)

# 데이터 추출
location = xml_data.find('.//name').text        # 위치
temperature = xml_data.find('.//temp_C').text   # 기온 (°C)
humidity = xml_data.find('.//humidity').text    # 습도 (%)
mm = float(xml_data.find('.//precip_mm').text)  # 강수량 (mm)
```

#### 📊 날씨별 제어 전략

| 날씨 조건 | 강수량 (mm) | PWM 보정 |
|:---:|:---:|:---:|
| ☀️ 맑음 | 0 | -0 |
| 🌧️ 비 | > 0.1 | -10 |
| ❄️ 적설 | > 0 | -10 | 

#### 🎯 기술적 의의

1. **외부 API 통합**: REST API 활용한 실시간 데이터 수집
2. **크롤링 기술**: XML 파싱 및 데이터 추출
3. **시스템 통합**: 웹 데이터 → 임베디드 하드웨어 제어
4. **실용성 고려**: 안전을 위한 환경 변수 반영


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

## 설치 및 실행

### 📋 사전 요구사항

#### 하드웨어
- **Raspberry Pi 5** (8GB RAM)
- **Arduino UNO** (R3)
- **Logitech C270** 웹캠 (또는 호환 USB 카메라)
- **L298N** 모터 드라이버
- **DC 모터** 
- **RC Car Kit** (아두이노 4WD 주행로봇 프레임 세트 [SZH-EK098] 또는 호환 rc카)
- **Raspberry Pi 전원** 
- **RC Car 전원** 

#### 소프트웨어
- **Raspberry Pi OS** 
- **Python** 3.9 이상
- **Arduino IDE** 
---

### 🛠️ 설정 파일 수정
#### 포트 변경
```
# Line Detection 
SERIAL_PORT =
# Object Detection 
SERIAL_PORT =

```
#### 날씨 API 키 설정
```
# Object Detection 
WEATHER_API_URL =
```

---

### 🚀 Start

```
# 1. 시스템 준비
sudo apt-get update && sudo apt-get upgrade -y

# 2. 프로젝트 클론
git clone https://github.com/YOUR_USERNAME/Vision-Based-ADAS.git
cd Vision-Based-ADAS

# 3. 패키지 설치
pip3 install -r requirements.txt

# 4. 모델 다운로드
# 커스텀 모델 학습 혹은 yolov5 models 다운 → models/ 폴더에 배치

# 5. Arduino 업로드
# Arduino IDE에서 arduino/motor_control.ino 업로드

# 6. 실행
python3 lane_detection/main.py
# 또는
python3 object_detection/main.py
```

## 프로젝트 결과

### 🎥 실행 영상 

#### 🛣️ 차선 탐지 모드 
https://www.youtube.com/watch?v=Ap_QmALgXLc

**주요 시연 내용:**
- Canny Edge Detection + Hough Transform을 통한 실시간 차선 인식
- 중심점 거리 기반 자동 방향 제어
- 날씨 정보 기반 PWM 자동 보정


#### 🚦 객체 탐지 모드 
https://www.youtube.com/watch?v=2-qXVjHOrG8

**주요 시연 내용:**
- YOLOv5 기반 9개 클래스 실시간 탐지
- 신호등, 표지판, 보행자, 차량 인식
- 거리 측정 및 자동 속도 제어 (정지, 감속, 주행)


### 결과물 상세 이미지
| <img width="280" alt="Top View" src="https://github.com/user-attachments/assets/8778e7f6-ef6b-4f6c-b12a-f2ed8befb65c" /> | <img width="280" alt="Front View" src="https://github.com/user-attachments/assets/0fa877a7-93de-4f68-b0ac-10db86956b67" /> | <img width="280" alt="Side View" src="https://github.com/user-attachments/assets/6c098dff-3e52-4a94-ab38-d708033b7ed3" /> |



## 기술적 도전과 해결
## 향후 개선 방향
## 팀 및 기여
## 라이선스



