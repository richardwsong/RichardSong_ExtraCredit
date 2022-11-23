# Uses Runge-Kutta Method to approximate and plot the value of p

import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return 10*y*(1-y)

x = [0]*60
y = [0]*60

x[0] = 0
y[0] = 0.1
h = 0.35

for i in range(1, 60):
    k1 = h*f(x[i-1], y[i-1])
    k2 = h*f(x[i-1] + h/2, y[i-1] + k1/2)
    k3 = h*f(x[i-1] + h/2, y[i-1] + k2/2)
    k4 = h*f(x[i-1] + h, y[i-1] + k3)

    x[i] = x[i-1] + h
    y[i] = y[i-1] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

x_np = np.array(x)
y_np = np.array(y)
plt.scatter(x_np, y_np)
plt.plot(x_np, y_np)

plt.title("Runge-Kutta h = " + str(h))
plt.show()

print(y)