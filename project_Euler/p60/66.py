from __future__ import division
import fractions

def mul(a, b):
    return a[0]*b[0] + a[1]*b[1]

def div(a,b):
    return (a[0]+a[1])/b

def conj(a):
    return (a[0], -a[1])

def continued(n):
    i = 0
    frac = []
    aconv = []
    bconv = [1]
    a = n**.5
    frac.append(int(a))
    aconv.append(int(a))
    top = 1
    bot = (a, -int(a))
    while aconv[-1]**2 - n*bconv[-1]**2 != 1:
        ntop = conj(bot)
        nbot = round(mul(bot, ntop)/top)
        a = div(ntop, nbot)
        frac.append(int(a))
        if i == 0:
            aconv.append(frac[-1]*frac[-2] + 1)
            bconv.append(frac[-1])
            i = 1
        else:
            aconv.append(frac[-1]*aconv[-1] + aconv[-2])
            bconv.append(frac[-1]*bconv[-1] + bconv[-2])
            
        top = nbot
        bot = (n**.5, ntop[1]- nbot*frac[-1])

    return aconv[-1]

Sq = [n**2 for n in xrange(40)]
A = []

for i in xrange(1001):
    if i not in Sq:
        A.append((continued(i), i))

print max(A, key=lambda x: x[0])


