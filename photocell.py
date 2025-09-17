import RPi.GPIO as GPIO
import time
from gpiozero import InputDevice
from time import sleep
GPIO.setmode(GPIO.BCM
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

sensor = InputDevice(23)

while True:
  if sensor.is_active:
    print("All off")
    GPIO.output(18,GPIO.LOw)
    GPIO.output(17,GPIO.LOw)
    GPIO.output(16,GPIO.LOw)
    time.sleep(1)
  else:
    print("All on")
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    time.sleep(1)
