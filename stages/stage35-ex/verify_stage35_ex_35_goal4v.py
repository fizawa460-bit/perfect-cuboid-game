#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4v-full-picard-galois-module-adapter.json'
LOCK = ROOT / 'stages/stage35-ex/35ex-35/goal4v-full-picard-galois-source-lock.md'
U = ROOT / 'stages/stage35-ex/35ex-35/goal4u-coordinate-ramification-divisor-rank64-adapter.json'
S33SRC = ROOT / 'stages/stage33/33-09/marked-picard-basis-source.json'
S33BRIDGE = ROOT / 'stages/stage33/33-09/marked-picard-basis-bridge-certified.json'
S33CLOSURE = ROOT / 'stages/stage33/33-09/stage33-09-closure.json'
S33CERT = ROOT / 'stages/stage33/33-09/certify_stage33_09_exit.py'
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


a = json.loads(ART.read_text())
u = json.loads(U.read_text())
lock = LOCK.read_text()

assert a['schema'] == 'STAGE35_EX_35_GOAL4V_FULL_PICARD_GALOIS_MODULE_ADAPTER_V1'
assert a['base_main_sha'] == '69ac6635fb7a7808bca7aad72c5b7e61bcb5cbb6'
assert a['parent']['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V58_GOAL4U_GEOMETRIC_PICARD_RANK64_PENDING_LATER_AUDIT'
assert a['parent']['source_head_sha'] == 'addbe2cd7f0d16a1414319a5a2a8386a4d0d7720'
assert a['parent']['hostile_audited'] is False

# Fail closed on all local source objects, including the large certified bridge.
for key, path in [
    ('goal4v_source_lock', LOCK),
    ('goal4u', U),
    ('stage33_marked_source', S33SRC),
    ('stage33_certified_bridge', S33BRIDGE),
    ('stage33_closure', S33CLOSURE),
    ('stage33_certifier', S33CERT),
]:
    assert git_blob_sha(path) == a['source_locks'][key]['blob_sha'], (key, git_blob_sha(path))

# Exact theory version lock. arXiv versioned identifiers are immutable locators.
th = a['source_locks']['stoll_testa_theorem']
assert th['arxiv_id'] == '1009.0388v2'
assert th['revision_date'] == '2025-02-24'
assert th['load_bearing_result'] == 'Theorem 8'
assert th['theorem10_imported_here'] is False
for needle in [
    'arXiv:1009.0388v2',
    'Theorem 8',
    'full geometric Picard group',
    'Q(i,sqrt(2))',
    'does not import Theorem 10',
]:
    assert needle in lock

# Goal4U exact surface identity is the semantic adapter into the theorem's S.
m = a['exact_surface_and_resolution_adapter']
assert u['exact_surface_adapter']['coordinate_map'] == m['coordinate_map']
assert u['exact_surface_adapter']['same_projective_surface'] is True
assert u['known_divisor_configuration']['total_divisors'] == 140
assert u['known_divisor_configuration']['intersection_matrix_rank'] == 64
assert u['rank_proof']['geometric_picard_rank'] == 64
assert m['same_projective_surface'] is True
assert m['same_48_A1_singularities'] is True
assert m['same_minimal_desingularization'] is True
assert m['birational_only'] is False

# Replay Stage33's exact integral marking/action certifier runner-side. This is the
# context-safe path for the >64KiB bridge and retained encoded Picard payloads.
proc = subprocess.run(
    [sys.executable, '-B', str(S33CERT)],
    cwd=str(ROOT),
    check=True,
    capture_output=True,
    text=True,
)
out = proc.stdout
assert 'STAGE33_09_LOCAL_CERTIFICATE_REPLAY=PASS_EXACT' in out
assert 'STAGE33_09_PICARD_EQUIVARIANT_TRANSPORT=PASS_EXACT' in out
assert 'REPLAYED=BRIDGE_INVERSE,DETERMINANT,GRAM,CC_CT_7SIGNS,SWAPS_INVOLUTIONS_ISOMETRIES,S3,SIGN_CONJUGATION' in out

closure = json.loads(S33CLOSURE.read_text())
body = dict(closure)
claimed = body.pop('canonical_sha256')
assert claimed == csha(body)
assert claimed == a['source_locks']['stage33_closure']['canonical_sha256']
assert closure['historical_q256_basis_marking_exact'] is True
assert closure['exit_condition']['PICARD_EQUIVARIANT_TRANSPORT_CLOSED'] is True
assert closure['exit_condition']['NAMED_INTEGRAL_AND_TWO_TORSION_ACTIONS_SOURCE_LOCKED'] is True
assert {'cc', 'ct'}.issubset(set(closure['named_integral_action_coverage']))

src = json.loads(S33SRC.read_text())
src_body = dict(src)
src_claimed = src_body.pop('canonical_sha256')
assert src_claimed == csha(src_body)
assert src_claimed == a['source_locks']['stage33_marked_source']['canonical_sha256']
assert len(src['indlist_1based']) == 64
assert len(src['indlist_to_magma_picard_matrix_64x64']) == 64
assert all(len(row) == 64 for row in src['indlist_to_magma_picard_matrix_64x64'])

# Theory saturation + exact integral marking upgrades the modeled lattice to the
# actual full geometric Picard group for this exact Stage35-EX surface.
p = a['full_picard_identification']
assert p['geometric_picard_rank'] == 64
assert p['known_divisor_count'] == 140
assert p['known_divisor_intersection_rank'] == 64
assert p['theorem8_full_integral_generation'] is True
assert p['known_divisor_lattice_equals_full_Picard'] is True
assert p['finite_index_overlattice_remaining'] is False
assert p['picard_discriminant'] == '-2^28'
assert p['integral_marked_basis_rank'] == 64

# Since the full set of generators is defined over L=Q(i,sqrt(2)), the absolute
# action factors through V4 and is determined by the exact integral cc/ct actions.
g = a['galois_module']
assert g['field_of_definition_of_generators'] == 'Q(i,sqrt(2))'
assert g['absolute_galois_action_factors_through'] == 'Gal(Q(i,sqrt(2))/Q)'
assert g['finite_quotient_isomorphic_to'] == 'C2 x C2'
assert g['integral_generators'] == ['cc', 'ct']
assert g['matrix_dimension'] == 64
assert g['matrix_ring'] == 'Z'
assert g['stage33_exact_intertwining_replayed'] is True
assert g['historical_q256_basis_marking_exact'] is True
assert g['full_integral_marked_picard_galois_module_certified'] is True

f = a['credit_firewall']
for key in [
    'full_Picard_H1_computed',
    'algebraic_brauer_group_computed',
    'stoll_testa_theorem10_imported',
    'nonconstant_stage35_brauer_class_constructed',
    'brauer_manin_obstruction_obtained',
    'E1_proved',
    'R29_PESCH_E1_closed',
    'R29_FIB2_closed',
    'stage35_closed',
    'perfect_cuboid_existence_claim',
    'perfect_cuboid_nonexistence_claim',
]:
    assert f[key] is False

st = json.loads(STATE.read_text())
assert st['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V59_GOAL4V_FULL_PICARD_GALOIS_MODULE_PENDING_LATER_AUDIT'
assert st['current']['unit'] == '35EX-35_GOAL4V_FULL_PICARD_GALOIS_MODULE_MARKED_BASIS_ADAPTER_PREFLIGHT'
assert st['claims']['goal4v_executed'] is True
assert st['claims']['full_geometric_picard_group_computed'] is True
assert st['claims']['full_integral_marked_picard_isomorphism_for_stage35ex_computed'] is True
assert st['claims']['full_picard_galois_module_computed'] is True
assert st['claims']['full_Picard_H1_computed'] is False
assert st['claims']['algebraic_brauer_group_computed'] is False
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4V: Theorem8 saturation + exact Stage33 cc/ct transport gives the full integral Picard Galois module')
