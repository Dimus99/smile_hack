import cv.darknet.darknet as darknet


network, classes, colors = darknet.load_network('cv/darknet/cfg/yolov4-custom.cfg', 'cv/darknet/data/obj.data',
                                                    'cv/yolov4-custom_last.weights', 1)

