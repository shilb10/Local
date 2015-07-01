from __future__ import division

x = [1]
y = [0]

for i in xrange(1,20):
    x.append(3*x[i-1] + 4*y[i-1] - 1)
    y.append(2*x[i-1] + 3*y[i-1] - 1)
    if x[-1] + 2*y[-1] > 10**12:
        print x[-1] + y[-1]