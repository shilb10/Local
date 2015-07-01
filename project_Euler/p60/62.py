import itertools
import thread

A = [n**3 for n in xrange(10000)]


def digits(n):
    digList = [0,0,0,0,0,0,0,0,0,0,n]
    for dig in str(n):
        digList[int(dig)] += 1
    return digList

def listeq(s, t):
    for i in xrange(10):
        if s[i] != t[i]:
            return False
    return True

B = [digits(a) for a in A]

for i in reversed(range(11)):
    B.sort(key=lambda x: x[i])

start = B[0]
count = 1
for i in xrange(len(B) - 1):
    if listeq(start, B[i + 1]):
        count += 1
    else:
        count = 1
    if count == 5:
        for j in xrange(5):
            print B[i - j + 1]
        print
        count = 1

    start = B[i + 1]



