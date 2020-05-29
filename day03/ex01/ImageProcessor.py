import numpy as np
import matplotlib.pyplot as plt
import os


class ImageProcessor:
    def load(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            img = plt.imread(path)
            print('Loading image of dimensions {} x {}'.format(img.shape[0], img.shape[1]))
            return np.array(img)
        else:
            return None

    def display(self, array: np.array):
        if array is not None:
            plt.imshow(array)
            plt.axis('off')
            plt.title("That's a beautiful image there ", fontweight ="bold")
            plt.show()