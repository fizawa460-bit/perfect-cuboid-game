#!/usr/bin/env python3
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4u-coordinate-ramification-divisor-rank64-adapter.json'
LOCK=ROOT/'stages/stage35-ex/35ex-35/goal4u-picard-rank64-source-lock.md'
MODEL=ROOT/'stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md'
Q=ROOT/'stages/stage35-ex/35ex-35/goal4q-compactification-picard-galois-brauer-candidate-preflight.json'
T=ROOT/'stages/stage35-ex/35ex-35/goal4t-full-picard-rank-gap-hodge-cap.json'
MKS=ROOT/'stages/stage33/33-09/marked-picard-basis-source.json'
RES=ROOT/'stages/stage33/33-09/result.md'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

a=json.loads(ART.read_text())
t=json.loads(T.read_text())
q=json.loads(Q.read_text())
lock=LOCK.read_text()

assert a['schema']=='STAGE35_EX_35_GOAL4U_COORDINATE_RAMIFICATION_DIVISOR_RANK64_ADAPTER_V1'
assert a['base_main_sha']=='69ac6635fb7a7808bca7aad72c5b7e61bcb5cbb6'
assert a['parent']['schema']=='STAGE35_EX_PESCH_E1_STATE_V57_GOAL4T_HODGE_CAP_RHO_53_TO_64_PENDING_LATER_AUDIT'
assert a['parent']['hostile_audited'] is False

# Exact local source locks: Goal4U must fail closed if any imported model/Picard
# source or the Hodge-cap parent is edited without an explicit new adapter.
for key,path in [
    ('goal4u_source_lock',LOCK),
    ('stage35ex_global_model',MODEL),
    ('goal4q',Q),
    ('goal4t',T),
    ('stage33_marked_picard_source',MKS),
    ('stage33_result',RES),
]:
    assert git_blob_sha(path)==a['source_locks'][key]['blob_sha'], (key,git_blob_sha(path))

up=a['source_locks']['upstream']
assert up=={
    'repo':'MichaelStollBayreuth/Verification',
    'commit':'51233ed5ef2bf228fac9416c66db9adc0ebcaadd',
    'path':'Cuboids/cuboids.magma',
    'blob_sha':'0422b69847f2afb97cb7b3ed02ebef91279f61b1'
}
assert 'assert #pts eq 48;' in lock
assert 'assert Rank(pairingmat) eq 64;' in lock
assert 'does not use the later upstream comment/assumption' in lock

# Exact model adapter, not a rank-only or birational analogy.
m=a['exact_surface_adapter']
assert m['coordinate_map']=={'a1':'h','a2':'x','a3':'y','b1':'z','b2':'q','b3':'p','c':'w'}
assert m['same_projective_surface'] is True and m['birational_only'] is False
assert set(m['stage35ex_equations'])=={
    'p^2=h^2+x^2','q^2=h^2+y^2','z^2=x^2+y^2','w^2=h^2+x^2+y^2'}
assert q['projective_closure']['ambient']=='P^6'
assert q['projective_closure']['complete_intersection_type']=='(2,2,2,2)'
assert q['singular_locus']['geometric_node_count']==48

# Coordinate/ramification bridge: useful for object identification, but not
# falsely credited as a rank-64 statement by itself.
c=a['coordinate_divisor_alignment']
assert c['C1_block_size']==8
assert [(e['upstream'],e['stage35ex']) for e in c['C1_blocks']]==[
    ('a1=0','h=0'),('a2=0','x=0'),('a3=0','y=0'),('c=0','w=0')]
assert c['goal4q_visible_boundary_block']=='h=0'
assert c['coordinate_conics_alone_rank64_claim'] is False

# The pinned source has 92 nonexceptional known curves plus 48 exceptional
# divisors. Their actual intersection matrix has rank 64 on the exact surface.
k=a['known_divisor_configuration']
assert (k['C1_conics'],k['C2_genus1_curves'],k['C3_genus1_curves'],k['exceptional_divisors'])==(32,12,48,48)
assert k['total_divisors']==32+12+48+48==140
assert k['intersection_matrix_rank']==64
assert k['upstream_exact_assertion']=='assert Rank(pairingmat) eq 64;'

# Independent Hodge cap from Goal4T closes the rank without assuming that the
# known curves generate Picard.
h11=t['topological_hodge_invariants']['h11']
assert h11==64
r=a['rank_proof']
assert r['actual_divisor_intersection_rank_lower_bound']==64
assert r['geometric_picard_rank_lower_bound']==64
assert r['goal4t_h11_upper_bound']==h11
assert r['geometric_picard_rank_upper_bound']==64
assert r['geometric_picard_rank']==64
assert r['missing_picard_rank']==0
assert r['uses_upstream_full_generation_assumption'] is False

f=a['credit_firewall']
for key in ['full_integral_marked_picard_isomorphism_for_stage35ex_computed','full_picard_galois_module_computed','full_Picard_H1_computed','algebraic_brauer_group_computed','nonconstant_stage35_brauer_class_constructed','brauer_manin_obstruction_obtained','E1_proved','R29_PESCH_E1_closed','stage35_closed','perfect_cuboid_nonexistence_claim']:
    assert f[key] is False

st=json.loads(STATE.read_text())
assert st['schema']=='STAGE35_EX_PESCH_E1_STATE_V58_GOAL4U_GEOMETRIC_PICARD_RANK64_PENDING_LATER_AUDIT'
assert st['current']['unit']=='35EX-35_GOAL4U_COORDINATE_RAMIFICATION_DIVISOR_CLASS_RANK_AUGMENTATION_PREFLIGHT'
assert st['claims']['goal4u_executed'] is True
assert st['claims']['geometric_picard_rank_exact'] is True
assert st['claims']['geometric_picard_rank']==64
assert st['claims']['missing_picard_rank_upper_bound']==0
assert st['claims']['full_Picard_H1_computed'] is False
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4U: exact surface adapter + divisor rank 64 + h11 64 forces rho(Xbar)=64')
