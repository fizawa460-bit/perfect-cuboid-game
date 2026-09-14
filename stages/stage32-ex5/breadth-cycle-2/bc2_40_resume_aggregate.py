#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import bc2_40_replay_explicit_fresh_unknown23 as b40

TARGET_COUNT=23
TARGET_SHA="29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02"
PARENT_WORKER_BLOB="a28061b99527c6585c3f4016992d1ef6e47b42de"
TIMEOUT_MS=180000

def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def git_blob_sha(path: Path):
    raw=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def checked_unit(path:Path):
    o=json.loads(path.read_text()); q=dict(o); got=q.pop('canonical_sha256_without_this_field',None)
    if got!=csha(q): raise ValueError(f'canonical drift: {path}')
    if o.get('schema')!='STAGE32EX5_BC2_40_PARENT_UNIT_CERT_V1': raise ValueError(f'schema: {path}')
    if o.get('partition_key')!='parent_index' or o.get('target',{}).get('audited_parent_indices_sha256')!=TARGET_SHA: raise ValueError(f'target drift: {path}')
    if o.get('execution',{}).get('per_parent_timeout_ms')!=TIMEOUT_MS: raise ValueError(f'timeout drift: {path}')
    if o.get('result',{}).get('status') not in ('UNSAT','UNKNOWN','SAT'): raise ValueError(f'status: {path}')
    return o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--units-dir',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--allow-partial',action='store_true'); args=ap.parse_args()
    worker=Path(__file__).resolve().parent/'bc2_40_replay_parent_unit.py'
    if git_blob_sha(worker)!=PARENT_WORKER_BLOB: raise ValueError('parent worker drift')
    cp=b40.load_target(); expected=[int(v) for v in cp['replay']['unknown_parent_indices']]
    if len(expected)!=TARGET_COUNT or csha(expected)!=TARGET_SHA: raise ValueError('expected target drift')
    by_idx={}
    for path in sorted(args.units_dir.glob('parent-*.json')):
        u=checked_unit(path); idx=int(u['parent_index'])
        if idx not in expected: raise ValueError(f'out-of-population unit {idx}')
        if idx in by_idx: raise ValueError(f'duplicate unit {idx}')
        by_idx[idx]=u
    complete=sorted(by_idx); missing=[i for i in expected if i not in by_idx]
    statuses={i:by_idx[i]['result']['status'] for i in complete}
    if missing and not args.allow_partial: raise ValueError(f'incomplete coverage: {missing}')
    if missing:
        body={'schema':'STAGE32EX5_BC2_40_RECOVERY_SNAPSHOT_V1','stage':'32EX5','unit':'BC2_40_RESUME_RECOVERY','status':'PARTIAL_RECOVERABLE','partition':{'key':'parent_index','expected_count':TARGET_COUNT,'expected_indices_sha256':TARGET_SHA,'complete_indices':complete,'missing_indices':missing,'complete_count':len(complete),'missing_count':len(missing)},'carry_validation':{'unit_schema':'STAGE32EX5_BC2_40_PARENT_UNIT_CERT_V1','parent_worker_git_blob_sha':PARENT_WORKER_BLOB,'source_semantics_match':True,'duplicate_units':False},'result_counts':{'unsat':sum(v=='UNSAT' for v in statuses.values()),'unknown':sum(v=='UNKNOWN' for v in statuses.values()),'sat':sum(v=='SAT' for v in statuses.values())},'next_execution':{'schedule_only_missing_parent_indices':missing,'fresh_runkey_generation_required':True},'credit':{'stage32_main_credit':False,'full178_complete':False,'theorem_credit':False},'firewalls':{'partial_snapshot_promoted_to_complete':False,'main_promotion':False,'merge_authorized':False}}
    else:
        unsat_ids=[i for i in expected if statuses[i]=='UNSAT']; unknown_ids=[i for i in expected if statuses[i]=='UNKNOWN']; sat_ids=[i for i in expected if statuses[i]=='SAT']; sats=[{'parent_index':i,**by_idx[i]['result']['sat_witness']} for i in sat_ids]
        body={'schema':'STAGE32EX5_BC2_40_FRESH_UNKNOWN23_REPLAY_V2_RESUMABLE','stage':'32EX5','unit':'BC2_40_REFINE_REMAINING_FRESH_UNKNOWN_SET','status':'COMPLETE_EXACT_UNION','partition':{'key':'parent_index','expected_count':TARGET_COUNT,'expected_indices_sha256':TARGET_SHA,'complete_indices':expected,'coverage_exact':True,'gap_count':0,'overlap_count':0},'replay':{'parents_checked':TARGET_COUNT,'per_parent_timeout_ms':TIMEOUT_MS,'unsat_count':len(unsat_ids),'unknown_count':len(unknown_ids),'sat_count':len(sat_ids),'unsat_parent_indices':unsat_ids,'unknown_parent_indices':unknown_ids,'unknown_parent_indices_sha256':csha(unknown_ids),'sat_parent_indices':sat_ids},'sat_witnesses':sats,'source_locks':{'parent_worker_git_blob_sha':PARENT_WORKER_BLOB,'bc2_39_checkpoint_git_blob_sha':b40.BC2_39_BLOB,'bc2_39_checkpoint_canonical':b40.BC2_39_CANONICAL,'bc2_39_hostile_audit_exact_head':b40.BC2_39_AUDIT_HEAD,'bc2_39_hostile_audit_review_id':b40.BC2_39_AUDIT_REVIEW},'credit':{'new_exact_parent_unsat_count':len(unsat_ids),'known_parent_unsat_count_lower_bound':7313+len(unsat_ids),'whole_first_block_picard64_unsat_candidate':len(unsat_ids)==TARGET_COUNT,'whole_stratum_closed':False,'full178_complete':False,'stage32_main_credit':False,'effectivity_or_actual_curve_existence_proved':False,'theorem_credit':False,'endpoint_credit':False},'firewalls':{'timeout_unknown_relabelled_unsat':False,'unknown_dropped':False,'sat_relabelled_actual_curve':False,'main_promotion':False,'merge_authorized':False,'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False}}
    body['canonical_sha256_without_this_field']=csha(body); args.output.write_text(json.dumps(body,sort_keys=True,indent=2)+'\n'); print(json.dumps({'schema':body['schema'],'complete':len(complete),'missing':len(missing),'canonical':body['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
