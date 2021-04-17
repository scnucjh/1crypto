from sage.all_cmdline import *   # import sage library
from sage.crypto.sbox import SBox
import crypta

def show_sbox_propety(S, table=False):
    S = SBox(S)
    
    if table: print('difference_distribution_table ', S.difference_distribution_table())
    print('differential_branch_number ',S.differential_branch_number())
    print('differential_uniformity ' ,S.differential_uniformity())
    print('maximal_difference_probability_absolute ', S.maximal_difference_probability_absolute())
    
    if table: print('linear_approximation_table ', S.linear_approximation_table())
    print('linear_branch_number ',S.linear_branch_number())
    print('linearity ', S.linearity())
    print('nonlinearity ', S.nonlinearity())
    
    print('max_degree ', S.max_degree())
    print('min_degree ', S.min_degree())
        
show_sbox_propety(crypta.sbox.dxf01)
print()
show_sbox_propety(crypta.sbox.AES)

