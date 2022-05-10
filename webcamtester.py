# https://dev.classmethod.jp/articles/opencv-webcam-setting/
import cv2

# Webカメラ
DEVICE_ID = 0 

# 1024 Kit
WIDTH = 1280
HEIGHT = 1024
FPS = 60

# VGA 60FPS Kt
WIDTH = 800
HEIGHT = 600
FPS = 60

# 1024 Kit
WIDTH = 1280
HEIGHT = 1024
FPS = 30


def decode_fourcc(v):
        v = int(v)
        return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

def main():
    cap = cv2.VideoCapture (DEVICE_ID)

    # フォーマット・解像度・FPSの設定
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    # フォーマット・解像度・FPSの取得
    fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("fourcc:{} fps:{}　width:{}　height:{}".format(fourcc, fps, width, height))
    size = (int(width),int(height))

    frame_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter('video.mp4',fourcc,fps,(frame_width,frame_height))
    
    # video = cv2.VideoWriter('video.mp4', fourcc, fps, size)  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    while True:
        
        # カメラ画像取得
        _, frame = cap.read()
        if(frame is None):
            continue
        video.write(frame)  

        # 画像表示
        cv2.imshow('frame', frame)
        
        # キュー入力判定(1msの待機)
        # waitKeyがないと、imshow()は表示できない
        # 'q'をタイプされたらループから抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # VideoCaptureオブジェクト破棄
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()