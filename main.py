from queue import Queue
import threading
import servo
import camera_dashboard

def main():
    command_queue = Queue()

    # Start servo thread
    servo.start_servo_thread(command_queue)

    # Start camera dashboard with queue access
    camera_thread = threading.Thread(target=camera_dashboard.start_dashboard, args=(command_queue,))
    camera_thread.start()

if __name__ == "__main__":
    main()
