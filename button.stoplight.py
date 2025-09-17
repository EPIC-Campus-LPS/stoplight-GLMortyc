import RPi.GPIO as GPIO
import time
from gpiozero import Button
from signla import pause
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

def touched():
  print()

def not_touched():
  print("Green on")
  GPIO.output(18,GPIO.HIGH)
  time.sleep(5)
  print("Green off")
  GPIO.output(18,GPIO.LOW)
  print("Yellow on")
  GPIO.output(17,GPIO.HIGH)
  time.sleep(1)
  print("Yellow off")
  GPIO.output(17,GPIO.LOW)
  print("Red on")
  GPIO.output(16,GPIO.HIGH)
  time.sleep(4)
  print("Red off")
  GPIO.output(16,GPIO.LOW)

touch_sensor = Button(23, pull_up=None, active_state=True)
touch_sensor.when_pressed = touched
touch_sensor.when_released = not_touched
