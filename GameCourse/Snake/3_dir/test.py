import numpy as np
import new_snake_nn as nn

model = nn.NN(lr=0.01)
x = np.random.random((400))
y = np.random.random((4))
print(x)

h, d3, d2, d1 = model.feed(x)
# print("h=", h)
# print("d3=", d3)
# print("d2=", d2)
# print("d1=", d1)
model.fit(h, d3, d2, d1, y, x)

h, d3, d2, d1 = model.feed(x)
print("h=", h)
print("d3=", d3)
print("d2=", d2)
print("d1=", d1)
