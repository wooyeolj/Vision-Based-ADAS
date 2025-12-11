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
- ✅ **프레임 스킵**: 6프레임마다 처리하여 성능 안정화 및 과부하 방지

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
    if distance < 0.4:
        emergency_stop(pwm=0)      # 긴급 정지
    elif distance < 0.6:
        slow_down(pwm=140)         # 서행
    else:
        normal_speed(pwm=200)      # 정상 주행

# 예시 2: 신호등 감지
if class_id == 1:  # 빨간불
    if distance < 0.3:
        stop(pwm=0)                # 정지선 준수
    else:
        prepare_stop(pwm=140)      # 서행
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
WEATHER_API_URL = # API KEY 입력 필요
```

---

### 🚀 Start

```
# 1. 시스템 준비
sudo apt-get update && sudo apt-get upgrade -y

# 2. 프로젝트 클론
git clone https://github.com/wooyeolj/Vision-Based-ADAS.git
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
<img width="280" alt="Top View" src="https://github.com/user-attachments/assets/8778e7f6-ef6b-4f6c-b12a-f2ed8befb65c" />  <img width="280" alt="Front View" src="https://github.com/user-attachments/assets/0fa877a7-93de-4f68-b0ac-10db86956b67" />  <img width="280" alt="Side View" src="https://github.com/user-attachments/assets/6c098dff-3e52-4a94-ab38-d708033b7ed3" /> 

---

## 기술적 도전과 해결

프로젝트 진행 중 마주한 기술적 문제들에 대한 해결 과정을 기술함

### ⚡ Challenge 1: 실시간 처리 성능 이슈

#### 🔴 문제 

초기 목표는 **차선 탐지와 객체 탐지를 동시에 실행**하는 통합 시스템
하지만 Raspberry Pi 5의 성능 한계로 인해 다음과 같은 문제 발생

```
단일 프레임 처리 시간:
- 차선 탐지 (Canny + Hough): ~50ms
- 객체 탐지 (YOLOv5): ~200ms
- 총 처리 시간: ~250ms  (실시간 처리 불가)
```

**증상:**
- 영상 프레임 지연 및 끊김
- RC카 제어 반응 속도 저하
- 시스템 과부하로 인한 불안정

#### 🟢 해결

**1️⃣ 듀얼 모드 분리 아키텍처**

통합 시스템 대신 **독립적인 두 가지 모드**로 분리 결정

```python
# Before: 통합 실행 
def main_loop():
    frame = capture_frame()
    lane_result = detect_lane(frame)      # 50ms
    object_result = detect_object(frame)  # 200ms
    control_car(lane_result, object_result)

# After: 모드 분리
# Mode 1: Lane Detection Only
def lane_mode():
    frame = capture_frame()
    lane_result = detect_lane(frame)      # 50ms
    control_car(lane_result)
  
# Mode 2: Object Detection Only
def object_mode():
    frame = capture_frame()
    object_result = detect_object(frame)  # 200ms
    control_car(object_result)
```

**2️⃣ 프레임 스킵 기법 적용**

모든 프레임을 처리하지 않고 **6프레임마다 처리**

```python
frame_count = 0
while True:
    ret, frame = cap.read()
    frame_count += 1
    
    if frame_count % 6 == 0:  # 6프레임마다 처리
        result = process_frame(frame)
        control_car(result)
```

**3️⃣ RoI 마스킹으로 연산 영역 최소화**

전체 프레임 대신 **관심 영역만 처리**:
```python
# 전체 프레임: 640x480 = 307,200 pixels
# RoI 영역: 480x220 = 105,600 pixels
# 연산량 65% 감소
```

#### 📝 결과

- 각 모드에서 최적의 성능 발휘
- 연산량 83% 감소
- 안정적인 실시간 처리 가능 
- 두 기능을 동시에 사용 불가 (향후 개선 과제)

---

### 🚗 Challenge 2: 모터 제어 불안정

#### 🔴 문제

하드웨어에 PWM 신호를 전송해도 **RC카가 의도한 대로 주행하지 않는** 치명적인 문제가 발생

**증상:**
```
명령: 직진 (left=200, right=200)
실제: 좌측으로 급격히 회전

명령: 우회전 (left=50, right=200)
실제: 제자리 회전
```

**원인 분석:**

1. 2륜 구조의 불안정성
2. 모터 성능 차이
3. 무게 중심 불균형

#### 🟢 해결

**1️⃣ 2륜 → 4륜 RC카로 교체**

**2️⃣ 고품질 모터로 교체**

#### 📝 결과

- 무게 중심 균형 개선
- 직진 및 회전 제어 향상

---

### 🔄 Challenge 3: 방향 전환의 한계

#### 🔴 문제

일반 자동차와 달리 Arduino RC카는 구조적으로  **바퀴의 방향을 조절할 수 없음**

#### 🟢 해결 

**양쪽 바퀴 속도 차이로 회전**

```python
def turn_left():
    """드리프트 방식 우회전"""
    left_pwm = 220   # 좌측 고속
    right_pwm = 10   # 우측 서행
    send_pwm(left_pwm, right_pwm)
    time.sleep(0.3)  # 회전 시간

def turn_right():
    """드리프트 방식 좌회전"""
    left_pwm = 10    # 좌측 서행
    right_pwm = 220  # 우측 고속
    send_pwm(left_pwm, right_pwm)
    time.sleep(0.3)
```

#### 📝 결과

- 안정적인 곡선 주행 가능
- 추가 하드웨어 없이 문제해결
- 정밀한 곡선 주행 불가 (향후 개선 과제)

---

## 향후 개선 방향

프로젝트의 한계점과 개선 방안

### ⚠️ 현재 한계점

#### 1. 차선 탐지와 객체 탐지의 분리
**영향**
- 복합 상황 대응 불가
- 실제 자율주행 시나리오 구현 제한

#### 2. 프레임 처리 속도 부족
**영향**
- 고속 주행시 반응 지연
- 동적 장애물 추적 제한

#### 3. 객체 인식 정확도 및 범위
**영향**
- 정확도 부족 및 오검출 발생
- 탐지 클래스 제한 (9개)
  
---
### 🚀 개선 방향

#### 1. 차선 + 객체 탐지 실시간 통합

**목표:** 두 기능을 하나로 통합

**접근 방법:**

Option A: 멀티스레딩

Option B: 프레임 분할 처리

Option C: GPU 가속 

**예상 효과:**
- ✅ 복합 시나리오 대응 가능
- ✅ 실제 자율주행에 가까운 동작

---

#### 2. 딥러닝 기반 차선 검출

**목표:** Canny + Hough → 딥러닝 모델로 대체

**딥러닝 모델 도입:**

| 모델 | 장점 | 단점 | 특징 |
|:---:|---|---|---|
| **U-Net** | 높은 정확도 | 연산량 많음 | 실시간 연산 부적합  |
| **ENet** | 초경량, 실시간 가능 | 정확도 낮음 | 임베디드 보드를 목표로 만든 경량 모델 |
| **SCNN** | 차선 특화 모델 | 구현 난이도 높음 | 2D CNN 메세지 전달 |
| **LaneATT** | 높은 정확도, 빠름 | 구조 복잡 | Anchor 기반 차선 검출 |
| **UFLD** | 실시간 300FPS 이상 | 세밀한 표현 불가 | 키포인트 기반 차선 검출 |


**예상 효과:**
- ✅ 복잡한 환경에서 정확도 향상
- ✅ 곡선 차선 정확도 개선
- ✅ 처리 속도 개선
  
---

#### 3. Depth Estimation 모델 적용

**현재 방식의 한계:**
- 객체 실제 크기 DB 필요

**목표:** 단일 카메라 기반 객체 높이 비례 거리 추정 → MiDaS 모델로 대체

**예상 효과:**
- ✅ 모든 객체의 상대 거리 측정 가능
- ✅ 객체 크기 DB 불필요
- ⚠️ 절대 거리 변환 시 스케일 보정 필요
- ⚠️ 연산량 증가

---

#### 4. PID 제어 추가

**현재 제어 방식의 한계:**
- 급격한 PWM 변화로 인한 불안정한 주행
- 부드러운 제어 불가

**목표:** PWM 제어 → PID 제어로 개선

**예상 효과:**

- ✅ Kp,Kd,Ki 튜닝으로 주행 최적화
- ✅ 부드러운 주행 제어
- ✅ 다양한 속도에서 일관된 성능
- ⚠️ 노이즈 취약

---

### 5. 모델 경량화

**목표:** YOLOv5 → YOLOv8-nano로 업그레이드

**비교 분석:**

| 항목 | YOLOv5s (현재) | YOLOv8-nano | 개선율 |
|---|:---:|:---:|:---:|
| **파라미터 수** | 7.2M | 3.2M | ⬇️ 56% |
| **모델 크기** | 14MB | 6MB | ⬇️ 57% |
| **추론 속도 (CPU)** | ~200ms | ~80ms | ⬆️ 150% |
| **정확도 (mAP)** | 높음 | 약간 낮음 | ⬇️ 5% |

---


## 팀 및 기여

|     성명    |  역할 | 담당 업무                                         |
| :-------: | :-: | --------------------------------------------- |
|  **김신형**  |  멘토 | 프로젝트 일정 관리, 기술 자문 및 Q&A                    |
|  **임재혁**  |  팀장 | Weather API 기능 구현, Raspberry Pi 프로그래밍       |
|  **장민혁**  |  팀원 | 차선·객체 탐지 알고리즘 개발 및 Raspberry Pi 적용             |
|  **조수연**  |  팀원 | 차선·객체 탐지 알고리즘 개발, Arduino 제어, 프로젝트 시나리오 구성   |
|  **진우열**  |  팀원 | 차선·객체 탐지 알고리즘 개발, Arduino 제어, 프로젝트 시나리오 구성 |
| **공통 업무** |  -  | YOLO 데이터셋 제작 및 모델 학습, RC카 제작                  |

---


## 라이선스


MIT License

Copyright (c) 2025 wooyeolj

본 소프트웨어는 2024 한이음 ICT 멘토링 프로그램의 팀 프로젝트로 개발되었습니다.
This software was developed as a team project of the 2024 Hanium ICT mentoring program.

⚠️
본 소프트웨어는 실제 차량이나 안전 시스템에 사용되어서는 안 됩니다.
This software should not be used in actual vehicles or safety systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


