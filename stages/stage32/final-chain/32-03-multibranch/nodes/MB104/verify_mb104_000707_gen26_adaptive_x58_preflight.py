#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; REPO=HERE.parents[5]
RUNKEY=HERE/'runkeys'/'000707-FIBRATION-ISOTROPIC-SHELLS-V1.json'; STATE=HERE.parents[1]/'fib'/'STATE.json'
CARRY_SOURCE=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-SOURCE.json'; CARRY_INDEX=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-INDEX.json'; CARRY_VERIFIER=HERE/'verify_mb104_000707_gen29_x58_singleton_carry.py'
RESIDUAL=HERE/'MB104-000707-GEN30-X58-SINGLETON-RESIDUAL49.json'; DERIVE=HERE/'derive_mb104_000707_gen30_adaptive_affine_cold.py'; COLD=HERE/'MB104-000707-GEN30-ADAPTIVE-AFFINE-COLD.json'; COLD_VERIFIER=HERE/'verify_mb104_000707_gen30_adaptive_affine_cold.py'
LOCAL=HERE/'run_mb104_000707_fibration_shell_local_exact.py'; RETAINED=HERE/'run_mb104_000707_fibration_isotropic_shells.py'; WORKFLOW=REPO/'.github/workflows/stage32-mb-fib-isotropic-shell-pilot.yml'
PATHS={'workflow_git_blob':WORKFLOW,'adaptive_x58_preflight_git_blob':Path(__file__).resolve(),'local_exact_engine_git_blob':LOCAL,'runner_git_blob':RETAINED,'gen29_x58_singleton_carry_source_git_blob':CARRY_SOURCE,'gen29_x58_singleton_carry_index_git_blob':CARRY_INDEX,'gen29_x58_singleton_carry_verifier_git_blob':CARRY_VERIFIER,'gen30_residual49_git_blob':RESIDUAL,'gen30_adaptive_affine_deriver_git_blob':DERIVE,'gen30_adaptive_affine_output_git_blob':COLD,'gen30_adaptive_affine_verifier_git_blob':COLD_VERIFIER}
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],cwd=REPO,text=True).strip()
def main():
 k=json.loads(RUNKEY.read_text()); s=json.loads(STATE.read_text()); sl=k['source_locks']
 if int(k['generation'])!=30 or k['mode']!='COLD' or k['armed'] is not False: raise SystemExit('Gen30 COLD/unarmed preflight contract drift')
 if s['execution']['runkey_generation']!=30 or s['execution']['heavy_armed'] is not False or s['execution']['execution_authorized'] is not False: raise SystemExit('Gen30 STATE execution gate drift')
 if k['execution_gate']['automatic_execution_authorized'] is not False or k['execution_gate']['current_head_execution_blocked'] is not True: raise SystemExit('Gen30 runkey execution gate drift')
 verified={}
 for f,p in PATHS.items():
  got=blob(p); want=sl[f]
  if got!=want: raise SystemExit(f'source-lock mismatch before exec: {f}: {got} != {want}')
  verified[f]=got
 subprocess.run([sys.executable,str(CARRY_VERIFIER)],cwd=HERE,check=True)
 subprocess.run([sys.executable,str(COLD_VERIFIER),'--certificate',str(COLD)],cwd=HERE,check=True)
 r=json.loads(RESIDUAL.read_text()); d=json.loads(COLD.read_text()); idx=json.loads(CARRY_INDEX.read_text())
 if r['schema']!='STAGE32_MB104_000707_GEN30_X58_SINGLETON_RESIDUAL49_V1' or len(r['residual_singletons'])!=49 or r['complete_singleton_child_count']!=111 or r['residual_timeout_singleton_count']!=49: raise SystemExit('Gen30 residual49 drift')
 if idx['complete_child_count']!=111 or idx['incomplete_child_count']!=49 or idx['packet_count']!=54 or idx['x58_singleton_child_count']!=160: raise SystemExit('Gen29 carry accounting drift')
 if d['summary']['selected_coordinate_histogram']!={'56':49} or d['summary']['total_interval_child_count']!=392 or d['heavy_surface_present'] or d['heavy_armed'] or d['execution_authorized']: raise SystemExit('Gen30 COLD diagnostic drift')
 if any(bool(v) for v in k['credit'].values()) or any(bool(v) for v in s['credit_firewall'].values()) or any(bool(v) for v in d['credit_firewall'].values()): raise SystemExit('credit firewall leak')
 print(json.dumps({'success':True,'generation':30,'mode':'COLD','gen29_complete_x58_singletons':111,'residual_timeout_singletons':49,'next_coordinate_0based':56,'next_parent_leaves':49,'next_interval_children':392,'heavy_armed':False,'execution_authorized':False},sort_keys=True))
if __name__=='__main__': main()
