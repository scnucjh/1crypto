import crypta
Bit = crypta.Bit

def BS(A,B,C,D):
    a = ((~A)|B) & ((~A)|C|D) & (A|B|C|D) & (A|(~B)|(~C)|D) & (B|(~C)|(~D))
    b = ((~B)|C) & (A|B|(~C)) & (A|B|C|D) & ((~A)|C|(~D))
    c = ((~C)|D) & ((~B)|D)   & (B|C|(~D))
    d = (A|(~D)) & (A|B|(~C)) & ((~A)|C|D) & (A|(~B)|(~C)|D)
    return [a,b,c,d]

r2 = range(2)

for x3 in r2: 
    for x2 in r2: 
        for x1 in  r2:
            for x0 in r2:
                X0 = Bit(x0)
                X1 = Bit(x1)
                X2 = Bit(x2)
                X3 = Bit(x3)
                print(BS(X0,X1,X2,X3))
