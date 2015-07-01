from __future__ import division
import fractions


def isPrime(n):
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

def phi(n):
    if n in Primes:
        return n - 1
    for i in xrange(2, int(n**.5) + 1):
        if n % i == 0:
            if i in Primes:
                return 

F = {0: 1, 1: 2}
def Farey(n):
    if n in F:
        return F[n]
    else:
        F[n] = .5*(n + 3)*n - sum([Farey(int(n/d)) for d in xrange(2, n + 1)])
        return F[n]
    
print Farey(10**6) - 2