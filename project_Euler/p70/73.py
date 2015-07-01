from __future__ import division
import fractions

F = {0: 1, 1: 2}
def Farey(n):
    if n in F:
        return F[n]
    else:
        F[n] = .5*(n + 3)*n - sum([Farey(int(n/d)) for d in xrange(2, n + 1)])
        return F[n]

def phi(n):
    count = 0
    for i in xrange(1,n):
        if fractions.gcd(i,n) == 1:
            count += 1
    return count

def countBetween(n):
    count = 0
    while n > 3:
        for d in xrange(int(n/3) + 1, int(n/2) + 1):
            if fractions.gcd(n, d) == 1:
                count += 1
        print n
        n -= 1
    return count

print countBetween(12000)
