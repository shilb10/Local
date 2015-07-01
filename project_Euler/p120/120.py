from __future__ import division

s = 0
for a in xrange(3, 1001):
    s += max([(pow(a-1, n, a**2) + pow(a+1, n, a**2)) % a**2 for n in xrange(2*a)])

print s