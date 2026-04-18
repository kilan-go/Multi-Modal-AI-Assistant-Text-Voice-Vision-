from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_objects():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if not ret:
        return ["camera error"]

    results = model(frame)

    objects = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            objects.append(model.names[cls])

    cap.release()
    return list(set(objects))