from __future__ import division
from timeit import default_timer as timer

start = timer()

np_list = [2]
def cdf_primes(n):
    '''Generates primes <= n. Returns list indexed by n instead of pi(n)'''
    p_sieve = [True]*(n+1)
    p_list = [0]*(n+1)
    p_list[2] = 1
    for i in xrange(3, n+1, 2):
        if p_sieve[i]:
            np_list.append(i)
            p_list[i] = 1
            for k in xrange(i**2, n+1, i):
                p_sieve[k] = False
    return p_list

# plist = cdf_primes(10**8)
# end = timer()
# print len(plist), len(np_list), end - start

def div_primes(n):
    if n**.5 == int(n**.5):
        return False
    for i in xrange(1, int(n**.5)):
        if n % i == 0:
            if plist[int(i + n/i)] == 0:
                return False
    return True

print div_primes(3)

# n_sum = 0
# n_end = timer()
# for i in np_list:
#     if div_primes(i-1):
#         n_sum += i-1
#     if timer() - n_end > 10:
#         print i
#         n_end = timer()

# print n_sum

def is_square(n):
    if n**.5 == int(n**.5):
        return True 
    else:
        return False

def has_square(n):
    if is_square(n):
        return True
    for i in xrange(2, n**.5):
        if is_square(i) or is_square(n/i):
            return True 
    return False

def factors(n):
    facs = []
    for i in xrange(1, int(n**.5)):
        if n % i == 0:
            facs.append(i)
            facs.append(n/i)
    return sorted(facs)

def dec_sum(n, l, i, j):
    if i == 1:
        return
    if has_square(i) or has_square(j):
        dec_sum(n, l, i-1, j+1)


def isPrime(n):
    if n == 1:
        return False
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

