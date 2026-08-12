def endpoints(x,y,p,q):
    return x*p-y*q, x*q+y*p, x*p+y*q, y*p-x*q

def check_norm_identity(x,y,p,q):
    e1,e2,e3,e4=endpoints(x,y,p,q)
    s2=(x*x+y*y)*(p*p+q*q)
    assert e1*e1+e2*e2==s2
    assert e3*e3+e4*e4==s2
    assert e3+e1==2*x*p
    assert e3-e1==2*y*q
    assert e2+e4==2*y*p
    assert e2-e4==2*x*q
    return s2
