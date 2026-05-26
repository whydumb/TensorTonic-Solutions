import numpy as np

def sigmoid(x):
    x = np.array(x)
    return 1 / (1 + np.exp(-x))

xs = [-2, -1, 0, 1, 2]
print(sigmoid(xs))