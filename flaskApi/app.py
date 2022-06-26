import base64
from flask_cors import CORS

from flask import Flask, request

from utils import get_img

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/predict', methods=["POST"])
def predict():
    key = "imgs"
    imgs = request.json.get(key)
    res_predict = 0.0
    res_imgs = []
    for t in imgs:
        b64_prefix = t[0]
        imgb64 = t[1]
        if not imgb64:
            return "No image", 400
        try:
            img = base64.b64decode(str(imgb64))
        except Exception as e:
            return f"bad decode image, {e}", 500
        res_img, prediction = get_predict(img, b64_prefix)
        res_imgs.append(res_img)
        res_predict = max(res_predict, prediction)
    return {"imgs": res_imgs, "predict": res_predict}


def get_predict(img, b64_prefix):
    image_to_return, prediction = get_img(img)

    return str(b64_prefix) + "," + str(base64.b64encode(image_to_return))[2:-1], prediction


if __name__ == '__main__':
    app.run()
