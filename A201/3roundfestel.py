from sage.all_cmdline import *   # import sage library
from sage.crypto.sbox import SBox
from sage.crypto.sbox import feistel_construction
import crypta

S = crypta.sbox.LDC
S = SBox(S)
print( feistel_construction(S,S,S,S) )