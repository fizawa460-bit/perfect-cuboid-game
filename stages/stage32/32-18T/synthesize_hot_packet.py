#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,pathlib
MAGIC=b'S32D16C1'; RECORD_SIZE=141
CHILD_SCHEMA='STAGE32_18T_D16_B14_HOT_SUBSHARD_V1'
LOCK_KEYS=['aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count']
COUNTERS=['nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes','exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves','leaf_cap_survivors_after_branch_symmetry','precanonical_survivors','canonical_rejects','split_prefixes_seen','owned_prefixes']
def recs(p:pathlib.Path):
    raw=p.read_bytes()
    if raw[:8]!=MAGIC or len(raw[8:])%RECORD_SIZE: raise RuntimeError(f'bad dump {p}')
    return [raw[i:i+RECORD_SIZE] for i in range(8,len(raw),RECORD_SIZE)]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',type=pathlib.Path,required=True); ap.add_argument('--packet-id',type=int,required=True); ap.add_argument('--input',type=pathlib.Path,required=True); ap.add_argument('--output',type=pathlib.Path,required=True)
    a=ap.parse_args(); manifest=json.loads(a.manifest.read_text()); packet=manifest['packets'][a.packet_id]
    if packet['tier']!='hot-single' or len(packet['residues'])!=1: raise RuntimeError('packet is not hot-single')
    residue=int(packet['residues'][0]); all_records=[]; hist={}; totals={k:0 for k in COUNTERS}; lock=None; split_seen=set(); owned=0; canonical_nonzero=0
    per_children=[]
    for sid in range(4):
        jp=a.input/f'hot-packet-{a.packet_id}-sub-{sid}.json'; bp=a.input/f'hot-packet-{a.packet_id}-sub-{sid}.bin'
        if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing child {sid}')
        d=json.loads(jp.read_text())
        if d.get('schema')!=CHILD_SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=14: raise RuntimeError(f'bad child {sid}')
        if d.get('two_stage_partition') is not True: raise RuntimeError(f'missing two-stage flag {sid}')
        if (d.get('primary_split_coordinate'),d.get('primary_shard_id'),d.get('primary_shard_count'))!=(54,residue,1024): raise RuntimeError(f'bad primary gate {sid}')
        if (d.get('secondary_split_coordinate'),d.get('secondary_shard_id'),d.get('secondary_shard_count'))!=(45,sid,4): raise RuntimeError(f'bad secondary gate {sid}')
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True or d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True: raise RuntimeError(f'missing exact cert {sid}')
        here=tuple(d.get(k) for k in LOCK_KEYS)
        if lock is None: lock=here
        if here!=lock: raise RuntimeError('source lock mismatch')
        rs=recs(bp)
        if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)): raise RuntimeError('record count mismatch')
        all_records.extend(rs); canonical_nonzero+=int(d.get('canonical_nonzero_survivors',0)); split_seen.add(int(d.get('split_prefixes_seen',-1))); owned+=int(d.get('owned_prefixes',0))
        for k,v in d.get('canonical_norm_histogram',{}).items(): hist[str(k)]=hist.get(str(k),0)+int(v)
        for k in COUNTERS: totals[k]+=int(d.get(k,0))
        per_children.append({'secondary_shard_id':sid,'canonical_survivors_including_zero':len(rs),'canonical_dump_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),'nodes':d.get('nodes')})
    if len(split_seen)!=1 or owned!=next(iter(split_seen)): raise RuntimeError('secondary partition coverage mismatch')
    if len(all_records)!=len(set(all_records)): raise RuntimeError('duplicate rescued records')
    record_hist={}
    for x in all_records: record_hist[str(x[0])]=record_hist.get(str(x[0]),0)+1
    if record_hist!=hist: raise RuntimeError('hist mismatch')
    all_records=sorted(all_records); a.output.mkdir(parents=True,exist_ok=True); dump=a.output/'packet-canonical.bin'; dump.write_bytes(MAGIC+b''.join(all_records)); dump_sha=hashlib.sha256(dump.read_bytes()).hexdigest(); locks=dict(zip(LOCK_KEYS,lock)); manifest_sha=hashlib.sha256(a.manifest.read_bytes()).hexdigest()
    out={'schema':'STAGE32_18O_D16_B14_PACKET_PILOT_V1','status':'COMPLETE','bound':14,'packet_id':a.packet_id,'tier':packet['tier'],'residues':[residue],'residue_count':1,'manifest_sha256':manifest_sha,'hybrid_risk_sum':packet['hybrid_risk_sum'],'p50_probe_prefix_sum':packet['p50_probe_prefix_sum'],'p48_probe_prefix_sum':packet['p48_probe_prefix_sum'],'canonical_survivors_including_zero':len(all_records),'canonical_nonzero_survivors':canonical_nonzero,'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,'packet_residue_partition_complete':True,'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,'execution_work_counters_are_sum_of_independent_residue_runs_with_repeated_presplit_work':True,'execution_work_totals':totals,'per_residue':[{'residue':residue,'canonical_survivors_including_zero':len(all_records),'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,'nodes':totals['nodes'],'coordinate_trials':totals['coordinate_trials']}],**locks,'hot_resume_secondary_partition_certificate':True,'hot_resume_secondary_split_coordinate':45,'hot_resume_secondary_shard_count':4,'hot_resume_common_split_prefixes_seen':next(iter(split_seen)),'hot_resume_children':per_children,'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False}
    (a.output/'packet-certificate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'packet_id':a.packet_id,'residue':residue,'canonical':len(all_records),'dump_sha256':dump_sha},sort_keys=True))
if __name__=='__main__': main()
