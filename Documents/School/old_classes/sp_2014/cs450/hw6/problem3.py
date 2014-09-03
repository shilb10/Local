from __future__ import division
import numpy as np 
import numpy.linalg as la
import scipy.sparse as sps
import scipy.sparse.linalg as sla
import matplotlib.pyplot as pt


a = 0
b = 1

def bvp_solve(p, q, f, x, g, h):
	n = len(x)
	step = x[1]-x[0]
	
	E = sps.diags([1,-2,1], offsets=np.array([-1,0,1])+1, shape=(n-2, n))/step**2
	D = sps.diags([-1,1], offsets=np.array([-1,1])+1, shape=(n-2, n))/(2*step)
	D = sps.vstack([sps.coo_matrix(([1], ([0],[0])), shape=(1, n)), D, sps.coo_matrix(([1], ([0],[n-1])), shape=(1, n)), ])

	P_mat = sps.diags([p(x[1:])], offsets=[1], shape=(n-2,n))
	Q_mat = sps.diags([q(x[1:])], offsets=[1], shape=(n-2,n))
	A_int = E + P_mat.dot(D) + Q_mat
	A = sps.vstack([sps.coo_matrix(([1], ([0],[0])), shape=(1, n)), A_int, sps.coo_matrix(([1], ([0],[n-1])), shape=(1, n)), ])
	A = sps.csr_matrix(A)
	rhs = np.array(f(x))
	rhs[0] = g
	rhs[-1] = h
	return [sla.spsolve(A, rhs), A]

'''
Test cases for method of manufactured solutions
'''

# (i)
def true_u_i(x):
	return (1/3)*np.e**(-4*x) + (2/3)*np.e**(2*x)

def p_i(x):
	return [2 for i in x]

def q_i(x):
	return [-8 for i in x]

def f_i(x):
	return 0*x

pt.figure(1)
e_i = []
for k in xrange(3,21):
	approx_u_i = bvp_solve(p_i, q_i, f_i, np.linspace(0, 1, 2**k), true_u_i(0), true_u_i(1))
	e_i.append(max(abs(true_u_i(np.linspace(0, 1, 2**k)) - approx_u_i)))

pt.loglog([2**i for i in range(3,21)], e_i, label='Error for (i)')
pt.loglog(np.linspace(0,2**20, 2**20), 2*np.linspace(0,2**20, 2**20), label='Line of slope 2')
pt.legend()
pt.savefig('fig3_1')

# #(ii)

def true_u_ii(x):
	return np.sin(np.log(x))

def p_ii(x):
	return 2/x

def q_ii(x):
	return -2/x**2

def f_ii(x):
	return np.cos(np.log(x))/x**2 - 3*np.sin(np.log(x))/x**2

pt.figure(2)
e_ii = []
for k in xrange(3,21):
	approx_u_ii = bvp_solve(p_ii, q_ii, f_ii, np.linspace(1, 2, 2**k), true_u_ii(1), true_u_ii(2))
	e_ii.append(max(abs(true_u_ii(np.linspace(1, 2, 2**k)) - approx_u_ii)))

pt.loglog([2**i for i in range(3,21)], e_ii, label='Error for (ii)')
pt.loglog(np.linspace(1,2**20, 2**20), 2*np.linspace(1,2**20, 2**20), label='Line of slope 2')
pt.legend()
pt.savefig('fig3_2')

# #(iii)
def true_u_iii(x):
	return -np.sin(x) + 3*np.cos(x)

def p_iii(x):
	return [-1 for i in x]

def q_iii(x):
	return [-2 for i in x]

def f_iii(x):
	return 4*np.sin(x) - 2*np.cos(x) - 2*(3*np.cos(x) - np.sin(x))

pt.figure(3)
e_iii = []
for k in xrange(3,21):
	approx_u_iii = bvp_solve(p_iii, q_iii, f_iii, np.linspace(0, np.pi/2, 2**k), true_u_iii(0), true_u_iii(np.pi/2))
	e_iii.append(max(abs(true_u_iii(np.linspace(0, np.pi/2, 2**k)) - approx_u_iii)))

pt.loglog([2**i for i in range(3,21)], e_iii, label='Error (iii)')
pt.loglog(np.linspace(1,2**20, 2**20), 2*np.linspace(1,2**20, 2**20), label='Line of slope 2')
pt.legend()
pt.savefig('fig3_3')

##############################
#part d 

cond = []
for k in xrange(3, 12):
	A = bvp_solve(p_i, q_i, f_i, np.linspace(0,1,2**k), true_u_i(0), true_u_i(1))[1]
	cond.append(la.cond(A.todense()))

pt.figure(4)
pt.loglog([2**k for k in xrange(3, 12)], cond, label='Condition')
pt.legend()
pt.savefig('fig3_4')