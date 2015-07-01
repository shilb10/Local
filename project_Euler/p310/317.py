from __future__ import division
import matplotlib.pyplot as pt 
import numpy as np 

a = -9.81
b = 20 
c = 100

def y_dist(theta, t):
    return c + b*np.sin(theta)*t + a*t**2/2

def x_dist(theta, t):
    return b*np.cos(theta)*t

def theta_t(x0, theta):
    return x0/(b*np.cos(theta))

def theta_max(x0):
    return np.arctan(-b**2/(a*x0))

def optimal(x0):
    return c + (-b**2)/a + .5*a*(b**4 + a**2*x0**2)/(b**2*a**2)

x0_list = np.arange(0, 100, .01)
y = [y_dist(theta_max(x0), theta_t(x0, theta_max(x0))) for x0 in x0_list]
o = [optimal(x0) for x0 in x0_list]
pt.plot(x0_list, y, linewidth=4)
pt.plot(x0_list, o, 'r', linewidth=4)

# pt.show()

t_list = np.arange(0,6,.01)
for theta in np.arange(0, np.pi/2, .1):
    x_list = [x_dist(theta, t) for t in t_list]
    y_list = [y_dist(theta, t) for t in t_list]
    if theta == 0:
        pt.plot(x_list, y_list, '--')
    else:
        pt.plot(x_list, y_list)

pt.plot(np.arange(0,100,.1), [0]*len(np.arange(0,100,.1)), linewidth=2)
pt.show()
print np.sin(np.pi/2)