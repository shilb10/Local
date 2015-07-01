from __future__ import division

f = open('p082_matrix.txt', 'r')
A = []
for line in f:
    l = line.split(',')
    A.append([int(s) for s in l])

n = len(A)
mdict = {(level, 0): A[level][0] for level in xrange(n)}

def min_sum(level, i):
    if mdict.has_key((level, i)):
        return mdict[(level, i)]
    if level == 0:
        mdict[(level, i)] = A[level][i] + min([min_sum(level+s, i-1) + sum([A[level+j][i-1] for j in xrange(s)]) for s in xrange(n - level - 1)])
        return mdict[(level,i)]
    if level == n-1:
        mdict[(level, i)] = A[level][i] + min([min_sum(level-s, i-1) + sum([A[level-j][i-1] for j in xrange(s)]) for s in xrange(level+1)])
        return mdict[(level,i)]
    mdict[(level, i)] = A[level][i] + min([min_sum(level-s, i-1) + sum([A[level-j][i-1] for j in xrange(s)]) for s in xrange(level+1)] + [min_sum(level+s, i-1) + sum([A[level+j][i-1] for j in xrange(s)]) for s in xrange(n - level - 1)])
    return mdict[(level, i)]

l = []
for i in reversed(xrange(n)):
    l.append(min_sum(i, n-1))
print min(l)