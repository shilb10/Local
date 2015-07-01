import string

f = open('p098_words.txt', 'r')
for line in f:
    words = line.split(',')
    words = [word[1:-1] for word in words]

word_dict = dict(zip(string.ascii_uppercase, range(26)))
anagram_dict = {}

def anagram(w):
    letter_count = [0]*26
    for l in w:
        letter_count[word_dict[l]] += 1
    letter_count = tuple(letter_count)
    if anagram_dict.has_key(letter_count):
        anagram_dict[letter_count].append(w)
        anagram_dict[letter_count][1] = 1
    else:
        anagram_dict[letter_count] = [len(w), 0, w]

def dig_sum(n):
    return sum([int(i) for i in str(n)])

def dig_len(n):
    return len(str(n))

def permutation(w1, w2):
    perm = []
    for l in w1:
        perm.append(w2.index(l))
    return perm

def satisfies_perm(n1, n2, perm):
    m1 = str(n1)
    m2 = str(n2)
    for i in xrange(len(m1)):
        if m2[perm[i]] != m1[i]:
            return False
    return True


for word in words:
    anagram(word)

anagram_keys = [k for k in anagram_dict.keys() if anagram_dict[k][1] == 1 and anagram_dict[k][0] == 6]
print anagram_dict[anagram_keys[4]]
# print anagram_keys[29]
print permutation(anagram_dict[anagram_keys[4]][-2], anagram_dict[anagram_keys[4]][-1])
# print anagram_dict[anagram_keys[29]]

nine_dig_squares = [i**2 for i in xrange(1000, 3163)]
num_ana = {}
def num_ana_gen(n):
    perm = [4, 2, 3, 0, 1, 5]
    m = str(n)
    dig_count = [0]*10
    for i in m:
        dig_count[int(i)] += 1
    dig_count = tuple(dig_count)
    if num_ana.has_key(dig_count) and sum([1 for l in m if int(l) == 1]) == 7:
        for m in num_ana[dig_count][1:]:
            if satisfies_perm(m, n, perm) or satisfies_perm(n, m, perm):
                num_ana[dig_count].append(n)
                num_ana[dig_count][0] = 1
    else:
        num_ana[dig_count] = [0, n]

for num in nine_dig_squares:
    num_ana_gen(num)

num_keys = [k for k in num_ana.keys() if num_ana[k][0] == 1]
print max([max(num_ana[k]) for k in num_keys])
for k in num_keys:
    print num_ana[k]

