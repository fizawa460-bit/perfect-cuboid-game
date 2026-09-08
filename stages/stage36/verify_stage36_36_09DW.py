#!/usr/bin/env python3
import json, math, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DW/fixed-p2-phi-selmer-five-place-local-image-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DW/phi-selmer-five-place-local-image-source-lock.md'
DT=ROOT/'stages/stage36/36-09DT/fixed-p2-v4-isogeny-proselmer-defect-preflight.json'
DU=ROOT/'stages/stage36/36-09DU/fixed-p2-phi-selmer-local-condition-defect-preflight.json'
DV=ROOT/'stages/stage36/36-09DV/fixed-p2-phi-selmer-required-places-local-image-preflight.json'

def gh(p): return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()
assert gh(CERT)=='ffa5d8ee9fceed3cfcfc05ce029538557a803ac7'
assert gh(SOURCE)=='08c91eed30774fa5c44509bb61f1c3b1386f2266'
assert gh(DT)=='362326de8d6ecc0b415ecf29c6eb936134e395ce'
assert gh(DU)=='d2a8bab0ab63406c7c1ced5d077cc523d5648ba2'
assert gh(DV)=='cc3c071315c92f4cb398e18d650d5cd3652413c8'
c=json.loads(CERT.read_text())
assert c['schema']=='STAGE36_36_09DW_FIXED_P2_PHI_SELMER_FIVE_PLACE_LOCAL_IMAGE_PREFLIGHT_V1'
assert c['batch_parent']['36_09DV_exact_green_head']=='25d27029099611f24752b6443a3ec4859afe0c19'
assert c['batch_parent']['36_09DV_exact_head_ci']=='34256784848/102164496201'
assert c['batch_parent']['36_09DV_promotion_replay_head']=='29b7bfcbb9b977f53e85472b37b5a7a0d9b904cb'
assert c['batch_parent']['36_09DV_promotion_replay_ci']=='34256917588/102164942463'

# ---------- F2 linear algebra ----------
def rref(vs):
    if not vs:return ()
    a=[list(map(int,v)) for v in vs if any(v)]; n=len(vs[0]); r=0
    for j in range(n):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]: a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return tuple(tuple(x) for x in a[:r])
def rank(vs): return len(rref(vs))
def nullspace(rows,n):
    a=[list(map(int,r)) for r in rows if any(r)]; piv=[]; rr=0
    for j in range(n):
        q=next((i for i in range(rr,len(a)) if a[i][j]),None)
        if q is None:continue
        a[rr],a[q]=a[q],a[rr]
        for i in range(len(a)):
            if i!=rr and a[i][j]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
        piv.append(j); rr+=1
        if rr==len(a):break
    free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        x=[0]*n; x[f]=1
        for i,p in reversed(list(enumerate(piv))):
            s=0
            for j in free:s^=a[i][j]&x[j]
            x[p]=s
        out.append(tuple(x))
    return out

def same_span(a,b): return rref(a)==rref(b)

# ---------- local squareclasses / roots ----------
def vpi(n,p):
    if n==0:return 10**9
    n=abs(n); z=0
    while n%p==0:z+=1;n//=p
    return z
def vp(q,p):
    q=F(q)
    if not q:return 10**9
    return vpi(q.numerator,p)-vpi(q.denominator,p)
def scaled_mod(q,p,m,M):
    q=F(q); qq=q/F(p**m) if m>=0 else q*F(p**(-m)); mod=p**M
    return (qq.numerator%mod)*pow(qq.denominator%mod,-1,mod)%mod
def unit_mod(q,p,M):
    z=vp(q,p); return scaled_mod(q,p,z,M),z
def sqrt_units(u,p,M):
    mod=p**M; u%=mod
    if p==2:
        if u%8!=1:return []
        roots=[1,3,5,7]; m=8
        for _ in range(3,M):
            nm=2*m; roots=sorted({x for r in roots for x in (r,r+m) if (x*x-u)%nm==0}); m=nm
        return roots
    roots=[r for r in range(p) if r*r%p==u%p]; m=p
    for _ in range(1,M):
        nm=m*p; roots=sorted({r+d*m for r in roots for d in range(p) if ((r+d*m)**2-u)%nm==0}); m=nm
    return roots
def roots(q,p,M=14):
    q=F(q)
    if not q:return []
    z=vp(q,p)
    if z&1:return []
    u,_=unit_mod(q,p,M)
    return [(z//2,r) for r in sqrt_units(u,p,M)]
def sc(q,p):
    q=F(q)
    if not q:return None
    z=vp(q,p); u,_=unit_mod(q,p,3 if p==2 else 1)
    if p==2:
        nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u%8]
        return (z&1,)+nm
    return (z&1,0 if pow(u%p,(p-1)//2,p)==1 else 1)
def root_plus_sc(rt,A,p,M=14,coef=2):
    s,r=rt; A=F(A); va=vp(A,p) if A else 10**9; m=min(s,va); mod=p**M
    y=(r*p**(s-m))%mod; a=scaled_mod(A,p,m,M) if A else 0; x=(y+a)%mod
    if not x:return None
    k=vpi(x,p); vc=vp(F(coef),p); z=m+k+vc
    u=(x//p**k)%(8 if p==2 else p); cu,_=unit_mod(F(coef),p,3 if p==2 else 1)
    if p==2:
        u=u*(cu%8)%8; nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
        return (z&1,)+nm
    u=u*(cu%p)%p; return (z&1,0 if pow(u,(p-1)//2,p)==1 else 1)

def rhs(kind,x):
    x=F(x)
    if kind=='E_tau':return (x+4)*(x+F(1,4))*(x+9)*(x+F(1,9))
    if kind=='E_sigma':return (x*x+F(9,4))*(x*x+F(64,9))
    return (x*x+F(25,4))*(x*x+F(100,9))
def ab(kind,x,rt,p):
    x=F(x)
    if kind=='E_tau':
        a=sc((x+4)*(x+F(1,4)),p); b=sc((x+4)*(x+9),p)
    elif kind=='E_sigma':
        a=sc(x*x+F(9,4),p); b=root_plus_sc(rt,x*x-4,p)
    else:
        a=sc(x*x+F(25,4),p); b=root_plus_sc(rt,x*x-F(25,3),p)
    return None if a is None or b is None else tuple(a)+tuple(b)

def local_factor_span(kind,p):
    out=[]
    for n in range(-250,251):
        for rt in roots(rhs(kind,F(n)),p):
            q=ab(kind,F(n),rt,p)
            if q is not None:out.append(q)
    return rref(out)

# Exact finite-place factor images: bounded witness generation saturates the theorem upper dimensions.
for p in [2,3,5,7]:
    for kind in ['E_tau','E_sigma','E_rho']:
        got=local_factor_span(kind,p); exp=c['factor_2_kummer_bases'][str(p)][kind]
        assert same_span(got,exp),(p,kind,got,exp)
        assert rank(got)==c['factor_2_kummer_dimensions'][str(p)][kind]

# Real factor images.
real={'E_tau':[(1,0)],'E_sigma':[(0,1)],'E_rho':[(0,1)]}
for kind,b in real.items():
    assert same_span(b,c['factor_2_kummer_bases']['infinity'][kind])
    assert rank(b)==1

# ---------- push factor Kummer images to delta_Psi ----------
def G(kind,v,d):
    a=v[:d]; b=v[d:]
    z=(0,)*d
    if kind=='E_tau':return tuple(a+a+b)
    if kind=='E_sigma':return tuple(a+z+b)
    return tuple(z+a+b)

def psi_from_factors(place):
    d=1 if place=='infinity' else (3 if place==2 else 2); gens=[]
    key=str(place)
    for kind in ['E_tau','E_sigma','E_rho']:
        for v in c['factor_2_kummer_bases'][key][kind]:gens.append(G(kind,tuple(v),d))
    return rref(gens)
for place in ['infinity',2,3,5,7]:
    got=psi_from_factors(place); exp=c['local_Psi_images'][str(place)]['basis']
    assert same_span(got,exp)
    assert rank(got)==c['local_Psi_images'][str(place)]['dimension']

# ---------- Tate/Hilbert orthogonal complement ----------
def H(place):
    if place=='infinity':return [[1]]
    if place==2:return [[0,0,1],[0,1,0],[1,0,0]]
    return [[((place-1)//2)&1,1],[1,0]]
def orth(psi,place):
    h=H(place); d=len(h); rows=[]
    for y in psi:
        r=[]
        for q in range(3):
            yy=y[q*d:(q+1)*d]
            for i in range(d):
                r.append(sum(h[i][j]*yy[j] for j in range(d))&1)
        rows.append(tuple(r))
    return rref(nullspace(rows,3*d))
for place in ['infinity',2,3,5,7]:
    psi=psi_from_factors(place); got=orth(psi,place); exp=c['local_Phi_images'][str(place)]['basis']
    assert same_span(got,exp),(place,got,exp)
    assert rank(got)==c['local_Phi_images'][str(place)]['dimension']

assert {k:c['local_Phi_images'][k]['dimension'] for k in ['infinity','2','3','5','7']}=={'infinity':1,'2':4,'3':3,'5':2,'7':2}
assert c['exactness_argument']['five_local_Phi_images_computed'] is True
assert c['exactness_argument']['global_Phi_Selmer_group_computed'] is False
assert c['route_result']['next_leaf']=='36-09DX_FIXED_P2_GLOBAL_PHI_SELMER_INTERSECTION_PREFLIGHT'
for k,v in c['scope_firewalls'].items():assert v is False,k
print('36-09DW verified: exact local Phi images have dimensions infinity/2/3/5/7 = 1/4/3/2/2 via saturated factor Kummer images, dual-isogeny pushforward, and Tate orthogonal complement. Global intersection remains closed.')
