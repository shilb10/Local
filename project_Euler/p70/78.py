from __future__ import division

# Indices = []
# for i in xrange(1,500):
#     Indices.append(i)
#     Indices.append(-i)

# GenPent = [i*(3*i - 1)/2 for i in Indices]
# print GenPent[499]


'''
449, 3
599, 4
11224, 5

'''

# P = {0: 1}
# def part(n):
#     if n < 0:
#         return 0

#     if n in P:
#         return P[n]

#     l = [int((-1)**(i + 1)*(part(n - .5*i*(3*i - 1)) + part(n - .5*i*(3*i + 1)))) for i in xrange(1, int(n + 1))]
#     P[n] = sum(l) % 10**6
#     return P[n]

# print part(10**2)

# n = 100
# while part(n) != 0:
#     if n % 20 == 0:
#         print n, P[n]
#     n += 1

# print n, P[n]

P = {0: 1, 1: 1}
d = 10**6
n = 1
while P[n] != 0:
    n += 1
    i = 0
    m1 = int(n - i * (3 * i - 1) / 2)
    m2 = int(n - i * (3 * i + 1) / 2)
    while m1 >= 0 or m2 >= 2:
        s = 1
        if i % 2 == 0:
            s = -1
        if m1 >= 0:
            P[n] += s*P[m1]
        if m2 >= 0:
            P[n] += s* P[m2]
    P[n] = P[n] % d 

print n