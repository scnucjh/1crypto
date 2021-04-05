import crypta

def show_sbox_propety(sboxname, S:list):
    print('|%s' % (sboxname),end='\t')
    print('|%d' % (crypta.diffa.maxv_in_ddt(S)), end='\t')
    print(crypta.lina.get_lat(S))
    # print('|%d' % (crypta.lina.maxv_in_lat(S)), end='\t')
    
    print('|')
    

show_sbox_propety('Skinny4', crypta.sbox.Skinny4)
print(crypta.sbox.Piccolo)
show_sbox_propety('Piccolo', crypta.sbox.Piccolo)

    