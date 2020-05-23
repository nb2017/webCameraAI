from modules.appBase import appBase
import cv2

import os

cascade_path = '/Users/user/workspace/rep/opencv/data/haarcascades/haarcascade_frontalface_alt.xml'
color = (255, 255, 255) #白

"""
   画像解析モジュール
"""
class faceAnalize(appBase):
    def __init__(self):
        super().__init__()

    def analizeImage(self, src):
        # グレー色に変換
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cascade_path)
        # 顔認識発動!!
        faces = face_cascade.detectMultiScale(src_gray)

        for x, y, w, h in faces:
            cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = src[y: y + h, x: x + w]
            face_gray = src_gray[y: y + h, x: x + w]

        return src

    def __del__(self):
        self.destroyModule()


if __name__ == '__main__':
    faceAnalize()
