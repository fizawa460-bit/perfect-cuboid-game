#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
ctrl=ROOT/'stages/stage33/controller.json'
cert=ROOT/'stages/stage33/33-11/stage33-11-carrier-geometric-orbit-reduction.json'
c=json.loads(ctrl.read_text()); x=json.loads(cert.read_text()); s=x['summary']
if x.get('schema')!='STAGE33_11_CARRIER_GEOMETRIC_ORBIT_REDUCTION_V1': raise SystemExit('orbit schema moved')
if s.get('original_carrier_count')!=30 or not s.get('all_30_original_carriers_partitioned_exactly'): raise SystemExit('orbit partition incomplete')
children={z['id']:z for z in c['repair_children']}; q=children['33-11']; r=children['33-12']
q['carrier_geometric_orbit_reduction']={'certificate_sha256':x['canonical_sha256'],'original_carrier_count':30,'geometric_orbit_count':s['geometric_orbit_count'],'unresolved_original_carrier_count':s['unresolved_original_carrier_count'],'unresolved_geometric_orbit_count':s['unresolved_geometric_orbit_count'],'prime_refinement_representatives':s['prime_refinement_representatives'],'exact_stage33_11_columns_promoted':0}
q['connecting_columns_exact_audited']=0; q['exact_exit_progress']='0/26'; q['audit_required']=True
r['status']='BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE'; r['prerequisites_satisfied']=False
c['current_item']='Stage33-11_MAIN_CARRIER_GEOMETRIC_ORBIT_REDUCTION_DONE'; c['next_item']='Stage33-11_MAIN_FACTOR_PRIME_REFINEMENT_ORBIT_REPRESENTATIVES'; c['next_expected_command']='Stage33-main-batch'
for k in ('merge_allowed','advance_allowed','stage33_08_released','stage33_08_release_allowed','stage33_40_released','stage33_40_release_allowed','theorem_credit','endpoint_credit','stage33_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'): c[k]=False
ck=c.setdefault('controller_writeback_checkpoint',{}); ck['stage33_11_carrier_geometric_orbit_sha256']=x['canonical_sha256']; ck['stage33_11_carrier_geometric_orbit_count']=s['geometric_orbit_count']; ck['stage33_11_unresolved_geometric_orbit_count']=s['unresolved_geometric_orbit_count']; ck['stage33_11_exact_exit_progress']='0/26'; ck['stage33_12_released']=False
ctrl.write_text(json.dumps(c,indent=2,sort_keys=False)+'\n')
print('CARRIER_GEOMETRIC_ORBITS='+str(s['geometric_orbit_count']))
print('UNRESOLVED_GEOMETRIC_ORBITS='+str(s['unresolved_geometric_orbit_count']))
print('STAGE33_11_EXACT_PROGRESS=0/26')
