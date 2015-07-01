
C = {1: 1, 89: 89}
def sq(n):
    if n not in C:
        C[n] = sq(sum([int(i)**2 for i in str(n)]))
    return C[n]

print sum([1 for i in xrange(1,10**7) if sq(i) == 89])