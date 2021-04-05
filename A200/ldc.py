import crypta
S = crypta.sbox.LDC


print('DDT')
print( crypta.diffa.get_ddt(S) )
print('\n\nLAT')
print( crypta.lina.get_lat(S) )
