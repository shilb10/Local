def isPrime(n):
	for i in xrange(2,int(n**.5)+1):
		if (n % i) == 0:
			return False
	return True

def concat(x, y):
    return int(str(x)+str(y))

j = 0
P = [i for i in xrange(3, 50000) if isPrime(i)]
for p in P:
    A = [i for i in P if i > p and isPrime(concat(i,p)) and isPrime(concat(p,i))]
    j += 1
    if j % 50 == 0:
        print j
    if len(A) > 0:
        for a in A:
            B = [i for i in A if i > a and isPrime(i) and isPrime(concat(i,a)) and isPrime(concat(a,i))]
            if len(B) > 0:
                for b in B:
                    C = [i for i in B if i > b and isPrime(concat(i,b)) and isPrime(concat(b,i))]
                    if len(C) > 0:
                        for c in C:
                            D = [i for i in C if i > c and isPrime(concat(i,c)) and isPrime(concat(c,i))]
                            if len(D) > 0:
                                print [p,a,b,c,D[0]]
                                print p + a + b + c + D[0]

