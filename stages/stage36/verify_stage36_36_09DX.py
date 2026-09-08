#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DX/fixed-p2-global-phi-selmer-intersection-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DX/global-phi-selmer-intersection-source-lock.md'
DV=ROOT/'stages/stage36/36-09DV/fixed-p2-phi-selmer-required-places-local-image-preflight.json'
DW=ROOT/'stages/stage36/36-09DW/fixed-p2-phi-selmer-five-place-local-image-preflight.json'

def gh(p):return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()
assert gh(CERT)=='ee8fda5da9fdd7ea26220740eecb07b2d8a0effe'
assert gh(SOURCE)=='403c6bf71acbce1e1f83b3ec855dd2a1e5f7ea90'
assert gh(DV)=='cc3c071315c92f4cb398e18d650d5cd3652413c8'
assert gh(DW)=='ffa5d8ee9fceed3cfcfc05ce029538557a803ac7'
c=json.loads(CERT.read_text()); dw=json.loads(DW.read_text())
assert c['schema']=='STAGE36_36_09DX_FIXED_P2_GLOBAL_PHI_SELMER_INTERSECTION_PREFLIGHT_V1'
assert c['batch_parent']['36_09DW_exact_green_head']=='70762720e965e97c0442777b00a1794f906821e8'
assert c['batch_parent']['36_09DW_exact_head_ci']=='34266118614/102195801165'
assert c['batch_parent']['36_09DW_promotion_replay_head']=='ac530681e1cc57b7e2b3d12a5e49d875d30e1c41'
assert c['batch_parent']['36_09DW_promotion_replay_ci']=='34266240249/102196213776'

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
    q=F(q);v=vp_int(q.numerator,p)-vp_int(q.denominator,p)
    n=q.numerator//(p**vp_int(q.numerator,p));d=q.denominator//(p**vp_int(q.denominator,p))
    if p==2:
        u=(n*pow(d,-1,8))%8; nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
        return (v&1,)+nm
    u=(n*pow(d,-1,p))%p
    return (v&1,0 if pow(u,(p-1)//2,p)==1 else 1)

gens=[-1,2,3,5,7]
def loc(q,place):
    if place=='infinity':return (1 if q<0 else 0,)
    return sc(q,place)

# Recompute and verify the retained localization table.
for place in ['infinity',2,3,5,7]:
    for q in gens:
        assert list(loc(q,place))==c['localization_table'][str(place)][str(q)]

# Build linear membership constraints for each exact local Phi image.
def annihilator_of_span(basis,n):return nullspace(basis,n)
constraints=[]
for place in ['infinity',2,3,5,7]:
    d=1 if place=='infinity' else (3 if place==2 else 2)
    L=[tuple(v) for v in dw['local_Phi_images'][str(place)]['basis']]
    assert rank(L)==dw['local_Phi_images'][str(place)]['dimension']
    for r in annihilator_of_span(L,3*d):
        row=[0]*15
        for coord in range(3):
            for gi,q in enumerate(gens):
                lv=loc(q,place); row[coord*5+gi]=sum(r[coord*d+j]*lv[j] for j in range(d))&1
        constraints.append(tuple(row))
assert rank(constraints,15)==13
ker=rref(nullspace(constraints,15),15)
expected=[tuple(v) for v in c['intersection_linear_algebra']['basis_vectors_in_15bit_order']]
assert rref(expected,15)==ker
assert len(ker)==2

# Independent exhaustive replay of all 32768 ambient classes.
def local_vector(bits,place):
    d=1 if place=='infinity' else (3 if place==2 else 2); out=[]
    for coord in range(3):
        z=[0]*d
        for gi,q in enumerate(gens):
            if bits[coord*5+gi]:
                lv=loc(q,place);z=[a^b for a,b in zip(z,lv)]
        out+=z
    return tuple(out)
def in_span(v,basis):return rank([tuple(x) for x in basis]+[tuple(v)])==rank([tuple(x) for x in basis])
valid=[]
for m in range(1<<15):
    bits=tuple((m>>i)&1 for i in range(15))
    ok=True
    for place in ['infinity',2,3,5,7]:
        if not in_span(local_vector(bits,place),dw['local_Phi_images'][str(place)]['basis']):ok=False;break
    if ok:valid.append(bits)
assert len(valid)==4
assert all(not any(v[10:15]) for v in valid)

def triple(bits):
    out=[]
    for coord in range(3):
        a=1
        for gi,q in enumerate(gens):
            if bits[coord*5+gi]:a*=q
        out.append(a)
    return tuple(out)
assert set(map(triple,valid))=={(1,1,1),(-1,-1,1),(6,3,1),(-6,-3,1)}
assert c['global_Phi_Selmer_group']['F2_dimension']==2
assert c['global_Phi_Selmer_group']['cardinality']==4
assert c['global_Phi_Selmer_group']['third_coordinate_trivial_on_entire_group'] is True
assert c['route_result']['next_leaf']=='36-09DY_FIXED_P2_PHI_SELMER_TO_PROSELMER_DEFECT_PREFLIGHT'
for k,v in c['scope_firewalls'].items():assert v is False,k
print('36-09DX verified: the 32768-class ambient intersects the five exact local images in a 2-dimensional/four-class Phi-Selmer group with basis (-1,-1,1) and (6,3,1); pro-Selmer and downstream credit remain closed.')
