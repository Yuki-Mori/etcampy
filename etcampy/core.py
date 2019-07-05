import cv2
import copy

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

    next_path_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        sv_frame = copy.deepcopy(frame)
        path = 'img_{:05}.jpg'.format(next_path_id)
        cv2.putText(frame, 'quit: q key', (10,80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), thickness=3)
        cv2.putText(frame, f'capture: s key as {path}', (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), thickness=3)
        
        # フレームを表示する
        cv2.imshow(WINDOW_NAME, frame)
        
        key = cv2.waitKey(1)&0xff
        
        if key == ord('q'):
            return
        elif key == ord('s'):
            cv2.imwrite(path,sv_frame)
            next_path_id += 1
    return