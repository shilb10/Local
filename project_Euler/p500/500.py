from __future__ import division
import threading
import numpy as np
import math
import operator
import functools

def divisors(n):
    div_list = []
    for i in xrange(1, int(n**.5)+ 1):
        if n % i == 0:
            div_list.append(i)
            if n/i != i:
                div_list.append(n/i)

    return len(div_list)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def isPrime(n):
    if n == 1:
        return False
    for i in xrange(2,int(n**.5)+1):
        if (n % i) == 0:
            return False
    return True

def isPowTwoPrimePower(n):
    if n == 1:
        return False
    up_lim = int(math.log(n,2)) + 2
    i = 2
    while i < up_lim:
        j = math.pow(n, 1/i)
        j = long(round(j))
        if j**i == n:
            if isPrime(j):
                return True
        i = 2*i
    return False

# div_nums = []
# for i in xrange(1, factorial(8)+1):
#     div_nums.append((i, divisors(i)))

# div_nums.sort(key=lambda x: x[1], reverse=True)
# div = div_nums[0][1]
# count = 0 
# for elem in div_nums:
#     if elem[1] == div:
#         if count == 0:
#             print elem
#             count += 1
#     else:
#         div = elem[1]
#         print elem

# j = 120
# for i in xrange(7,40,2):
#     if j % i != 0:
#         print j, divisors(j), i
#         j = j*i 

# j = 120
# count = 4
# i = 7
# while count < 30:
#     if j%i != 0:
#         print j, i, count, isPrime(i)
#         count += 1
#         j = (j*i)
#     i += 2

# print j % 500500507, i

# p_or_square = [i for i in xrange(7, 3000000,2) if isPrime(i) or (int(i**.5) == i**.5)]

# print p_or_square[:10], len(p_or_square)

# f = open('plist.txt', 'w')

# a_list = []
# for i in xrange(30):
#     a_list.append([])

# def prime_enum(p_range, l):
#     print 'starting. started at {0}'.format(p_range[0])
#     for i in p_range:
#         if isPrime(i) or isPowTwoPrimePower(i):
#             l.append(i)
#     print 'done. started at {0}'.format(p_range[0])

# threads = []
# for i in xrange(30):
#     t = threading.Thread(target=prime_enum, args=(range(i*300000 + 1, (i+1)*300000+1,2), a_list[i]))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# final_a = [n for l in a_list for n in l]
# print len(final_a)
# f.write(','.join(str(elem) for elem in final_a))

f = open('plist.txt', 'r')
p_list = map(int, f.readline().split(','))
pow_twos = [2, 2**2, 2**4, 2**8, 2**16]
print pow_twos
cur = 0
i = 0
while cur < len(pow_twos):
    if pow_twos[cur] < p_list[i]:
        p_list.insert(i, pow_twos[cur])
        cur += 1
    i += 1
print p_list[:10]
for i in xrange(1,14):
    a = functools.reduce(lambda x, y: x*y, p_list[:i])
    print a, divisors(a), i
print functools.reduce(lambda x, y: x*y % 500500507, p_list[:500500])


