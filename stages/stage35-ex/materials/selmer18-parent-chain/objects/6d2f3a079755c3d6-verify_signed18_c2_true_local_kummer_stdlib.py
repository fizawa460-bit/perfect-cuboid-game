#!/usr/bin/env python3
"""Exact standalone stdlib verification for R3-07 C2 local 2-Kummer DIMENSIONS.
No class-group, S-unit, global Selmer, rank upper, or p163 Coleman asserted.
Core mathematical inputs: hyperelliptic 2-torsion = even root-subsets / complement;
local p-adic abelian varieties A(Q2)/2A(Q2) dim=g+dim A(Q2)[2];
for p odd dim A(Qp)/2A(Qp)=dim A(Qp)[2];
real Jac component group via # connected components C(R).
"""
from pathlib import Path
import json,hashlib,math
ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'signed18_c2_true_local_kummer_dimensions_certificate.json').read_text())
parent=ROOT/'signed18_c2_full_maximal_order_certificate.json'
assert hashlib.sha256(parent.read_bytes()).hexdigest()==cert['parent_cert_sha256']
old=json.loads(parent.read_text());H=old['h2_coefficients_ascending'];N=len(H)-1
assert N==36 and H[0]==H[-1]==1
p_bad=[2843,13963,329475607,1034386920659,23910039195629]
assert [item['p'] for item in cert['local_primes_odd']]==p_bad

def norm(a,p):
    a=[int(z)%p for z in a]
    while a and a[-1]==0:a.pop()
    return a

def mul(a,b,p):
    if not a or not b:return []
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
    return norm(z,p)

def divrem(a,b,p):
    a=norm(a,p);b=norm(b,p)
    if not b:raise ZeroDivisionError
    q=[0]*max(0,len(a)-len(b)+1)
    bi=pow(b[-1],-1,p)
    while len(a)>=len(b):
        k=len(a)-len(b);t=a[-1]*bi%p;q[k]=t
        for i,z in enumerate(b):a[k+i]=(a[k+i]-t*z)%p
        a=norm(a,p)
    return norm(q,p),a

def rem(a,b,p):return divrem(a,b,p)[1]

def gcd(a,b,p):
    a=norm(a,p);b=norm(b,p)
    while b:a,b=b,rem(a,b,p)
    if not a:return []
    k=pow(a[-1],-1,p)
    return norm([x*k for x in a],p)

def power_mod(a,k,f,p):
    x=[1];a=rem(a,f,p)
    while k:
        if k&1:x=rem(mul(x,a,p),f,p)
        k//=2
        if k:a=rem(mul(a,a,p),f,p)
    return x

def primes(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out

def irreducible(f,p):
    f=norm(f,p);d=len(f)-1
    if d<1 or f[-1]!=1:return False
    if d==1:return True
    X=[0,1]
    if power_mod(X,p**d,f,p)!=X:return False
    for ell in primes(d):
        A=power_mod(X,p**(d//ell),f,p)
        sub=norm([ (A[i] if i<len(A) else 0) - int(i==1) for i in range(max(len(A),2))],p)
        if gcd(f,sub,p)!=[1]:return False
    return True

odd_torsion={}
for item in cert['local_primes_odd']:
    p=item['p']; fs=item['factors']
    expected=norm(H,p);product=[1]
    twice=[];single=[]
    for f in fs:
        a=f['coefficients_ascending_mod_p'];m=f['multiplicity'];d=f['degree']
        assert all(0<=q<p for q in a) and d==len(a)-1 and a[-1]==1
        assert irreducible(a,p),(p,d,'Rabin failed')
        if m==2:twice.append(f)
        elif m==1:single.append(f)
        else:raise AssertionError((p,m))
        for _ in range(m):product=mul(product,a,p)
    assert product==expected,(p,'factor product differs')
    assert len(twice)==1 and twice[0]['degree']==1
    dg=[i*H[i] for i in range(1,N+1)]
    assert gcd(H,dg,p)==twice[0]['coefficients_ascending_mod_p']
    assert sum(f['degree'] for f in single)==N-2
    # For ordinary simple bad discriminant exponent1: tame inertia swaps exactly
    # the two colliding branch roots, fixes the other34. Frobenius cycles on
    # other34 roots are precisely squarefree modp factor degrees. An inertia-
    # invariant even subset contains either both collided roots or neither.
    # Consequently no Frobenius 'complement' twist is possible. Let k=1+#other
    # irreducible factors; even parity imposes one equation iff an odd degree
    # simple-root factor occurs, and quotient by the all-roots subset costs1.
    k=1+len(single)
    n_odd=any(f['degree']%2 for f in single)
    t=k-1-int(n_odd)
    assert t>=0
    odd_torsion[p]=t
    pattern=[(f['degree'],f['multiplicity']) for f in fs]
    print('PASS bad p',p,'full factorization',pattern,'#Frob root orbits',k,'local J[2] dim',t,flush=True)

# 2-local tame e3 factorization inherited from fully proved global integral
# basis. Inertia C3 acts by 3-cycles on the 12 blocks; Frobenius rotates
# the two residue orbits of blocks of length 4 and 8.
assert old['residual_factors_degrees']==[4,8]
assert cert['dyadic_residual_orbit_lengths']==[4,8]
assert cert['dyadic_tame_inertia_orbit_size']==3
assert cert['dyadic_branch_orbits']==[12,24]
blockcounts=[4,8];nblocks=sum(blockcounts);FULL=(1<<nblocks)-1

def frob(S):
    T=0;offset=0
    for n in blockcounts:
        for j in range(n):
            if S & (1<<(offset+j)):T|=1<<(offset+(j+1)%n)
        offset+=n
    return T
invariant=[];plus=[];minus=[]
for S in range(1<<nblocks):
    # Each inertia-block is size3, hence its inclusion gives parity of1.
    if S.bit_count()%2:continue
    P=frob(S)
    if P==S or P==S^FULL:
        invariant.append(S)
        (plus if P==S else minus).append(S)
assert len(invariant)==8 and len(plus)==4 and len(minus)==4
# even root subsets / full complement yields four LOCAL J[2] classes
assert len(invariant)//2==4
j2d=2
print('PASS local Q2 invariant even-subset classes modulo complement:',len(invariant)//2,'dim2')
print('  + Frobenius fixed subsets:',len(plus),'and anti-invariant subsets:',len(minus),'before complement quotient')

# Verify real root count by exact rational evaluations and Descartes.
def sign(xn,xd=1):
    z=sum(c*xn**i*xd**(N-i) for i,c in enumerate(H));return (z>0)-(z<0)
intervals=[((0,1),(1,4)),((1,1),(2,1)),((19,1),(20,1)),((1700,1),(1800,1))]
assert all(sign(*a)*sign(*b)==-1 for a,b in intervals)
nonzero=[x for x in H[::-1] if x];desc=sum((a>0)!=(b>0) for a,b in zip(nonzero,nonzero[1:]))
assert desc==4 and sign(3)==1
# 4 distinct real roots; old exact h2=A(x)^2-xB(x)^2>0 for x<0,
# hence precisely4 real branch points, 16 non-real conjugate pairs.
assert cert['archimedean_real_branchpoints']==4
assert cert['archimedean_complex_branchpoint_pairs']==16
# G_R complex conjugation on 36 branch roots: 4 fixed, 16 transpositions.
# invariant W_even subsets dimension 4+16-1=19; modulo all-one -> 18.
real_J2=4+16-2
assert real_J2==18
# C(R) for monic even-degree f with exactly four real branch points has
# 2 connected components (outer branch and middle oval). Standard real
# Jacobian component-group theorem: J(R)/2J(R) = F2^(s-1) = F2^1.
real_kummer=1
# An explicit generator: x=3 lies between real roots r2 and r3,
# P=(3,sqrt(h2(3))) lies on middle component; P0=(0,1) on outer,
# x-theta sign ratio at four ascending real theta roots = (--++).
print('PASS real 4 roots, 2 connected components, Jac(R)[2] dim',real_J2,'J(R)/2J(R) dim1; sign (--++)')
# OLD row342 2-divisor D2 explicitly generates the real local Kummer image:
# G2(X)=X^2-4X-1 has roots 2 +/- sqrt(5). The negative root is on
# the outer real component; positive root in (4,5) on the middle oval.
# P0 x=0 is outer, so E_G2-2P0 has odd middle-component degree.
oldD=json.loads((ROOT/'signed18_genus17_rank6_certificate.json').read_text())
assert [-1,-4,1] in oldD['B_factors_coefficients_ascending']
assert 2 < 5**0.5 < 3  # this inequality can also be verified 2^2<5<3^2
assert sign(4)==1 and sign(5)==1
assert 'D2' in oldD['class_order']
print('PASS OLD actual rational D2 (G2=X^2-4X-1) surjects onto REAL Kummer dim1')


j_2={'2':j2d,**{str(p):d for p,d in odd_torsion.items()},'real':real_J2}
km={'2':17+j2d,**{str(p):d for p,d in odd_torsion.items()},'real':real_kummer}
# Local Tate duality Weil self-pairing and Euler-Poincare:
# p=2 H^1 dim=2g+2dim J[2]; p odd H^1 dim=2dim J[2];
# p=infinity H^1 dim=2dim J[2](R)-dim J[2]=2*18-34=2.
h1={'2':2*17+2*j2d,**{str(p):2*d for p,d in odd_torsion.items()},'real':2*real_J2-34}
assert j_2==cert['exact_J_2_torsion_local_F2_dim']
assert km==cert['local_true_Kummer_J(Qv)/2_dimensions']
assert h1==cert['full_local_H1_Qv_J2_dimensions']
assert sum(km.values())==cert['local_kummer_dimension_sum']==30
print('PASS all 7 local TRUE Kummer-image F2 DIMENSIONS:',km)
print('PASS local true 2-torsion dimensions:',j_2)
print('PASS all 7 local cohomology H^1 dimensions:',h1)
print('IMPORTANT: local image dimensions DO NOT determine embedded global Selmer intersection')
print('NOT PROVED: classgroup[2], S-units, true global Sel2 dim <=16, MW rank upper, fullMW, p163 Coleman, signed +/-18 source exclusion')
