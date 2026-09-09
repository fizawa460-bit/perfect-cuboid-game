#!/usr/bin/env python3
import json, subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09ED/fixed-p2-dyadic-rank-one-mw-saturation-preflight.json'
SRC=ROOT/'stages/stage36/36-09ED/dyadic-rank-one-mw-saturation-source-lock.md'
DZ=ROOT/'stages/stage36/36-09DZ/fixed-p2-mw-phi-quotient-preflight.json'
DZS=ROOT/'stages/stage36/36-09DZ/mw-phi-quotient-source-lock.md'
DWS=ROOT/'stages/stage36/36-09DW/phi-selmer-five-place-local-image-source-lock.md'
EC=ROOT/'stages/stage36/36-09EC/fixed-p2-factor-proselmer-mw-closure-preflight.json'
ECS=ROOT/'stages/stage36/36-09EC/factor-proselmer-mw-closure-source-lock.md'
ARS=ROOT/'docs/arsenal/cards/workflows/S31-WF01.md'
LOCKS={
 CERT:'87e4dd2074f4e7264c728d5e999cd321ba81e2e0',
 SRC:'cc62f75cc4de2b1542db9df4c0b1f7e7976ca3a4',
 DZ:'5fb697e6d450ab46adde1a4a40cde9c415e4cd90',
 DZS:'4ff753f9933f56cd33accaac264ddc7e936d2364',
 DWS:'08c91eed30774fa5c44509bb61f1c3b1386f2266',
 EC:'f3f4c7e126ba2b81c6fb593d9db513d9c61297a0',
 ECS:'c3bc3947747ad72a7708cbdce5b109a9286be6d3',
 ARS:'feb9a0581d378beccd1dc58cf9dd20e6c41347bc',
}
def gh(p):return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items():assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); dz=json.loads(DZ.read_text()); ec=json.loads(EC.read_text())
assert c['schema']=='STAGE36_36_09ED_FIXED_P2_DYADIC_RANK_ONE_MW_SATURATION_PREFLIGHT_V1'
assert c['status']=='PASS_E_TAU_2ADIC_FREE_GENERATOR_SATURATED_ONE_Z2_VARIABLE_REMAINS'
assert c['base_main_sha']=='e1696bd4f9debc753128e41fb34e368fc77c3fea'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])
assert dz['E_tau_Weierstrass']['equation']=='V^2 = U(U+1)(U+49)'
assert dz['E_tau_Weierstrass']['mapped_point_P']==['1','10']
assert ec['rank_and_rational_2torsion']['rank_vector']=={'E_tau':1,'E_sigma':0,'E_rho':0}
assert ec['global_factor_2Selmer']['E_tau']['F2_dimension']==3
assert ec['factor_Sha']['Sha_E_tau_2primary_zero'] is True

# Exact group law on V^2=U^3+50U^2+49U.
O=None; a2=F(50); a4=F(49)
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and y1==-y2:return None
    if P==Q:
        if y1==0:return None
        m=(3*x1*x1+2*a2*x1+a4)/(2*y1)
    else:m=(y2-y1)/(x2-x1)
    x3=m*m-a2-x1-x2
    y3=-y1+m*(x1-x3)
    return (x3,y3)
def mul(n,P):
    if n<0:return mul(-n,(P[0],-P[1]))
    R=None;Q=P
    while n:
        if n&1:R=add(R,Q)
        Q=add(Q,Q);n//=2
    return R

def onE(P):
    if P is None:return True
    x,y=P;return y*y==x*(x+1)*(x+49)
P=(F(1),F(10));Q4=(F(7),F(56));T=(F(-1),F(0))
for X in [P,Q4,T,(F(0),F(0)),(F(-49),F(0))]:assert onE(X)
assert mul(2,Q4)==(F(0),F(0))
assert mul(4,Q4) is None
assert mul(2,T) is None
assert T not in {None,Q4,mul(2,Q4),mul(3,Q4)}
Q4T=add(Q4,T)
assert Q4T==(F(-7),F(42))
assert c['exact_rational_torsion']['two_Q4']==['0','0']
assert c['exact_rational_torsion']['Q4_T_independent'] is True

# Good-reduction point-count replay. The cubic roots are 0,-1,-49, so the
# discriminant has the same prime support as 16*prod(root differences)^2.
disc_support_integer=16*(1**2)*(49**2)*(48**2)
def prime_support(n):
    n=abs(n);out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out
assert prime_support(disc_support_integer)==[2,3,7]
def count_mod_p(p):
    total=1 # point at infinity
    for x in range(p):
        rhs=(x*(x+1)*(x+49))%p
        if rhs==0:total+=1
        elif pow(rhs,(p-1)//2,p)==1:total+=2
    return total
assert count_mod_p(5)==8
assert count_mod_p(11)==16
assert c['exact_rational_torsion']['reduced_group_orders']=={'5':8,'11':16}
# The certificate's exact torsion conclusion combines the standard
# good-reduction injection theorem with the explicit order-8 subgroup.
assert c['exact_rational_torsion']['subgroup_order_lower_bound']==8
assert c['exact_rational_torsion']['rational_torsion_order']==8
assert c['exact_rational_torsion']['rational_torsion_structure']=='Z/4Z x Z/2Z'
assert c['exact_rational_torsion']['rational_torsion_all_2primary'] is True

# DZ inverse birational map and retained DW Kummer functions.
def inv_map(Q):
    U,V=Q
    den=4*U+7
    assert den!=0
    return (-(U+28)/den, F(175)*V/(2*den*den))
qQ4=inv_map(Q4);qQ4T=inv_map(Q4T)
assert qQ4==(F(-1),F(4))
assert qQ4T==(F(1),F(25,3))
def quartic_on(Q):
    x,y=Q
    return y*y==(x+4)*(x+F(1,4))*(x+9)*(x+F(1,9))
assert quartic_on(qQ4) and quartic_on(qQ4T)
base=(F(0),F(1))
def ka(Q):
    x,y=Q;return (x+4)*(x+F(1,4))
def kb(Q):
    x,y=Q;return (x+4)*(x+9)
def sqclass(q):
    q=F(q); sign=-1 if q<0 else 1
    num=abs(q.numerator);den=q.denominator;out=sign
    def fac(n):
        z=[];p=2
        while p*p<=n:
            e=0
            while n%p==0:e^=1;n//=p
            if e:z.append(p)
            p+=1
        if n>1:z.append(n)
        return z
    parity={}
    for p in fac(num)+fac(den):parity[p]=parity.get(p,0)^1
    for p,e in parity.items():
        if e:out*=p
    return out
def kum(Q):return (sqclass(ka(Q)/ka(base)),sqclass(kb(Q)/kb(base)))
kQ4=kum(qQ4);kQ4T=kum(qQ4T)
assert kQ4==(-1,6)
assert kQ4T==(1,2)
def mul_sc(a,b):return sqclass(F(a*b))
kT=(mul_sc(kQ4[0],kQ4T[0]),mul_sc(kQ4[1],kQ4T[1]))
assert kT==(-1,3)
assert c['retained_Kummer_coordinates']['delta_Q4']==['[-1]','[6]']
assert c['retained_Kummer_coordinates']['delta_Q4_plus_T']==['[1]','[2]']
assert c['retained_Kummer_coordinates']['delta_T']==['[-1]','[3]']

# F2 squareclass vectors over the EC global generator order [-1,2,3,5,7].
gens=[-1,2,3,5,7]
def scbits(q):
    q=sqclass(F(q));bits=[]
    bits.append(1 if q<0 else 0);n=abs(q)
    for p in gens[1:]:bits.append(1 if n%p==0 else 0)
    return tuple(bits)
def pairbits(pair):return scbits(pair[0])+scbits(pair[1])
def rank(rows):
    a=[list(r) for r in rows if any(r)];r=0
    if not a:return 0
    for j in range(len(a[0])):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
    return r
ktors=[pairbits(kT),pairbits(kQ4T)] # (-1,3),(1,2)
kP=pairbits((-7,42))
assert rank(ktors)==2
assert rank(ktors+[kP])==3
basis=[pairbits((-1,3)),pairbits((7,7)),pairbits((1,2))]
# XOR of all three EC rows is P.
xor=tuple(basis[0][i]^basis[1][i]^basis[2][i] for i in range(10))
assert xor==kP
assert ec['E_tau_generator_witness']['factor_2Kummer_squareclass_pair']==['[-7]','[42]']
assert ec['global_factor_2Selmer']['E_tau']['basis_squareclass_pairs']==[['[-1]','[3]'],['[7]','[7]'],['[1]','[2]']]
assert c['retained_Kummer_coordinates']['torsion_image_F2_dimension']==2
assert c['retained_Kummer_coordinates']['rank_torsion_plus_P']==3

# Rank one + nonzero free mod-2 coordinate is exactly the required Z_2 saturation.
sat=c['dyadic_saturation']
assert sat['E_tau_Q_mod_2E_F2_dimension']==3
assert sat['P_class_outside_torsion_image'] is True
assert sat['free_coefficient_mod2']==1
assert sat['free_coefficient_is_2adic_unit'] is True
assert sat['P_is_2adically_saturated_free_generator'] is True
assert sat['P_claimed_integral_MW_generator'] is False
assert sat['completion_identity']=='E_tau(Q)^hat_2 = Z_2 P + E_tau(Q)_tors'
red=c['A_completion_reduction']
assert red['rank_vector']=={'E_tau':1,'E_sigma':0,'E_rho':0}
assert red['infinite_Z2_directions']==1
assert red['E_tau_2primary_torsion_exact']=='Z/4Z x Z/2Z'
assert red['E_sigma_2primary_torsion_finite'] is True and red['E_rho_2primary_torsion_finite'] is True
assert red['E_sigma_2primary_torsion_fully_enumerated'] is False
assert red['E_rho_2primary_torsion_fully_enumerated'] is False
assert red['EB_representative_set']==['0','D_plus','D_minus','D_sum']
assert c['route_result']['next_leaf']=='36-09EE_FIXED_P2_FINITE_TORSION_Q2_RETAINED_OPEN_INTERSECTION_PREFLIGHT'
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09ED verified: E_tau(Q)_tors is exactly Z/4 x Z/2; the retained Kummer class of P lies outside the torsion image and spans the third mod-2 direction. Hence P is 2-adically saturated in the unique rank-one free direction. The four retained-open intersections remain undecided.')
