#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib, subprocess, sys

MAGIC=b'S32D16C1'
RECORD_SIZE=141
SCHEMA='STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1'
COUNTERS=['nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes','exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves','leaf_cap_survivors_after_branch_symmetry','precanonical_survivors','canonical_rejects','split_prefixes_seen','owned_prefixes']
LOCK_KEYS=['aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count']


def read_records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=MAGIC: raise RuntimeError(f'bad dump magic: {path}')
    body=raw[8:]
    if len(body)%RECORD_SIZE: raise RuntimeError(f'truncated dump: {path}')
    return [body[i:i+RECORD_SIZE] for i in range(0,len(body),RECORD_SIZE)]


def write_json(path:pathlib.Path,obj):
    path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')


def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',type=pathlib.Path,required=True)
    ap.add_argument('--packet-id',type=int,required=True)
    ap.add_argument('--exe',type=pathlib.Path,required=True)
    ap.add_argument('--input',type=pathlib.Path,required=True)
    ap.add_argument('--bundle',type=pathlib.Path,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    ap.add_argument('--node-cap',type=int,required=True)
    args=ap.parse_args()
    manifest=json.loads(args.manifest.read_text())
    assert manifest['schema']=='STAGE32_18O_D16_B14_PACKET_MANIFEST_V1'
    assert manifest['bound']==14 and manifest['parent_coordinate']==54 and manifest['parent_modulus']==1024
    packet=manifest['packets'][args.packet_id]
    assert packet['packet_id']==args.packet_id
    residues=[int(x) for x in packet['residues']]
    args.output.mkdir(parents=True,exist_ok=True)
    runroot=args.output/'residue-runs'; runroot.mkdir(exist_ok=True)
    manifest_sha=hashlib.sha256(args.manifest.read_bytes()).hexdigest()
    docs=[]; all_records=[]; hist={}; totals={k:0 for k in COUNTERS}; lock=None
    per_residue=[]
    for r in residues:
        jp=runroot/f'residue-{r}.json'; bp=runroot/f'residue-{r}.bin'
        cmd=[str(args.exe),'--input',str(args.input),'--bundle',str(args.bundle),'--output',str(jp),'--dump-canonical',str(bp),'--bound','14','--shard-id',str(r),'--shard-count','1024','--split-coordinate','54','--node-cap',str(args.node_cap)]
        proc=subprocess.run(cmd,text=True,capture_output=True)
        (runroot/f'residue-{r}.stdout.txt').write_text(proc.stdout)
        (runroot/f'residue-{r}.stderr.txt').write_text(proc.stderr)
        if proc.returncode!=0:
            if 'exact traversal node cap exceeded' in proc.stderr:
                out={
                  'schema':'STAGE32_18O_D16_B14_PACKET_PILOT_V1','status':'RESOURCE_WALL_NODE_CAP','bound':14,
                  'packet_id':args.packet_id,'tier':packet['tier'],'residues':residues,'completed_residues':[x['residue'] for x in per_residue],
                  'wall_residue':r,'per_residue_node_cap':args.node_cap,'manifest_sha256':manifest_sha,
                  'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
                }
                write_json(args.output/'packet-certificate.json',out); print(json.dumps(out,sort_keys=True)); return
            raise RuntimeError(f'unexpected exact residue failure {r}: rc={proc.returncode}: {proc.stderr[-2000:]}')
        d=json.loads(jp.read_text())
        if d.get('schema')!=SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=14:
            raise RuntimeError(f'bad residue certificate {r}')
        if (d.get('shard_id'),d.get('shard_count'),d.get('split_coordinate'))!=(r,1024,54):
            raise RuntimeError(f'bad residue partition metadata {r}')
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True:
            raise RuntimeError(f'missing traversal completeness {r}')
        if d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True:
            raise RuntimeError(f'missing exact symmetry certificate {r}')
        here=tuple(d.get(k) for k in LOCK_KEYS)
        if lock is None: lock=here
        if here!=lock: raise RuntimeError(f'source-lock mismatch at residue {r}')
        rs=read_records(bp)
        if len(rs)!=int(d['canonical_survivors_including_zero']): raise RuntimeError(f'record count mismatch {r}')
        bp_sha=hashlib.sha256(bp.read_bytes()).hexdigest()
        # 18E certificates intentionally do not promise an embedded dump SHA;
        # historical aggregators compute it from the exact BIN.  If a later
        # compatible certifier does embed one, require agreement.
        embedded_sha=d.get('canonical_dump_sha256')
        if embedded_sha is not None and embedded_sha!=bp_sha: raise RuntimeError(f'dump SHA mismatch {r}')
        all_records.extend(rs); docs.append(d)
        for k,v in d['canonical_norm_histogram'].items(): hist[str(k)]=hist.get(str(k),0)+int(v)
        for k in COUNTERS: totals[k]+=int(d.get(k,0))
        per_residue.append({'residue':r,'canonical_survivors_including_zero':d['canonical_survivors_including_zero'],'canonical_norm_histogram':d['canonical_norm_histogram'],'canonical_dump_sha256':bp_sha,'nodes':d.get('nodes'),'coordinate_trials':d.get('coordinate_trials'),'exact_constraint_prunes':d.get('exact_constraint_prunes'),'exact_symmetry_prunes':d.get('exact_symmetry_prunes')})
    if len(all_records)!=len(set(all_records)): raise RuntimeError('duplicate canonical record across packet residues')
    record_hist={}
    for rec in all_records: record_hist[str(rec[0])]=record_hist.get(str(rec[0]),0)+1
    if record_hist!=hist: raise RuntimeError(f'packet histogram mismatch {record_hist} != {hist}')
    all_records=sorted(all_records)
    dump=args.output/'packet-canonical.bin'; dump.write_bytes(MAGIC+b''.join(all_records))
    dump_sha=hashlib.sha256(dump.read_bytes()).hexdigest()
    locks=dict(zip(LOCK_KEYS,lock)) if lock else {}
    out={
      'schema':'STAGE32_18O_D16_B14_PACKET_PILOT_V1','status':'COMPLETE','bound':14,'packet_id':args.packet_id,
      'tier':packet['tier'],'residues':residues,'residue_count':len(residues),'manifest_sha256':manifest_sha,
      'hybrid_risk_sum':packet['hybrid_risk_sum'],'p50_probe_prefix_sum':packet['p50_probe_prefix_sum'],'p48_probe_prefix_sum':packet['p48_probe_prefix_sum'],
      'canonical_survivors_including_zero':len(all_records),'canonical_nonzero_survivors':len(all_records)-hist.get('0',0),
      'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,'packet_residue_partition_complete':True,
      'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,
      'execution_work_counters_are_sum_of_independent_residue_runs_with_repeated_presplit_work':True,
      'execution_work_totals':totals,'per_residue':per_residue,**locks,
      'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
    }
    write_json(args.output/'packet-certificate.json',out)
    print(json.dumps({'status':'COMPLETE','packet_id':args.packet_id,'tier':packet['tier'],'residues':residues,'canonical':len(all_records),'hist':hist,'nodes':totals['nodes'],'trials':totals['coordinate_trials'],'dump_sha256':dump_sha},sort_keys=True))

if __name__=='__main__':
    try: main()
    except Exception as e:
        print(f'ERROR: {e}',file=sys.stderr); raise
