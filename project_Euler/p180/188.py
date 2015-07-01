from __future__ import division 

a = [1777**i % 10**8 for i in xrange(1,10000)]
print min(a[1:]), a.index(min(a[1:]))