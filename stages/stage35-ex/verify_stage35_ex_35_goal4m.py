#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4m-stage14-global-triple-population-height-transfer.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
FINAL=ROOT/'stages/stage14/final.md'
G4L=ROOT/'stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json'
S3SNAP=ROOT/'stages/stage35-ex/snapshots/STAGE14-S3-result-46e5b7cf383d.md'
AUDITED='6fa39f76be24b55153f118812b1bd7f41c43e399'

def blob(path: Path) -> str:
    return subprocess.check_output(['git','hash-object',str(path.relative_to(ROOT))],cwd=ROOT,text=True).strip()

a=json.loads(ART.read_text()); s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4M_STAGE14_GLOBAL_TRIPLE_POPULATION_HEIGHT_TRANSFER_V1'
assert a['base_main_sha']==s['base_main_sha']
assert a['stacked_parent']['hostile_audited'] is False
assert blob(FINAL)=='f6520537c05a0e537d587a8c7777bb75d420c379'
assert blob(G4L)=='0717ca307162d5559a005801848288daa91285fd'
assert blob(S3SNAP)=='830f124e3b22e47693eec101f407e7d402b437d9'

final=FINAL.read_text()
assert 'E(B)=N_2(B)+3T(B)' in final
assert 'E(B)\\ll V(B)B^{o(1)}' in final
assert 'V(B)\\ll B^{1/2+o(1)}' in final
assert 'It neither proves `T(B)=0` nor produces a member of `T(B)`.' in final
assert 'strict fixed-power improvement `B^(1/2-delta)` is also not proved' in final

g4l=json.loads(G4L.read_text())
assert g4l['rank_jump_receiver']['new_receiver_obtained'] is True
assert 'positive Mordell-Weil rank' in g4l['rank_jump_receiver']['endpoint_consequence']
assert g4l['credit_boundary']['uniform_rank_jump_exclusion_obtained'] is False

s3_text=S3SNAP.read_text()
assert 'physical hit below B' in s3_text
assert r'\hat h(P)=O(\log B+\log H)' in s3_text
assert 'PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW=true' in s3_text
assert 'UNIFORM_FIRST_GENERATOR_DISTRIBUTION_PROVED=false' in s3_text

old_text=subprocess.check_output(['git','show',f'{AUDITED}:stages/stage35-ex/MAIN-STATE.json'],cwd=ROOT,text=True)
old=json.loads(old_text)
assert old['target']['audited_endpoint_relation']=='E1 counterexamples modulo source-pair swap are exactly positive rational perfect cuboids modulo positive scaling and edge permutation'
assert subprocess.check_output(['git','rev-parse',f'{AUDITED}:stages/stage35-ex/MAIN-STATE.json'],cwd=ROOT,text=True).strip()=='5030d3e67914f8fd34c0175f8497ccc222c81011'

assert a['derived_triple_population_corollary']['conclusion']=='T(B)<<B^{1/2+o(1)}'
assert a['derived_triple_population_corollary']['strict_subsqrt_power_saving_obtained'] is False
assert a['derived_triple_population_corollary']['eventual_emptiness_obtained'] is False
assert a['derived_triple_population_corollary']['perfect_cuboid_nonexistence_obtained'] is False
assert a['stage35_e1_class_transfer']['audited_equivalence_used'] is True
assert a['stage35_e1_class_transfer']['finite_total_class_count_proved'] is False
assert a['stage35_e1_class_transfer']['zero_class_count_proved'] is False
assert a['rankjump_height_interpretation']['stage14_logarithmic_canonical_height_window_imported'] is True
assert a['rankjump_height_interpretation']['uniform_distribution_of_least_nontorsion_heights_proved'] is False
assert a['route_decision']['new_global_population_theorem_obtained'] is True
assert a['route_decision']['exact_endpoint_elimination_obtained'] is False

assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V50_GOAL4M_STAGE14_GLOBAL_TRIPLE_SQRT_TRANSFER_PENDING_LATER_AUDIT'
assert s['current']['unit']=='35EX-35_GOAL4M_UNIFORM_RANK_JUMP_FIRST_SMALL_POINT_HEIGHT_PREFLIGHT'
assert s['claims']['goal4m_executed'] is True
assert s['claims']['perfect_cuboid_triple_sqrt_upper_bound_obtained'] is True
assert s['claims']['E1_counterexample_class_sqrt_upper_bound_obtained'] is True
assert s['claims']['first_nontorsion_point_height_bound_obtained'] is True
assert s['claims']['strict_subsqrt_power_saving_obtained'] is False
assert s['claims']['finite_height_reduction_obtained'] is False
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
assert s['claims']['perfect_cuboid_nonexistence_claim'] is False
print('PASS STAGE35_EX_35_GOAL4M_STAGE14_GLOBAL_TRIPLE_POPULATION_HEIGHT_TRANSFER_V1')
