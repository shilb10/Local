def create_proper_divisors(limit):
    '''Gives divisor sums for each number <= limit'''
    table = [1] * limit
    for n in xrange(2, limit):
        for m in xrange(n + n, limit, n):
            table[m] += n
    return table

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

def cdf_primes(n):
    '''Generates primes <= n. Returns list indexed by n instead of pi(n)'''
    p_sieve = [True]*(n+1)
    p_list = [0]*(n+1)
    p_list[2] = 1
    for i in xrange(3, n+1, 2):
        if p_sieve[i]:
            p_list[i] = 1
            for k in xrange(i**2, n+1, i):
                p_sieve[k] = False
    return p_list