def s(p):
    y = pow(6,p-2,p)
    x = y*pow(p-4, p-2, p)
    return ((p-1)/2 + y + x) % p


def gen_primes(n):
    '''Generates primes <= n'''
    p_sieve = [True]*(n+1)
    p_list = [2]
    for i in xrange(3, n+1, 2):
        if p_sieve[i]:
            p_list.append(i)
            for k in xrange(i**2, n+1, i):
                p_sieve[k] = False
    return p_list

p_list = gen_primes(10**8)
print 'done'

print sum([s(p) for p in p_list[2:]])