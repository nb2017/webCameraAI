# main.py

from flask import Flask, render_template, Response

from cameraModule import cameraModule
from faceAnalize import faceAnalize


analizeModule = faceAnalize()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    # "/" を呼び出したときには、indexが表示される。

def gen(camera):
    while True:
        camImage = camera.getImage()
        analizedImage = analizeModule.analizeImage(camImage)
        frame = camera.converetJpegImageForByte(analizedImage)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# returnではなくジェネレーターのyieldで逐次出力。
# Generatorとして働くためにgenとの関数名にしている
# Content-Type（送り返すファイルの種類として）multipart/x-mixed-replace を利用。
# HTTP応答によりサーバーが任意のタイミングで複数の文書を返し、紙芝居的にレンダリングを切り替えさせるもの。
#（※以下に解説参照あり）

@app.route('/video_feed')
def video_feed():
    return Response(gen(cameraModule()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# 0.0.0.0はすべてのアクセスを受け付けます。    
# webブラウザーには、「localhost:5000」と入力