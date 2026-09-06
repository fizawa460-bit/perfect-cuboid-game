#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4n-post-sqrt-exact-zero-finite-height-preflight.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
G4M=ROOT/'stages/stage35-ex/35ex-35/goal4m-stage14-global-triple-population-height-transfer.json'
G4I=ROOT/'stages/stage35-ex/35ex-35/goal4i-v2-infinite-descent-self-map-preflight.json'
FINAL=ROOT/'stages/stage14/final.md'
def blob(p:Path)->str:
    return subprocess.check_output(['git','hash-object',str(p.relative_to(ROOT))],cwd=ROOT,text=True).strip()
a=json.loads(ART.read_text()); s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4N_POST_SQRT_EXACT_ZERO_FINITE_HEIGHT_PREFLIGHT_V1'
assert a['base_main_sha']==s['base_main_sha']
assert a['stacked_parent']['hostile_audited'] is False
assert blob(G4M)=='1c7a3e9e23dd8bbc41fc331b8c43e4023f5d3909'
assert blob(G4I)=='d9121d2fdb9b202bc0ffc72678e74e9ccb5a87c2'
assert blob(FINAL)=='f6520537c05a0e537d587a8c7777bb75d420c379'
g4m=json.loads(G4M.read_text()); g4i=json.loads(G4I.read_text())
assert g4m['derived_triple_population_corollary']['conclusion']=='T(B)<<B^{1/2+o(1)}'
assert g4m['derived_triple_population_corollary']['eventual_emptiness_obtained'] is False
assert g4m['credit_boundary']['finite_height_reduction_obtained'] is False
assert g4i['result']['minimum_v2_scalar_descent_route_closed'] is True
assert g4i['result']['genuine_nonlinear_v2_infinite_descent_constructed'] is False
final=FINAL.read_text()
assert 'strict fixed-power improvement `B^(1/2-delta)` is also not proved' in final
assert 'It neither proves `T(B)=0` nor produces a member of `T(B)`.' in final
mechs={x['id']:x for x in a['logical_gate']['sufficient_conversion_mechanisms_checked']}
assert set(mechs)=={'EVENTUAL_ZERO_THEOREM','EFFECTIVE_FINITE_HEIGHT_REDUCTION','STRICT_HEIGHT_DECREASING_FULL_ENDPOINT_SELF_MAP','SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION'}
assert all(x['current_asset_available'] is False for x in mechs.values())
v=a['exact_current_asset_verdict']
assert v['sqrt_bound_to_eventual_zero_conversion_obtained'] is False
assert v['effective_global_height_bound_obtained'] is False
assert v['full_endpoint_strict_descent_self_map_obtained'] is False
assert v['super_sqrt_distinct_class_amplification_obtained'] is False
assert v['finite_exhaustive_search_authorized'] is False
assert v['mathematical_nonexistence_of_any_future_zero_conversion_method_claimed'] is False
assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V51_GOAL4N_POST_SQRT_ZERO_CONVERSION_FAILCLOSE_PENDING_LATER_AUDIT'
assert s['current']['unit']=='35EX-35_GOAL4N_POST_SQRT_EXACT_ZERO_OR_FINITE_HEIGHT_REDUCTION_PREFLIGHT'
assert s['claims']['goal4n_executed'] is True
assert s['claims']['post_sqrt_zero_conversion_obtained'] is False
assert s['claims']['finite_height_reduction_obtained'] is False
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
assert s['claims']['perfect_cuboid_nonexistence_claim'] is False
print('PASS STAGE35_EX_35_GOAL4N_POST_SQRT_EXACT_ZERO_FINITE_HEIGHT_PREFLIGHT_V1')
