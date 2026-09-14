#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from z3 import Int, SolverFor, sat, unknown, unsat, get_version_string
import bc2_40_replay_explicit_fresh_unknown23 as b40

HERE=Path(__file__).resolve().parent
TIMEOUT_MS=180000
TARGET_COUNT=23
TARGET_SHA="29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02"
UPSTREAM_B40_BLOB="acccc2360a2b113b4d568c86bb4be48152a68013"

def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def git_blob_sha(path: Path):
    raw=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def build_solver():
    cp=b40.load_target()
    target_indices=[int(v) for v in cp['replay']['unknown_parent_indices']]
    if len(target_indices)!=TARGET_COUNT or csha(target_indices)!=TARGET_SHA:
        raise ValueError('BC2-40 target drift')
    if git_blob_sha(Path(b40.__file__).resolve())!=UPSTREAM_B40_BLOB:
        raise ValueError('BC2-40 upstream producer drift')
    b39=b40.b39; b32=b39.b38.b37.b36.b32; b19=b32.b19
    if git_blob_sha(Path(b39.__file__).resolve())!=b40.BC2_39_SOURCE_BLOB: raise ValueError('BC2-39 producer drift')
    if git_blob_sha(Path(b32.__file__).resolve())!=b40.B32_BLOB: raise ValueError('BC2-32 producer drift')
    if git_blob_sha(Path(b19.__file__).resolve())!=b40.B19_BLOB: raise ValueError('BC2-19 source drift')
    if git_blob_sha(Path(b32.d18.__file__).resolve())!=b40.D18_BLOB: raise ValueError('BC2-18 source drift')
    selected_exceptional_labels, parents, P=b32.build_parent_space()
    bc217=json.loads(b19.BC2_17_EVIDENCE.read_text())
    fixed={int(k):int(v) for k,v in bc217['retarget']['fixed_exceptional_pairings'].items()}
    x=[Int(f'x_{j}') for j in range(b19.PICARD_RANK)]
    p=[sum(int(P[i,j])*x[j] for j in range(b19.PICARD_RANK)) for i in range(b19.ALL140_COUNT)]
    solver=SolverFor('QF_LIA'); solver.set(timeout=TIMEOUT_MS)
    for i in range(b19.NORMAL_COUNT): solver.add(p[i]>=0,p[i]<=b19.NORMAL_MASS)
    for i in range(b19.NORMAL_COUNT,b19.ALL140_COUNT): solver.add(p[i]>=0,p[i]<=b19.TARGET_E)
    solver.add(sum(p[:b19.NORMAL_COUNT])==b19.NORMAL_MASS)
    solver.add(sum(p[b19.NORMAL_COUNT:])==b19.TARGET_E)
    for label,value in fixed.items(): solver.add(p[label-1]==value)
    solver.add(p[b19.X4_LABEL-1]>=0,p[b19.X4_LABEL-1]<=b19.NORMAL_MASS)
    return target_indices, selected_exceptional_labels, parents, P, b19, fixed, x, p, solver

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--parent-index',type=int,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--per-parent-timeout-ms',type=int,default=TIMEOUT_MS); args=ap.parse_args()
    if args.per_parent_timeout_ms!=TIMEOUT_MS: raise ValueError('locked timeout drift')
    target_indices, labels, parents, P, b19, fixed, x, p, solver=build_solver()
    if args.parent_index not in target_indices: raise ValueError('parent_index not in audited BC2-39 UNKNOWN complement')
    comp,yE,allowed=parents[args.parent_index]
    for label,value in zip(labels,yE): solver.add(p[label-1]==int(value))
    result=solver.check(); witness=None; reason=None
    if result==unsat: status='UNSAT'
    elif result==unknown: status='UNKNOWN'; reason=solver.reason_unknown()
    elif result==sat:
        status='SAT'; model=solver.model(); xv=[int(model.eval(q,model_completion=True).as_long()) for q in x]
        pv=[sum(int(P[i,j])*xv[j] for j in range(b19.PICARD_RANK)) for i in range(b19.ALL140_COUNT)]
        if min(pv)<0 or sum(pv[:b19.NORMAL_COUNT])!=b19.NORMAL_MASS or sum(pv[b19.NORMAL_COUNT:])!=b19.TARGET_E: raise ValueError('SAT witness feasibility regression')
        if any(pv[label-1]!=value for label,value in fixed.items()): raise ValueError('SAT witness fixed-pairing regression')
        if any(pv[label-1]!=value for label,value in zip(labels,yE)): raise ValueError('SAT witness parent regression')
        x4=pv[b19.X4_LABEL-1]
        if not 0<=x4<=b19.NORMAL_MASS or x4%8 not in allowed: raise ValueError('SAT witness residue regression')
        witness={'picard64_coordinates':xv,'all140_pairings':pv,'all140_pairings_sha256':csha(pv),'x4':x4,'x4_mod8':x4%8,'selected_residual_mass':sum(comp)}
    else: raise ValueError('unexpected solver status')
    body={'schema':'STAGE32EX5_BC2_40_PARENT_UNIT_CERT_V1','stage':'32EX5','unit':'BC2_40_PARENT_INDEX','partition_key':'parent_index','parent_index':args.parent_index,'target':{'audited_parent_count':TARGET_COUNT,'audited_parent_indices_sha256':TARGET_SHA,'prior_audited_unsat_count':7313},'execution':{'per_parent_timeout_ms':TIMEOUT_MS,'solver':'Z3_QF_LIA','z3_solver_version':get_version_string()},'result':{'status':status,'reason_unknown':reason,'sat_witness':witness},'source_locks':{'upstream_bc2_40_producer_git_blob_sha':UPSTREAM_B40_BLOB,'bc2_39_checkpoint_git_blob_sha':b40.BC2_39_BLOB,'bc2_39_checkpoint_canonical':b40.BC2_39_CANONICAL,'bc2_39_hostile_audit_exact_head':b40.BC2_39_AUDIT_HEAD,'bc2_39_hostile_audit_review_id':b40.BC2_39_AUDIT_REVIEW},'firewalls':{'unit_certificate_is_global_credit':False,'timeout_unknown_relabelled_unsat':False,'sat_relabelled_actual_curve':False,'main_promotion':False,'merge_authorized':False}}
    body['canonical_sha256_without_this_field']=csha(body); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(body,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'parent_index':args.parent_index,'status':status,'canonical':body['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
