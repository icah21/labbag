import threading
from queue import Queue
import camera_dashboard
import servo

if __name__ == "__main__":
    # Shared queue for communication
    detection_queue = Queue()

    # Start the servo control thread
    servo_thread = threading.Thread(target=servo.servo_control, args=(detection_queue,), daemon=True)
    servo_thread.start()

    # Start the dashboard (must run in main thread due to Tkinter)
    camera_dashboard.start_dashboard(detection_queue)
