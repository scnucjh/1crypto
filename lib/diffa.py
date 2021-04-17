import numpy
from crypto_tool import *

def get_ddt(S):
    n = len(S)
    ddt = numpy.zeros((n,n))
    for i in range(n):
        for j in range(n):
            ddt[i^j][S[i]^S[j]] += 1
    return ddt


def maxv_in_ddt(Sbox):
    ddt = get_ddt(Sbox)
    n = len(Sbox)
    res = -1
    for i in range(1,n):
        for j in range(1,n):
            res = max(res, ddt[i][j])
    return res

def Diff(Sbox):
    '''
    Diff(S) := Differential uniformity
    '''
    return maxv_in_ddt(Sbox)

