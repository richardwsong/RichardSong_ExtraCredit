""" 
This code sses Euler's Method to approximate and plot the value of p. 
It starts by importing the proper libraries, matplotlib.pyploy (which can create
scatter plots when given a list of x and a list of y values) and numpy (which will
turn regular arrays into numpy arrays for matplotlib). We initialize a vector of 
length 40 called x and y, which will represent our points across 40 time points that
we calculate using Euler's method. Our step size, h, can be arbitrarily specified.
In our problem, we used h values of 0.18, 0.23, 0.25, and 0.3 to estimate the
function p (in our case, the y coordinate). Next, we create a for loop going from 1 
to 40. From part b, we determined that p_(n+1) = (1+10h)*p_n - (10h)*(p_n)^2. We 
will use this equation to calculate individual values of y in the for loop. Each 
value of x will be step count, i, multiplied by the step size, h. Finally, we create
numpy verisons of the x and y arrays, and display the scatter plot. 

Interestingly, for low step sizes (i.e., h = 0.18), the value of p will approach 1
as x approaches infinity. We verified this to be true from part a, since the limit of
p as x approaches infinity is 1. However, our Euler's Identity estimation will 
exhibit more and more chaos as the value of h increases. For example, for h = 0.23, 
p alternates between 1.18 and 0.69 as x increases (i.e., it oscillates between 2 
different points). For h = 0.25, p jumps between 1.23, 0.54, 1.16, and 0.7 as x 
increases (i.e., it osccilates between 4 different points). And for h = 0.3, there is
no observable pattern for the oscillation activity of p as x increases. 
"""

import matplotlib.pyplot as plt
import numpy as np

x = [0]*40
y = [0]*40

x[0] = 0
y[0] = 0.1
h = 0.30

for i in range(1, 40):
    y[i] = y[i-1]*(1+10*h) - (10*h)*y[i-1]*y[i-1]
    x[i] = h*i

x_np = np.array(x)
y_np = np.array(y)
plt.scatter(x_np, y_np)
plt.plot(x_np, y_np)


plt.title("h = " + str(h))
plt.show()