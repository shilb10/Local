from __future__ import division
from timeit import default_timer as timer


def invmodp(a, p):
    '''
    The multiplicitive inverse of a in the integers modulo p.
    Return b s.t.
    a * b == 1 mod p
    '''
    for d in xrange(1, p):
        r = (d * a) % p
        if r == 1:
            break
    return d


sstart = timer()
start = timer()
m = 1000000007
s = 0
for k in xrange(1, 10**6+1):
    s  = (s + (1-pow(1-k**2, 10**6+1, m))*pow(k**2, m-2, m) - 1) % m
    if timer() - start > 10:
        start = timer()
        print k

print s