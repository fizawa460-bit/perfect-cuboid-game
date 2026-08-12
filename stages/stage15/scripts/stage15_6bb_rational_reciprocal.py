from fractions import Fraction


def reciprocal_parts(kf:int,kg:int,c:int,e:int,lam:int):
    plus=Fraction(2*kf*c,lam*e)
    minus=Fraction(2*kg*e,lam*c)
    return plus,minus

if __name__=='__main__':
    a,b=reciprocal_parts(1,3,2,5,1)
    assert a*b==12
    print('Stage15-6bb PASS')
