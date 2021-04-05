class Bit :
    a = 0
    def __init__(self, a) -> None:
        assert 0<= a <= 1
        self.a = a
    
    def __or__(self, other):
        # print('or')
        if self.a==1 or other.a==1:
            return Bit(1)
        return Bit(0)

    def __and__(self, other):
        # print('and')
        if self.a==1 and other.a==1:
            return Bit(1)
        return Bit(0)

    def __xor__(self, other):
        # print('xor')
        if self.a != other.a:
            return Bit(1)
        return Bit(0)

    def __str__(self):
        return str(self.a)
    
    def __invert__(self):
        # print('not')
        if self.a==1:
            return Bit(0)
        return Bit(1)
    def __repr__(self):
        return self.__str__()
