from __future__ import division
import fractions

def mul(a, b):
    return a[0]*b[0] + a[1]*b[1]

def div(a,b):
    return (a[0]+a[1])/b

def conj(a):
    return (a[0], -a[1])

def continued(n):
    frac = []
    a = n**.5
    frac.append(int(a))
    top = 1
    bot = (a, -int(a))
    for i in xrange(100):
        ntop = conj(bot)
        nbot = round(mul(bot, ntop)/top)
        print nbot
        a = div(ntop, nbot)
        frac.append(int(a)) 
        top = nbot
        bot = (n**.5, ntop[1]- nbot*frac[-1])

    return frac

def periodCount(n):
    frac = []
    count = 0
    a = n**.5
    frac.append(int(a))
    top = 1
    bot = (a, -int(a))
    for i in xrange(500):
        ntop = conj(bot)
        nbot = round(mul(bot, ntop)/top)
        count += 1
        try:
            a = div(ntop, nbot)
        except:
            print ntop, nbot, n
            return
        frac.append(int(a)) 
        top = nbot
        bot = (n**.5, ntop[1]- nbot*frac[-1])
        if nbot == 1.0:
            return count

    return 0

Sq = [n**2 for n in xrange(101)]

count = 0
for i in xrange(2,10001):
    if i not in Sq:
        if periodCount(i) % 2 == 1:
            count += 1

print count