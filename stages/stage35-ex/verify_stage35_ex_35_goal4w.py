#!/usr/bin/env python3
"""Verify Goal4W: full Picard H1 vanishes and algebraic Brauer is constant-only."""
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4w-full-picard-h1-algebraic-brauer.json'
LOCK=ROOT/'stages/stage35-ex/35ex-35/goal4w-full-picard-h1-algebraic-brauer-source-lock.md'
V=ROOT/'stages/stage35-ex/35ex-35/goal4v-full-picard-galois-module-adapter.json'
CLOSURE=ROOT/'stages/stage33/33-09/stage33-09-closure.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'

def blob(path:Path)->str:
    d=path.read_bytes();return hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()

a=json.loads(ART.read_text())
v=json.loads(V.read_text())
c=json.loads(CLOSURE.read_text())
s=LOCK.read_text()
st=json.loads(STATE.read_text())

assert a['schema']=='STAGE35_EX_35_GOAL4W_FULL_PICARD_H1_ALGEBRAIC_BRAUER_V1'
assert a['base_main_sha']=='69ac6635fb7a7808bca7aad72c5b7e61bcb5cbb6'
assert a['parent']['schema']=='STAGE35_EX_PESCH_E1_STATE_V59_GOAL4V_FULL_PICARD_GALOIS_MODULE_PENDING_LATER_AUDIT'
assert a['parent']['source_head_sha']=='67db3d433102bf00ca686427a29e5c835cf997ac'
assert a['parent']['snapshot_blob_sha']=='51b047e5da7c9898abc0198cbd36f8929d0f6834'

assert blob(LOCK)==a['source_locks']['goal4w_source_lock']['blob_sha']
assert blob(V)==a['source_locks']['goal4v']['blob_sha']
assert blob(CLOSURE)==a['source_locks']['stage33_picard_transport_closure']['blob_sha']
assert c['canonical_sha256']==a['source_locks']['stage33_picard_transport_closure']['canonical_sha256']

# Parent must be the full integral Picard module, not the old visible rank-53 lattice.
assert v['full_picard_identification']['known_divisor_lattice_equals_full_Picard'] is True
assert v['full_picard_identification']['geometric_picard_rank']==64
assert v['full_picard_identification']['picard_discriminant']=='-2^28'
assert v['galois_module']['absolute_galois_action_factors_through']=='Gal(Q(i,sqrt(2))/Q)'
assert v['galois_module']['finite_quotient_isomorphic_to']=='C2 x C2'
assert v['galois_module']['integral_generators']==['cc','ct']
assert v['galois_module']['matrix_dimension']==64
assert v['galois_module']['full_integral_marked_picard_galois_module_certified'] is True
assert c['historical_q256_basis_marking_exact'] is True
assert 'cc' in c['named_integral_action_coverage'] and 'ct' in c['named_integral_action_coverage']

# Exact external computation/theorem locks. The immutable upstream blob is the
# same source used by the marked Picard transport; Goal4W does not silently
# substitute a finite mod-2 or visible-lattice computation.
u=a['source_locks']['upstream_computation']
assert u=={
    'repository':'MichaelStollBayreuth/Verification',
    'commit':'51233ed5ef2bf228fac9416c66db9adc0ebcaadd',
    'path':'Cuboids/cuboids.magma',
    'git_blob_sha1':'0422b69847f2afb97cb7b3ed02ebef91279f61b1',
    'group_definition':'Gal=<ccPic,ctPic> on Picard rank 64',
    'cohomology_assertion':'assert #H1 eq 1;'
}
assert 'Theorem 10' in s
assert 'assert #H1 eq 1;' in s
assert 'Br_1(X)/Br_0(X) = 0' in s
assert 'transcendental quotient' in s

m=a['full_picard_module_input']
assert m['rank']==64 and m['discriminant']=='-2^28'
assert m['integrally_generated_by_known_divisors'] is True
assert m['torsion_free'] is True
assert m['splitting_field']=='Q(i,sqrt(2))'
assert m['finite_galois_quotient']=='C2 x C2'
assert m['integral_action_generators']==['cc','ct']
assert m['same_module_as_pinned_upstream_cohomology_computation'] is True

h=a['cohomology']
assert h['finite_quotient_H1_order']==1
assert h['finite_quotient_H1_trivial'] is True
assert h['absolute_H1_identified_with_finite_quotient_H1'] is True
assert h['H1_Q_Pic_trivial'] is True and h['H1_Q_Pic_structure']=='0'

b=a['algebraic_brauer']
assert b['hochshild_serre_quotient']=='Br_1(X)/Br_0(X)'
assert b['quotient_isomorphic_to_H1_Q_Pic'] is True
assert b['quotient_trivial'] is True
assert b['nonconstant_algebraic_brauer_class_exists'] is False
assert b['algebraic_brauer_manin_obstruction_available'] is False
assert b['transcendental_brauer_quotient_computed'] is False

r=a['route_result']
assert r['algebraic_brauer_route']=='CLOSED_NEGATIVELY_TRIVIAL_QUOTIENT'
assert r['full_picard_H1_zero_now_certified'] is True
assert r['any_future_brauer_route_must_be_transcendental'] is True

f=a['credit_firewall']
for k in ['transcendental_brauer_group_computed','nonconstant_transcendental_brauer_class_constructed','brauer_manin_obstruction_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
    assert f[k] is False

assert st['schema']=='STAGE35_EX_PESCH_E1_STATE_V60_GOAL4W_FULL_PICARD_H1_ZERO_ALGEBRAIC_BRAUER_CONSTANT_ONLY_PENDING_LATER_AUDIT'
assert st['current']['unit']=='35EX-35_GOAL4W_FULL_PICARD_H1_AND_ALGEBRAIC_BRAUER_PREFLIGHT'
assert st['claims']['full_Picard_H1_computed'] is True
assert st['claims']['full_Picard_H1_trivial'] is True
assert st['claims']['algebraic_brauer_group_computed'] is True
assert st['claims']['algebraic_brauer_quotient_trivial'] is True
assert st['claims']['nonconstant_stage35_algebraic_brauer_class_exists'] is False
assert st['claims']['transcendental_brauer_group_computed'] is False
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4W: H^1(Q,Pic)=0 and Br_1/Br_0=0; transcendental Brauer remains open')
