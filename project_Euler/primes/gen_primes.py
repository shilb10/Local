from __future__ import division

def gen_primes(n):
    '''Generates primes <= n'''
    f = open('plist_2_1000000.txt', 'w')
    interval = 10**6
    upper = interval
    count = 1
    p_sieve = [True]*(n+1)
    f.write('2')
    for i in xrange(3, n+1, 2):
        if i > upper:
            f.close()
            f = open('plist_{0}_{1}.txt'.format(upper+1, upper + interval), 'w')
            count = 0
            upper += interval
        if p_sieve[i]:
            if count == 0:
                f.write('{0}'.format(i))
                count += 1
            else:
                f.write(',{0}'.format(i))
            for k in xrange(i**2, n+1, i):
                p_sieve[k] = False

gen_primes(10**8)
