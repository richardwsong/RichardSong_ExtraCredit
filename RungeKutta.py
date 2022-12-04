"""
This script uses Runge-Kutta Method to approximate and plot the value of p. The
Runge-Kutta method is descirbed in Section 5.7 of the textbook, and rescursively
calculates the value of x and y based on intermediate claculations of the values 
k1, k2, k3, and k4. Although the Runge-Kutta Method is fairly accurate with smaller
step sizes, several errors can arise when the step size is too large. The values of 
h that are displayed with this problem demonstrate some of those errors. We used
h = 0.3, 0.325, and 0.35 for this problem. For the largest value h = 0.35, we saw
that the value of p tended to oscillate between 0.51 and 0.72. Lowering the value 
of h to 0.325 solved the oscillating problem, however p ended up converging to 
0.67 as x increased, even though it should have convered to 1. Lowering the value of h
again to 0.3 caused p to converge to 0.76, which is closer to the actual answer. 
Interestingly, lowering the value of p to 0.2 causes it to converge to the correct 
answer (p = 1) as x increases. 

The way that this script works is quite similar to the EulerMethod.py script. We 
first import the necessary libraries for plotting, namely matplotlib.pyplot and 
numpy. We then define a function f that represents the value of dp/dt for 
code-writing simplicity. We then intitialze the arrays x and y, which are the 
coordinates of our eventual scatter plot, to size 60 because we have 60 step counts. 
The variable h will represent our step size, which in this case are 0.3, 0.325, and 
0.35. To recursively calculate the values of x and y, we create a for loop that loops
from 1 to 60 that will update k1, k2, k3, and k4 based on the value of the function
f at the previous step and the step count. The values of k1, k2, k3, and k4 at the
current iteration will then be used to update the values of x and y for the current
iteration. Finally, we convert and x and y arrays to numpy arrays and plot them using
matplotlib. 
"""
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