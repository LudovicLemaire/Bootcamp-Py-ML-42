import numpy as np

class NumPyCreator:
    def from_list(self, lst: list, dtype=None):
        return np.asarray(lst, dtype=dtype)

    def from_tuple(self, tup: tuple, dtype=None):
        return np.asarray(tup, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        return np.asarray(itr, dtype=dtype)

    def from_shape(self, shp, dtype=None):
        return np.zeros(shp, dtype=dtype)

    def random(self, shp, dtype=None):
        return np.random.rand(shp[0], shp[1]).astype(dtype)

    def identity(self, n, dtype=None):
        return np.eye(n, dtype=dtype)