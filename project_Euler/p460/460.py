from __future__ import division

rec = {1:1, 3:3}
def f(n):
    if n == 1:
        return rec[n]
    if n == 3:
        return rec[n]
    if n % 2 == 0:
        if rec.has_key(n/2):
            return rec[n/2]
        else:
            rec[n/2] = f(n/2)
            return rec[n/2]
    elif n % 4 == 1:
        m = int(n/4)
        if rec.has_key(2*m + 1):
            if rec.has_key(m):
                return 2*rec[2*m + 1] - rec[m]
            else:
                rec[m] = f(m)
                return 2*rec[2*m + 1] - rec[m]
        else:
            rec[2*m + 1] = f(2*m + 1)
            if rec.has_key(m):
                return 2*rec[2*m + 1] - rec[m]
            else:
                rec[m] = f(m)
                return 2*rec[2*m + 1] - rec[m]
    else:
        m = int(n/4)
        if rec.has_key(2*m + 1):
            if rec.has_key(m):
                return 3*rec[2*m + 1] - 2*rec[m]
            else:
                rec[m] = f(m)
                return 3*rec[2*m + 1] - 2*rec[m]
        else:
            rec[2*m + 1] = f(2*m + 1)
            if rec.has_key(m):
                return 3*rec[2*m + 1] - 2*rec[m]
            else:
                rec[m] = f(m)
                return 3*rec[2*m + 1] - 2*rec[m]

for i in xrange(1,100, 4):
    if i % 4 == 1:
        print i, f(i), f(i+2), f(i) - f(i+2), int(i/4)

for i in xrange(1,10):
    print sum([f(4*j+5) + f(4*j + 6) +  f(4*j+7) + f(4*j+8) for j in xrange(1,2**i+1)])