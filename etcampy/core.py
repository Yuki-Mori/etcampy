import cv2

def show_video(cap):
    # カメラFPSを30FPSに設定
    cap.set(cv2.CAP_PROP_FPS, 30)

    # カメラ画像の横幅を1280に設定
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

    # カメラ画像の縦幅を720に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # 表示するWindow名を設定
    WINDOW_NAME = "camera"
    cv2.namedWindow(WINDOW_NAME)

    while cap.isOpened():
        ret, frame = cap.read()
        
        # フレームを表示する
        cv2.imshow(WINDOW_NAME, frame)
        
        key = cv2.waitKey(1)&0xff
        
        if key == ord('q'):
            return
    return