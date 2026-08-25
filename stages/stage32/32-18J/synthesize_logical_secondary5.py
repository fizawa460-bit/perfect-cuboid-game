#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib

M=140
MAGIC=b"S32D16C1"
CHILD_SCHEMA="STAGE32_18J_D16_EXACT_THREE_STAGE_SHARDED_TRAVERSAL_CERT_V1"
PARENT_SCHEMA="STAGE32_18I_D16_EXACT_TWO_STAGE_SHARDED_TRAVERSAL_CERT_V1"
EXEC_KEYS=[
    'nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes',
    'exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves',
    'leaf_cap_survivors_after_branch_symmetry','precanonical_survivors','canonical_rejects'
]


def read_records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=MAGIC: raise RuntimeError(f"bad dump magic {path}")
    body=raw[8:]; size=M+1
    if len(body)%size: raise RuntimeError(f"truncated dump {path}")
    return [body[i:i+size] for i in range(0,len(body),size)]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=pathlib.Path,required=True)
    ap.add_argument('--output-json',type=pathlib.Path,required=True)
    ap.add_argument('--output-dump',type=pathlib.Path,required=True)
    ap.add_argument('--certificate',type=pathlib.Path,required=True)
    args=ap.parse_args()

    execution={k:0 for k in EXEC_KEYS}
    records=[]; hist={}; lock=None
    secondary_seen=set(); secondary_owned=set(); tertiary_seen=set(); tertiary_owned_total=0
    canonical=0; canonical_nonzero=0
    for sid in range(16):
        jp=args.input/f'd16-b12-exact-tertiary-{sid}-of16.json'
        bp=args.input/f'd16-b12-exact-tertiary-{sid}-of16.bin'
        if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing tertiary shard {sid}')
        d=json.loads(jp.read_text())
        if d.get('schema')!=CHILD_SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=12:
            raise RuntimeError(f'bad status/schema {sid}')
        if d.get('three_stage_partition') is not True: raise RuntimeError(f'missing three-stage flag {sid}')
        if (d.get('primary_split_coordinate'),d.get('primary_shard_id'),d.get('primary_shard_count'))!=(54,26,1024):
            raise RuntimeError(f'bad primary gate {sid}')
        if (d.get('secondary_split_coordinate'),d.get('secondary_shard_id'),d.get('secondary_shard_count'))!=(45,5,32):
            raise RuntimeError(f'bad secondary gate {sid}')
        if (d.get('tertiary_split_coordinate'),d.get('tertiary_shard_id'),d.get('tertiary_shard_count'))!=(36,sid,16):
            raise RuntimeError(f'bad tertiary gate {sid}')
        if d.get('aut_group_order')!=1536 or d.get('dfs_symmetry_breaker_count')!=256:
            raise RuntimeError(f'bad group/breaker metadata {sid}')
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True or d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True:
            raise RuntimeError(f'missing exact traversal/symmetry certificate {sid}')
        here=(d.get('stable_aut_content_sha256'),d.get('prepared_input_sha256'),d.get('canonical_bundle_sha256'))
        if lock is None: lock=here
        if here!=lock: raise RuntimeError(f'source lock mismatch {sid}')
        rs=read_records(bp)
        if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)): raise RuntimeError(f'record count mismatch {sid}')
        records.extend(rs); canonical+=len(rs); canonical_nonzero+=int(d.get('canonical_nonzero_survivors',0))
        secondary_seen.add(int(d.get('secondary_split_prefixes_seen',-1)))
        secondary_owned.add(int(d.get('secondary_owned_prefixes',-1)))
        tertiary_seen.add(int(d.get('split_prefixes_seen',-1)))
        tertiary_owned_total+=int(d.get('owned_prefixes',0))
        for k in EXEC_KEYS: execution[k]+=int(d.get(k,0))
        for k,v in d.get('canonical_norm_histogram',{}).items(): hist[str(k)]=hist.get(str(k),0)+int(v)

    if len(secondary_seen)!=1 or len(secondary_owned)!=1 or len(tertiary_seen)!=1:
        raise RuntimeError('repeated parent/tertiary prefix scans differ across rescue jobs')
    if tertiary_owned_total!=next(iter(tertiary_seen)):
        raise RuntimeError('tertiary owned-prefix union does not cover common tertiary prefix scan')
    if len(records)!=canonical or len(records)!=len(set(records)):
        raise RuntimeError('duplicate or missing canonical records across tertiary children')
    record_hist={}
    for r in records: record_hist[str(r[0])]=record_hist.get(str(r[0]),0)+1
    if record_hist!=hist: raise RuntimeError(f'histogram mismatch {record_hist} != {hist}')

    records=sorted(records)
    args.output_dump.parent.mkdir(parents=True,exist_ok=True)
    args.output_dump.write_bytes(MAGIC+b''.join(records))
    dump_sha=hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    stable_aut,prepared_input,bundle_sha=lock
    out={
        'schema':PARENT_SCHEMA,'status':'COMPLETE','bound':12,
        'aut_group_order':1536,'stable_aut_content_sha256':stable_aut,
        'prepared_input_sha256':prepared_input,'canonical_bundle_sha256':bundle_sha,
        'dfs_symmetry_breaker_count':256,
        'shard_id':5,'shard_count':32,'split_coordinate':45,
        'two_stage_partition':True,
        'primary_split_coordinate':54,'primary_shard_count':1024,'primary_shard_id':26,
        'secondary_split_coordinate':45,'secondary_shard_count':32,'secondary_shard_id':5,
        'split_prefixes_seen':next(iter(secondary_seen)),
        'owned_prefixes':next(iter(secondary_owned)),
        'canonical_survivors_including_zero':canonical,
        'canonical_nonzero_survivors':canonical_nonzero,
        'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,
        'tertiary_rescue_partition_certificate':True,
        'tertiary_split_coordinate':36,'tertiary_shard_count':16,
        'tertiary_common_split_prefixes_seen':next(iter(tertiary_seen)),
        'tertiary_execution_work_counters_not_logical_parent_equivalent':True,
        'tertiary_16_run_execution_work_totals':execution,
        **execution,
        'D16_B12_NUMERICAL_CREDIT':False,'AUDIT_STATUS':'PENDING',
        'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,
    }
    args.output_json.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    cert={
        'schema':'STAGE32_18J_D16_B12_TERTIARY_RESCUE_CERTIFICATE_V1',
        'verdict':'PASS_EXACT_TERTIARY_RESCUE_LOGICAL_SECONDARY5_PENDING_PARENT_SYNTHESIS_AND_HOSTILE_AUDIT',
        'logical_secondary_shard_id':5,'logical_secondary_shard_count':32,
        'tertiary_split_coordinate':36,'tertiary_shard_count':16,
        'canonical_survivors_including_zero':canonical,'canonical_norm_histogram':hist,
        'canonical_dump_sha256':dump_sha,'tertiary_partition_complete':True,
        'execution_work_counters_not_logical_parent_equivalent':True,
        'D16_B12_NUMERICAL_CREDIT':False,'GLOBAL_B12_AGGREGATION_COMPLETE':False,
        'AUDIT_STATUS':'PENDING','THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,
    }
    args.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps(cert,sort_keys=True))


if __name__=='__main__': main()
