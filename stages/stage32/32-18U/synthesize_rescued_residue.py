#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

MAGIC=b'S32D16C1'
RECORD_SIZE=141
CHILD_SCHEMA='STAGE32_18T_D16_B14_HOT_SUBSHARD_V1'
OUT_SCHEMA='STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1'
LOCK_KEYS=['aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count']
COUNTERS=['nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes','exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves','leaf_cap_survivors_after_branch_symmetry','precanonical_survivors','canonical_rejects','split_prefixes_seen','owned_prefixes']

def recs(p:pathlib.Path):
    raw=p.read_bytes()
    if raw[:8]!=MAGIC or len(raw[8:])%RECORD_SIZE:
        raise RuntimeError(f'bad dump {p}')
    return [raw[i:i+RECORD_SIZE] for i in range(8,len(raw),RECORD_SIZE)]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--residue',type=int,required=True)
    ap.add_argument('--input',type=pathlib.Path,required=True)
    ap.add_argument('--output-json',type=pathlib.Path,required=True)
    ap.add_argument('--output-bin',type=pathlib.Path,required=True)
    ap.add_argument('--secondary-split-coordinate',type=int,default=45)
    ap.add_argument('--secondary-shard-count',type=int,default=4)
    a=ap.parse_args()
    r=a.residue
    if not 0<=r<1024: raise RuntimeError('residue outside 0..1023')

    all_records=[]; hist={}; totals={k:0 for k in COUNTERS}; lock=None
    split_seen=set(); owned=0; per=[]; nonzero=0
    for sid in range(a.secondary_shard_count):
        jp=a.input/f'tail-residue-{r}-sub-{sid}.json'
        bp=a.input/f'tail-residue-{r}-sub-{sid}.bin'
        if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing child {sid}')
        d=json.loads(jp.read_text())
        if d.get('schema')!=CHILD_SCHEMA or d.get('status')!='COMPLETE' or int(d.get('bound',-1))!=14:
            raise RuntimeError(f'bad child {sid}')
        if d.get('two_stage_partition') is not True:
            raise RuntimeError(f'missing two-stage flag {sid}')
        if (int(d.get('primary_split_coordinate',-1)),int(d.get('primary_shard_id',-1)),int(d.get('primary_shard_count',-1)))!=(54,r,1024):
            raise RuntimeError(f'bad primary gate {sid}')
        if (int(d.get('secondary_split_coordinate',-1)),int(d.get('secondary_shard_id',-1)),int(d.get('secondary_shard_count',-1)))!=(a.secondary_split_coordinate,sid,a.secondary_shard_count):
            raise RuntimeError(f'bad secondary gate {sid}')
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True or d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True:
            raise RuntimeError(f'incomplete exact child {sid}')
        here=tuple(d.get(k) for k in LOCK_KEYS)
        if lock is None: lock=here
        if here!=lock: raise RuntimeError('source lock mismatch')
        rs=recs(bp)
        if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)):
            raise RuntimeError(f'child record count mismatch {sid}')
        all_records.extend(rs); nonzero+=int(d.get('canonical_nonzero_survivors',0))
        for k,v in d.get('canonical_norm_histogram',{}).items(): hist[str(k)]=hist.get(str(k),0)+int(v)
        for k in COUNTERS: totals[k]+=int(d.get(k,0))
        split_seen.add(int(d.get('split_prefixes_seen',-1))); owned+=int(d.get('owned_prefixes',0))
        per.append({'secondary_shard_id':sid,'nodes':int(d.get('nodes',0)),'canonical_survivors_including_zero':len(rs),'canonical_dump_sha256':hashlib.sha256(bp.read_bytes()).hexdigest()})

    if len(split_seen)!=1 or owned!=next(iter(split_seen)):
        raise RuntimeError('secondary partition coverage mismatch')
    if len(all_records)!=len(set(all_records)):
        raise RuntimeError('duplicate records across secondary shards')
    record_hist={}
    for x in all_records: record_hist[str(x[0])]=record_hist.get(str(x[0]),0)+1
    if record_hist!=hist: raise RuntimeError('hist mismatch')

    all_records=sorted(all_records)
    a.output_bin.parent.mkdir(parents=True,exist_ok=True)
    a.output_json.parent.mkdir(parents=True,exist_ok=True)
    a.output_bin.write_bytes(MAGIC+b''.join(all_records))
    dump_sha=hashlib.sha256(a.output_bin.read_bytes()).hexdigest()
    locks=dict(zip(LOCK_KEYS,lock))
    out={
      'schema':OUT_SCHEMA,'status':'COMPLETE','bound':14,
      'shard_id':r,'shard_count':1024,'split_coordinate':54,
      'canonical_survivors_including_zero':len(all_records),'canonical_nonzero_survivors':nonzero,
      'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,
      'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
      'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,
      'two_stage_rescue_certificate':True,'primary_split_coordinate':54,'primary_shard_id':r,'primary_shard_count':1024,
      'secondary_split_coordinate':a.secondary_split_coordinate,'secondary_shard_count':a.secondary_shard_count,
      'secondary_partition_complete':True,'secondary_common_split_prefixes_seen':next(iter(split_seen)),
      'secondary_owned_prefixes_sum':owned,'secondary_children':per,
      **totals,**locks,
      'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
    }
    a.output_json.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'residue':r,'canonical':len(all_records),'nodes':totals['nodes'],'dump_sha256':dump_sha},sort_keys=True))

if __name__=='__main__': main()
