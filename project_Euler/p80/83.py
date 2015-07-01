from __future__ import division

f = open('p083_matrix.txt', 'r')
A = []
for line in f:
    l = line.split(',')
    A.append([int(s) for s in l])

n = len(A)
G = {}
for l in xrange(n):
    for i in xrange(n):
        if i == 0:
            if l == 0:
                G[(l, i)] = [(l+1,i), (l, i+1)]
            elif l == n-1:
                G[(l, i)] = [(l-1,i), (l,i+1)]
            else:
                G[(l, i)] = [(l-1,i), (l+1,i), (l,i+1)]
        elif i == n-1:
            if l == 0:
                G[(l, i)] = [(l,i-1), (l+1,i)]
            elif l == n-1:
                G[(l, i)] = [(l-1,i), (l,i-1)]
            else:
                G[(l, i)] = [(l-1,i), (l+1,i), (l,i-1)]
        elif l == 0:
            G[(l, i)] = [(l,i-1), (l+1,i), (l,i+1)]
        elif l == n-1:
            G[(l, i)] = [(l,i-1), (l-1,i), (l,i+1)]
        else:
            G[(l, i)] = [(l-1,i), (l+1,i), (l,i-1), (l,i+1)]

dist_dict = {}
def min_dist(Q):
    m_vert = None
    cur_min = 10**9
    for elem in Q:
        if dist_dict[elem] < cur_min:
            m_vert = elem
            cur_min = dist_dict[elem]
    return m_vert

def dijkstra(s, t):
    Q = set([])
    dist_dict[s] = A[s[0]][s[1]]
    Q.add(s)
    for l in xrange(n):
        for i in xrange(n):
            if i == 0 and l == 0:
                Q.add((l, i))
            else:
                dist_dict[(l, i)] = 10**9
                Q.add((l, i))

    while len(Q) > 0:
        u = min_dist(Q)
        if u == t:
            return dist_dict[t]
        Q.discard(u)
        for elem in G[u]:
            alt = dist_dict[u] + A[elem[0]][elem[1]]
            if alt < dist_dict[elem]:
                dist_dict[elem] = alt

print dijkstra((0,0), (79,79))