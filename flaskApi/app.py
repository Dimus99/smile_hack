import base64

import cv2
import numpy as np
from flask_cors import CORS
import cv.darknet.darknet as darknet
from cv.darknet.darknet_images import image_detection

from flask import Flask, request

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/predict', methods=["POST"])
def predict():
    key = "img"
    imgb64 = request.json.get(key)
    b64_prefix = request.json.get("b64_prefix")
    if not imgb64:
        return "No image", 400
    try:
        img = base64.b64decode(str(imgb64))
    except Exception as e:
        return f"bad decode image, {e}", 500
    res_img, predict = get_predict(img)
    return {"img": str(b64_prefix)+"," + str(res_img)[2:-1], "predict": predict}


def get_predict(img):
    image = np.frombuffer(img, dtype=np.uint8)
    image = cv2.imdecode(image, flags=1)
    img_res, a = image_detection(
        image,
        network,
        classes,
        colors,
        0.3
    )
    cv2.imwrite("./0.jpg", img_res)
    with open("0.jpg", 'rb') as f:
        image_to_return = f.read()

    return base64.b64encode(image_to_return), 0.8


if __name__ == '__main__':
    network, classes, colors = darknet.load_network('cv/darknet/cfg/yolov4-custom.cfg', 'cv/darknet/data/obj.data',
                                                    'cv/yolov4-custom_last.weights', 1)
    app.run()
