import cv2
import numpy as np
import torch
import serial
import time
import platform
import pathlib
import warnings


"""
Object Detection Module for Vision-Based ADAS
- Detects 8 classes using custom-trained YOLOv5 model
- Estimates distance using geometric triangulation (camera model)
- Implements collision avoidance logic based on object type and distance
- Stabilizes detection with consecutive frame validation
"""
# ========================================
# Configuration
# ========================================

warnings.filterwarnings("ignore", category=FutureWarning)
port = "" # Change to your Arduino port
baud_rate = 9600

# CAMERA Parameters
camera_matrix = np.array([[616.0, 0.0, 320.0], [0.0, 616.0, 240.0], [0.0, 0.0, 1.0]]) #adjust if needed

# OS-Specific Path Handling
if platform.system() == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath
else:
    pathlib.WindowsPath = pathlib.PosixPath

# ========================================
# Load YOLOv5 Model
# ========================================
model_path = "" # Update this path
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

confidence_threshold = 0.3

# ========================================
# Object Real-World Heights (meters)
# ========================================
class_heights = {
    0: 0.01,  # green
    1: 0.01,  # red
    2: 0.01,  # yellow
    3: 0.02,  # person
    4: 0.04,  # car
    5: 0.02,  # 30
    6: 0.02,  # 50
    7: 0.03,  # crosswalk
    8: 0.03,  # childrenzone
}

# ========================================
# Serial Communication
# ========================================
def connect_serial():
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port}")
        return ser
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
        return None

# ========================================
# Detection Stabilization
# ========================================
last_detected = {"class": None, "count": 0}
frame_threshold = 3  # Minimum number of consecutive frames for a valid detection

# Send PWM Command
def send_pwm(ser, left_pwm, right_pwm, class_name):
    try:
        command = f"{left_pwm},{right_pwm}\n"
        ser.write(command.encode())
        print(f"{class_name} detected , trip by ({left_pwm}, {right_pwm})")
    except serial.SerialException as e:
        print(f"PWM send error: {e}")

# ========================================
# Frame Processing
# ========================================
def process_frame(frame, ser):
    global last_detected
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb)

    closest_distance = float('inf')
    closest_class = None

    # Assign unique colors for each class
    colors = {
        0: (0, 255, 0),     # green
        1: (0, 0, 255),     # red
        2: (0, 255, 255),   # yellow
        3: (255, 0, 0),     # person
        4: (255, 255, 0),   # car
        5: (128, 128, 128), # 30
        6: (0, 128, 255),   # 50
        7: (255, 0, 255),   # crosswalk
        8: (255, 128, 0),   # childrenzone
    }

    for det in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = det
        if conf > confidence_threshold:
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            h =y2- y1
            distance = (class_heights[int(cls)] * camera_matrix[1, 1]) / h

            # Draw bounding box and display class/detection info
            label = model.names[int(cls)]
            cv2.rectangle(frame, (x1, y1), (x2, y2), colors[int(cls)], 2)
            cv2.putText(frame, f"{label} {distance:.2f}m ",(x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[int(cls)], 2)

            # Track the closest object
            if distance < closest_distance:
                closest_distance = distance
                closest_class = int(cls)

    # Check if the closest class is detected consecutively
    if closest_class == last_detected["class"]:
        last_detected["count"] += 1
    else:
        last_detected["class"] = closest_class
        last_detected["count"] = 1

    # Execute PWM command only if the class is stable for 'frame_threshold' frames
    if last_detected["count"] == frame_threshold:
        execute_pwm_command(ser, closest_class, closest_distance)

    return frame


# ========================================
# Collision Avoidance Logic
# ========================================
def execute_pwm_command(ser, cls, distance):
    if cls == 0:  # green
        send_pwm(ser, 200, 200, "green")

    elif cls == 1 and distance < 0.3:  # red
        send_pwm(ser, 0, 0, "red")
    elif cls == 1:
        send_pwm(ser, 140, 140, "red")

    elif cls == 2 and distance < 0.3:  # yellow (close)
        send_pwm(ser, 140, 140, "yellow")
    elif cls == 2:  # yellow (far)
        send_pwm(ser, 200, 200, "yellow")

    elif cls == 3 and distance < 0.4:  # person (very close)
        send_pwm(ser, 0, 0, "person")
    elif cls == 3 and distance < 0.6:  # person (moderately close)
        send_pwm(ser, 140, 140, "person")
    elif cls == 3:  # person (far)
        send_pwm(ser, 200, 200, "person")

    elif cls == 4 and distance < 0.6:
        send_pwm(ser, 0, 0, "car")
    elif cls == 4 and distance < 0.8:
        send_pwm(ser, 140, 140, "car")
    elif cls == 4:
        send_pwm(ser, 200, 200, "car")

    elif cls == 5:  # 30
        send_pwm(ser, 140, 140, "30")

    elif cls == 6:  # 50
        send_pwm(ser, 200, 200, "50")

    elif cls == 7 and distance < 0.3:  # crosswalk
        send_pwm(ser, 140, 140, "crosswalk")
    elif cls == 7:
        send_pwm(ser, 200, 200, "crosswalk")

    elif cls == 8 and distance < 0.3:  # childrenzone
        send_pwm(ser, 140, 140, "childrenzone")
    elif cls == 8:
        send_pwm(ser, 200, 200, "childrenzone")


# Main function
def main():
    cap = cv2.VideoCapture(1)
    ser = connect_serial()
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            frame = cv2.resize(frame, (320, 240))
            processed_frame = process_frame(frame.copy(), ser)
            cv2.imshow("Frame", processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Program interrupted. Stopping the robot.")

    finally:
        if ser:
            ser.write(b"0, 0, stop")
            ser.close()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()