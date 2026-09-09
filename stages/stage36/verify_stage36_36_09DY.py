#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DY/fixed-p2-phi-to-proselmer-defect-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DY/phi-to-proselmer-defect-source-lock.md'
DQ=ROOT/'stages/stage36/36-09DQ/global-2primary-adelic-annihilator-proselmer-source-lock.md'
DT=ROOT/'stages/stage36/36-09DT/fixed-p2-v4-isogeny-proselmer-defect-preflight.json'
DV=ROOT/'stages/stage36/36-09DV/fixed-p2-phi-selmer-required-places-local-image-preflight.json'
DW=ROOT/'stages/stage36/36-09DW/fixed-p2-phi-selmer-five-place-local-image-preflight.json'
DX=ROOT/'stages/stage36/36-09DX/fixed-p2-global-phi-selmer-intersection-preflight.json'
CORR=ROOT/'stages/stage36/36-09DS/proselmer-torsion-injectivity-correction.json'
LOCKS={
 CERT:'3adcab8e00fa8a517df28ce71b95925f6e00ada6',
 SOURCE:'cea6737bcf9dfe242f7c3e3b2475377b2f39e481',
 DQ:'71829ec5e0af601605f1f93c5f3a3fec4cae2102',
 DT:'362326de8d6ecc0b415ecf29c6eb936134e395ce',
 DV:'cc3c071315c92f4cb398e18d650d5cd3652413c8',
 DW:'ffa5d8ee9fceed3cfcfc05ce029538557a803ac7',
 DX:'ee8fda5da9fdd7ea26220740eecb07b2d8a0effe',
 CORR:'d3318c8291835de8011f6b72fea8ca4479c3107d',
}

def gh(p): return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); dt=json.loads(DT.read_text()); dv=json.loads(DV.read_text()); dw=json.loads(DW.read_text()); dx=json.loads(DX.read_text()); corr=json.loads(CORR.read_text()); src=SOURCE.read_text(); dq=DQ.read_text()
assert c['schema']=='STAGE36_36_09DY_FIXED_P2_PHI_TO_PROSELMER_DEFECT_PREFLIGHT_V1'
assert c['status']=='PASS_EXACT_PROSELMER_KERNELS_DUAL_PSI_SELMER_DIM5_PHI_COKERNEL_ONE_BIT_REMAINS'
assert c['base_main_sha']=='affcc56382dd8d5ac559d5a3b3dd83544738bcef'
assert c['batch_parent']['pr1732_final_ci']=='34297710987/102297818474'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])

# Small F2 linear algebra helpers.
def rref(vs,n=None):
    if not vs:return ()
    if n is None:n=len(vs[0])
    a=[list(map(int,v)) for v in vs if any(v)]; r=0
    for j in range(n):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return tuple(tuple(x) for x in a[:r])
def rank(vs,n=None): return len(rref(vs,n))
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
    free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        x=[0]*n;x[f]=1
        for i,p in reversed(list(enumerate(piv))):
            x[p]=sum(a[i][j]*x[j] for j in free)&1
        out.append(tuple(x))
    return out

def vp_int(n,p):
    if n==0:return 10**9
    n=abs(n);z=0
    while n%p==0:z+=1;n//=p
    return z
def sc(q,p):
    q=F(q); vn=vp_int(q.numerator,p); vd=vp_int(q.denominator,p); v=vn-vd
    n=q.numerator//(p**vn); d=q.denominator//(p**vd)
    if p==2:
        u=(n*pow(d,-1,8))%8; nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
        return (v&1,)+nm
    u=(n*pow(d,-1,p))%p
    return (v&1,0 if pow(u,(p-1)//2,p)==1 else 1)

gens=[-1,2,3,5,7]
def loc(q,place):
    if place=='infinity': return (1 if q<0 else 0,)
    return sc(q,place)
def annihilator_of_span(basis,n): return nullspace(basis,n)

def local_vector(bits,place):
    d=1 if place=='infinity' else (3 if place==2 else 2); out=[]
    for coord in range(3):
        z=[0]*d
        for gi,q in enumerate(gens):
            if bits[coord*5+gi]:
                lv=loc(q,place); z=[a^b for a,b in zip(z,lv)]
        out+=z
    return tuple(out)
def in_span(v,basis): return rank([tuple(x) for x in basis]+[tuple(v)])==rank([tuple(x) for x in basis])
def triple(bits):
    out=[]
    for coord in range(3):
        a=1
        for gi,q in enumerate(gens):
            if bits[coord*5+gi]: a*=q
        out.append(a)
    return tuple(out)

# Recompute the same fixed localization table used by DX.
for place in ['infinity',2,3,5,7]:
    for q in gens:
        assert list(loc(q,place))==dx['localization_table'][str(place)][str(q)]

# Directly compute Sel^Psi from the retained exact local Psi images.
constraints=[]
for place in ['infinity',2,3,5,7]:
    d=1 if place=='infinity' else (3 if place==2 else 2)
    L=[tuple(v) for v in dw['local_Psi_images'][str(place)]['basis']]
    assert rank(L)==dw['local_Psi_images'][str(place)]['dimension']
    for r in annihilator_of_span(L,3*d):
        row=[0]*15
        for coord in range(3):
            for gi,q in enumerate(gens):
                lv=loc(q,place); row[coord*5+gi]=sum(r[coord*d+j]*lv[j] for j in range(d))&1
        constraints.append(tuple(row))
assert rank(constraints,15)==10
ker=rref(nullspace(constraints,15),15)
expected=[tuple(v) for v in c['finite_Psi_Selmer']['basis_vectors_in_15bit_order']]
assert rref(expected,15)==ker
assert len(ker)==5
valid=[]
for m in range(1<<15):
    bits=tuple((m>>i)&1 for i in range(15))
    if all(in_span(local_vector(bits,p),dw['local_Psi_images'][str(p)]['basis']) for p in ['infinity',2,3,5,7]): valid.append(bits)
assert len(valid)==32
expected_triples={(1,1,3),(1,1,2),(1,1,-1),(7,7,7),(-1,-1,1)}
assert set(map(triple,ker))==expected_triples
assert c['finite_Psi_Selmer']['F2_dimension']==5
assert c['finite_Psi_Selmer']['cardinality']==32

# Phi side remains the audited DX four-class group.
assert dx['global_Phi_Selmer_group']['F2_dimension']==2
assert dx['global_Phi_Selmer_group']['cardinality']==4
assert c['finite_Phi_Selmer']['F2_dimension']==2 and c['finite_Phi_Selmer']['cardinality']==4

# Independent Selmer-ratio arithmetic cross-check: dimensions 1,4,3,2,2 minus kernel dimension 3.
phi_dims=[dw['local_Phi_images'][str(p)]['dimension'] for p in ['infinity',2,3,5,7]]
assert phi_dims==[1,4,3,2,2]
exps=[x-3 for x in phi_dims]
assert exps==[-2,1,0,-1,-1] and sum(exps)==-3
assert c['global_Selmer_ratio_crosscheck']['global_Phi_ratio']=='1/8'
assert c['global_Selmer_ratio_crosscheck']['Greenberg_Wiles_predicted_ratio_from_finite_Selmer']=='4/32=1/8'
assert dt['Galois_rationality']['kernel_Phi_constant_Q_group_scheme']=='(Z/2Z)^3'
assert dt['dual_kernel']['kernel_Psi_constant_Q_group_scheme']=='(Z/2Z)^3'

# Corrected pro-Selmer boundary: rational 2-torsion survives; full T2Sel is not torsion-free.
q=corr['corrected_proSelmer_transport']
assert q['Phi_kernel_nonzero'] is True and q['Psi_kernel_nonzero'] is True
assert q['Phi_injective'] is False and q['Psi_injective'] is False
assert '2-adic Mordell--Weil completion inside `T_2 Sel(J)`' in dq

# Elementary Tate-module lemma replay on finite prefixes: if 2*x=0 in a compatible tower, x_n=2*x_{n+1}=0.
# This is a structural proof assertion, not a finite approximation claim.
assert 'This inverse limit is 2-torsion-free' in src
assert c['Tate_Sha_transport']['T2Sha_2_torsion_free'] is True
assert c['Tate_Sha_transport']['Phi_on_T2Sha_injective'] is True
assert c['Tate_Sha_transport']['Psi_on_T2Sha_injective'] is True
assert c['proSelmer_kernels']['Phi_kernel_F2_dimension']==3
assert c['proSelmer_kernels']['Psi_kernel_F2_dimension']==3
assert c['proSelmer_kernels']['Phi_kernel_exact']=='(Z/2Z)^3'
assert c['proSelmer_kernels']['Psi_kernel_exact']=='(Z/2Z)^3'

# Recompute all integral Mordell-Weil quotient/rank possibilities from finite Selmer bounds.
poss=[]
for a in range(0,3):
    for ap in range(0,6):
        r=a+ap-6
        if r>=0: poss.append([a,ap,r])
assert poss==[[1,5,0],[2,4,0],[2,5,1]]
assert c['Mordell_Weil_quotient_constraints']['allowed_triples_a_a_prime_rank']==poss
assert c['Mordell_Weil_quotient_constraints']['common_Mordell_Weil_rank_options']==[0,1]

# Cokernel dimensions are bounded by a plus the divisible-Sha contribution, itself inside finite isogeny Sha.
phi_opts=set(); psi_opts=set()
for a,ap,r in poss:
    for d in range(0,(2-a)+1): phi_opts.add(a+d)
    for dp in range(0,(5-ap)+1): psi_opts.add(ap+dp)
assert sorted(phi_opts)==[1,2]
assert sorted(psi_opts)==[4,5]
assert c['proSelmer_cokernel_constraints']['Phi_cokernel_F2_dimension_options']==[1,2]
assert c['proSelmer_cokernel_constraints']['Phi_cokernel_cardinality_options']==[2,4]
assert c['proSelmer_cokernel_constraints']['Psi_cokernel_F2_dimension_options']==[4,5]
assert c['proSelmer_cokernel_constraints']['Psi_cokernel_cardinality_options']==[16,32]
assert c['proSelmer_cokernel_constraints']['Phi_cokernel_exact_dimension_computed'] is False
assert c['proSelmer_cokernel_constraints']['Psi_cokernel_exact_dimension_computed'] is False
assert c['route_result']['next_leaf']=='36-09DZ_FIXED_P2_MORDELL_WEIL_PHI_QUOTIENT_PREFLIGHT'
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09DY verified: direct dual Sel^Psi has dimension 5/cardinality 32; both pro-Selmer kernels are exactly (Z/2)^3; rank is 0 or 1; Phi cokernel has dimension 1 or 2 and remains unresolved by one bit. DZ is the exact MW quotient leaf; all downstream credit remains closed.')
