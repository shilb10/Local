import math

f = open('p099_base_exp.txt', 'r')

m = 0
count = 0
lineNum = 0
for line in f:
    count += 1
    a = int(line.split(',')[0])
    b = int(line.split(',')[1])
    if m < b*math.log(a):
        m = b*math.log(a)
        lineNum = count

print lineNum

