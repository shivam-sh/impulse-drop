import time, gc, os
import board
import pwmio
from adafruit_motor import servo
import analogio

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

phototransistor = analogio.AnalogIn(board.A1)

def get_light_level():
    return phototransistor.value

# Test to get the payload to release based on the light level
while True:
    light_level = get_light_level()
    print("Light Level: {}\n".format(light_level))

    if light_level > 30000:
        my_servo.angle = 120
    else:
        my_servo.angle = 30

    time.sleep(0.3)