import numpy

def get_lat(S):
    n = len(S)
    lat = numpy.zeros((n,n))
    for inputmask in range(n):
        for outputmask in range(n):
            lat[inputmask][outputmask] = - n//2
            for i in range(n):
                if ( one_count(i) + one_count(S[i]) ) % 2 == 0:
                    lat[inputmask][outputmask] += 1

def maxv_in_lat(Sbox):
    lat = get_lat(Sbox)
    res = 0
    n = len(Sbox)
    for i in range(1,n):
        for j in range(1,n):
            res = max(res, abs(lat[i][j]))
    return res


