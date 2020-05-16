from modules.appBase import appBase

from cameraModule import cameraModule
from faceAnalize import faceAnalize
from cv2 import cv2

CascadeFile = "../data/haarcascade_frontalface_default.xml"

"""
    カメラ画像バッファ処理
"""
def cameraImageBufferingFunction():
    pass

"""
    Webカメラ画像解析モジュール
"""
class webCameraAnallyMainModule(appBase):
    webCamera = None
    def __init__(self):
        super().__init__()
        # Webカメラモジュール生成
        self.webcamera = cameraModule()
        # 顔認識モジュール生成
        self.faceAnalize = faceAnalize()
        # メイン処理実行
        self.runningModule()
        # 完了復帰なので抜けたら終了処理を行う
        self.destroyModule()
        print("end application")
    def runningModule(self):
        while True:
            # ウィンドウ処理
            self.frameProcess()
            # キー入力を1ms待って、k が27（ESC）だったらBreakする
            k = cv2.waitKey(1)
            if k == 27:
                break
        return super().runningModule()
    def destroyModule(self):
        self.webcamera.destroyModule()
        return super().destroyModule()
    # ウィンドウ処理
    def frameProcess(self):
        frame = self.webcamera.getImage()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        viewframe = self.faceAnalize.analizeImage(frame)
        # viewframe = frame
        cv2.putText(viewframe, 'faceAnalizeTool', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)
        # 加工済の画像を表示する
        cv2.imshow('Edited Frame', viewframe)

if __name__ == '__main__':
    webCameraAnallyMainModule()
