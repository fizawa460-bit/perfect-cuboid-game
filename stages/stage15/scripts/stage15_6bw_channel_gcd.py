from math import gcd

def channel_gcds(m,n,r,s):
    return gcd(m*m+n*n,abs(r*r-s*s)), gcd(abs(m*m-n*n),r*r+s*s)

def check_divisibility(kS,kO,m,n,r,s):
    GS,GO=channel_gcds(m,n,r,s)
    return GS%kS==0 and GO%kO==0 and (GS*GO)%(kS*kO)==0
