import numpy as np


class MF_DCCA(np.array):
    def f(self, i):
        # комментарии надо оставлять
        mean = np.mean(self)
        x = 0
        for k in range(i):
            x += self[k] - mean
        return x
