from __future__ import division
import numpy as np 

mat = np.arange(25).reshape((5,5))
fin_mat = mat + mat.T - np.diag(mat.diagonal()) - np.diag(mat.diagonal())
t = np.copy(fin_mat)

print fin_mat
fin_mat[3, 0] = fin_mat[0,3] = fin_mat[3, 1] = fin_mat[1, 3] = fin_mat[3, 2] = fin_mat[2, 3] = 0
fin_mat[4, 0] = fin_mat[0,4] = fin_mat[4, 1] = fin_mat[1, 4] = fin_mat[2, 4] = fin_mat[4, 2] = 0
print fin_mat
print np.linalg.eigvals(fin_mat)

def lap(mat):
    return np.diag([sum(mat[i]) for i in xrange(len(mat))]) - mat

lap_fin_mat = lap(fin_mat)
print np.linalg.eigvals(fin_mat)
print np.linalg.eigvals(lap_fin_mat)
print np.linalg.eigvals(lap(t))