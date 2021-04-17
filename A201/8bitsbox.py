import crypta

def show_sbox_propety(sboxname, S:list):
    print('|%s' % (sboxname),end='\t')
    print('|%d' % (crypta.diffa.Diff(S)), end='\t')
    print('|%d' % (crypta.lina.Lin(S)), end='\t')
    print('|')
    

show_sbox_propety('AES      ', crypta.sbox.AES)
show_sbox_propety('Skinny8  ', crypta.sbox.Skinny8)

    
