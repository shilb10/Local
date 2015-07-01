from __future__ import division
import fractions

def isPrime(n):
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

Primes = [i for i in xrange(2, int((50*10**6)**.5)) if isPrime(i)]

Nums = set([])
count = 0
for p1 in Primes:
    if p1**2 < 50*10**6:
        count += 1
        print count
        for p2 in Primes:
            if p1**2 + p2**3 < 50*10**6:
                for p3 in Primes:
                    if p1**2 + p2**3 + p3**4< 50*10**6:
                        Nums.add(p1**2 + p2**3 + p3**4)

print len(Nums)