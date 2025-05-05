import time
import RPi.GPIO as GPIO

SERVO_PIN = 18

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo_pwm = GPIO.PWM(SERVO_PIN, 50)
servo_pwm.start(0)

def set_angle(angle):
    # Maps -90 to +90 degrees to PWM duty cycle
    duty = 2.5 + (angle + 90) * 10 / 180
    servo_pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo_pwm.ChangeDutyCycle(0)

def servo_control(queue):
    try:
        while True:
            if not queue.empty():
                bean_type = queue.get()

                if bean_type == "Criollo":
                    set_angle(45)
                elif bean_type == "Forastero":
                    set_angle(90)
                elif bean_type == "Trinitario":
                    set_angle(-45)
                elif bean_type == "Unknown":
                    set_angle(-90)

                time.sleep(5)
                set_angle(0)
    except KeyboardInterrupt:
        pass
    finally:
        servo_pwm.stop()
        GPIO.cleanup()
