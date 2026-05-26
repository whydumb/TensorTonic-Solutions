import numpy as np

def relu(x):
    x = np.array(x)
    return np.maximum(0, x)

xs = [-2, -1, 0, 1, 2]
print(relu(xs))