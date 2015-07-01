from __future__ import division

def isPrime(n):
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

C = {1: 0}
def c(n):
    if n not in C:
        C[n] = 0
        for i in xrange(2, n+1):
            if n % i == 0:
                if isPrime(i):
                    C[n] += i
    return C[n]

B = {1: c(1)}

def b(n):
    if n not in B:
        B[n] = (1/n)*(c(n) + sum([c(k)*b(n-k) for k in xrange(1, n)]))
    return B[n]

n = 2
while b(n) < 5000:
    if n % 100 == 0:
        print n, B[n]
    n += 1

print n, B[n]