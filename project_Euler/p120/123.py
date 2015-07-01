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

p_list = [1] + gen_primes(10**6)
print p_list.index(2)
print len(p_list)
for p in p_list:
    if ((pow(p-1, p_list.index(p), p**2) + pow(p+1, p_list.index(p), p**2)) % p**2)  > 10**(10):
        print p_list.index(p) 
        break
