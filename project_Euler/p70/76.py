from __future__ import division

Indices = []
for i in xrange(1,11):
    Indices.append(i)
    Indices.append(-i)

GenPent = [i*(3*i - 1)/2 for i in Indices]

print Indices
print GenPent
print Indices[GenPent.index(5)]

P = {0: 1}
def part(n):
    if n < 0:
        return 0

    if n in P:
        return P[n]

    l = [(-1)**(Indices[GenPent.index(i)] - 1)*part(n - i) for i in GenPent]
    P[n] = sum(l)
    return P[n]

print part(100)