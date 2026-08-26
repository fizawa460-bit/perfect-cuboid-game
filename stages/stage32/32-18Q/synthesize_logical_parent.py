#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,pathlib
MAGIC=b'S32D16C1'; RECORD_SIZE=141
SCHEMA='STAGE32_18Q_D16_B14_EXACT_TWO_STAGE_SHARDED_TRAVERSAL_CERT_V1'
EXEC_KEYS=['nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes','exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves','leaf_cap_survivors_after_branch_symmetry','precanonical_survivors','canonical_rejects','owned_prefixes']

def records(p):
    raw=p.read_bytes()
    if raw[:8]!=MAGIC: raise RuntimeError(f'bad magic {p}')
    body=raw[8:]
    if len(body)%RECORD_SIZE: raise RuntimeError(f'truncated {p}')
    return [body[i:i+RECORD_SIZE] for i in range(0,len(body),RECORD_SIZE)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',type=pathlib.Path,required=True); ap.add_argument('--primary-id',type=int,required=True); ap.add_argument('--output-json',type=pathlib.Path,required=True); ap.add_argument('--output-dump',type=pathlib.Path,required=True); ap.add_argument('--certificate',type=pathlib.Path,required=True)
    a=ap.parse_args(); pid=a.primary_id
    docs=[]; recs=[]; hist={}; execution={k:0 for k in EXEC_KEYS}; lock=None; split_seen=set(); total=nonzero=0
    for sid in range(32):
        jp=a.input/f'd16-b14-primary-{pid}-secondary-{sid}-of32.json'; bp=a.input/f'd16-b14-primary-{pid}-secondary-{sid}-of32.bin'
        if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing secondary {pid}/{sid}')
        d=json.loads(jp.read_text())
        if d.get('schema')!=SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=14: raise RuntimeError(f'bad cert {pid}/{sid}')
        if d.get('two_stage_partition') is not True: raise RuntimeError('missing two-stage flag')
        if (d.get('primary_split_coordinate'),d.get('primary_shard_id'),d.get('primary_shard_count'))!=(54,pid,1024): raise RuntimeError(f'bad primary {sid}')
        if (d.get('secondary_split_coordinate'),d.get('secondary_shard_id'),d.get('secondary_shard_count'))!=(45,sid,32): raise RuntimeError(f'bad secondary {sid}')
        if d.get('aut_group_order')!=1536 or d.get('dfs_symmetry_breaker_count')!=256: raise RuntimeError('group/breaker mismatch')
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True or d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True: raise RuntimeError('missing exact completeness')
        here=(d.get('stable_aut_content_sha256'),d.get('prepared_input_sha256'),d.get('canonical_bundle_sha256'))
        if lock is None: lock=here
        if here!=lock: raise RuntimeError('source lock mismatch')
        rs=records(bp)
        if len(rs)!=int(d.get('canonical_survivors_including_zero',0)): raise RuntimeError('record count mismatch')
        recs.extend(rs); docs.append(d); total+=int(d.get('canonical_survivors_including_zero',0)); nonzero+=int(d.get('canonical_nonzero_survivors',0)); split_seen.add(int(d.get('split_prefixes_seen',-1)))
        for k in EXEC_KEYS: execution[k]+=int(d.get(k,0))
        for k,v in d.get('canonical_norm_histogram',{}).items(): hist[str(k)]=hist.get(str(k),0)+int(v)
    if len(split_seen)!=1: raise RuntimeError(f'split scans differ {sorted(split_seen)}')
    if execution['owned_prefixes']!=next(iter(split_seen)): raise RuntimeError('secondary coverage mismatch')
    if len(recs)!=total or len(recs)!=len(set(recs)): raise RuntimeError('duplicate/missing records')
    rh={}
    for r in recs: rh[str(r[0])]=rh.get(str(r[0]),0)+1
    if rh!=hist: raise RuntimeError(f'hist mismatch {rh}!={hist}')
    recs=sorted(recs); a.output_dump.parent.mkdir(parents=True,exist_ok=True); a.output_dump.write_bytes(MAGIC+b''.join(recs)); sha=hashlib.sha256(a.output_dump.read_bytes()).hexdigest(); aut,inputsha,bundle=lock
    out={'schema':'STAGE32_18Q_D16_B14_EXACT_LOGICAL_HOT_PARENT_V1','status':'COMPLETE','bound':14,'aut_group_order':1536,'stable_aut_content_sha256':aut,'prepared_input_sha256':inputsha,'canonical_bundle_sha256':bundle,'dfs_symmetry_breaker_count':256,'shard_id':pid,'shard_count':1024,'split_coordinate':54,'two_stage_partition_certificate':True,'primary_residue':f'h54%1024=={pid}','secondary_split_coordinate':45,'secondary_shard_count':32,'secondary_partition_complete':True,'secondary_split_prefixes_seen_per_run':next(iter(split_seen)),'canonical_survivors_including_zero':total,'canonical_nonzero_survivors':nonzero,'canonical_norm_histogram':hist,'canonical_dump_sha256':sha,'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,'execution_work_counters_not_parent_equivalent':True,'secondary_32_run_execution_work_totals':execution,'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING','FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False}
    a.output_json.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    cert={'schema':'STAGE32_18Q_D16_B14_HOT_PARENT_RESCUE_CERTIFICATE_V1','verdict':'PASS_EXACT_TWO_STAGE_HOT_PARENT_RESCUE_PENDING_GLOBAL_INTEGRATION_AND_HOSTILE_AUDIT','primary_shard_id':pid,'canonical_survivors_including_zero':total,'canonical_norm_histogram':hist,'canonical_dump_sha256':sha,'secondary_partition_complete':True,'execution_work_counters_not_parent_equivalent':True,'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING','THEOREM_CREDIT':False,'RECEIVER_CREDIT':False}
    a.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n'); print(json.dumps(cert,sort_keys=True))
if __name__=='__main__': main()
