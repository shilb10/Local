
def digits(n):
    digList = [0,0,0,0,0,0,0,0,0,0]
    for dig in str(n):
        digList[int(dig)] += 1
    return digList

def listeq(s, t):
    for i in xrange(10):
        if s[i] != t[i]:
            return False
    return True

count = 0
for i in xrange(int(1.3*10**8), int(1.4*10**8)):
    if str(i**2)[-1] == '9' and str(i**2)[-3] == '8' and str(i**2)[-5] == '7' and str(i**2)[-7] == '6' and str(i**2)[-9] == '5' and str(i**2)[-11] == '4' and str(i**2)[-13] == '3' and str(i**2)[-15] == '2':
        print i, i**2

print count