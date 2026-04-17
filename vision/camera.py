import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite("scene.jpg", frame)
    
    cap.release()
    return "scene.jpg"