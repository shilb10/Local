from __future__ import division
import fractions

def phi(n):
    count = 0
    for i in xrange(1,n):
        if fractions.gcd(i,n) == 1:
            count += 1
    return count

def digits(n):
    digList = [0,0,0,0,0,0,0,0,0,0,n]
    for dig in str(n):
        digList[int(dig)] += 1
    return digList

def listeq(s, t):
    for i in xrange(10):
        if s[i] != t[i]:
            return False
    return True

def listmul(s,t,b):
    A = set()
    for i in s:
        for j in t:
            if i*j < b:
                A.add(i*j)
    return A

def isPrime(n):
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

Primes = [i for i in xrange(1,int(10**(7/1.5))) if isPrime(i)]

def primePhi(plist):
    phi = 1
    for p in plist:
        phi *= int(p*(1 - 1/p))
    return phi


def primefac(n):
    facs = []
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            facs.append((i, n/i))
    return facs

A = []
for i in xrange(len(Primes)):
    for j in xrange(i,len(Primes)):
        if Primes[i]*Primes[j] < 10**7:
            if listeq(digits(Primes[i]*Primes[j]), digits(primePhi([Primes[i],Primes[j]]))):
                A.append((Primes[i]*Primes[j], primePhi([Primes[i],Primes[j]])))

print min(A, key=lambda x: x[0]/x[1])