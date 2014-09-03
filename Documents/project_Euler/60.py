def isPrime(n):
	for i in xrange(2,int(n**.5)+1):
		if (n % i) == 0:
			return False
	return True

A = ['3', '7', '109', '673']

flag = True
count = 1

for i in [x for x in xrange(2000000) if isPrime(x)]:
	if count == 50:
		count = 0
		print i
	for j in xrange(4):
		if isPrime(int(A[j] + str(i))) and isPrime(int(str(i) + A[j])):
			flag &= True
		else:
			flag &= False
	if flag:
		print i
		break
	count += 1

