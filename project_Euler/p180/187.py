from __future__ import division

def gen_primes(n):
    '''Generates primes <= n'''
    p_sieve = [True]*(n+1)
    p_list = [2]
    comp_list = [4]
    for i in xrange(3, n+1, 2):
        if p_sieve[i]:
            p_list.append(i)
            for p in p_list:
                if i*p < n:
                    comp_list.append(i*p)
                else:
                    break
            for k in xrange(i**2, n+1, i):
                p_sieve[k] = False
    return comp_list

print len(gen_primes(100000000))