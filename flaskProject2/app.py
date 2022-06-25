import base64

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/predict', methods=["POST"])
def predict():
    key = "img"
    imgb64 = request.json.get(key)
    if not imgb64:
        return "No image", 400
    try:
        img = base64.b64decode(str(imgb64))
    except Exception as e:
        return f"bad decode image, {e}", 500
    res_img, predict = get_predict(img)
    return {"img": res_img, "predict": predict}


def get_predict(img):
    return str(base64.b64encode(img)), 0.8


if __name__ == '__main__':
    app.run()
