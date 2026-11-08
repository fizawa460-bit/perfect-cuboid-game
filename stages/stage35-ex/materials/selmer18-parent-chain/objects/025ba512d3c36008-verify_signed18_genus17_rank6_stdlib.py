#!/usr/bin/env python3
"""Standalone Python-stdlib exact replay of conditional class-theoretic proof:
  rank Jac(C2)(Q) >= 6 for the OLD fixed signed +/-18 genus17 C2.
Verifies polynomial identities, finite-field factorization, character bits by TWO
independent methods (extension-field exponent and determinant of multiplication),
rational divisor inputs, F2 rank6, no rational 2-torsion via p19.
The final mathematical implication uses standard even-degree hyperelliptic
x-theta 2-Kummer NECESSITY; it proves NO original signed source exclusion,
rank upper, full-MW generating set, or p163 Coleman annihilator.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parent
oldbytes=(ROOT/'signed18_genus17_rank2_certificate.json').read_bytes()
r3bytes=(ROOT/'signed18_genus17_rank3_certificate.json').read_bytes()
old=json.loads(oldbytes)
old3=json.loads(r3bytes)
new=json.loads((ROOT/'signed18_genus17_rank6_certificate.json').read_bytes())
assert hashlib.sha256(oldbytes).hexdigest()==new['old_rank2_sha256']
assert hashlib.sha256(r3bytes).hexdigest()==new['old_rank3_sha256']
H=old['curves'][1]['h_coefficients_ascending']
A=old3['A_coefficients_ascending'];B=old3['B_coefficients_ascending']
assert (H,A,B)==tuple(new[k] for k in ('h2_coefficients_ascending','A_coefficients_ascending','B_coefficients_ascending'))


def intmul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):z[i+j]+=c*d
    return z

def intadd(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def intscale(a,c):return [int(t)*c for t in a]

def trim(a,p):
    a=[int(x)%p for x in a]
    while a and a[-1]==0:a.pop()
    return a

def mul(a,b,p):
    if not a or not b:return []
    res=[0]*(len(a)+len(b)-1)
    for i,t in enumerate(a):
        for j,u in enumerate(b):res[i+j]=(res[i+j]+t*u)%p
    return trim(res,p)

def divrem(a,b,p):
    a=trim(a,p);b=trim(b,p)
    if not b:raise ZeroDivisionError()
    q=[0]*max(0,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        j=len(a)-len(b)
        c=a[-1]*inv%p;q[j]=c
        for i,t in enumerate(b):a[i+j]=(a[i+j]-c*t)%p
        a=trim(a,p)
    return trim(q,p),a

def remainder(a,f,p):return divrem(a,f,p)[1]

def mulrem(a,b,f,p):return remainder(mul(a,b,p),f,p)

def powrem(a,n,f,p):
    v=[1];a=remainder(a,f,p)
    while n:
        if n&1:v=mulrem(v,a,f,p)
        n//=2
        if n:a=mulrem(a,a,f,p)
    return v

def gcdpoly(a,b,p):
    a=trim(a,p);b=trim(b,p)
    while b:a,b=b,remainder(a,b,p)
    return trim([c*pow(a[-1],-1,p)%p for c in a],p) if a else []

def sub(a,b,p):return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))],p)

def prime_divisors(n):
    out=[];k=2
    while k*k<=n:
        if n%k==0:
            out.append(k)
            while n%k==0:n//=k
        k+=1
    if n>1:out.append(n)
    return out

def irreducible_monic(f,p):
    f=trim(f,p)
    if len(f)<=1 or f[-1]!=1:return False
    d=len(f)-1; X=[0,1]
    if d==1:return True
    if powrem(X,p**d,f,p)!=X:return False
    for ell in prime_divisors(d):
        if len(gcdpoly(f,sub(powrem(X,p**(d//ell),f,p),X,p),p))>1:return False
    return True

# Independent character method 1: directly exponentiate in F_(p^d)
# (Euler's criterion).  Method 2: determinant of multiplication-by-g matrix,
# then Legendre symbol of Norm in F_p.  These methods cannot share the
# common spurious resultant bug seen in a discarded exploratory CAS check.
def chi_pow(g,f,p):
    d=len(f)-1
    z=powrem(g,(p**d-1)//2,f,p)
    if z==[1]:return 0
    if z==[p-1]:return 1
    raise AssertionError(('NOT_UNIT_OR_INCORRECT_FINITE_FIELD',p,d,g,z))

def det_mod(A,p):
    a=[[int(x)%p for x in row] for row in A]
    n=len(a)
    det=1
    for k in range(n):
        j=next((i for i in range(k,n) if a[i][k]),None)
        if j is None:return 0
        if j!=k:a[k],a[j]=a[j],a[k];det=(-det)%p
        piv=a[k][k];det=det*piv%p
        inv=pow(piv,-1,p)
        for i in range(k+1,n):
            if a[i][k]:
                t=a[i][k]*inv%p
                for j in range(k+1,n):a[i][j]=(a[i][j]-t*a[k][j])%p
                a[i][k]=0
    return det

def norm_det(g,f,p):
    d=len(f)-1
    col=remainder(g,f,p)
    matrix=[[0]*d for _ in range(d)]
    for j in range(d):
        for i,c in enumerate(col):matrix[i][j]=c
        x=[0]+col
        col=remainder(x,f,p)
    return det_mod(matrix,p)

def chi_norm(g,f,p):
    det=norm_det(g,f,p)
    if det==0:raise AssertionError(('NORM_ZERO',p,g))
    v=pow(det,(p-1)//2,p)
    assert v in (1,p-1)
    return int(v==p-1)

def homoeval(a,u,v):
    d=len(a)-1
    return sum(c*u**j*v**(d-j) for j,c in enumerate(a))

# Preserve old exact curve model, original h2 = A² - X B².
assert len(H)==37 and H[0]==H[-1]==1
assert len(A)==19 and A[-1]==1 and A[0]==1
assert len(B)==18 and B[-1]==-36 and B[0]==4
AA=intmul(A,A)
XBB=[0]+intmul(B,B)
assert [AA[i] - (XBB[i] if i<len(XBB) else 0) for i in range(37)] == H
assert homoeval(A,-1,1)==2**18 and homoeval(B,-1,1)==0
assert homoeval(A,-1,3)==2**24 and homoeval(B,-1,3)==0
assert H[0]==1
print('PASS full ZZ identity: h2=A²-X B²; P0,Q_A,Q_B are actual rational curve points.')

BF=new['B_factors_coefficients_ascending']
assert len(BF)==5 and [len(g)-1 for g in BF]==[1,1,2,4,9]
BBprod=[1]
for g in BF:BBprod=intmul(BBprod,g)
assert intscale(BBprod,-4)==B
assert B[0]!=0
# mod163 squarefreeness and coprimality ensure the rational E_j are disjoint,
# separable, not branch points, not P0; this uses the OLD p163 source prime.
assert gcdpoly(B,[j*B[j] for j in range(1,len(B))],163)==[1]
assert gcdpoly(B,A,163)==[1]
print('PASS full ZZ B=-4*G1a*G1b*G2*G4*G9, rational E_j off branch and basepoint.')

G2=new['intersection_quadratic_coefficients_ascending']
G16=new['intersection_degree16_coefficients_ascending']
assert G2==[1,6,1] and len(G16)==17
K=intadd(intscale(A,2),intmul([1,1],B))
assert K==intscale(intmul(G2,G16),-2)
T=intadd(A,B)
TT=intmul(T,T)
assert [TT[i]-H[i] for i in range(36)]==intmul(B,K) and TT[36]==H[36]
assert gcdpoly(G2,[j*G2[j] for j in range(1,len(G2))],29)==[1]
assert gcdpoly(G2,B,29)==[1]
assert gcdpoly(G2,H,29)==[1]
print('PASS full ZZ (A+B)²-h2=B*(2A+(X+1)B)=-2*B*G2*G16.')
print('PASS rational degree2 F2 selected by (X,Y)=(alpha,A(alpha)+B(alpha)), G2(alpha)=0.')

class_order=new['class_order']; assert class_order==['D1a','D1b','D2','D4','D9','F2']
class_G=new['class_G_coefficients_ascending'];assert class_G==BF+[G2]
class_degrees=new['class_degree_basepoint'];assert class_degrees==[1,1,2,4,9,2]
char_data={}
for pdata in new['primes']:
    p=pdata['p']
    factors=pdata['factors_ascending_centered']
    degree=[len(f)-1 for f in factors]
    assert degree==pdata['degrees']
    assert all(irreducible_monic(f,p) for f in factors),p
    prod=[1]
    for f in factors:prod=mul(prod,f,p)
    assert prod==trim(H,p),(p,'factorization invalid')
    assert gcdpoly(H,[j*H[j] for j in range(1,len(H))],p)==[1]
    # Local image in product F_(p^d) square-class groups.
    scalar=[d%2 for d in degree]
    theta=[chi_pow([0,1],f,p) for f in factors]
    assert theta==[chi_norm([0,1],f,p) for f in factors]
    assert theta==[0]*len(factors),'theta local square is essential for rank6 matrix'
    chars=[];project=[]
    for name,g,base_d in zip(class_order,class_G,class_degrees):
        row=[]
        for f in factors:
            a=chi_pow(g,f,p)
            b=chi_norm(g,f,p)
            assert a==b,(p,name,len(f)-1,a,b)
            row.append(a ^ (base_d%2)*theta[len(row)])
        chars.append(row)
        if any(scalar):
            k=scalar.index(1)
            proj=[row[j]^(row[k]*scalar[j]) for j in range(len(scalar)) if j!=k]
        else:proj=row[:]
        project.append(proj)
    char_data[p]={'raw':chars,'quotient':project,'scalar':scalar,'degrees':degree}
    print('PASS p=',p, 'factor degrees=',degree,'theta local square=',theta,'scalar=',scalar)
    for name,r,pr in zip(class_order,chars,project):
        print(' ',name,'raw=',''.join(map(str,r)),'mod-Q*=',''.join(map(str,pr)))

expected=new['expected_character_bits']
for i,r in enumerate(char_data[3]['raw']):assert ''.join(map(str,r))==expected['p3'][i]
for i,r in enumerate(char_data[29]['raw']):assert ''.join(map(str,r))==expected['p29_raw'][i]
for i,r in enumerate(char_data[29]['quotient']):assert ''.join(map(str,r))==expected['p29_quotient'][i]
assert ''.join(map(str,char_data[29]['scalar']))==expected['p29_scalar_parity']

def rank_f2(rows):
    echelon=[]
    for row in rows:
        v=sum(int(z)<<j for j,z in enumerate(row))
        for b in echelon:v=min(v,v^b)
        if v:echelon.append(v);echelon.sort(reverse=True)
    return len(echelon)

combined=[[int(z) for z in char_data[3]['quotient'][i]+char_data[29]['quotient'][i]] for i in range(6)]
assert all(len(row)==9 for row in combined)
assert rank_f2(combined)==expected['combined_rank']==6
print('PASS six-by-nine mod2 matrix rank=6 using ONLY p3 and p29 local 2-Kummer necessary directions.')

# Good p19, rational 2-torsion =0: 36 hyperelliptic Weierstrass roots
# split into two F19-Frobenius odd-length cycles 17 and19; their union is
# the only nonempty even Frobenius-stable subset (mod complement), and an
# anti-invariant representative is impossible for an odd permutation order.
for pold in old['curves'][1]['primes']:
    if pold['p']==19:
        assert pold['degree_sequence']==[17,19]
        factors=pold['factors_ascending']
        assert all(irreducible_monic(f,19) for f in factors)
        fprod=[1]
        for f in factors:fprod=mul(fprod,f,19)
        assert fprod==trim(H,19)
        assert gcdpoly(H,[i*H[i] for i in range(1,len(H))],19)==[1]
        break
else:raise AssertionError('p19 cert missing')
print('PASS q19 good two odd [17,19] Frobenius orbits => Jac(C2)(Q)[2]=0.')

# Classical theorem used only in necessary direction: for even-degree
# hyperelliptic Jac(Q), delta(2D)=1 in L*/L*²Q*; for finite effective
# rational divisor at roots of G, delta(E-deg(G)*P0)=[G(theta)/theta^degG]
# up to a rational scalar.  Local Norm chars at p3/p29 are compatible
# since h2 is squarefree and each G(theta) is a unit.
print('NEW_SCOPED_THEOREM: rank Jac(C2)(Q)>=6 (from six independent Jac(Q)/2 classes, J(Q)[2]=0).')
print('CONSISTENCY: theta=(A(theta)/B(theta))^2 in L, so old row341 delta(S)=[1/B(theta)] remains globally valid.')
print('NOT_PROVED: rank upper<=16, fullMW finite-index generators, p163 genuine annihilator a0 unit,')
print('NOT_PROVED: any original signed +18/-18 source exclusion; Branch B/R3-07 OPEN; formal R0 C35-200 unchanged.')
print('SHA256_RANK6_CERT='+hashlib.sha256((ROOT/'signed18_genus17_rank6_certificate.json').read_bytes()).hexdigest())
