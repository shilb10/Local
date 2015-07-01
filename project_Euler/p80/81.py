from __future__ import division

f = open('p081_matrix.txt', 'r')
A = []
for line in f:
    l = line.split(',')
    A.append([int(s) for s in l])

mdict = {(79, 79): A[79][79]}

def min_sum(level, i):
    if mdict.has_key((level, i)):
        return mdict[(level, i)]
    if i == 79:
        mdict[(level, i)] = A[level][i] + min_sum(level+1, i)
        return mdict[(level, i)]
    if level == 79:
        mdict[(level, i)] = A[level][i] + min_sum(level, i+1)
        return mdict[(level, i)]
    mdict[(level, i)] = A[level][i] + min([min_sum(level+1, i), min_sum(level, i+1)])
    return mdict[(level, i)]

print min_sum(0,0)