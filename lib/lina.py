import numpy
from crypto_tool import *
import math


def get_lat(S):
    n = len(S)
    lat = numpy.zeros((n,n))
    for inputmask in range(n):
        for outputmask in range(n):
            lat[inputmask][outputmask] = - n//2
            for i in range(n):
                if ( one_count(i&inputmask) + one_count(S[i]&outputmask) ) % 2 == 0:
                    lat[inputmask][outputmask] += 1
    return lat

def maxv_in_lat(Sbox):
    lat = get_lat(Sbox)
    res = 0
    n = len(Sbox)
    for i in range(1,n):
        for j in range(1,n):
            res = max(res, abs(lat[i][j]))
    return res


def Lin(Sbox):
    return 2 * maxv_in_lat(Sbox)