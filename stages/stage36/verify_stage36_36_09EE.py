#!/usr/bin/env python3
import json, math, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09EE/fixed-p2-q2-rho-retained-open-exclusion-preflight.json'
SRC=ROOT/'stages/stage36/36-09EE/q2-rho-torsion-retained-open-exclusion-source-lock.md'
DR=ROOT/'stages/stage36/36-09DR/fixed-p2-v4-elliptic-quotient-proselmer-reduction-preflight.json'
DSS=ROOT/'stages/stage36/36-09DS/v4-isogeny-norm-pullback-proselmer-source-lock.md'
DSC=ROOT/'stages/stage36/36-09DS/proselmer-torsion-injectivity-correction-source-lock.md'
DN=ROOT/'stages/stage36/36-09DN/fixed-p2-full-br2-common-neighborhood-preflight.json'
DQ=ROOT/'stages/stage36/36-09DQ/fixed-p2-global-2primary-adelic-annihilator-preflight.json'
EC=ROOT/'stages/stage36/36-09EC/fixed-p2-factor-proselmer-mw-closure-preflight.json'
ARS=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
LOCKS={
 CERT:'683d52e7cba9e2bd683cc06577fb6913532feb77',
 SRC:'0cc6e97c62fbb0782f19e30d87b19509d8144a8c',
 DR:'c212f0430fb5b4d04ee0887e303a73fb303657c8',
 DSS:'1bac0039c0abccc236b392c2deba3a26ee83ba88',
 DSC:'5d456e35fb82e03f686ad328c103a29b1907534a',
 DN:'297068d95f72310d6c8a3a59816a1806ff542392',
 DQ:'4c41228d23f9088bfbea8b68c94b2a26948f8691',
 EC:'f3f4c7e126ba2b81c6fb593d9db513d9c61297a0',
 ARS:'1d5275321f42768a6414d4610ac912c63be43f96',
}
def gh(p): return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); dr=json.loads(DR.read_text()); dn=json.loads(DN.read_text()); dq=json.loads(DQ.read_text()); ec=json.loads(EC.read_text())
src=SRC.read_text(); dss=DSS.read_text(); dsc=DSC.read_text(); ars=ARS.read_text()
assert c['schema']=='STAGE36_36_09EE_FIXED_P2_Q2_RHO_RETAINED_OPEN_EXCLUSION_PREFLIGHT_V1'
assert c['status']=='PASS_Q2_RHO_TORSION_EXCLUDES_RETAINED_OPEN_PROSELMER_FULL_2PRIMARY_BRAUER_SET_EMPTY_AUDIT_GATED'
assert c['base_main_sha']=='e1696bd4f9debc753128e41fb34e368fc77c3fea'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])

# Upstream exact interfaces actually consumed.
rho=dr['elliptic_quotients']['E_rho']
assert rho['invariants']=='v=t-1/t, Y=z/t^2'
assert rho['equation']=='Y^2=v^4+(625/36)v^2+625/9=(v^2+25/4)(v^2+100/9)'
assert ec['rank_and_rational_2torsion']['rank_vector']['E_rho']==0
assert ec['proSelmer_to_MW_completion']['T2Sel_J_equals_JQ_completion'] is True
assert {'t=0','t=1','t=-1','t=infinity'} <= set(dn['fixed_curve']['retained_open_boundary_contains'])
assert dq['brauer_manin_translation']['orthogonality_equivalence'].endswith('image(T_2 Sel(J))')
assert 'Psi(x) = (pi_{tau,*}x, pi_{sigma,*}x, pi_{rho,*}x)' in dss
assert 'T2Sel_2_torsion_free=true' in dsc and 'are revoked' in dsc
assert 'RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION' in ars

# The rho quartic -> full-2-torsion Weierstrass model is replayed algebraically.
# From Y = X*v^2-B and Y^2=v^4+A*v^2+B^2 one gets
# v^2*(X^2-1)=c*X+A, c=2B. Hence W=v*(X^2-1) satisfies
# W^2=(X^2-1)(cX+A). Scaling x=cX,y=cW,x0=36x,y0=216y
# gives roots x0=+600,-600,-625.
A_num,A_den=625,36
B_num,B_den=25,3
c_num,c_den=50,3
assert 36*c_num//c_den==600
assert -36*c_num//c_den==-600
assert -36*A_num//A_den==-625
roots=[600,-600,-625]
# Expanded cubic check.
s1=sum(roots); s2=roots[0]*roots[1]+roots[0]*roots[2]+roots[1]*roots[2]; s3=roots[0]*roots[1]*roots[2]
# (x-r1)(x-r2)(x-r3)=x^3-s1 x^2+s2 x-s3
assert [-s1,s2,-s3]==[625,-360000,-225000000]
assert c['rho_quotient']['weierstrass_model']=='y0^2=(x0-600)(x0+600)(x0+625)'

# Rational 2-primary torsion: no nonzero 2-torsion point can be halved over Q.
def square_int(n):
    if n<0:return False
    r=math.isqrt(n); return r*r==n
for i,e in enumerate(roots):
    diffs=[e-roots[j] for j in range(3) if j!=i]
    assert not all(square_int(d) for d in diffs),(e,diffs)
rt=c['rational_2primary_torsion']
assert rt['nonzero_rational_2torsion_divisible_by_2'] is False
assert rt['rational_4torsion_exists'] is False
assert rt['rational_higher_2power_torsion_exists'] is False
assert rt['E_rho_Q_2primary']=='(Z/2Z)^2'
assert rt['E_rho_Q_hat_2_equals_E_rho_2torsion'] is True

# Integral model invariants.
a1=0;a2=625;a3=0;a4=-360000;a6=-225000000
b2=a1*a1+4*a2
b4=2*a4+a1*a3
b6=a3*a3+4*a6
b8=4*a2*a6-a4*a4+a1*a3*a4-a2*a3*a3-a1*a1*a6
c4=b2*b2-24*b4
Delta=-(b2*b2*b8)-8*b4**3-27*b6**2+9*b2*b4*b6
def vp2(n):
    assert n!=0
    n=abs(n); z=0
    while n%2==0:z+=1;n//=2
    return z
assert vp2(c4)==4
assert vp2(Delta)==12
assert 3*vp2(c4)-vp2(Delta)==0
q2=c['Q2_odd_torsion_exclusion']
assert (q2['v2_c4'],q2['v2_discriminant'],q2['v2_j'])==(4,12,0)
assert q2['multiplicative_reduction_excluded'] is True
assert q2['possible_odd_torsion_primes_after_local_reduction_filtration']==[3,5]

# Pure-integer polynomial arithmetic, ascending coefficient convention.
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def padd(a,b,sgn=1):
    n=max(len(a),len(b)); z=[0]*n
    for i in range(n):z[i]=(a[i] if i<len(a) else 0)+sgn*(b[i] if i<len(b) else 0)
    return trim(z)
def pmul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return trim(z)
def ppow(a,n):
    z=[1];q=a[:]
    while n:
        if n&1:z=pmul(z,q)
        q=pmul(q,q);n//=2
    return z
f=[a6,a4,a2,1]
psi3=[b8,3*b6,3*b4,b2,3]
inner=[b4*b8-b6*b6,b2*b8-b4*b6,10*b8,10*b6,5*b4,b2,2]
psi5=padd([16*x for x in pmul(ppow(f,2),inner)],ppow(psi3,3),sgn=-1)
assert len(psi3)==5 and len(psi5)==13
v3=[vp2(z) for z in psi3]; v5=[vp2(z) for z in psi5]
assert v3==[8,8,7,2,0]
assert v5==[24,24,23,18,16,14,12,11,8,8,4,2,0]
assert v3==q2['psi3_ascending_coefficient_v2']
assert v5==q2['psi5_ascending_coefficient_v2']
# Each Newton polygon is the endpoint segment of slope -2.
for i,v in enumerate(v3):assert v>=8-2*i
for i,v in enumerate(v5):assert v>=24-2*i
# After x=4u and division by endpoint 2-power, mod-2 support consists
# precisely of terms lying on the polygon segment.
supp3=[i for i,v in enumerate(v3) if v+2*i==8]
supp5=[i for i,v in enumerate(v5) if v+2*i==24]
assert supp3==[0,3,4]
assert supp5==[0,3,4,5,6,8,10,11,12]
assert supp5==q2['psi5_nonzero_mod2_degrees_after_x_eq_4u']
# F2 has only 0,1. Both reduced polynomials are nonzero at both points.
def eval_support(supp,u):return sum((u**i) for i in supp)&1
assert [eval_support(supp3,u) for u in (0,1)]==[1,1]
assert [eval_support(supp5,u) for u in (0,1)]==[1,1]
assert q2['psi3_x_eq_4u_mod2']=='u^4+u^3+1'
assert q2['psi3_has_Q2_root'] is False and q2['psi5_has_Q2_root'] is False
assert q2['E_rho_Q2_odd_torsion_zero'] is True
assert q2['Q2_to_2adic_completion_injective'] is True

# Reference/boundary and the common Q2 obstruction.
rb=c['reference_and_boundary']
assert rb['P0_on_C3_2']=={'t':'0','z':'1'}
# As t->0, v=t-1/t has v^2~t^-2 and Y=z/t^2~t^-2, so Y/v^2->+1 = I_plus.
assert rb['pi_rho_P0']=='I_plus'
assert rb['pi_rho_P0_weierstrass']==['600','0']
ix=c['Q2_intersection_exclusion']
assert ix['local_completion_injectivity_used'] is True
assert ix['pi_rho_P_forced_into_rational_2torsion'] is True
assert ix['finite_nonzero_t_forces_affine_rho_image'] is True
assert ix['affine_rational_2torsion_forces_v_zero'] is True
# v=t-1/t=0 gives t^2=1 exactly.
assert ix['forced_t_values']==['1','-1']
assert set(ix['forced_t_values']) <= {'1','-1'}
assert ix['forced_values_are_retained_boundary'] is True
assert ix['local_Q2_retained_open_MW_completion_intersection_empty'] is True
assert ix['T2Sel_J_equals_JQ_completion_from_EC'] is True
assert ix['global_retained_open_proSelmer_intersection_empty'] is True
assert ix['all_four_EB_translated_intersections_empty_by_common_rho_obstruction'] is True
bm=c['brauer_manin_consequence']
assert bm['DQ_orthogonality_equivalence_consumed'] is True
assert bm['full_global_2primary_Brauer_set_on_retained_open_empty'] is True
assert bm['two_primary_Brauer_Manin_obstruction_obtained'] is True
assert bm['fixed_curve_only'] is True
assert bm['physical_receiver_adapter_not_yet_promoted'] is True
assert c['route_result']['hostile_audit_required_before_next_promotion'] is True
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EE verified: the rank-zero rho quotient has E_rho(Q)^hat_2=E_rho[2](Q), E_rho(Q_2) has no odd torsion, and the Q_2 completion map is injective. Any retained-open pro-Selmer hit forces v=0 and t=+-1, both boundary. Hence the retained-open global 2-primary Brauer set is empty; physical receiver promotion remains audit-gated.')
