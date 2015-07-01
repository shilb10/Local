from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as pt

f = open('p102_triangles.txt', 'r')
coord_list = [lines.split(',') for lines in f]

def f(x1, y1, x2, y2):
    if x2 == x1:
        if 0 < x1:
            return [-1, 2] 
        else:
            return [1, 2]
    m = (y2-y1)/(x2-x1)
    if y1 > m*x1:
        if m != 0:
            return [-1, m/abs(m)]
        else:
            return [-1, 0]
    else:
        if m != 0:
            return [1, m/abs(m)]
        else:
            return [1, 0]

def norm(coord):
    return (coord[0]**2 + coord[1]**2)**.5

def dp(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1]

def angle(vec1, vec2):
    return np.arccos(dp(vec1, vec2)/(norm(vec1)*norm(vec2)))

num = 0
for coord in coord_list:
    vec1 = [int(coord[0]), int(coord[1])]
    vec2 = [int(coord[2]), int(coord[3])]
    vec3 = [int(coord[4]), int(coord[5])]
    t1 = angle(vec1, vec2)
    t2 = angle(vec1, vec3)
    t3 = angle(vec2, vec3)
    if abs(t1 + t2 + t3 - 2*np.pi)/(2*np.pi) <= .000001 :
        num += 1

print num
