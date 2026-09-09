#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DW/dual-basis-pairing-correction.json'
SRC=ROOT/'stages/stage36/36-09DW/dual-basis-pairing-correction-source-lock.md'
DT=ROOT/'stages/stage36/36-09DT/fixed-p2-v4-isogeny-proselmer-defect-preflight.json'
DU=ROOT/'stages/stage36/36-09DU/fixed-p2-phi-selmer-local-condition-defect-preflight.json'
DUS=ROOT/'stages/stage36/36-09DU/phi-descent-character-functions-source-lock.md'
DW=ROOT/'stages/stage36/36-09DW/fixed-p2-phi-selmer-five-place-local-image-preflight.json'
DX=ROOT/'stages/stage36/36-09DX/fixed-p2-global-phi-selmer-intersection-preflight.json'
LOCKS={
 CERT:'5135ad3afac4960b9d48445c6e840c5ce3798bd7',
 SRC:'ed5125e7d4d7f4688b50dd4a59467a71d197b533',
 DT:'362326de8d6ecc0b415ecf29c6eb936134e395ce',
 DU:'d2a8bab0ab63406c7c1ced5d077cc523d5648ba2',
 DUS:'c9e9f9309555106ff5c0ed947c3973c0b11b1753',
 DW:'ffa5d8ee9fceed3cfcfc05ce029538557a803ac7',
 DX:'ee8fda5da9fdd7ea26220740eecb07b2d8a0effe',
}
def gh(p):return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); dt=json.loads(DT.read_text()); du=json.loads(DU.read_text()); dw=json.loads(DW.read_text()); dx=json.loads(DX.read_text()); src=SRC.read_text()
assert c['schema']=='STAGE36_36_09DW_DUAL_BASIS_PAIRING_CORRECTION_V1'
assert c['base_main_sha']=='b4357252bf492a0934fe47812ffa2421a342f954'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])

# F2 helpers.
def rref(vs,n=None):
    if not vs:return ()
    if n is None:n=len(vs[0])
    a=[list(map(int,v)) for v in vs if any(v)]; r=0
    for j in range(n):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]: a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return tuple(tuple(x) for x in a[:r])
def rank(vs,n=None):return len(rref(vs,n))
def nullspace(rows,n):
    a=[list(map(int,r)) for r in rows if any(r)]; piv=[]; rr=0
    for j in range(n):
        q=next((i for i in range(rr,len(a)) if a[i][j]),None)
        if q is None:continue
        a[rr],a[q]=a[q],a[rr]
        for i in range(len(a)):
            if i!=rr and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[rr])]
        piv.append(j);rr+=1
        if rr==len(a):break
    free=[j for j in range(n) if j not in piv];out=[]
    for f in free:
        x=[0]*n;x[f]=1
        for i,p in reversed(list(enumerate(piv))):x[p]=sum(a[i][j]*x[j] for j in free)&1
        out.append(tuple(x))
    return out

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))&1 for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return [list(x) for x in zip(*A)]
def inverse3(A):
    aug=[list(map(int,A[i]))+[1 if i==j else 0 for j in range(3)] for i in range(3)]
    r=0
    for j in range(3):
        q=next(i for i in range(r,3) if aug[i][j]);aug[r],aug[q]=aug[q],aug[r]
        for i in range(3):
            if i!=r and aug[i][j]:aug[i]=[x^y for x,y in zip(aug[i],aug[r])]
        r+=1
    return [row[3:] for row in aug]
def kron(A,H):
    m=len(A);n=len(H);out=[]
    for i in range(m):
        for a in range(n):
            row=[]
            for j in range(m):row += [(A[i][j]*H[a][b])&1 for b in range(n)]
            out.append(row)
    return out

# Reconstruct the Cartier pairing matrix from the actual chosen bases.
# Each factor has symplectic basis alpha=(1,0), beta=(0,1).
alpha=(1,0);beta=(0,1);zero=(0,0)
k=[alpha+alpha+zero, alpha+zero+alpha, beta+beta+beta]
z=[alpha+zero+zero, beta+zero+zero, zero+beta+zero]  # Phi(z_j)=lambda_j
def e2(v,w):
    s=0
    for h in range(3):
        a,b=v[2*h:2*h+2]; c0,d=w[2*h:2*h+2]
        s ^= (a*d)^(b*c0)
    return s
C=[[e2(ki,zj) for zj in z] for ki in k]
assert C==[[0,1,1],[0,1,0],[1,0,0]]
Ci=inverse3(C)
assert Ci==[[0,0,1],[0,1,0],[1,1,0]]
assert c['cartier_pairing']['matrix_C_rows_k_cols_lambda']==C
assert c['cartier_pairing']['matrix_C_inverse']==Ci
assert C!=[[1,0,0],[0,1,0],[0,0,1]]

# Historical direct Psi local images are retained. Correct Phi images are their orthogonal complements under Ci tensor H_v.
Hs={
 'infinity':[[1]],
 '2':[[0,0,1],[0,1,0],[1,0,0]],
 '3':[[1,1],[1,0]],
 '5':[[0,1],[1,0]],
 '7':[[1,1],[1,0]],
}
def corrected_phi(place):
    H=Hs[place]; d=len(H); B=kron(Ci,H)
    Y=[tuple(v) for v in dw['local_Psi_images'][place]['basis']]
    # x^T B y = 0 for each y, so rows are (B y)^T.
    constraints=[]
    for y in Y:
        By=[sum(B[i][j]*y[j] for j in range(3*d))&1 for i in range(3*d)]
        constraints.append(tuple(By))
    return rref(nullspace(constraints,3*d),3*d)
for place in ['infinity','2','3','5','7']:
    got=corrected_phi(place)
    exp=rref([tuple(v) for v in c['corrected_local_Phi_images'][place]['basis']],len(got[0]))
    assert got==exp,(place,got,exp)
    assert len(got)==c['corrected_local_Phi_images'][place]['dimension']
assert [c['corrected_local_Phi_images'][p]['dimension'] for p in ['infinity','2','3','5','7']]==[1,4,3,2,2]

# Recompute the fixed localization table used by DX.
def vp_int(n,p):
    if n==0:return 10**9
    n=abs(n);z=0
    while n%p==0:z+=1;n//=p
    return z
def sc(q,p):
    q=F(q);vn=vp_int(q.numerator,p);vd=vp_int(q.denominator,p);v=vn-vd
    n=q.numerator//(p**vn);d=q.denominator//(p**vd)
    if p==2:
        u=(n*pow(d,-1,8))%8; nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
        return (v&1,)+nm
    u=(n*pow(d,-1,p))%p
    return (v&1,0 if pow(u,(p-1)//2,p)==1 else 1)
gens=[-1,2,3,5,7]
def loc(q,place):
    if place=='infinity':return (1 if q<0 else 0,)
    return sc(q,int(place))
for place in ['infinity','2','3','5','7']:
    for q in gens: assert list(loc(q,place))==dx['localization_table'][place][str(q)]

# Build global corrected constraints from the corrected local Phi images.
constraints=[]
for place in ['infinity','2','3','5','7']:
    d=1 if place=='infinity' else (3 if place=='2' else 2)
    L=corrected_phi(place)
    for a in nullspace(L,3*d):
        row=[0]*15
        for coord in range(3):
            for gi,q in enumerate(gens):
                lv=loc(q,place); row[coord*5+gi]=sum(a[coord*d+j]*lv[j] for j in range(d))&1
        constraints.append(tuple(row))
assert rank(constraints,15)==13
ker=rref(nullspace(constraints,15),15)
assert len(ker)==2

def triple(bits):
    out=[]
    for coord in range(3):
        a=1
        for gi,q in enumerate(gens):
            if bits[coord*5+gi]:a*=q
        out.append(a)
    return tuple(out)
assert set(map(triple,ker))=={(1,1,-1),(1,2,6)}
valid=[]
for m in range(1<<15):
    bits=tuple((m>>i)&1 for i in range(15))
    if all(sum(r[i]*bits[i] for i in range(15))%2==0 for r in constraints):valid.append(bits)
assert len(valid)==4
assert set(map(triple,valid))=={(1,1,1),(1,1,-1),(1,2,6),(1,2,-6)}
assert c['corrected_global_Phi_Selmer']['F2_dimension']==2
assert c['corrected_global_Phi_Selmer']['cardinality']==4
assert c['corrected_global_Phi_Selmer']['third_coordinate_trivial_on_entire_group'] is False

# Direct rational witness P+=(1,25/3), P0=(0,1) under DU's exact functions.
t=F(1); zp=F(25,3); zm=-zp
F1=lambda t,z:(t*t+4)*(t*t+F(1,4))
F2=lambda t,z:(t*t+4)*(t*t+9)
F3=lambda t,z:2*(z+(t*t-1)**2)
t0=F(0);z0=F(1)
r1=F1(t,zp)/F1(t0,z0);r2=F2(t,zp)/F2(t0,z0);r3p=F3(t,zp)/F3(t0,z0);r3m=F3(t,zm)/F3(t0,z0)
assert r1==F(25,4) and r2==F(25,18) and r3p==F(25,6) and r3m==F(-25,6)
assert r1/F(1)==F(5,2)**2
assert r2/F(2)==F(5,6)**2
assert r3p/F(6)==F(5,6)**2
assert r3m/F(-6)==F(5,6)**2

# Q2 localization of (1,2,6) is excluded by the historical Phi image but included by the corrected image.
x=[]
for q in [1,2,6]: x += list(loc(q,'2'))
hist=[tuple(v) for v in dw['local_Phi_images']['2']['basis']]
corr=corrected_phi('2')
def in_span(v,basis):return rank(list(basis)+[tuple(v)],len(v))==rank(basis,len(v))
assert not in_span(tuple(x),hist)
assert in_span(tuple(x),corr)
assert c['direct_rational_witness']['P_plus_excluded_by_historical_Q2_Phi_image'] is True
assert c['direct_rational_witness']['P_plus_in_corrected_all_local_images'] is True

# Impact firewall: dimensions survive; historical labels do not.
assert dx['global_Phi_Selmer_group']['F2_dimension']==2 and dx['global_Phi_Selmer_group']['cardinality']==4
assert dx['global_Phi_Selmer_group']['third_coordinate_trivial_on_entire_group'] is True
assert c['retained_claims']['Phi_Selmer_F2_dimension_2'] is True
assert c['retained_claims']['Phi_Selmer_cardinality_4'] is True
assert c['authority_reopen']['external_hostile_reaudit_required'] is True
assert c['authority_reopen']['36_09EB_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09DW correction verified: chosen K/K^D bases have Cartier matrix C!=I, so historical coordinatewise local duality was wrong. Corrected Phi local images yield Sel^Phi=F2^2 with classes (1,1,1),(1,1,-1),(1,2,6),(1,2,-6); P=(1,25/3) is an exact witness. Numerical DY/DZ/EA dimensions survive, label-dependent authority reopens, and EB is relocked pending hostile re-audit.')
