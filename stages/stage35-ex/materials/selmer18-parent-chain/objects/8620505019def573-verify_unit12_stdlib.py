#!/usr/bin/env python3
"""Independent exact Python-stdlib audit of 12 explicitly constructed units in
K=Q(theta), deg(h2)=36, and their GF(2) independence at p=61,167.
This DOES NOT compute Cl(K)[2], Cl_S[2], full S-units, true Selmer, MW upper or Coleman.
"""
import json,hashlib,math
from pathlib import Path
from fractions import Fraction
BASE=Path(__file__).resolve().parent
C=json.loads((BASE/'unit12_certificate.json').read_text())
for name,dig in C['parent_sha256'].items():
    a=(BASE/name).read_bytes()
    assert hashlib.sha256(a).hexdigest()==dig,('BAD_PARENT_SHA',name)
R=json.loads((BASE/'signed18_genus17_rank6_certificate.json').read_text())
O=json.loads((BASE/'signed18_c2_full_maximal_order_certificate.json').read_text())
h=C['h2_coefficients_ascending'];A=R['A_coefficients_ascending'];B=R['B_coefficients_ascending']
assert h==R['h2_coefficients_ascending']==O['h2_coefficients_ascending']
assert len(h)==37 and h[-1]==1 and h[0]==1
assert O['slope']=='-1/3' and O['global_maximal_order_established'] is True
assert O['number_field_signature']==[4,16] and O['unit_rank']==19

def poly_add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def poly_sub(a,b):return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def poly_mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def trZ(a):
    z=list(a)
    while z and z[-1]==0:z.pop()
    return z

def rem_Q(a,b):
    a=[Fraction(t) for t in a];b=[Fraction(t) for t in b]
    while a and a[-1]==0:a.pop()
    while b and b[-1]==0:b.pop()
    assert b
    while len(a)>=len(b):
        c=a[-1]/b[-1];j=len(a)-len(b)
        for i,t in enumerate(b):a[i+j]-=c*t
        while a and a[-1]==0:a.pop()
    return a

def res_bareiss(f,g):
    m=len(f)-1;n=len(g)-1;N=m+n
    if n==0:return g[0]**m
    a=[[0]*N for _ in range(N)]
    for i in range(n):a[i][i:i+m+1]=list(reversed(f))
    for i in range(m):a[n+i][i:i+n+1]=list(reversed(g))
    sign=1;prev=1
    for k in range(N-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,N) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        piv=a[k][k]
        for i in range(k+1,N):
            t=a[i][k]
            for j in range(k+1,N):
                num=a[i][j]*piv-t*a[k][j]
                assert num%prev==0,('BAREISS_NONEXACT',k,i,j)
                a[i][j]=num//prev
            a[i][k]=0
        prev=piv
    return sign*a[-1][-1]

# Old fixed curve exactly reproduced as a square-minus-X-square.
assert poly_sub(poly_mul(A,A),[0]+poly_mul(B,B))==h
print('PASS same fixed genus17 h2(X)=A(X)^2-XB(X)^2 and SHA-locked order')

# q(2u-3) integer coefficients; omega_j=u^j/2^floor(j/3) is globally integral.
def q_of_2u_minus3(q):
    coeff=[0]*len(q)
    for i,v in enumerate(q):
        for j in range(i+1):
            coeff[j]+=v*math.comb(i,j)*2**j*(-3)**(i-j)
    return coeff

qtheta_minus1=[-1,1];q3theta_plus1=[1,3];qK2=[1,6,1]
assert res_bareiss(h,qtheta_minus1)==-2**48
assert res_bareiss(h,q3theta_plus1)==2**48
assert res_bareiss(h,qK2)==2**96
assert res_bareiss(h,[1,1])==2**36
assert C['unit_definitions'][0]['name']=='epsilon'
assert C['unit_definitions'][1]['name']=='eta'
assert C['unit_definitions'][2]['name']=='sigma'
assert all(z['norm'] in (-1,1) for z in C['unit_definitions'])
# epsilon=((theta-1)^3)/16=((u-2)^3)/2=omega3-3omega2+6omega1-4omega0
assert C['unit_definitions'][0]['norm']==-1
assert (-2**48)**3 == -(16**36)
# eta=(3theta+1)/(theta-1): Q2 valuations 4/3 in both numerator/denominator.
# sigma=(theta^2+6theta+1)/(theta-1)^2: Q2 valuations 8/3 in both.
# Their numerator and denominator absolute field norms are powers of 2,
# so no odd-prime valuations; thus they and inverses are everywhere integral.
assert C['unit_definitions'][1]['norm']==-1
assert C['unit_definitions'][2]['norm']==1
assert res_bareiss(h,q3theta_plus1)//res_bareiss(h,qtheta_minus1)==-1
assert res_bareiss(h,qK2)==res_bareiss(h,qtheta_minus1)**2
print('PASS epsilon, eta, sigma are true global algebraic-integer UNITS of norms -1,-1,+1')

for un in C['unit_definitions'][3:]:
    assert un['kind']=='polynomial'
    q=un['q'];k=un['two_power']
    assert isinstance(k,int) and k>0
    source={'A':A,'B':B,'A+B':poly_add(A,B),'A+xB':poly_add(A,[0]+B)}[un['factor_of']]
    assert rem_Q(source,q)==[],('NOT_FACTOR',un['name'])
    cu=q_of_2u_minus3(q)
    coeff=[]
    for j,c in enumerate(cu):
        z=c*2**(j//3)
        assert z%2**k==0,('NOT_IN_OLD_INTEGER_BASIS',un['name'],j,z,2**k)
        coeff.append(z//2**k)
    norm=res_bareiss(h,q)
    assert norm==un['norm']*2**(36*k),('BAD_NORM',un['name'],norm)
    print('PASS',un['name'],'global integer-unit, norm',un['norm'],
           'basis length',len(coeff),'largest abs basis coeff',max(map(abs,coeff)))

# Finite-field modular polynomial tools (ascending coefficient convention).
def trim(a,p):
    v=[int(z)%p for z in a]
    while v and v[-1]==0:v.pop()
    return v

def mul(a,b,p):
    if not a or not b:return []
    out=[0]*(len(a)+len(b)-1)
    for i,t in enumerate(a):
        for j,v in enumerate(b):out[i+j]=(out[i+j]+t*v)%p
    return trim(out,p)

def divrem(a,b,p):
    a=trim(a,p);b=trim(b,p);assert b
    q=[0]*max(0,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        j=len(a)-len(b);v=a[-1]*inv%p;q[j]=v
        for i,t in enumerate(b):a[j+i]=(a[j+i]-v*t)%p
        a=trim(a,p)
    return trim(q,p),a

def rem(a,f,p):return divrem(a,f,p)[1]
def sub(a,b,p):return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))],p)
def powrem(a,n,f,p):
    out=[1];a=rem(a,f,p)
    while n:
        if n&1:out=rem(mul(out,a,p),f,p)
        a=rem(mul(a,a,p),f,p);n//=2
    return out

def gcd(a,b,p):
    a=trim(a,p);b=trim(b,p)
    while b:a,b=b,rem(a,b,p)
    return [z*pow(a[-1],-1,p)%p for z in a] if a else []

def irreducible(f,p):
    f=trim(f,p); assert f and f[-1]==1
    d=len(f)-1
    if d==1:return True
    X=[0,1]
    if powrem(X,p**d,f,p)!=X:return False
    nn=d;divs=[];i=2
    while i*i<=nn:
        if nn%i==0:
            divs.append(i)
            while nn%i==0:nn//=i
        i+=1
    if nn>1:divs.append(nn)
    return all(gcd(f,sub(powrem(X,p**(d//q),f,p),X,p),p)==[1] for q in divs)

def det_mod(M,p):
    a=[[v%p for v in row] for row in M];n=len(a);det=1
    for k in range(n):
        j=next((j for j in range(k,n) if a[j][k]!=0),None)
        if j is None:return 0
        if j!=k:a[j],a[k]=a[k],a[j];det=-det
        pivot=a[k][k];det=det*pivot%p;iv=pow(pivot,-1,p)
        for i in range(k+1,n):
            factor=a[i][k]*iv%p
            if factor:
                for t in range(k+1,n):a[i][t]=(a[i][t]-factor*a[k][t])%p
                a[i][k]=0
    return det%p

def chi_pow(g,f,p):
    d=len(f)-1;v=powrem(g,(p**d-1)//2,f,p)
    if v==[1]:return 0
    if v==[p-1]:return 1
    raise AssertionError(('NOT_UNIT_OR_BAD_FIELD',p,d,g))

def chi_norm(g,f,p):
    d=len(f)-1;col=rem(g,f,p)
    columns=[]
    for j in range(d):
        columns.append(col)
        col=rem([0]+col,f,p)
    M=[[columns[j][i] if i<len(columns[j]) else 0 for j in range(d)] for i in range(d)]
    de=det_mod(M,p)
    assert de!=0,('NORM_ZERO',p,d,g)
    leg=pow(de,(p-1)//2,p)
    assert leg in (1,p-1)
    return int(leg==p-1)

all_fs=[]
for pair in C['finite_square_tests']:
    p=pair['p'];fs=pair['factors_ascending_modp'];degrees=pair['degrees']
    assert p in (61,167)
    assert [len(f)-1 for f in fs]==degrees and sum(degrees)==36
    prod=[1]
    for f in fs:
        assert f[-1]==1 and irreducible(f,p),('FACTOR_NOT_IRREDUCIBLE',p,f)
        prod=mul(prod,f,p)
    assert prod==trim(h,p),('FACTOR_PRODUCT_MISMATCH',p)
    assert gcd(h,[j*h[j] for j in range(1,len(h))],p)==[1]
    all_fs.extend((p,f) for f in fs)
    print('PASS p',p,'Rabin irreducible factor list',degrees,'full product and squarefree')
assert len(all_fs)==14

# The local squareclass is computed TWICE: finite-extension Euler criterion and
# an independent multiplication-matrix Norm determinant + Legendre symbol.
rows=[];names=['minus_one']+[d['name'] for d in C['unit_definitions']]
for name in names:
    if name=='minus_one':
        numerator=[-1];k=0
    else:
        un=next(z for z in C['unit_definitions'] if z['name']==name)
        if un['kind']=='polynomial':
            numerator=un['q'];k=un['two_power']
        else:
            numerator=un['charpoly'];k=0
    row=[]
    for p,f in all_fs:
        q=[int(z)*pow(2,-k%2,p)%p for z in numerator]
        a=chi_pow(q,f,p)
        b=chi_norm(q,f,p)
        assert a==b,(name,p,len(f)-1,a,b)
        row.append(a)
    rows.append(row)
expected=C['expected_bit_matrix']
assert [z['name'] for z in expected]==names
assert [z['bits'] for z in expected]==rows,('CHARACTER_MISMATCH',names,rows)

def gf2rank(rows):
    piv={}
    for row in rows:
        x=sum(int(v)<<i for i,v in enumerate(row))
        while x:
            j=x.bit_length()-1
            if j in piv:x^=piv[j]
            else:piv[j]=x;break
    return len(piv)

assert len(rows)==13 and all(len(r)==14 for r in rows)
rank=gf2rank(rows)
assert rank==C['expected_GF2_rank']==13
assert gf2rank([r[1:] for r in rows])==13  # explicit 13x13 invertible minor
print('PASS 13x14 GF2 matrix rank13, minor deleting column0 also invertible; two independent chi methods')
print('THEOREM: -1 and 12 explicit units have independent K*/K*2 squareclasses;')
print('  because units inject into K*/K*2, the 12 non-torsion units are Z-independent.')
print('STRICT: this is a rank-12 subgroup of rank-19 ordinary unit group, NOT saturation/full unit basis;')
print('  rank-40 S-unit group NOT fully generated, Cl(O_K)[2], Cl_S[2] UNKNOWN,')
print('  true Sel2 dim≤16, MW upper, p163 Coleman allMW annihilator and source veto NOT PROVED.')
