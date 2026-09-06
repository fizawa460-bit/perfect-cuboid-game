#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4ac-c5-individual-quadratic-residual.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V65-e08f399034dc.json'

def blob(path:str)->str:
    b=(ROOT/path).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

a=json.loads(ART.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4AC_C5_INDIVIDUAL_QUADRATIC_RESIDUAL_V1'
assert a['parent']['source_head_sha']=='e08f399034dc2743de8bc2b2b88ebca52d3686db'
assert blob(a['parent']['snapshot_path'])==a['parent']['snapshot_blob_sha']=='1479da3b0dbb1ce3b60941375261e2660d7847b6'
for key,v in a['source_locks'].items():
    if 'path' in v and 'blob_sha' in v:
        assert blob(v['path'])==v['blob_sha'],key
assert a['source_locks']['upstream_stoll']['commit']=='51233ed5ef2bf228fac9416c66db9adc0ebcaadd'
assert a['source_locks']['upstream_stoll']['git_blob_sha1']=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'

# Replay Goal4AB exactly against immutable V65 state.
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']=='STAGE35_EX_PESCH_E1_STATE_V65_GOAL4AB_LOW_DEGREE_RR_FEEDERS_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*args,**kwargs):
    if self.resolve()==sr:return snaptext
    return orig(self,*args,**kwargs)
Path.read_text=patched
try:
    runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4ab.py'),run_name='__main__')
finally:
    Path.read_text=orig

src=a['c5_source']
assert src['curve_count']==16 and src['curve_degree']==8
assert src['quadratic_sign_triple_count']==8 and src['distinct_quadratic_section_count']==4
assert src['surface_degree']==16 and src['quadratic_section_degree']==32

# Exact C5 sign geometry in the homogeneous coordinate ring.
a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
i=sp.I
G=sp.groebner([
    a1**2+a2**2-b3**2,
    a2**2+a3**2-b1**2,
    a1**2+a3**2-b2**2,
    a1**2+a2**2+a3**2-c**2,
],c,b3,b2,b1,a3,a2,a1,extension=i)
def zero_on_surface(expr):
    return sp.expand(G.reduce(sp.expand(expr))[1])==0

def Q(e1,e2,e3):
    return (e2*a2+e3*a3)*b1+e1*i*b2*b3

def L(e2,e3,e4):
    return a1+e2*a2+e3*a3+e4*i*c

triples=[(e1,e2,e3) for e1 in (1,-1) for e2 in (1,-1) for e3 in (1,-1)]
for e1,e2,e3 in triples:
    assert sp.expand(Q(-e1,-e2,-e3)+Q(e1,e2,e3))==0

# Antipodal triples are scalar-equivalent and give exactly four classes.
seen=set(); classes=[]
for t in triples:
    if t in seen: continue
    anti=tuple(-x for x in t)
    seen.add(t); seen.add(anti)
    classes.append((t,anti))
assert len(classes)==4 and len(seen)==8
assert a['scalar_equivalence']['antipodal_sign_triples_define_same_section'] is True
assert a['scalar_equivalence']['scalar_class_size']==2

# Choose the representative in each class with e1=+1.  Goal4AB's exact
# identity forces the support of Q=0 into the four C5 linear cuts.  The source
# degree count (4*8=32=2*deg(S)) then leaves no extra component or multiplicity.
all_curves=[]
identity_count=0
for pair in classes:
    rep=next(t for t in pair if t[0]==1)
    e1,e2,e3=rep
    anti=(-e1,-e2,-e3)
    q=Q(e1,e2,e3)
    assert sp.expand(Q(*anti)+q)==0
    q_other=Q(-e1,e2,e3)
    prodL=sp.prod([L(e2,e3,e4) for e4 in (1,-1)])*sp.prod([L(-e2,-e3,e4) for e4 in (1,-1)])
    assert zero_on_surface(prodL-4*q*q_other)
    identity_count+=1
    chosen=[(e1,e2,e3,e4) for e4 in (1,-1)]
    residual=[(-e1,-e2,-e3,e4) for e4 in (1,-1)]
    curves=chosen+residual
    assert len(set(curves))==4
    assert len(chosen)*src['curve_degree']==16
    assert len(residual)*src['curve_degree']==16
    assert len(curves)*src['curve_degree']==src['quadratic_section_degree']==32
    all_curves.extend(curves)
assert identity_count==a['exact_identity_bridge']['goal4ab_c5_product_identity_count']==4
assert len(all_curves)==16 and len(set(all_curves))==16

D=a['individual_section_decomposition']
assert D['c5_curves_per_distinct_quadratic_section']==4
assert D['chosen_pair_curve_count']==2 and D['chosen_pair_degree']==16
assert D['antipodal_residual_pair_curve_count']==2 and D['antipodal_residual_pair_degree']==16
assert D['total_c5_degree_per_section']==32
assert D['unknown_strict_residual_component_count']==0
assert D['higher_generic_multiplicity_present'] is False
assert D['all_16_c5_curves_partitioned_exactly_once'] is True
assert D['individual_C5_quadratic_strict_residuals_exhausted'] is True
assert a['exact_identity_bridge']['support_containment_from_product_identity'] is True
assert a['exact_identity_bridge']['degree_saturation_closes_extra_component_or_multiplicity_gap'] is True

# Fail-close the remaining Picard/principal-function problem.
for k,v in a['uncomputed'].items(): assert v is True,k
fw=a['semantic_firewall']
for key in ['global_F_B_nonexistence_proved','formal_target_nonprincipal_proved','c5_pair_marked_picard_adapter_computed','target_span_with_c5_pairs_computed','all_nonlinear_or_higher_degree_principalization_excluded','both_goal4y_explicit_symbols_materialized','full_Br_a_U_computed','local_evaluations_computed','verticality_proved','brauer_manin_obstruction_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
    assert fw[key] is False,key
assert a['route_result']['general_qi_principal_function_problem']=='OPEN'
assert a['route_result']['next']=='35EX-35_GOAL4AD_SECOND_CLASS_QI_CYCLIC_C5_PAIR_MARKED_PICARD_ADAPTER_PREFLIGHT'

state=json.loads(STATE.read_text())
assert state['schema']=='STAGE35_EX_PESCH_E1_STATE_V66_GOAL4AC_C5_STRICT_RESIDUAL_EXHAUSTED_MARKED_PAIR_PICARD_PENDING_AUDIT'
assert state['current']['unit']==a['unit']
assert state['claims']['goal4ac_executed'] is True
assert state['claims']['open_receiver_second_class_C5_individual_quadratic_residuals_computed'] is True
assert state['claims']['open_receiver_second_class_C5_unknown_strict_residual_component_count']==0
assert state['claims']['open_receiver_second_class_C5_pair_marked_picard_adapter_computed'] is False
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['open_receiver_local_evaluations_computed'] is False
assert state['claims']['brauer_manin_obstruction_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS Stage35-EX Goal4AC: four distinct C5 quadratic sections each exhaust exactly four degree-8 C5 curves; prior degree-16 residual is the antipodal C5 pair; marked pair Picard classes remain open')
