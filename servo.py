import RPi.GPIO as GPIO
import time
import threading
from queue import Queue

SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz for SG90
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle + 90) * 10 / 180  # Map -90 to 90 deg to duty 2–12
    pwm.ChangeDutyCycle(duty)

def reset_servo():
    set_angle(0)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

def servo_worker(queue: Queue):
    while True:
        bean_type = queue.get()
        if bean_type == "Criollo":
            set_angle(45)
        elif bean_type == "Forastero":
            set_angle(90)
        elif bean_type == "Trinitario":
            set_angle(-45)
        elif bean_type == "Unknown":
            set_angle(-90)
        else:
            queue.task_done()
            continue

        time.sleep(5)
        reset_servo()
        queue.task_done()

def start_servo_thread(queue: Queue):
    thread = threading.Thread(target=servo_worker, args=(queue,), daemon=True)
    thread.start()
