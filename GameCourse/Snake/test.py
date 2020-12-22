import mynn_test as nn
import numpy as np


# np.random.seed(1)
x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])

nn = nn.NeuralNet([[2, "input"],
                   [4, "sigmoid"],
                   [1, "sigmoid"]], lr=0.1)
"""
print("Network has", nn.l_count, "layers.")
print(nn.feed(x[3]))
print(nn.outputs)
print(nn.fit(y[3]))
"""
for _ in range(10000):
    i = np.random.randint(0, 3)
    nn.feed(x[i])
    nn.fit(y[i])


print(x[0], "-->", nn.feed(x[0]))
print(x[1], "-->", nn.feed(x[1]))
print(x[2], "-->", nn.feed(x[2]))
print(x[3], "-->", nn.feed(x[3]))
