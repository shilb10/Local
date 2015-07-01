from __future__ import division
import math

checked = {}
def num_sols(trip, lim):
    a = min(trip)
    b = int((trip[2]**2 - a**2)**.5)
    if checked.has_key((a,b)):
        return 0
    checked[(a,b)] = 1
    if a > lim:
        return 0
    if 2*a >= b:
        if b <= lim:
            return int(a/2) + math.ceil((2*a - b + 1)/2)
        else:
            return math.ceil((2*a - b + 1)/2)
    else:
        if b <= lim:
            return int(a/2)
        else:
            return 0

# upper_lim = 7
# sols = 0
# num_list = []
# for l in xrange(1,upper_lim+1):
#     for w in xrange(l, upper_lim+1):
#         for h in xrange(w, upper_lim+1):
#             if ((w+l)**2 + h**2) == 100:
#                 print l, w, h
#                 num_list.append([l,w,h])
#                 sols += 1

# print sols, num_sols([6,8,10], upper_lim)

# for a in xrange(2, 2*upper_lim):
#     for h in xrange(int(a/2), upper_lim):
#         if (a**2 + h**2)**.5 == int((a**2 + h**2)**.5):
#             sols += int(a/2)

# print sols

f = open('PythagTriples.txt', 'r')
trips = []
for line in f:
    h = line.split()[3:]
    trips.append(map(int, h))

sols = 0
for trip in trips:
    sols += num_sols(trip, 1818)

print sols