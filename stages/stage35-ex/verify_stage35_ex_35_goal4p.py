#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4p-stage35-specific-vertical-brauer-from-scratch-preflight.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
S21=ROOT/'stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md'
S22=ROOT/'stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json'
S23=ROOT/'stages/stage35-ex/35ex-23/character-quotient-certificate.json'
G4H=ROOT/'stages/stage35-ex/35ex-35/goal4h-vertical-brauer-source-lock-preflight.json'
def blob(p:Path)->str:return subprocess.check_output(['git','hash-object',str(p.relative_to(ROOT))],cwd=ROOT,text=True).strip()
a=json.loads(ART.read_text());s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4P_STAGE35_SPECIFIC_VERTICAL_BRAUER_FROM_SCRATCH_PREFLIGHT_V1'
assert a['base_main_sha']==s['base_main_sha']
assert blob(S21)=='6a8d8c71d50d9667330badca914a8967b4f87577'
assert blob(S22)=='537ca589cd45112cca4c8f8091f5c8c77264e70d'
assert blob(S23)=='2bdb51de3bdda91de54a139e4ca485a7c33082d5'
assert blob(G4H)=='a66c4ef0dff2b96f1c4d6d11223af12d03f639e7'
s22=json.loads(S22.read_text());s23=json.loads(S23.read_text());g4h=json.loads(G4H.read_text())
assert s22['result']['obvious_symbol_layer_Brauer_Manin_obstruction'] is False
assert s22['result']['Brauer_group_computed'] is False
assert s22['result']['nonobvious_Brauer_classes_ruled_out'] is False
assert s23['full_differential_accounting']['generic_fiber_jacobian_five_elliptic_isogeny'] is True
assert s23['uniformity']['all_five_elliptic_factors_nonisotrivial'] is True
assert g4h['result']['S33_PW07_direct_transfer_applicable'] is False
assert g4h['result']['nonobvious_vertical_brauer_mathematical_route_proved_impossible'] is False
g=a['from_scratch_construction_gate']
for k in ['smooth_compactification_and_resolution_materialized','geometric_picard_galois_module_computed','H1_Q_Pic_candidate_space_computed','nonconstant_stage35_brauer_representative_materialized','unramified_residue_proof_for_nonobvious_class_materialized','physical_adelic_evaluation_obstruction_materialized']:
    assert g[k] is False
assert a['exact_interpretation']['five_elliptic_isogeny_implies_brauer_class'] is False
assert a['exact_interpretation']['obvious_symbol_failure_implies_Brauer_group_trivial'] is False
assert a['exact_interpretation']['brauer_manin_obstruction_obtained'] is False
assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V53_GOAL4P_BRAUER_FROM_SCRATCH_INTERFACE_LOCALIZED_PENDING_LATER_AUDIT'
assert s['current']['unit']=='35EX-35_GOAL4P_STAGE35_SPECIFIC_VERTICAL_BRAUER_FROM_SCRATCH_PREFLIGHT'
assert s['claims']['goal4p_executed'] is True
assert s['claims']['stage35_specific_brauer_construction_problem_localized'] is True
assert s['claims']['nonconstant_stage35_brauer_class_constructed'] is False
assert s['claims']['brauer_manin_obstruction_obtained'] is False
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4P_STAGE35_SPECIFIC_VERTICAL_BRAUER_FROM_SCRATCH_PREFLIGHT_V1')
