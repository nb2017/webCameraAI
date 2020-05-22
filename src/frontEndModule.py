


from flask import * # flaskのインポート

app = Flask(__name__)

@app.route("/")
def main():
    return """
    <h1> 撮影した画像を判定します <h1>
    <form action="/" method="POST">
    <input name="num"></input>
    </form>"""

@app.route("/<AICamera>")
def hello_name(AICamera):
    return "Hello, {}".format(AICamera)

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行
