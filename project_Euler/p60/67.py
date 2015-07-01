from __future__ import division

f = open('p067_triangle.txt', 'r')
A = []
for line in f:
    l = line.split(' ')
    A.append([int(s) for s in l])


mdict = {(99, i): A[99][i] for i in xrange(100)}
def max_sum(i, level):
    if mdict.has_key((level, i)):
        return mdict[(level, i)]
    mdict[(level, i)] = A[level][i] + max([max_sum(i, level+1), max_sum(i+1, level+1)])
    return mdict[(level, i)]

print max_sum(0,0)
