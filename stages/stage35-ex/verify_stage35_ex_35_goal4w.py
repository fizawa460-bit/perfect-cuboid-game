#!/usr/bin/env python3
"""Verify Goal4W scope repair: proper-S H1/Br1 is zero; open receiver remains untested."""
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

assert a['schema']=='STAGE35_EX_35_GOAL4W_PROPER_SURFACE_H1_ALGEBRAIC_BRAUER_V2'
assert a['base_main_sha']=='69ac6635fb7a7808bca7aad72c5b7e61bcb5cbb6'
assert a['parent']['schema']=='STAGE35_EX_PESCH_E1_STATE_V59_GOAL4V_FULL_PICARD_GALOIS_MODULE_PENDING_LATER_AUDIT'
assert a['parent']['source_head_sha']=='67db3d433102bf00ca686427a29e5c835cf997ac'
assert a['parent']['snapshot_blob_sha']=='51b047e5da7c9898abc0198cbd36f8929d0f6834'

ar=a['hostile_audit_repair']
assert ar['review_id']==5124106960
assert ar['failed_exact_head_sha']=='24cc2973fc022c89cd240fd4a26c92637e1d2e78'
assert ar['verdict']=='FAIL_SCOPE'
assert ar['goal4w_proper_surface_statement']=='PASS'
assert ar['repair_choice']=='SHRINK_GOAL4W_TO_PROPER_S_AND_RESTORE_OPEN_RECEIVER_TO_UNTESTED'

assert blob(LOCK)==a['source_locks']['goal4w_source_lock']['blob_sha']
assert blob(V)==a['source_locks']['goal4v']['blob_sha']
assert blob(CLOSURE)==a['source_locks']['stage33_picard_transport_closure']['blob_sha']
assert c['canonical_sha256']==a['source_locks']['stage33_picard_transport_closure']['canonical_sha256']

# Proper parent Picard module only.
assert v['full_picard_identification']['known_divisor_lattice_equals_full_Picard'] is True
assert v['full_picard_identification']['geometric_picard_rank']==64
assert v['full_picard_identification']['picard_discriminant']=='-2^28'
assert v['galois_module']['absolute_galois_action_factors_through']=='Gal(Q(i,sqrt(2))/Q)'
assert v['galois_module']['integral_generators']==['cc','ct']
assert v['galois_module']['matrix_dimension']==64
assert c['historical_q256_basis_marking_exact'] is True
assert 'cc' in c['named_integral_action_coverage'] and 'ct' in c['named_integral_action_coverage']

# Theorem/upstream computation is deliberately locked to the smooth proper S.
u=a['source_locks']['upstream_computation']
assert u['commit']=='51233ed5ef2bf228fac9416c66db9adc0ebcaadd'
assert u['git_blob_sha1']=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'
assert u['cohomology_assertion']=='assert #H1 eq 1;'
assert 'H^1(Q,Pic(Sbar)) = 0' in s
assert 'Br_1(S)/Br_0(S) = 0' in s
# The open quotient may appear textually only as an explicitly unproved target;
# the machine certificate below is the authoritative fail-close on its status.
assert 'It does not compute `Pic(Ubar)` or `Br_1(U)/Br_0(U)`' in s
assert 'Goal4W does **not** prove any of the following:' in s
assert 'Stage35 open-receiver algebraic Brauer route remains untested' in s

p=a['proper_surface']
assert p['kind']=='SMOOTH_PROPER_MINIMAL_RESOLUTION'
assert p['picard_rank']==64
assert p['H1_Q_Pic_structure']=='0'
assert p['Br1_mod_Br0_structure']=='0'
assert p['nonconstant_algebraic_brauer_class_exists'] is False
assert p['algebraic_brauer_route']=='CLOSED_NEGATIVELY_FOR_PROPER_S_ONLY'

# Audit-critical fail-close: no promotion to U without boundary/localization data.
o=a['stage35_open_receiver']
assert o['boundary_divisor_complex_source_locked'] is False
assert o['Pic_Ubar_computed'] is False
assert o['Pic_Ubar_galois_module_computed'] is False
assert o['purity_localization_residues_computed'] is False
assert o['H1_Q_Pic_Ubar_computed'] is False
assert o['Br1_U_mod_Br0_U_computed'] is False
assert o['nonconstant_algebraic_brauer_class_exists'] is None
assert o['algebraic_brauer_manin_obstruction_available'] is None
assert o['B7_vertical_brauer_obstruction_status']=='UNTESTED_NOT_BLOCKED_BY_PROPER_S_H1_ZERO'
assert o['algebraic_brauer_route']=='UNTESTED_BOUNDARY_LOCALIZATION_ADAPTER_REQUIRED'

r=a['route_result']
assert r['proper_surface_algebraic_brauer_route']=='CLOSED_NEGATIVELY_TRIVIAL_QUOTIENT'
assert r['stage35_open_receiver_algebraic_brauer_route']=='UNTESTED'
assert r['any_future_brauer_route_must_be_transcendental'] is False
assert r['proper_to_open_promotion_allowed'] is False

f=a['credit_firewall']
for k in ['open_receiver_algebraic_brauer_group_computed','transcendental_brauer_group_computed','nonconstant_stage35_brauer_class_constructed','brauer_manin_obstruction_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
    assert f[k] is False

assert st['schema']=='STAGE35_EX_PESCH_E1_STATE_V60_GOAL4W_PROPER_SURFACE_H1_ZERO_OPEN_RECEIVER_BRAUER_UNTESTED_PENDING_LATER_AUDIT'
assert st['current']['unit']=='35EX-35_GOAL4W_FULL_PICARD_H1_AND_ALGEBRAIC_BRAUER_PREFLIGHT'
assert st['claims']['proper_surface_full_Picard_H1_computed'] is True
assert st['claims']['proper_surface_full_Picard_H1_trivial'] is True
assert st['claims']['proper_surface_algebraic_brauer_quotient_trivial'] is True
assert st['claims']['open_receiver_Picard_group_computed'] is False
assert st['claims']['open_receiver_algebraic_brauer_group_computed'] is False
assert st['claims']['nonconstant_stage35_open_receiver_algebraic_brauer_class_exists'] is None
assert st['claims']['B7_vertical_brauer_obstruction_status']=='UNTESTED'
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4W scope repair: proper S has H1=0 and Br1/Br0=0; open U algebraic Brauer remains UNTESTED')
