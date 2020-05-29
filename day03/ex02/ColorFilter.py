import numpy as np

class ColorFilter:
    def invert(self, array: np.array) -> np.array:
        return 1.0 - array


    def to_blue(self, array: np.array) -> np.array:
        if len(array[0][0]) == 4:
            return [[[0, 0, rgb[2], rgb[3]] for rgb in color_array] for color_array in array]
        else:
            return [[[0, 0, rgb[2]] for rgb in color_array] for color_array in array]


    def to_green(self, array: np.array) -> np.array:
        if len(array[0][0]) == 4:
            return [[[0, rgb[1], 0, rgb[3]] for rgb in color_array] for color_array in array]
        else:
            return [[[0, rgb[1], 0] for rgb in color_array] for color_array in array]


    def to_red(self, array: np.array) -> np.array:
        if len(array[0][0]) == 4:
            return [[[rgb[0], 0, 0, rgb[3]] for rgb in color_array] for color_array in array]
        else:
            return [[[rgb[0], 0, 0] for rgb in color_array] for color_array in array]
