from __future__ import division
import numpy as np 


def max_vals(mat):
    m_list = []
    for i in xrange(len(mat)):
        m_list.append(max(mat[i][i:]))
    return m_list

def lap(mat):
    return np.diag([sum(mat[i]) for i in xrange(len(mat))]) - mat

f = open('p107_network.txt', 'r')
mat = []
non_zero_elems = 0
weight_sum = 0
for line in f:
    s = line.split(',')
    non_zero_elems += sum([1 if i[0] != '-' else 0 for i in s])
    weight_sum += sum([int(i) if i[0] != '-' else 0 for i in s])
    mat.append([int(i) if i[0] != '-' else 0 for i in s])

mat = np.array(mat)
non_zero_elems = non_zero_elems / 2
print non_zero_elems
weight_sum = weight_sum / 2

flag = True
check_flag = True 
max_val = 0
while flag:
    m_list = sorted(max_vals(mat), reverse=True)
    print m_list, len(m_list)
    for val in m_list:
        indices = np.where( mat == val )
        i, j = indices[0][0], indices[0][1]
        max_val = val
        mat[i, j] = mat[j, i] = 0
        lap_mat = lap(mat)
        if sorted(np.linalg.eigvals(lap_mat))[1] == 0:
            print 'disconnected'
            mat[i, j] = mat[j, i] = max_val
        else:
            non_zero_elems -= 1
            if non_zero_elems == 39:
                flag = False
                break

new_weight = sum([sum([abs(mat[i][j]) for j in xrange(40)]) for i in xrange(40)])
new_weight = new_weight / 2

print non_zero_elems
print weight_sum - new_weight
print weight_sum
print new_weight


