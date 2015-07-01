from timeit import default_timer as timer

def create_proper_divisors(limit):
    '''Gives divisor sums for each number <= limit'''
    table = [1] * limit
    for n in xrange(2, limit):
        for m in xrange(n, limit, n):
            table[m] += 1
    return table

start = timer()
d_list = create_proper_divisors(10**7)
end = timer()

print 'done', start - end

num = 0
for i in xrange(2,len(d_list)):
    if d_list[i] == d_list[i-1]:
        num += 1

print num, timer() - end