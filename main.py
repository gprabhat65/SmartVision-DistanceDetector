import math
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

# Initialize YOLO model
model = YOLO("yolo11n.pt")

# Define class list for people and cars
# YOLO class indices: person = 0, car = 2
TARGET_CLASSES = [0, 2]  # person and car
CLASS_NAMES = {0: 'person', 2: 'car'}

cap = cv2.VideoCapture("test5.mp4")

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

out = cv2.VideoWriter("visioneye-distance-calculation.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

center_point = (int(w / 2), int(h))
pixel_per_meter = 100

txt_color, txt_background, bbox_clr = ((0, 0, 0), (255, 255, 255), (255, 0, 255))

# Define warning circle parameters
WARNING_DISTANCE = 5  # Distance threshold in meters
CIRCLE_RADIUS = 20
CIRCLE_CENTER = (50, h - 50)  # Bottom left position
GREEN = (0, 255, 0)
RED = (0, 0, 255)

while True:
    ret, im0 = cap.read()
    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    annotator = Annotator(im0, line_width=2)

    # Initialize minimum distance for this frame
    min_distance = float('inf')

    results = model.track(im0, persist=True, conf=0.5)

    if results[0].boxes.id is not None:
        boxes = results[0].boxes
        track_ids = boxes.id.int().cpu().tolist()
        class_ids = boxes.cls.int().cpu().tolist()
        xyxys = boxes.xyxy.cpu()

        # Filter and process only people and cars
        for box, track_id, class_id in zip(xyxys, track_ids, class_ids):
            if class_id in TARGET_CLASSES:
                # Create label with class name and tracking ID
                label = f"{CLASS_NAMES[class_id]}-{track_id}"

                annotator.box_label(box, label=label, color=bbox_clr)
                annotator.visioneye(box, center_point)

                x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)  # Bounding box centroid

                distance = (math.sqrt((x1 - center_point[0]) ** 2 + (y1 - center_point[1]) ** 2)) / pixel_per_meter
                min_distance = min(min_distance, distance)

                text_size, _ = cv2.getTextSize(f"Distance: {distance:.2f} m", cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
                cv2.rectangle(im0, (x1, y1 - text_size[1] - 10), (x1 + text_size[0] + 10, y1), txt_background, -1)
                cv2.putText(im0, f"Distance: {distance:.2f} m", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.2, txt_color,
                            3)

    # Draw warning circle
    circle_color = RED if min_distance <= WARNING_DISTANCE else GREEN
    cv2.circle(im0, CIRCLE_CENTER, CIRCLE_RADIUS, circle_color, -1)  # -1 fills the circle

    out.write(im0)
    cv2.imshow("visioneye-distance-calculation", im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()