import copy

Tri = [(str(n*(n+1)/2),3) for n in xrange(1,140) if n*(n+1)/2 >= 1000]
Sq = [(str(n**2),4) for n in xrange(1,100) if n**2 >= 1000 and n**2 < 10000]
Pen = [(str(n*(3*n-1)/2), 5) for n in xrange(1,100) if n*(3*n-1)/2 >= 1000 and n*(3*n-1)/2 < 10000]
Hex = [(str(n*(2*n-1)), 6) for n in xrange(1,100) if n*(2*n-1) >= 1000 and n*(2*n-1) < 10000]
Hep = [(str(n*(5*n-3)/2), 7) for n in xrange(1,100) if n*(5*n-3)/2 >= 1000 and n*(5*n-3)/2 < 10000]
Oct = [(str(n*(3*n-2)), 8) for n in xrange(1,100) if n*(3*n-2) >= 1000 and n*(3*n-2) < 10000]
ALL = Tri  + Sq + Pen + Hex + Hep + Oct


def cyclic(num, typeList, curList, depth):
    if depth == 6:
        return curList

    A = [elem for elem in ALL if (num[0][2:] == elem[0][:2]) and (elem[1] not in typeList)]
    if len(A) > 0:
        for a in A:
            tList = copy.deepcopy(typeList)
            tList.append(a[1])
            cList = copy.deepcopy(curList)
            cList.append(a)
            B = cyclic(a, tList, cList, depth + 1)
            if B != None:
                if B[5][0][2:] == B[0][0][:2]:
                    return B
for t in ALL:
    A = cyclic(t, [t[1]], [t], 1)
    if A != None:
        print sum([int(a[0]) for a in A])

