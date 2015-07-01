from decimal import *

getcontext().prec = 200
Sq = [i**2 for i in xrange(1,11)]
print Sq
num = Decimal(2)
s = str(num.sqrt())
print sum([int(j) for j in s[:101] if j != '.'])

total = 0
for i in xrange(int(2),int(100)):
    if i not in Sq:
        num = Decimal(i)
        s = str(num.sqrt())
        total += sum([int(j) for j in s[:101] if j != '.'])
        print i, sum([int(j) for j in s[:101] if j != '.'])

print total
