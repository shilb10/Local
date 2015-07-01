from __future__ import division
import math

def gen_primes(n):
    '''Generates primes <= n'''
    p_sieve = [True]*(n+1)
    p_list = [2**i for i in xrange(int(math.log(10**8, 2)) + 1)]
    for i in xrange(3, n+1, 2):
        if p_sieve[i]:
            l = [i**j for j in xrange(1, int(math.log(10**8, i))+1)]
            n_l = []
            for elem in l:
                for p in p_list:
                    if elem*p <= 10**8:
                        n_l.append(elem*p)
            p_list += n_l
            for k in xrange(i**2, n+1, i):
                p_sieve[k] = False
    return p_list

p_list = gen_primes(5)
print len(p_list)
