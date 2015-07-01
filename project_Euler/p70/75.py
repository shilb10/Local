from __future__ import division
import fractions

def isPrime(n):
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

T = {}

curr = 0
for m in xrange(2, 750001):
    curr += 1
    if curr % 10000 == 0:
        print curr
    for n in xrange(1, m):
        if m*(m + n) > 750000:
            break
        if (m - n) % 2 == 1:
            if fractions.gcd(m, n) == 1:
                for k in xrange(1, 7*10**5):
                    if k*m*(m + n) > 750000:
                        break
                    if k*m*(m + n) not in T:
                        T[k*m*(m + n)] = 1
                    else:
                        T[k*m*(m + n)] = 0

print sum([T[i] for i in T])
