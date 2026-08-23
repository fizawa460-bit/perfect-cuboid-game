#!/usr/bin/env python3
"""Replay remaining PR1343 residual parents in bounded intersection coordinates."""
from __future__ import annotations
import argparse, concurrent.futures, importlib.util, json, pathlib, subprocess, sys, time
from typing import Any

def load_predecessor():
    path=pathlib.Path(__file__).resolve().parents[1]/'32-02'/'run_pr1343_regression.py'; spec=importlib.util.spec_from_file_location('stage32_02_regression_coord',path)
    assert spec and spec.loader; m=importlib.util.module_from_spec(spec); sys.modules[spec.name]=m; spec.loader.exec_module(m); return m

def audited_closed():
    s=pathlib.Path(__file__).resolve().parents[1]; local=json.loads((s/'32-02'/'local-evidence.json').read_text()); labels={r['label'] for r in local['formerly_unresolved_residuals'] if r['disposition'].startswith('CLOSED_') and r['exact_survivor_count']==0}; assert len(labels)==14
    affine=json.loads((s/'32-03'/'certificates'/'closure-evidence.json').read_text()); assert affine['all_44_e4_a32_terminal_cells_exactly_closed'] and affine['unknown_count']==0 and affine['exact_survivor_count']==0; labels.add('d6-g1-e4-a32'); assert len(labels)==15
    return labels,{'stage32_02_local_evidence_sha256':local['canonical_sha256_without_this_field'],'stage32_03_affine_closure_sha256':affine['canonical_sha256_without_this_field']}

def run_one(task,artifact,out,cap,timeout,proof):
    cmd=[sys.executable,str(pathlib.Path(__file__).with_name('run_intersection_coord_budget.py')),'--core',str(artifact/'picard-core.json'),'--cap-certificate',str(cap),'--output-dir',str(out),'--degree',str(task.degree),'--genus',str(task.genus),'--exceptional-mass',str(task.exceptional_mass),'--curve-group-mass',str(task.curve_group_mass),'--timeout',str(timeout)]
    if proof: cmd.append('--proof')
    done=subprocess.run(cmd,capture_output=True,text=True,check=False); cp=out/task.label/'checkpoint.json'
    if not cp.exists(): return {'label':task.label,'complete':False,'solver_result':'missing_checkpoint','returncode':done.returncode,'stdout_tail':done.stdout[-2000:],'stderr_tail':done.stderr[-2000:]}
    p=json.loads(cp.read_text()); return {'label':task.label,'complete':bool(p['complete']),'solver_result':p['solver_result'],'unknown_reason':p['unknown_reason'],'exact_survivor_count':p['exact_survivor_count'],'elapsed_seconds':p['elapsed_seconds'],'deterministic_result_sha256':p['deterministic_result_sha256'],'checkpoint_sha256_without_this_field':p['checkpoint_sha256_without_this_field'],'smt2_sha256':p['smt2_sha256'],'proof_sha256':p['proof_sha256'],'transform_certificate':p['transform_certificate'],'returncode':done.returncode}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--artifact-dir',type=pathlib.Path,required=True); p.add_argument('--output-dir',type=pathlib.Path,required=True); p.add_argument('--cap-certificate',type=pathlib.Path,required=True); p.add_argument('--workers',type=int,default=4); p.add_argument('--timeout',type=float,default=180.0); p.add_argument('--proof',action='store_true'); a=p.parse_args()
    pred=load_predecessor(); hashes=pred.lock_artifacts(a.artifact_dir); _,residual=pred.source_tasks(a.artifact_dir); assert len(residual)==28; old,evidence=audited_closed(); targets=[t for t in residual if t.label not in old]; assert len(targets)==13; a.output_dir.mkdir(parents=True,exist_ok=True)
    started=time.perf_counter(); results={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as ex:
        fs={ex.submit(run_one,t,a.artifact_dir,a.output_dir,a.cap_certificate,a.timeout,a.proof):t for t in targets}
        for f in concurrent.futures.as_completed(fs): row=f.result(); results[fs[f].label]=row; print(json.dumps(row,sort_keys=True),flush=True)
    ordered=[results[t.label] for t in targets]; current={r['label'] for r in ordered if r.get('complete') and r.get('exact_survivor_count')==0}; combined=old|current; unresolved=[r['label'] for r in ordered if r['label'] not in current]
    m={'schema':'STAGE32_INTERSECTION_COORD_RESIDUAL_BATCH_V2','source_pr':1343,'source_runs':[32623143985,32623610941,32624596141],'source_artifact_hashes':hashes,'audited_predecessor_evidence':evidence,'original_residual_parent_count':28,'audited_predecessor_closed_parent_count':len(old),'current_target_parent_count':len(targets),'current_exactly_closed_parent_count':len(current),'combined_exactly_closed_parent_count':len(combined),'all_28_residual_parents_exactly_closed':len(combined)==28,'unresolved':unresolved,'entries':ordered,'wall_seconds':round(time.perf_counter()-started,6),'proof_requested':a.proof,'low_degree_prefix_complete':False,'full_d176_d192_numerical_orbit_census':False,'receiver_credit':False,'r29_lg2':'NOT_DISCHARGED','r29_lg2_eff':'NOT_DISCHARGED','r29_lg2_mb':'NOT_DISCHARGED','g10_lowgenus_picard':'AMBER'}
    (a.output_dir/'coord-residual-manifest.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n'); print(json.dumps(m,sort_keys=True))
if __name__=='__main__': main()
