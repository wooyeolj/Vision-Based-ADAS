import cv2
import numpy as np
import serial
import time
import signal
import sys
import requests
import xml.etree.ElementTree as ET

"""
Line Detection Module for Vision-Based ADAS
- Detects lane lines using Canny Edge Detection and Hough Transform
- Adapts PWM based on real-time weather conditions (rain/snow)
- Sends control commands to Arduino via Serial communication

"""


port = '' # Change to your Arduino port
baud_rate = 9600
ser = None # serial connection

# ========================================
# Weather API Integration
# ========================================
def get_weather():
    url = "" #Change to your api url
    resp = requests.get(url)
    xml_string = resp.content

    root = ET.fromstring(xml_string)
    location = root.find('.//name').text
    time = root.find('.//localTime').text
    update = root.find('.//last_updated').text
    temperature_c = root.find('.//temp_C').text
    humidity = root.find('.//humidity').text
    mm = float(root.find('.//precip_mm').text)
    cloud = root.find('.//cloud').text

    # Determine weather condition
    if cloud == '1':
        sky = '흐림'
    elif mm != 0:
        sky = '눈/비 내림'
    else:
        sky = '맑음'

    # Display weather info in terminal
    print(f"현재 {location}은 {time}이며, 기온은 {temperature_c}℃, 습도는 {humidity}%, 강우/적설량은 {mm}mm입니다")

    # Return PWM reduction for safety in rain/snow
    return 10 if mm !=0  else 0

# ========================================
# Signal Handler for Safe Exit
# ========================================
def signal_handler(sig, frame):
    print("Exitinf gracefully... ")
    if ser is not None:
        send_pwm(ser, 0, 0)  # Stop motors
        ser.close()
    cv2.destroyAllWindows()
    sys.exit(0)

# ========================================
# Serial Communication
# ========================================
def connect_serial():
    global ser
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port}.")
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")

def send_pwm(ser, left_pwm, right_pwm):
    try:
        command = f"{left_pwm}, {right_pwm}\n"
        ser.write(command.encode())
        print(f"Sent PWM: L({left_pwm}, R{right_pwm})")
    except serial.SerialException as e:
        print(f"PWM send error: {e}")

# ========================================
# Robot Control Logic
# ========================================
def control_robot(distance, side, pwm_offset):
    if side == 'right':
        print(f"**Right** side distance: {distance}")
        if distance < 80:
            send_pwm(ser, 10, 220)
            print(f"Moving Forward sharply to the right...")
        else:
            send_pwm(ser, 70 - pwm_offset, 70 - pwm_offset)
            print(f"Moving Forward gently...")

    elif side == 'left':
        print(f"**Left** side distance: {distance}")
        if distance < 80:
            send_pwm(ser, 220, 10)
            print(f"Moving Forward sharply to the left...")
        else:
            send_pwm(ser, 70 - pwm_offset, 70 - pwm_offset)
            print(f"Moving Forward gently...")

# ========================================
# Main Control Loop
# ========================================
def robot_control_loop(cap, roi_points, pwm_offset):
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        if frame_count % 6 == 0:  # Process every 6th frame for performance
            frame_with_box, distance, side = detect_lanes(frame, roi_points)

            if side is not None:
                print(f"Detected line on the {side} before moving.")
                control_robot(distance, side,pwm_offset)

            cv2.imshow("Original Frame", frame_with_box)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# ========================================
# Lane Detection Algorithm
# ========================================
def create_roi_mask(image, roi_points):
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [roi_points], 255)
    return mask

# 차선 감지
def detect_lanes(image, roi_points):
    height, width = image.shape[:2]
    roi_mask = create_roi_mask(image, roi_points)

    cv2.polylines(image, [roi_points], isClosed=True, color=(0, 255, 0), thickness=2)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 25, 255])
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    combined_mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(combined_mask, roi_mask)

    blurred = cv2.GaussianBlur(masked, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=150)
    detected_line = None

    if lines is not None:
        slopes = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x2 - x1 != 0:
                continue
            slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)

        if slopes:
            detected_line = lines[0][0]

    result = image.copy()
    distance = 0

    center_x = (roi_points[0][0] + roi_points[1][0]) // 2
    center_y = (roi_points[0][1] + roi_points[2][1]) // 2
    center_point = (center_x, center_y)

    cv2.circle(result, center_point,5, (255, 255, 0), -1)

    if detected_line is not None:
        x1, y1, x2, y2 = detected_line
        avg_x = (x1 + x2) // 2

        error = avg_x - center_x
        distance = abs(error)

        return result, distance, 'right' if avg_x > center_x else 'left'

    return result, distance, None

def main():
    global ser
    signal.signal(signal.SIGINT, signal_handler)
    connect_serial()

    pwm_offset = get_weather()

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Original Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original Frame", 640,480)

    roi_points = np.array([[80, 440], [560, 440], [560, 220], [80, 220]])

    try:
        robot_control_loop(cap, roi_points, pwm_offset)
    finally:
        cap.release()
        if ser is not None:
            ser.close()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()