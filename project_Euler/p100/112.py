from __future__ import division

def intArr(n):
    arr = []
    for i in str(n):
        arr.append(int(i))
    return arr

def bouncy(n):
    inc = sorted(intArr(n))
    dec = sorted(intArr(n), reverse=True) 
    if inc == intArr(n) or dec == intArr(n):
        return False
    else:
        return True

rat = 0
bcount = 0
tcount = 0
n = 1
while rat != .99:
    if bouncy(n):
        bcount += 1
    tcount += 1
    n += 1
    rat = bcount/tcount

print n