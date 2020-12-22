import numpy as np


def cost(x):
    return 3 * x ** 4 + 4


def relu(x):
    return np.array([0 if x[i] < 0 else x[i] for i in range(len(x))])


x = np.array([1, 2, -3, -4])
print(relu(x))
