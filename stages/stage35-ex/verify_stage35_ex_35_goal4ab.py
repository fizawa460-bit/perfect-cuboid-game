#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4ab-second-class-qi-cyclic-low-degree-rr-blocker.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V64-691e934b0f7b.json'

def blob(path:str)->str:
    b=(ROOT/path).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

a=json.loads(ART.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4AB_QI_CYCLIC_LOW_DEGREE_RIEMANN_ROCH_BLOCKER_V1'
assert blob(a['parent']['snapshot_path'])==a['parent']['snapshot_blob_sha']=='8122328a4f6592de1756a560f86f5999ec4310a7'
assert a['parent']['source_head_sha']=='691e934b0f7b2048cc4c862d3aeea6873c784b52'
for key,v in a['source_locks'].items():
    if 'path' in v and 'blob_sha' in v:
        assert blob(v['path'])==v['blob_sha'],key
assert a['source_locks']['upstream_stoll']['commit']=='51233ed5ef2bf228fac9416c66db9adc0ebcaadd'
assert a['source_locks']['upstream_stoll']['git_blob_sha1']=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'
assert a['source_locks']['arsenal_s33_pw07']['role']=='SEMANTIC_FIREWALL_ONLY_PROVISIONAL_NO_THEOREM_CREDIT'

# Replay Goal4AA exactly against immutable V64 state, then reuse only its
# deterministic reconstructed section/divisor data.  No temporary probe is used.
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']=='STAGE35_EX_PESCH_E1_STATE_V64_GOAL4AA_LINEAR_HYPERPLANE_PRODUCT_ROUTE_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*args,**kwargs):
    if self.resolve()==sr:return snaptext
    return orig(self,*args,**kwargs)
Path.read_text=patched
try:
    ns=runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4aa.py'))
finally:
    Path.read_text=orig

raw=ns['raw']; known=ns['known']; anchor_class=ns['anchor_class']; picclass=ns['picclass']; formal=ns['formal']
lin=a['exact_linear_completion']
assert len(ns['groups'])==lin['retained_distinct_linear_form_count']==79
assert len(raw)==lin['raw_degree16_linear_section_count']==43
assert sum(x!=0 for x in formal)==a['class_B_target']['formal_target_support_count']==69

# The 48 exceptional classes are independent.  Since every raw strict divisor
# already has total degree 16, H-[C_L] must be supported on exceptionals.  Solve
# this correction exactly for each of the 43 source linear sections.
Ecols=sp.Matrix(64,48,lambda i,j: known[92+j][i])
assert Ecols.rank()==lin['exceptional_class_rank']==48
full={}; hist={}; fail=0
for L,cs in raw.items():
    strict=[0]*140
    for ci in cs: strict[ci-1]+=1
    rhs=sp.Matrix(anchor_class)-sp.Matrix(picclass(strict))
    solset=sp.linsolve((Ecols,rhs))
    if solset==sp.EmptySet:
        fail+=1; continue
    sols=list(solset)
    assert len(sols)==1
    x=list(sols[0])
    assert not any(v.free_symbols for v in x)
    assert all(v.q==1 for v in x)
    xi=[int(v) for v in x]
    assert all(v>=0 for v in xi)
    vec=strict[:]
    for j,v in enumerate(xi): vec[92+j]=v
    assert picclass(vec)==anchor_class
    full[L]=vec
    for v in xi: hist[str(v)]=hist.get(str(v),0)+1
assert fail==lin['completion_fail_count']==0
assert len(full)==lin['exact_complete_linear_section_count']==43
assert hist==lin['exceptional_multiplicity_histogram']=={'0':1680,'1':336,'2':48}

M=sp.Matrix(140,len(full),lambda i,j:list(full.values())[j][i])
v=sp.Matrix(formal)
assert M.rank()==lin['complete_divisor_matrix_rank']==31
assert sp.linsolve((M,v))==sp.EmptySet
assert lin['formal_target_in_Q_span_of_all_43_complete_sections'] is False
vals=list(full.values())
D=sp.Matrix(140,len(vals)-1,lambda i,j: vals[j+1][i]-vals[0][i])
assert D.rank()==lin['difference_divisor_matrix_rank']==30
assert sp.linsolve((D,v))==sp.EmptySet
assert lin['formal_target_in_Q_span_of_complete_section_differences'] is False

# Exact natural C4/C5 low-degree elimination identities in the homogeneous
# coordinate ring of the projective cuboid surface.
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

c4_specs=[
    (1,1,a2*a3,i*a1*b1),
    (i,1,a1*a3,b2*c),
    (1,i,a1*a2,b3*c),
    (i,i,a2*a3,b1*c),
]
for alpha2,alpha3,q0,q1 in c4_specs:
    lp=sp.prod([b1+e2*alpha2*b2+e3*alpha3*b3 for e2 in (1,-1) for e3 in (1,-1)])
    qp=(q0+q1)*(q0-q1)
    assert zero_on_surface(lp+4*qp)

c5_count=0
for e2 in (1,-1):
    for e3 in (1,-1):
        l1=sp.prod([a1+e2*a2+e3*a3+e4*i*c for e4 in (1,-1)])
        l2=sp.prod([a1-e2*a2-e3*a3+e4*i*c for e4 in (1,-1)])
        qp=sp.prod([(e2*a2+e3*a3)*b1+e1*i*b2*b3 for e1 in (1,-1)])
        assert zero_on_surface(l1*l2-4*qp)
        c5_count+=1
nl=a['retained_low_degree_nonlinear']
assert len(c4_specs)==nl['C4_degree_balanced_exact_identity_count']==4
assert c5_count==nl['C5_paired_quadratic_exact_identity_count']==4
assert nl['all_identities_checked_mod_surface_defining_quadrics'] is True
assert nl['aggregate_elimination_adds_new_divisor_direction'] is False
assert nl['individual_C5_quadratic_residual_divisors_exhausted'] is False

# Fail-close the exact bounded scope and the live V65 authority boundary.
fw=a['semantic_firewall']
for key in ['global_F_B_nonexistence_proved','formal_target_nonprincipal_proved','all_nonlinear_or_higher_degree_principalization_excluded','individual_C5_quadratic_residual_divisors_exhausted','both_goal4y_explicit_symbols_materialized','full_Br_a_U_computed','local_evaluations_computed','verticality_proved','brauer_manin_obstruction_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
    assert fw[key] is False,key
assert a['route_result']['bounded_negative_result']=='ALL_43_RETAINED_DEGREE16_LINEAR_SECTIONS_PLUS_NATURAL_C4_C5_LOW_DEGREE_ELIMINATIONS_DO_NOT_SYNTHESIZE_F_B'
assert a['route_result']['general_qi_principal_function_problem']=='OPEN'
assert a['route_result']['next']=='35EX-35_GOAL4AC_SECOND_CLASS_QI_CYCLIC_C5_RESIDUAL_QUADRATIC_SECTION_PREFLIGHT'

state=json.loads(STATE.read_text())
assert state['schema']=='STAGE35_EX_PESCH_E1_STATE_V65_GOAL4AB_LOW_DEGREE_RR_FEEDERS_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
assert state['current']['unit']==a['unit']
assert state['claims']['goal4ab_executed'] is True
assert state['claims']['open_receiver_second_class_all_43_degree16_linear_sections_completed'] is True
assert state['claims']['open_receiver_second_class_linear_section_divisor_span_rank']==31
assert state['claims']['open_receiver_second_class_low_degree_C4_C5_nonlinear_elimination_route_blocked'] is True
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['open_receiver_local_evaluations_computed'] is False
assert state['claims']['brauer_manin_obstruction_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS Stage35-EX Goal4AB: all 43 degree-16 linear sections exactly completed; target remains outside rank-31 span; natural C4/C5 low-degree eliminations collapse to identities; general F_B remains open')
