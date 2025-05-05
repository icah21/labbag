# main.py
import threading
from queue import Queue
import servo
import camera_dashboard

def main():
    # Create a shared queue for communication
    q = Queue()

    # Start the servo controller in its own thread
    threading.Thread(target=servo.servo_control, args=(q,), daemon=True).start()

    # Start the camera dashboard (must be on main thread!)
    camera_dashboard.start_dashboard(q)

if __name__ == "__main__":
    main()
