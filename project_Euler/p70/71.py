from __future__ import division
import fractions

for i in reversed(range(10**6)):
    if (3*i - 1)/7 == int((3*i - 1)/7):
        print (3*i - 1)/7, i
        print fractions.gcd((3*i - 1)/7, i)
        break

print 428570/999997
print 3/7