from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import scipy.sparse as sps
import scipy.sparse.linalg as sla
import matplotlib.pyplot as pt

mesh = np.linspace(0, 1, 400)
dx = mesh[1]-mesh[0]

def f_advection_centered(t, u):
    du = (np.roll(u, -1, axis=-1) - np.roll(u, 1, axis=-1))/(2*dx)
    return -du

def upwind(t, u):
	du = (np.roll(u, 0, axis=-1) - np.roll(u, 1, axis=-1))/(-dx)
	return du

def runge_kutta(f, t, y, h):
	k1 = f(t, y)
	k2 = f(t + h/2, y + h/2 * k1)
	k3 = f(t + h/2, y + h/2 * k2)
	k4 = f(t +h, y + h*k3)
	return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

def fw_euler(f, t, y, h):
	return y + h*f(t, y)

n = 400

D1 = sps.diags([-1,1], offsets=np.array([-1,1])+1, shape=(n-2, n))/(-2*dx)
D1 = sps.vstack([sps.coo_matrix(([1], ([0],[0])), shape=(1, n)), D1, sps.coo_matrix(([1], ([0],[n-1])), shape=(1, n)), ])

eigs = sla.eigs(D1, k=n-2)[0]
pt.figure(1)
pt.scatter(eigs.real, eigs.imag, label='Centered Difference')
pt.legend()
pt.savefig('fig5_1')


D = sps.diags([-1,1], offsets=np.array([-1,0])+1, shape=(n-2, n))/(-dx)
D = sps.vstack([sps.coo_matrix(([1], ([0],[0])), shape=(1, n)), D, sps.coo_matrix(([1], ([0],[n-1])), shape=(1, n)), ])

eigs1 = sla.eigs(D, k=n-2)[0]
pt.figure(2)
pt.scatter(eigs1.real, eigs1.imag, label='Upwind')
pt.legend( )
pt.savefig('fig5_2')

eigs2 = sla.eigs(.005*D1, k=n-2)[0]
pt.figure(3)
pt.scatter(eigs2.real, eigs2.imag, label='Centered Difference with CFL = .005')
pt.legend()
pt.savefig('fig5_3')

pt.figure(4)
eigs3 = sla.eigs(.003*D, k=n-2)[0]
pt.scatter(eigs3.real, eigs3.imag, label='Upwind with CFL = .003')
pt.legend()
pt.savefig('fig5_4')
pt.show()

pt.figure(5)
eigs4 = sla.eigs(.001*D, k=n-2)[0]
pt.scatter(eigs4.real, eigs4.imag, label='Upwind with CFL = .001')
pt.legend()
pt.savefig('fig5_5')
pt.show()


