import time, gc, os
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

def get_light_level():
    return phototransistor.value

# Testing to see if the servo can trigger the release of CO2 for the payload
while True:
    for i in range(180, 30, -1):
        my_servo.angle = i
        time.sleep(0.005)
    
    for i in range(30, 180):
        my_servo.angle = i
        time.sleep(0.005)

    time.sleep(0.5)
