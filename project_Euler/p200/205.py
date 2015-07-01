from __future__ import division

pyrDist = [0]
pyrDist.extend([.25 for i in xrange(4)])
cubDist = [0]
cubDist.extend([1/6 for i in xrange(6)])

def conv(d1, d2):
    d3 = []
    for j in xrange(37):
        d3.append(sum([d1[k]*d2[j-k] for k in xrange(len(d1)) if j-k in xrange(len(d2))]))
    return d3

def convDiff(d1, d2):
    d3 = []
    for j in xrange(37):
        d3.append(sum([d1[k]*d2[j+k] for k in xrange(len(d1)) if j+k in xrange(len(d2))]))
    return d3

cub6Dist = conv(cubDist, cubDist)
for i in xrange(4):
    cub6Dist = conv(cub6Dist, cubDist)

pyr9Dist = conv(pyrDist, pyrDist)
for i in xrange(7):
    pyr9Dist = conv(pyr9Dist, pyrDist)

d = convDiff(cub6Dist, pyr9Dist)
print sum(d) - d[0] 
print sum(pyr9Dist)
