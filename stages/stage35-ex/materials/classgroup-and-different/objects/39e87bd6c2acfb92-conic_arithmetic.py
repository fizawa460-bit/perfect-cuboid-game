from local_ring import LocalRing, Elt, evaluate, coefficients, bitmask, binary_poly
import local_ring as lr
from flint import nmod_poly

def span(vectors):
    b={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p not in b:b[p]=v;break
            v^=b[p]
    return b


def parity(v):return v.bit_count()&1


def trace(r,v):
    t=0
    for _ in range(r.degree):t^=v;v=r.fpow(v,2)
    assert t in (0,1)
    return t


def unit_basis(r):
    out=[r.one+r.pi_powers[i]*r.lift(1<<j)
         for i in (1,3,5) for j in range(r.degree)]
    t=next(1<<j for j in range(r.degree) if trace(r,1<<j))
    out.append(r.one+r.pi_powers[6]*r.lift(t))
    assert all(r.coordinate(v)==1<<i for i,v in enumerate(out))
    return out


def decode(r,code,basis=None):
    basis=basis or unit_basis(r)
    v=r.one
    for i,x in enumerate(basis):
        if code>>i&1:v*=x
    return v


def divide_pi(v,k):
    assert v.valuation()>=k
    r=v.ring
    parts=[None]*3
    for i,p in enumerate(v.parts):
        q,j=divmod(i-k,3)
        if q>=0:cs=[int(c)*(2**q) for c in p]
        else:
            assert all(int(c)%(2**(-q))==0 for c in p)
            cs=[int(c)//(2**(-q)) for c in p]
        parts[j]=nmod_poly(cs,lr.MODULUS)
    w=Elt(r,tuple(parts))
    assert w*r.pi_powers[k]==v
    return w


def pairing(rows,a,b):
    v=0
    while a:
        q=a&-a;a^=q;v^=rows[q.bit_length()-1]
    return parity(v&b)


def transform(x,frob,zeta,j):
    r=x.ring
    return sum((evaluate([int(c) for c in a],frob)*r.pi_powers[i]*(zeta**(i*j))
                for i,a in enumerate(x.parts)),r.zero)


def twist_root(w,frob,zeta,j):
    return transform(w,frob,zeta,j)*(zeta**(2*j))


def equation(r,hilbert,wi,wj,di,dj,labels):
    # theta_i=-1+pi^2*w_i; theta_j=-1+pi^2*w_j. pi^2 is square.
    beta=r.coordinate(wi-wj)
    aa=[a^b for a,b in zip(di,dj)]
    lin=sum((pairing(hilbert,a,beta)^pairing(hilbert,a,dj[k]))<<k for k,a in enumerate(aa))
    cross=[]
    for k in range(9):
        for l in range(k+1,9):
            if pairing(hilbert,aa[k],dj[l])^pairing(hilbert,aa[l],dj[k]):cross.append([k,l])
    return {'field_f':r.degree,'pair':labels,'linear':hex(lin),'cross':cross}


def test_eq(eq,m):
    return parity(int(eq['linear'],16)&m)^ (sum(((m>>k)&1)*((m>>l)&1) for k,l in eq['cross'])&1)

