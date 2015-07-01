import math

def digitFacSum(n):
    s = 0
    for i in str(n):
        s += math.factorial(int(i))
    return s

A = []
for i in xrange(1, 10**6):
    B = []
    B.append(i)
    s = digitFacSum(i)
    while s not in B:
        B.append(s)
        s = digitFacSum(B[-1])
    if len(B) == 60:
        A.append(i)

print len(A)