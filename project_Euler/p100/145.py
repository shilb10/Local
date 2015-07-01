def allOdd(n):
    for i in str(n):
        if int(i) % 2 == 0:
            return False
    return True

def reversible(n):
    if str(n)[-1] != '0':
        if allOdd(n + int(str(n)[::-1])):
            return True 
    return False


count = 0
for i in xrange(1, 1000000  ):
    if reversible(i):
        count += 1

print count