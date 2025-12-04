from typing import List

/**
 * Motor Control for RC Car via Serial Communication
 *
 * Receives PWM commands from Raspberry Pi via Serial (9600 baud)
 * Format: "leftPWM,rightPWM\n"
 * Example: "200,200\n" → both motors forward at speed 200
 */


// ========================================
// Pin Definitions
// ========================================
const int ENA = 9;  // Right motor PWM (MOTOR A)
const int IN1 = 8;
const int IN2 = 7;
const int IN3 = 6;
const int IN4 = 5;
const int ENB = 3;  // Left motor PWM (MOTOR B)

void setup()
{
 pinMode(ENA, OUTPUT);
 pinMode(ENB, OUTPUT);
 pinMode(IN1, OUTPUT);
 pinMode(IN2, OUTPUT);
 pinMode(IN3, OUTPUT);
 pinMode(IN4, OUTPUT);
 Serial.begin(9600);
}

void setMotors(int leftSpeed, int rightSpeed)
{
// Left motor direction
if (leftSpeed >= 0)
{
digitalWrite(IN3, HIGH);
digitalWrite(IN4, LOW);
}
else
{
digitalWrite(IN3, LOW);
digitalWrite(IN4, HIGH);
leftSpeed = -leftSpeed;
}

// Right motor direction
if (rightSpeed >= 0)
{
digitalWrite(IN1, LOW);
digitalWrite(IN2, HIGH);
}
else
{
digitalWrite(IN1, HIGH);
digitalWrite(IN2, LOW);
rightSpeed = -rightSpeed;
}
// Set motor speeds (PWM)
analogWrite(ENB, leftSpeed);
analogWrite(ENA, rightSpeed);

// ========================================
// Main Loop
// ========================================
void loop()
{
 if (Serial.available() > 0)
  {
    String input = Serial.readStringUntil('Wn');
    int commalndex= input.indexOf(',');

    if (commalndex != -1)
    {
     int leftPWM = input.substring(0, commalndex).tolnt();
     int rightPWM = input.substring(commalndex + 1).tolnt();

     setMotors(leftPWM, rightPWM);

     Serial.print("Left PWM: ");
     Serial.print(Left PWM);
     Serial.print("Right PWM: ");
     Serial.print(Right PWM);
    }
  }
}
