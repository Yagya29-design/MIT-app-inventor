from applink import AppInventorLink
from machine import Pin, PWM
import time

# Setup Servo
servo_pin = Pin(18)   
pwm = PWM(servo_pin, freq=50)

# Function to convert angle → duty
def set_angle(angle):
    duty = int((angle / 180) * 75 + 40)  
    pwm.duty(duty)

# Function called when app sends data
def controlServo(params):
    print("Data Received:", params)

    angle = 90  # default

    if "angle" in params:
        angle = int(params.get("angle"))

    set_angle(angle)

# App link setup
servoApp = AppInventorLink()

servoApp.start_ap("siraki", "12345678")
servoApp.on_request(controlServo)

while True:
    servoApp.process()
    time.sleep_ms(1)