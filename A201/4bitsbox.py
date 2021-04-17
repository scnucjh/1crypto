import crypta

def show_sbox_propety(sboxname, S:list):
    print('|%s' % (sboxname),end='\t')
    print('|%d' % (crypta.diffa.Diff(S)), end='\t')
    print('|%d' % (crypta.lina.Lin(S)), end='\t')
    print('|')
    

show_sbox_propety('Skinny4', crypta.sbox.Skinny4)
show_sbox_propety('Piccolo', crypta.sbox.Piccolo)

    
