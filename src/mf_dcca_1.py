import numpy as np


def f(x, i):
    # комментарии надо оставлять
    mean = np.mean(x)
    a = 0
    for k in range(i):
        a += x[k] - mean
    return a





