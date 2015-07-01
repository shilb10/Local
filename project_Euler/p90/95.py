from __future__ import division

amic_divs = {1:1}
non_amic_divs = set([1, 2])

def div_sum(n):
    s = 1
    for i in xrange(2, int(n**.5)):
        if n % i == 0:
            s += i + n/i
    if int(n**.5) == n**.5:
        s += n**.5
    return s

def amicable(n):
    clen = 1
    flag = True
    s = div_sum(n)
    if s > 10**6:
        non_amic_divs.add(n)
        return
    if s == n:
        amic_divs[n] = clen
        return
    if amic_divs.has_key(s) or s in non_amic_divs: 
        non_amic_divs.add(n)
        return
    else:
        while flag:
            if clen > 50:
                non_amic_divs.add(n)
                flag = False
            clen += 1
            s = div_sum(s)
            if s > 10**6:
                non_amic_divs.add(n)
                flag = False
            elif s == n:
                amic_divs[n] = clen
                flag = False
            elif amic_divs.has_key(s) or s in non_amic_divs: 
                non_amic_divs.add(n)
                flag = False

for i in xrange(1,1000000):
    amicable(i)

print amic_divs