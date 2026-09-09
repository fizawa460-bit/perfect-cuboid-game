#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09EB/fixed-p2-corrected-phi-coset-representative-preflight.json'
SRC=ROOT/'stages/stage36/36-09EB/corrected-phi-coset-representatives-source-lock.md'
DU=ROOT/'stages/stage36/36-09DU/fixed-p2-phi-selmer-local-condition-defect-preflight.json'
CORR=ROOT/'stages/stage36/36-09DW/dual-basis-pairing-correction.json'
PASS=ROOT/'stages/stage36/36-09DW/hostile-reaudit-pass-receipt.json'
DZ=ROOT/'stages/stage36/36-09DZ/fixed-p2-mw-phi-quotient-preflight.json'
EA=ROOT/'stages/stage36/36-09EA/fixed-p2-defect-aware-retained-open-intersection-preflight.json'
LOCKS={
 CERT:'63f03e134273b33fa4a51ce67c867e169996939a',
 SRC:'e1250f712e2fb08d38a42312055a2ac7666c7a91',
 DU:'d2a8bab0ab63406c7c1ced5d077cc523d5648ba2',
 CORR:'5135ad3afac4960b9d48445c6e840c5ce3798bd7',
 PASS:'3420b0b147cc04b5f430fb7b8d7810437a788879',
 DZ:'5fb697e6d450ab46adde1a4a40cde9c415e4cd90',
 EA:'aea5c84bb2721a92759e4143f5199f607a31637d',
}
def gh(p):return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); du=json.loads(DU.read_text()); corr=json.loads(CORR.read_text()); receipt=json.loads(PASS.read_text()); dz=json.loads(DZ.read_text()); ea=json.loads(EA.read_text()); src=SRC.read_text()
assert c['schema']=='STAGE36_36_09EB_FIXED_P2_CORRECTED_PHI_COSET_REPRESENTATIVE_PREFLIGHT_V1'
assert c['status']=='PASS_ALL_FOUR_RATIONAL_PHI_COSET_REPRESENTATIVES_MATERIALIZED'
assert c['base_main_sha']=='e73cefc84a49e3a51cd7951fbde44897615ace7a'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])

# Authority is the corrected, hostile-audited coordinate system only.
assert receipt['external_reaudit']['external_review_id']==5149329866
assert receipt['external_reaudit']['result']=='PASS'
assert receipt['external_reaudit']['audited_exact_head']=='8bade5065ae9b727668163df284bb0c14886ac47'
assert c['authority_input']['corrected_labels_authority_valid'] is True
assert c['authority_input']['historical_DX_labels_valid'] is False
assert c['authority_input']['promotion_replay_ci']=='34306570884/102324397624'
assert c['authority_input']['promotion_final_ci']=='34306639842/102324606079'

# Exact curve model from DU: z^2=a^2+b^2, a=(t^2-1)^2, b=(25/6)t(t^2+1).
def rhs(t):
    a=(t*t-1)**2
    b=F(25,6)*t*(t*t+1)
    return a*a+b*b
P0=(F(0),F(1)); Pp=(F(1),F(25,3)); Pm=(F(1),F(-25,3))
for t,z in [P0,Pp,Pm]: assert z*z==rhs(t)
assert c['curve_points']['P0']==['0','1']
assert c['curve_points']['P_plus']==['1','25/3']
assert c['curve_points']['P_minus']==['1','-25/3']

# DU function evaluation on D=P-P0.
F1=lambda t,z:(t*t+4)*(t*t+F(1,4))
F2=lambda t,z:(t*t+4)*(t*t+9)
F3=lambda t,z:2*(z+(t*t-1)**2)

def eval_ratio(P,fun):return fun(*P)/fun(*P0)
vals_p=[eval_ratio(Pp,f) for f in (F1,F2,F3)]
vals_m=[eval_ratio(Pm,f) for f in (F1,F2,F3)]
assert vals_p==[F(25,4),F(25,18),F(25,6)]
assert vals_m==[F(25,4),F(25,18),F(-25,6)]

# Canonical rational squareclass representative: sign times product of primes with odd valuation.
def factor_int(n):
    n=abs(n); p=2; out=[]
    while p*p<=n:
        e=0
        while n%p==0:e+=1;n//=p
        if e&1:out.append(p)
        p=3 if p==2 else p+2
    if n>1:out.append(n)
    return out
def squareclass(q):
    q=F(q); s=-1 if q<0 else 1
    ps=factor_int(q.numerator)+factor_int(q.denominator)
    r=s
    for p in sorted(set(ps)):
        if ps.count(p)&1:r*=p
    return r
lab_p=tuple(squareclass(x) for x in vals_p)
lab_m=tuple(squareclass(x) for x in vals_m)
assert lab_p==(1,2,6)
assert lab_m==(1,2,-6)
lab_sum=tuple(squareclass(a*b) for a,b in zip(lab_p,lab_m))
assert lab_sum==(1,1,-1)
labels={(1,1,1),lab_p,lab_m,lab_sum}
corrected={tuple(int(x.strip('[]')) for x in row) for row in corr['corrected_global_Phi_Selmer']['all_classes']}
assert labels==corrected
assert c['corrected_Phi_Kummer_labels']['r0']==['[1]','[1]','[1]']
assert c['corrected_Phi_Kummer_labels']['r_plus']==['[1]','[2]','[6]']
assert c['corrected_Phi_Kummer_labels']['r_minus']==['[1]','[2]','[-6]']
assert c['corrected_Phi_Kummer_labels']['r_sum']==['[1]','[1]','[-1]']
assert c['corrected_Phi_Kummer_labels']['all_four_corrected_Selmer_classes_hit'] is True
assert c['corrected_Phi_Kummer_labels']['historical_labels_used'] is False

# Quotient exactness: finite descent plus Sha(A)[Phi]=0.
assert dz['finite_isogeny_Sha_kernels']['Sha_A_Phi_trivial'] is True
assert dz['rational_isogeny_quotients']['Phi_MW_quotient_F2_dimension']==2
assert dz['rational_isogeny_quotients']['Phi_MW_quotient_cardinality']==4
assert corr['corrected_global_Phi_Selmer']['F2_dimension']==2
assert corr['corrected_global_Phi_Selmer']['cardinality']==4
qi=c['quotient_identification']
assert qi['Sha_A_Phi_trivial'] is True
assert qi['connecting_map_isomorphism_to_corrected_Phi_Selmer'] is True
assert qi['representatives_pairwise_distinct_mod_PhiAQ'] is True
assert qi['representatives_exhaust_JQ_mod_PhiAQ'] is True
assert c['jacobian_representatives']['representative_set_cardinality']==4
assert c['jacobian_representatives']['all_representatives_Q_rational'] is True
assert ea['coset_decomposition']['representative_set_cardinality']==4

# Replay localization of all corrected labels at S and membership in corrected local Phi images.
def vp_int(n,p):
    if n==0:return 10**9
    n=abs(n);e=0
    while n%p==0:e+=1;n//=p
    return e
def sc(q,p):
    q=F(q);vn=vp_int(q.numerator,p);vd=vp_int(q.denominator,p);v=vn-vd
    n=q.numerator//(p**vn);d=q.denominator//(p**vd)
    if p==2:
        u=(n*pow(d,-1,8))%8; nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
        return (v&1,)+nm
    u=(n*pow(d,-1,p))%p
    return (v&1,0 if pow(u,(p-1)//2,p)==1 else 1)
def loc(q,place):
    if place=='infinity':return (1 if q<0 else 0,)
    return sc(q,int(place))
def rank(vs,n):
    a=[list(map(int,v)) for v in vs if any(v)]; r=0
    for j in range(n):
        k=next((i for i in range(r,len(a)) if a[i][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r
def in_span(v,basis):return rank(list(basis)+[tuple(v)],len(v))==rank(basis,len(v))
for place in ['infinity','2','3','5','7']:
    basis=[tuple(v) for v in corr['corrected_local_Phi_images'][place]['basis']]
    for triple in labels:
        bits=[]
        for q in triple:bits += list(loc(q,place))
        assert in_span(tuple(bits),basis),(place,triple,bits)
lt=c['local_translation_data']
assert lt['certified_place_set']==['infinity',2,3,5,7]
assert lt['translations_are_diagonal_localizations_of_rational_divisor_classes'] is True
assert lt['corrected_local_Kummer_labels_replayed'] is True
assert lt['p_adic_lift_choice_required'] is False
assert lt['all_four_EA_translations_materialized'] is True

assert 'R={0, D+, D-, Dsum}' in src
assert c['route_result']['next_leaf']=='36-09EC_FIXED_P2_FOUR_TRANSLATED_RETAINED_OPEN_INTERSECTION_PREFLIGHT'
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09EB verified: R={0,D+,D-,Dsum} gives all four Q-rational representatives of J(Q)/Phi A(Q), with corrected labels (1,1,1),(1,2,6),(1,2,-6),(1,1,-1). Localizations lie in every corrected required-place Phi image. EC is next; all intersection/Brauer/receiver/endpoint credit remains closed.')
