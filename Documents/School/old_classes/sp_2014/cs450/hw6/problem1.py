from __future__ import division
import numpy as np 
import matplotlib.pyplot as pt 

def runge_kutta(f, t, y, h):
	k1 = f(t, y)
	k2 = f(t + h/2, y + h/2 * k1)
	k3 = f(t + h/2, y + h/2 * k2)
	k4 = f(t +h, y + h*k3)
	return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

def h_step(f, t, y, h):
	k1 = y + h * f(t, y)
	return y + h/2 * (f(t, y) + f(t+h, k1))

def leap_frog(f, t, y_p, y, h):
	return y_p + 2 * h * f(t, y)

def f(t, y):
	u, u_p = y
	return np.array([u_p, -u])

def true(t):
	return np.cos(t)



times = [0]
y_vals = [np.array([1,0])]
leap_vals = [np.array([1,0])]
h = .1
t_end = 2*np.pi
while times[-1] < t_end:
	y_vals.append(runge_kutta(f, times[-1], y_vals[-1], h))
	if times[-1] == 0:
		leap_vals.append(h_step(f, times[-1], leap_vals[-1],h))
	else:
		leap_vals.append(leap_frog(f, times[-1], leap_vals[-2], leap_vals[-1], h))
	
	times.append(times[-1]+h)

times1 = [0]
y_vals1 = [np.array([1,0])]
leap_vals1 = [np.array([1,0])]
h1 = .01
t_end1 = 2*np.pi
while times1[-1] < t_end1:
	y_vals1.append(runge_kutta(f, times1[-1], y_vals1[-1], h1))
	if times1[-1] == 0:
		leap_vals1.append(h_step(f, times1[-1], leap_vals1[-1],h1))
	else:
		leap_vals1.append(leap_frog(f, times1[-1], leap_vals1[-2], leap_vals1[-1], h1))
	
	times1.append(times1[-1]+h1)


# uncomment for EOC for Runge-Kutta and leap frog
# y_vals = np.array(y_vals)
# y_vals1 = np.array(y_vals1)
# print np.log(max(abs(true(times) - y_vals[:, 0]))/max(abs(true(times1) - y_vals1[:, 0])))/np.log(.1/.01)
# leap_vals = np.array(leap_vals)
# leap_vals1 = np.array(leap_vals1)
# print np.log(max(abs(true(times) - leap_vals[:, 0]))/max(abs(true(times1) - leap_vals1[:, 0])))/np.log(.1/.01)

cop_y_vals = y_vals
cop_leap_vals = leap_vals
y_vals = np.array(y_vals)
leap_vals = np.array(leap_vals)
pt.figure(1)
pt.plot(times, y_vals[:, 0], label='runge_kutta')
pt.legend()
pt.savefig('fig1_1')

pt.figure(2)
pt.plot(times, leap_vals[:, 0], label='leap frog')
# pt.plot(times, np.cos(times), label='true')
pt.legend()
pt.savefig('fig1_2')


t_end = 400*t_end
while times[-1] < t_end:
	cop_y_vals.append(runge_kutta(f, times[-1], cop_y_vals[-1], h))
	if times[-1] == 0:
		cop_leap_vals.append(h_step(f, times[-1], cop_leap_vals[-1],h))
	else:
		cop_leap_vals.append(leap_frog(f, times[-1], cop_leap_vals[-2], leap_vals[-1], h))
	times.append(times[-1]+h)

cop_y_vals = np.array(cop_y_vals)
cop_leap_vals = np.array(cop_leap_vals)
e_vals_rk = [1/2*cop_y_vals[i, 1]**2 + 1/2*cop_y_vals[i, 0]**2 for i in xrange(len(times))]
e_vals_lf = [1/2*cop_leap_vals[i, 1]**2 + 1/2*cop_leap_vals[i, 0]**2 for i in xrange(len(times))]

pt.figure(3)
pt.plot(times, e_vals_rk, label='runge_kutta energy')
pt.legend()
pt.savefig('fig1_3')


pt.figure(4)
pt.plot(times, e_vals_lf, label='leap frog energy')
# pt.plot(times, np.cos(times), label='true')
pt.legend()
pt.savefig('fig1_4')

pt.figure(5)
pt.plot(times, cop_y_vals[:, 0], label='runge_kutta')
pt.plot(times, cop_leap_vals[:, 0], label='leap frog')
pt.legend()
pt.savefig('fig1_5')
pt.show()