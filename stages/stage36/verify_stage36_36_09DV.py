#!/usr/bin/env python3
import json
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DV/fixed-p2-phi-selmer-required-places-local-image-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DV/phi-selmer-required-place-source-lock.md'
DU=ROOT/'stages/stage36/36-09DU/fixed-p2-phi-selmer-local-condition-defect-preflight.json'

def git_hash(p):
    return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def deriv(a):
    return [F(i)*a[i] for i in range(1,len(a))]

def det(M):
    A=[list(map(F,row)) for row in M]
    n=len(A); d=F(1)
    for col in range(n):
        piv=next((r for r in range(col,n) if A[r][col]),None)
        if piv is None: return F(0)
        if piv!=col:
            A[col],A[piv]=A[piv],A[col]; d=-d
        p=A[col][col]; d*=p
        for j in range(col,n): A[col][j]/=p
        for r in range(col+1,n):
            q=A[r][col]
            if q:
                for j in range(col,n): A[r][j]-=q*A[col][j]
    return d

def resultant_ascending(a,b):
    ad=list(reversed(a)); bd=list(reversed(b)); m=len(a)-1; n=len(b)-1
    N=m+n; M=[]
    for shift in range(n): M.append([F(0)]*shift+ad+[F(0)]*(N-shift-len(ad)))
    for shift in range(m): M.append([F(0)]*shift+bd+[F(0)]*(N-shift-len(bd)))
    return det(M)

def disc(a):
    n=len(a)-1
    r=resultant_ascending(a,deriv(a))
    return ((-1)**(n*(n-1)//2))*r/a[-1]

assert git_hash(CERT)=='cc3c071315c92f4cb398e18d650d5cd3652413c8'
assert git_hash(SOURCE)=='cf822af037a429f8506b8d417c98790541fd08b7'
assert git_hash(DU)=='d2a8bab0ab63406c7c1ced5d077cc523d5648ba2'
c=json.loads(CERT.read_text()); du=json.loads(DU.read_text())
assert c['schema']=='STAGE36_36_09DV_FIXED_P2_PHI_SELMER_REQUIRED_PLACES_LOCAL_IMAGE_PREFLIGHT_V1'
assert c['status']=='PASS_REQUIRED_PLACE_SET_INFINITY_2_3_5_7_GLOBAL_AMBIENT_FINITE_LOCAL_IMAGES_STILL_MISSING'
assert c['batch_parent']['36_09DU_exact_green_head']=='b15538c46239dd7b2948ca722c3f6c9db2d93253'
assert c['batch_parent']['36_09DU_exact_head_ci']=='34240685194/102109753424'
assert c['batch_parent']['36_09DU_promotion_replay_head']=='a2b34030b31f6b034d802cb5e5e94962a40e5c11'
assert c['batch_parent']['36_09DU_promotion_replay_ci']=='34240911378/102110520799'
assert du['Phi_connecting_map_coordinates']['coordinate_connecting_map_constructed'] is True

C=[F(1)]
for q in [F(4),F(1,4),F(9),F(1,9)]: C=pmul(C,[q,F(0),F(1)])
Et=[F(1)]
for q in [F(4),F(1,4),F(9),F(1,9)]: Et=pmul(Et,[q,F(1)])
Es=pmul([F(9,4),F(0),F(1)],[F(64,9),F(0),F(1)])
Er=pmul([F(25,4),F(0),F(1)],[F(100,9),F(0),F(1)])
assert disc(C)==F(5**24*7**8,3**20)
assert disc(Et)==F(5**12*7**4,2**4*3**10)
assert disc(Es)==F(5**8*7**4,3**8)
assert disc(Er)==F(5**12*7**4,2**4*3**10)
assert c['model_discriminants']['coefficient_denominator_prime_support']==[2,3]
assert c['model_discriminants']['discriminant_prime_support']==[2,3,5,7]

S=c['required_places']
assert S['finite']==[2,3,5,7]
assert S['archimedean']==['infinity']
assert S['S']==['infinity',2,3,5,7]
assert S['certified_conservative_required_place_set'] is True
assert S['minimality_of_S_claimed'] is False

assert c['global_unramified_ambient']['Q_S_2_generators']==['[-1]','[2]','[3]','[5]','[7]']
assert c['global_unramified_ambient']['Q_S_2_F2_dimension']==5
assert c['global_unramified_ambient']['H1_S_Q_K_F2_dimension']==15
assert c['global_unramified_ambient']['H1_S_Q_K_cardinality']==32768
assert 2**15==32768
assert c['global_unramified_ambient']['all_global_Phi_Selmer_classes_lie_in_this_ambient'] is True

assert c['local_condition_status']['places_to_compute']==['infinity',2,3,5,7]
assert c['local_condition_status']['coordinate_functions']==['F1','F2','F3']
assert c['local_condition_status']['local_images_computed'] is False
assert c['local_condition_status']['global_Phi_Selmer_group_computed'] is False
assert c['route_result']['next_leaf']=='36-09DW_FIXED_P2_PHI_SELMER_FIVE_PLACE_LOCAL_IMAGE_PREFLIGHT'

src=SOURCE.read_text()
for token in ['unramified outside `S`','S={infinity,2,3,5,7}','Q(S,2)=<-1,2,3,5,7>','2^15=32768']:
    assert token in src
for k in ['Phi_Selmer_local_condition_map_computed','global_Phi_Selmer_group_computed','proSelmer_cokernel_size_computed','proSelmer_product_identification_obtained','T2Sel_J_computed','elliptic_quotient_T2Sel_computed','retained_open_curve_proSelmer_intersection_computed','global_2primary_Brauer_set_nonempty','global_2primary_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_nonexistence_claim']:
    assert c['scope_firewalls'][k] is False,k
print('36-09DV verified: conservative required-place set {infinity,2,3,5,7} and 15-dimensional/32768-class global unramified ambient are exact. Five local images and all downstream credit remain closed.')
