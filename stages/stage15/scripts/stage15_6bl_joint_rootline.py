from math import gcd

def joint_index(q:int)->int:
    assert q>=1
    return q*q

def roots_ok(lam,mu,kS,kO):
    q=kS*kO
    assert gcd(kS,kO)==1
    if q==1:return True
    return ((lam*lam+1)%kS==0 if kS>1 else True) and ((mu*mu-1)%kS==0 if kS>1 else True) and ((lam*lam-1)%kO==0 if kO>1 else True) and ((mu*mu+1)%kO==0 if kO>1 else True)
