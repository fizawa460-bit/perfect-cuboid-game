#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DJ/fixed-p2-f5-minus-r5-explicit-corestriction-preflight.json'
DI=ROOT/'stages/stage36/36-09DI/fixed-p2-f5-rational-component-relation-preflight.json'
DG=ROOT/'stages/stage36/36-09DG/qi-component-hilbert90-source-lock.md'
CW=ROOT/'stages/stage36/36-09CW/creutz-viray-hyperelliptic-brauer-source-lock.md'
SRC=ROOT/'stages/stage36/36-09DJ/creutz-viray-proposition-2-4-corestriction-source-lock.md'
BASE='1eea6800e479729c41ed8767a38298384a2dbc0f'
DI_HEAD='885349056cf203f8e3cfab735cea1870d4b3befa'
PROMO='7e2a04a5fdc56106a71af84a7912800e9b983b04'
SYNC='df725cb97f5a894622b91cdc2ca3be8dab370fe8'
LOCKS={
    CERT:'76b57c000b551846c24a0c7236c206d929faff20',
    DI:'52e860e51905f3b3ecc0e22b23791a0e8a33e0fc',
    DG:'f5b5e0a333464257ca29ea058de2cf3bd191636f',
    CW:'4657040230644aef1dbef427a3a5ab6afe3998aa',
    SRC:'fe91e95cac23754555896a534cf2f2c0a112b5e4',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def F(s:str)->Fraction:
    return Fraction(s)

def trim(a:list[Fraction])->list[Fraction]:
    a=a[:]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); out=[Fraction(0) for _ in range(n)]
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return trim(out)

def sub(a,b):
    return add(a,[-v for v in b])

def mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return trim(out)

def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    assert b!=[0]
    if len(a)<len(b):return [Fraction(0)],a
    q=[Fraction(0) for _ in range(len(a)-len(b)+1)]
    r=a[:]
    while not (len(r)==1 and r[0]==0) and len(r)>=len(b):
        k=len(r)-len(b); c=r[-1]/b[-1]; q[k]+=c
        for j,v in enumerate(b):r[k+j]-=c*v
        r=trim(r)
    return trim(q),trim(r)

def eval_poly(a,t:Fraction)->Fraction:
    z=Fraction(0)
    for c in reversed(a):z=z*t+c
    return z

def vp(a:Fraction,p:int)->int:
    assert a
    n=abs(a.numerator); d=a.denominator; v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def unit_mod(a:Fraction,p:int)->int:
    v=vp(a,p); n=a.numerator; d=a.denominator
    if v>=0:n//=p**v
    else:d//=p**(-v)
    return (n%p)*pow(d%p,-1,p)%p

def legendre(a:int,p:int)->int:
    a%=p; assert a
    z=pow(a,(p-1)//2,p)
    assert z in (1,p-1)
    return 1 if z==1 else -1

def hilbert_odd_parity(a:Fraction,b:Fraction,p:int)->int:
    va,vb=vp(a,p),vp(b,p); ua,ub=unit_mod(a,p),unit_mod(b,p)
    e=0
    if (((p-1)//2)&1) and ((va*vb)&1):e^=1
    if (vb&1) and legendre(ua,p)==-1:e^=1
    if (va&1) and legendre(ub,p)==-1:e^=1
    return e

def square_q5(a:Fraction)->bool:
    return vp(a,5)%2==0 and legendre(unit_mod(a,5),5)==1

def main()->None:
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    for h in [BASE,DI_HEAD,PROMO,SYNC]:
        subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); di=json.loads(DI.read_text()); src=SRC.read_text(); dg=DG.read_text(); cw=CW.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09DI_exact_green_head']==DI_HEAD
    assert c['batch_parent']['36_09DI_exact_head_ci']=='34208299093/102002976983'
    assert c['batch_parent']['promotion_replay_head']==PROMO
    assert c['batch_parent']['promotion_replay_ci']=='34208978272/102005169243'
    assert c['batch_parent']['freshness_sync_commit']==SYNC
    assert di['credit_boundary']['Q5_indistinguishability_with_R5_proved'] is True
    assert 'Proposition 2.4 gives' in src and 'constant over the base field' in src
    assert 'F_5=gamma(ell_5)' in dg
    assert 'A_{d,j}=(d,t^2+a_j^2)_2' in cw

    d=c['difference_input']
    assert d['delta']=='(2-i,2+i,1,1)'
    assert d['component_norms']==[5,5,1,1] and d['total_norm']==25 and d['delta_in_L1'] is True

    facs=[[F(x) for x in row] for row in c['curve_and_crt']['factor_coefficients_low_to_high']]
    targets=[[F(x) for x in row] for row in c['curve_and_crt']['target_residues']]
    g=[F(x) for x in c['curve_and_crt']['g_coefficients_low_to_high']]
    f=[Fraction(1)]
    for q in facs:f=mul(f,q)
    expected_f=[F(x) for x in c['euclidean_chain']['coefficients_low_to_high'][0]]
    assert f==expected_f
    for fac,target in zip(facs,targets):
        _,r=divmod_poly(sub(g,target),fac)
        assert r==[Fraction(0)],(fac,target,r)

    chain=[f,g]
    while True:
        _,r=divmod_poly(chain[-2],chain[-1])
        if r==[Fraction(0)]:break
        chain.append(r)
    stored=[[F(x) for x in row] for row in c['euclidean_chain']['coefficients_low_to_high']]
    assert chain==stored
    assert [len(r)-1 for r in chain]==c['euclidean_chain']['degrees']==[8,7,6,5,4,3,2,1,0]
    assert c['euclidean_chain']['n']==7 and c['euclidean_chain']['r9_zero'] is True

    got=[]
    for row in c['q5_separation_witnesses']:
        t=Fraction(row['t']); vals=[eval_poly(r,t) for r in chain]; rhs=vals[0]
        assert rhs==F(row['rhs']) and square_q5(rhs)
        assert vp(rhs,5)==row['v5_rhs'] and unit_mod(rhs,5)==row['rhs_unit_mod5']==1
        assert row['receiver_Q5_point_exists'] is True and row['retained_open'] is True
        assert t not in (Fraction(-1),Fraction(0),Fraction(1))
        assert all(v!=0 for v in vals)==row['all_chain_values_nonzero'] is True
        par=[hilbert_odd_parity(vals[i+1],vals[i],5) for i in range(8)]
        assert par==row['hilbert_parities_i0_to_i7']
        s=0
        for e in par:s^=e
        assert s==row['variable_sum_parity']
        got.append((int(t),s))
    assert got==[(2,0),(-11,1)]
    assert (-11)%5==4

    lc=c['local_consequence']; cb=c['credit_boundary']
    assert lc['constant_terms_cancel_in_point_difference'] is True
    assert lc['delta_local_invariant_difference']=='1/2'
    assert lc['F5_plus_R5_nonconstant_mod_BrQ'] is True
    assert lc['F5_equals_R5_mod_BrQ'] is False
    assert lc['DI_common_unit_identity_not_contradicted'] is True
    assert cb['explicit_F5_plus_R5_corestriction_chain_complete'] is True
    assert cb['F5_not_equal_R5_mod_BrQ_proved'] is True
    for k in ['F5_outside_entire_rational_component_image','F5_inside_entire_rational_component_image','Pic0_mod2_computed','full_L1_quotient_computed','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DK_FIXED_P2_F5_FULL_RATIONAL_COMPONENT_SPAN_PREFLIGHT'
    for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
    print('36-09DJ verified: CRT lift and full Euclidean remainder chain reproduce the F5+R5 corestriction input. Q5 receiver points t=2 and t=-11 give variable Rosset-Tate parity 0 and 1, so F5+R5 is nonconstant and F5 != R5 mod Br(Q). Full rational-component image/Picard/L1/full-Brauer/BM/fixed-p credit remains open.')

if __name__=='__main__':main()
