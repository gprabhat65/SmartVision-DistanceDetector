import threading
import time
import winsound
import cv2

# parameters
# Define warning circle parameters
cap = cv2.VideoCapture("test5.mp4")

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

WARNING_DISTANCE = 5  # Distance threshold in meters
CIRCLE_RADIUS = 20
CIRCLE_CENTER = (50, h - 50)  # Bottom left position
GREEN = (0, 255, 0)
RED = (0, 0, 255)


# functions
def beep_sound():
    global is_beeping
    while is_beeping:
        winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms
        time.sleep(0.1)


def start_beeping():
    global is_beeping, beep_thread
    if not is_beeping:
        is_beeping = True
        beep_thread = threading.Thread(target=beep_sound)
        beep_thread.daemon = True  # Thread will stop when main program stops
        beep_thread.start()


def stop_beeping():
    global is_beeping
    is_beeping = False
    if beep_thread is not None:
        beep_thread.join(timeout=1)  # Wait for beep thread to finish
