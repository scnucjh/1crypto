import numpy
import math
import sbox

def one_count(t):
    res = 0
    while t>0:
        res += t%2
        t//=2
    return res

def int2b(a,len):
    res = []
    for i in range(len):
        res.append(a%2)
        a//=2
    return res

def b2int(a):
    res = 0
    for i in range(len(a)):
        if a[i]==1:
            res += 2**i
    return res


def zeros(n,m):
    res = []
    for i in range(n):
        res.append([0]*m)
    return res

