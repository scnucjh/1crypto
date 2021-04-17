from crypto_tool import *
def get_all_set(n):
    res = []
    for i in range(2**n):
        t = [0]*n
        x = i
        for j in range(n):
            t[j] = x % 2
            x //= 2
        res.append(t)
    return res

def get_sbox_from_bs(bs, n):
    S = [0] * (2**n)
    for i in range(2**n):
        x = int2b(i, n)
        y = bs(x)
        S[i] = b2int(y)
    return S

def test() :
    def bs(x):
        x[0] ^= x[2] & x[3]
        x[1] ^= x[0] & x[2]
        x[2] ^= x[1] & x[3]
        x[3] ^= x[0] & x[1]
        return x
    S = get_sbox_from_bs(bs, 4) 
