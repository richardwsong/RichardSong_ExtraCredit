# Uses Euler's Method to approximate and plot the value of p

import matplotlib.pyplot as plt
import numpy as np

x = [0]*40
y = [0]*40

x[0] = 0
y[0] = 0.1
h = 0.30

for i in range(1, 40):
    y[i] = y[i-1]*(1+10*h) - (10*h)*y[i-1]*y[i-1]
    x[i] = .18*i

x_np = np.array(x)
y_np = np.array(y)
plt.scatter(x_np, y_np)
plt.plot(x_np, y_np)


plt.title("h = " + str(h))
plt.show()