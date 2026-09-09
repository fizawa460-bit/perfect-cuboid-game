#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09EC/fixed-p2-factor-proselmer-mw-closure-preflight.json'
SRC=ROOT/'stages/stage36/36-09EC/factor-proselmer-mw-closure-source-lock.md'
DR=ROOT/'stages/stage36/36-09DR/fixed-p2-v4-elliptic-quotient-proselmer-reduction-preflight.json'
DV=ROOT/'stages/stage36/36-09DV/fixed-p2-phi-selmer-required-places-local-image-preflight.json'
DW=ROOT/'stages/stage36/36-09DW/fixed-p2-phi-selmer-five-place-local-image-preflight.json'
CORR=ROOT/'stages/stage36/36-09DW/dual-basis-pairing-correction.json'
DZ=ROOT/'stages/stage36/36-09DZ/fixed-p2-mw-phi-quotient-preflight.json'
EA=ROOT/'stages/stage36/36-09EA/fixed-p2-defect-aware-retained-open-intersection-preflight.json'
EB=ROOT/'stages/stage36/36-09EB/fixed-p2-corrected-phi-coset-representative-preflight.json'
LOCKS={
 CERT:'4900977d4307911e4ccd7e0813f8bf0ede9478f8',
 SRC:'63a05fbf17fa51777039b5dddea412e397e9f49d',
 DR:'c212f0430fb5b4d04ee0887e303a73fb303657c8',
 DV:'cc3c071315c92f4cb398e18d650d5cd3652413c8',
 DW:'ffa5d8ee9fceed3cfcfc05ce029538557a803ac7',
 CORR:'5135ad3afac4960b9d48445c6e840c5ce3798bd7',
 DZ:'5fb697e6d450ab46adde1a4a40cde9c415e4cd90',
 EA:'aea5c84bb2721a92759e4143f5199f607a31637d',
 EB:'63f03e134273b33fa4a51ce67c867e169996939a',
}
def gh(p):return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items():assert gh(p)==h,(p,gh(p),h)
c=json.loads(CERT.read_text());dr=json.loads(DR.read_text());dv=json.loads(DV.read_text());dw=json.loads(DW.read_text());corr=json.loads(CORR.read_text());dz=json.loads(DZ.read_text());ea=json.loads(EA.read_text());eb=json.loads(EB.read_text())
assert c['schema']=='STAGE36_36_09EC_FIXED_P2_FACTOR_PROSELMER_MW_CLOSURE_PREFLIGHT_V1'
assert c['base_main_sha']=='e1696bd4f9debc753128e41fb34e368fc77c3fea'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])
assert dv['required_places']['S']==['infinity',2,3,5,7]
assert set(dv['model_discriminants']['discriminant_prime_support'])=={2,3,5,7}
assert corr['retained_claims']['Psi_local_images_direct_computation'] is True

# F2 helpers.
def rref(vs,n=None):
    if not vs:return ()
    if n is None:n=len(vs[0])
    a=[list(map(int,v)) for v in vs if any(v)];r=0
    for j in range(n):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return tuple(tuple(x) for x in a[:r])
def rank(vs,n=None):return len(rref(vs,n))
def nullspace(rows,n):
    a=[list(map(int,r)) for r in rows if any(r)];piv=[];rr=0
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

# Exact squareclass localization in the fixed DW conventions.
gens=[-1,2,3,5,7];places=['infinity','2','3','5','7']
def vp_int(n,p):
    if n==0:return 10**9
    n=abs(n);e=0
    while n%p==0:e+=1;n//=p
    return e
def sc(q,p):
    q=F(q);vn=vp_int(q.numerator,p);vd=vp_int(q.denominator,p);v=vn-vd
    n=q.numerator//(p**vn);d=q.denominator//(p**vd)
    if p==2:
        u=(n*pow(d,-1,8))%8;nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
        return (v&1,)+nm
    u=(n*pow(d,-1,p))%p
    return (v&1,0 if pow(u,(p-1)//2,p)==1 else 1)
def loc(q,place):
    if place=='infinity':return (1 if q<0 else 0,)
    return sc(q,int(place))

def factor_selmer(name):
    constraints=[]
    for place in places:
        d=1 if place=='infinity' else (3 if place=='2' else 2)
        L=[tuple(v) for v in dw['factor_2_kummer_bases'][place][name]]
        assert len(rref(L,2*d))==dw['factor_2_kummer_dimensions'][place][name]
        for ann in nullspace(L,2*d):
            row=[0]*10
            for coord in range(2):
                for gi,q in enumerate(gens):
                    lv=loc(q,place)
                    row[coord*5+gi]=sum(ann[coord*d+j]*lv[j] for j in range(d))&1
            constraints.append(tuple(row))
    return rank(constraints,10),rref(nullspace(constraints,10),10)

def pair(bits):
    out=[]
    for coord in range(2):
        x=1
        for i,q in enumerate(gens):
            if bits[coord*5+i]:x*=q
        out.append(x)
    return tuple(out)
expected={
 'E_tau':(7,3,{(-1,3),(7,7),(1,2)}),
 'E_sigma':(8,2,{(-1,1),(1,6)}),
 'E_rho':(8,2,{(-1,1),(1,3)}),
}
for name,(cr,dim,basis_pairs) in expected.items():
    got_cr,basis=factor_selmer(name)
    assert got_cr==cr and len(basis)==dim,(name,got_cr,basis)
    assert set(map(pair,basis))==basis_pairs,(name,set(map(pair,basis)),basis_pairs)
    cert=c['global_factor_2Selmer'][name]
    assert cert['constraint_rank']==cr and cert['F2_dimension']==dim and cert['cardinality']==2**dim

# Rank vector and Kummer exact-sequence dimension equality.
assert dz['rank_one_witness']['E_tau_rank_lower_bound']==1
assert dz['rank_one_witness']['A_rank_exact']==1
ranks={'E_tau':1,'E_sigma':0,'E_rho':0}
assert c['rank_and_rational_2torsion']['rank_vector']==ranks
for name in ranks:
    assert c['rank_and_rational_2torsion']['E_Q_mod_2E_dimensions'][name]==ranks[name]+2
    assert c['global_factor_2Selmer'][name]['F2_dimension']==ranks[name]+2
for k,v in c['factor_Sha'].items():assert v is True,(k,v)
for k,v in c['proSelmer_to_MW_completion'].items():assert v is True,(k,v)

# E_tau explicit witness Kummer class under the retained factor functions.
qx,qy=F(-29,11),F(875,121)
a=lambda x,y:(x+4)*(x+F(1,4))
b=lambda x,y:(x+4)*(x+9)
o=(F(0),F(1))
def sqclass(q):
    q=F(q);n=abs(q.numerator);d=q.denominator;res=-1 if q<0 else 1
    p=2
    while p*p<=max(n,d):
        e=0
        while n%p==0:e^=1;n//=p
        while d%p==0:e^=1;d//=p
        if e:res*=p
        p=3 if p==2 else p+2
    if n>1:res*=n
    if d>1:res*=d
    return res
kp=(sqclass(a(qx,qy)/a(*o)),sqclass(b(qx,qy)/b(*o)))
assert kp==(-7,42)
assert c['E_tau_generator_witness']['factor_2Kummer_squareclass_pair']==['[-7]','[42]']

# Exact downstream reformulation/firewall.
assert ea['elliptic_product_side']['T2Sel_A_identity']=='T2Sel(E_tau) x T2Sel(E_sigma) x T2Sel(E_rho)'
assert eb['jacobian_representatives']['representative_set_cardinality']==4
assert c['translated_intersection_reformulation']['representative_set']==['0','D_plus','D_minus','D_sum']
assert c['translated_intersection_reformulation']['all_proSelmer_Sha_ambiguity_removed'] is True
assert c['translated_intersection_reformulation']['free_rank']==1
assert c['translated_intersection_reformulation']['four_translated_intersections_decided'] is False
assert c['route_result']['next_leaf']=='36-09ED_FIXED_P2_DYADIC_RANK_ONE_MW_CLOSURE_INTERSECTION_PREFLIGHT'
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EC verified: exact factor Sel_2 dimensions are (3,2,2), matching rank+(rational 2-torsion dim), so all factor 2-primary Sha vanish. Hence T2Sel(A)=A(Q)^hat_2 and T2Sel(J)=J(Q)^hat_2. The four EB translations remain undecided and reduce to a rank-one dyadic Mordell-Weil closure intersection.')
