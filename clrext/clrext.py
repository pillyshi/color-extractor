import numpy as np
import cv2
from sklearn.cluster import MeanShift


class ColorExtractor(object):

    def __init__(self, max_sample_size=1000):
        self.max_sample_size = max_sample_size

    def extract(self, path):
        _img = cv2.imread(path)
        height, width = _img.shape[:2]
        scale = np.sqrt(self.max_sample_size / (height * width))
        _img = cv2.resize(_img, (int(width * scale), int(height * scale)))
        X = _img.reshape((_img.shape[0] * _img.shape[1], _img.shape[2]))
        model = MeanShift()
        y = model.fit_predict(X)
        return np.int32(model.cluster_centers_)
