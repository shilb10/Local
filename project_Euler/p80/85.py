from __future__ import division

A = {(1,1): 1}
def count_rec(r, c):
    if c <= 0:
        return 0
    if A.has_key((r,c)):
        return A[(r,c)]
    else:
        A[(r,c)] = 2*count_rec(r, c-1) - count_rec(r, c-2) + count_rec(1, r)
        A[(c,r)] = A[(r,c)]
        return A[(r,c)]


for i in xrange(1,300):
    for j in xrange(1,300):
        count_rec(i,j)

for a in A:
    if A[a] >= 2*10**6*.999 and A[a] <= 2*10**6*1.001:
        print a, A[a]