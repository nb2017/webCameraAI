from modules.appBase import appBase
import threading
from cv2 import cv2

# カメラ番号：デフォルトなので0
CAMERA_NUM = 0

"""
Webカメラ画像取得モジュール
"""
class cameraModule(appBase):
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_NUM)
        super().__init__()
    #　撮影画像取得
    def getImage(self):
        # 画像取得
        ret, frame = self.cap.read()
        return frame

    def destroyModule(self):
        self.cap.release()
        return super().destroyModule()
