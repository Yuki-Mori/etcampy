from .exception import CameraCannotOpenError
import cv2

def save_image(path, camera=0):
    cap = cv2.VideoCapture(camera)
    if not cap.isOpened:
        raise CameraCannotOpenError("Camera cannot open!")
    _, frame = cap.read()
    cv2.imwrite(path,frame)
    cap.release()