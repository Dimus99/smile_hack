import numpy as np

import cv.darknet.darknet as darknet
from cv.darknet.darknet_images import image_detection
import cv2

network, classes, colors = darknet.load_network('flaskApi/cv/darknet/cfg/yolov4-custom.cfg',
                                                'flaskApi/cv/darknet/data/obj.data',
                                                'flaskApi/cv/yolov4-custom_last.weights', 1)


def predict(image, thresh=0.3, clr=None):
    if clr:
        clr_return = clr
    else:
        clr_return = colors
    img_res, a = image_detection(
        image,
        network,
        classes,
        clr_return,
        thresh
    )
    apred = [float(e[1]) for e in a if e[0] == "caries"]
    apred.append(0)
    pred = max(apred)

    return img_res, pred


def get_img(image, thresh=0.5):
    image = np.frombuffer(image, dtype=np.uint8)
    image = cv2.imdecode(image, flags=1)
    img_res, pred = predict(image, thresh)
    cv2.imwrite("./0.jpg", img_res)
    with open("0.jpg", 'rb') as f:
        image_to_return = f.read()
    return image_to_return, pred


def predicts(imgs, thresh=0.3):
    """
    return predict for each img (0 or 1) list
    :param imgs: binary image
    :return: list
    """
    res = []
    for img in imgs:
        _, pred = get_img(img, thresh)
        if pred > 0:
            res.append(1)
        else:
            res.append(0)
    return res
