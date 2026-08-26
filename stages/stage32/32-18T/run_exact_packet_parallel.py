#!/usr/bin/env python3
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, pathlib, shutil, subprocess, sys
MAGIC=b'S32D16C1'; RECORD_SIZE=141
SCHEMA='STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1'
COUNTERS=['nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes','exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves','leaf_cap_survivors_after_branch_symmetry','precanonical_survivors','canonical_rejects','split_prefixes_seen','owned_prefixes']
LOCK_KEYS=['aut_group_order','stable_aut_content_sha256','prepared_input_sha256','canonical_bundle_sha256','dfs_symmetry_breaker_count']
def recs(p:pathlib.Path):
    raw=p.read_bytes()
    if raw[:8]!=MAGIC or len(raw[8:])%RECORD_SIZE: raise RuntimeError(f'bad dump {p}')
    return [raw[i:i+RECORD_SIZE] for i in range(8,len(raw),RECORD_SIZE)]
def validate_residue(jp:pathlib.Path,bp:pathlib.Path,r:int):
    if not jp.exists() or not bp.exists(): raise RuntimeError(f'missing residue files {r}')
    d=json.loads(jp.read_text())
    if d.get('schema')!=SCHEMA or d.get('status')!='COMPLETE' or int(d.get('bound',-1))!=14: raise RuntimeError(f'bad cert {r}')
    if (int(d.get('shard_id',-1)),int(d.get('shard_count',-1)),int(d.get('split_coordinate',-1)))!=(r,1024,54): raise RuntimeError(f'bad shard cert {r}')
    if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True or d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True: raise RuntimeError(f'missing exact cert {r}')
    rs=recs(bp)
    if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)): raise RuntimeError(f'record count mismatch {r}')
    rh={}
    for x in rs: rh[str(x[0])]=rh.get(str(x[0]),0)+1
    want={str(k):int(v) for k,v in d.get('canonical_norm_histogram',{}).items()}
    if rh!=want: raise RuntimeError(f'residue histogram mismatch {r}')
    return d,rs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',type=pathlib.Path,required=True); ap.add_argument('--packet-id',type=int,required=True)
    ap.add_argument('--exe',type=pathlib.Path,required=True); ap.add_argument('--input',type=pathlib.Path,required=True); ap.add_argument('--bundle',type=pathlib.Path,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True); ap.add_argument('--node-cap',type=int,required=True); ap.add_argument('--workers',type=int,default=4)
    ap.add_argument('--carry-residue-dir',type=pathlib.Path); a=ap.parse_args()
    manifest=json.loads(a.manifest.read_text()); packet=manifest['packets'][a.packet_id]; residues=[int(x) for x in packet['residues']]
    a.output.mkdir(parents=True,exist_ok=True); rr=a.output/'residue-runs'; rr.mkdir(exist_ok=True)

    carried=[]
    if a.carry_residue_dir and a.carry_residue_dir.exists():
        src=a.carry_residue_dir/'residue-runs' if (a.carry_residue_dir/'residue-runs').exists() else a.carry_residue_dir
        for r in residues:
            sj=src/f'residue-{r}.json'; sb=src/f'residue-{r}.bin'
            if not sj.exists() or not sb.exists(): continue
            validate_residue(sj,sb,r)
            shutil.copy2(sj,rr/f'residue-{r}.json'); shutil.copy2(sb,rr/f'residue-{r}.bin'); carried.append(r)

    missing=[r for r in residues if r not in set(carried)]
    def run_one(r:int):
        jp=rr/f'residue-{r}.json'; bp=rr/f'residue-{r}.bin'
        cmd=[str(a.exe),'--input',str(a.input),'--bundle',str(a.bundle),'--output',str(jp),'--dump-canonical',str(bp),'--bound','14','--shard-id',str(r),'--shard-count','1024','--split-coordinate','54','--node-cap',str(a.node_cap)]
        q=subprocess.run(cmd,text=True,capture_output=True)
        (rr/f'residue-{r}.stdout.txt').write_text(q.stdout); (rr/f'residue-{r}.stderr.txt').write_text(q.stderr)
        return q.returncode,jp,bp,q.stderr
    workers=max(1,min(a.workers,len(missing))) if missing else 0
    done={}
    if missing:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            futs={ex.submit(run_one,r):r for r in missing}
            for f in concurrent.futures.as_completed(futs): done[futs[f]]=f.result()

    walls=[]; all_records=[]; hist={}; totals={k:0 for k in COUNTERS}; lock=None; per=[]
    carried_set=set(carried)
    for r in residues:
        jp=rr/f'residue-{r}.json'; bp=rr/f'residue-{r}.bin'
        if r not in carried_set:
            rc,jp,bp,err=done[r]
            if rc!=0:
                if 'exact traversal node cap exceeded' in err: walls.append(r); continue
                raise RuntimeError(f'unexpected residue failure {r}: {err[-2000:]}')
        d,rs=validate_residue(jp,bp,r)
        here=tuple(d.get(k) for k in LOCK_KEYS)
        if lock is None: lock=here
        if here!=lock: raise RuntimeError('source lock mismatch')
        all_records.extend(rs)
        for k,v in d['canonical_norm_histogram'].items(): hist[str(k)]=hist.get(str(k),0)+int(v)
        for k in COUNTERS: totals[k]+=int(d.get(k,0))
        per.append({'residue':r,'source':'carry' if r in carried_set else 'current','canonical_survivors_including_zero':len(rs),
            'canonical_norm_histogram':d['canonical_norm_histogram'],'canonical_dump_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),
            'nodes':d.get('nodes'),'coordinate_trials':d.get('coordinate_trials')})
    manifest_sha=hashlib.sha256(a.manifest.read_bytes()).hexdigest()
    if walls:
        out={'schema':'STAGE32_18O_D16_B14_PACKET_PILOT_V1','status':'RESOURCE_WALL_NODE_CAP','bound':14,'packet_id':a.packet_id,'tier':packet['tier'],'residues':residues,
            'carried_residues':sorted(carried),'computed_residues':sorted(set(missing)-set(walls)),'completed_residues':[x['residue'] for x in per],
            'wall_residues':walls,'per_residue_node_cap':a.node_cap,'manifest_sha256':manifest_sha,'parallel_residue_workers':workers,
            'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False}
        (a.output/'packet-certificate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True)); return
    if len(all_records)!=len(set(all_records)): raise RuntimeError('duplicate packet records')
    record_hist={}
    for x in all_records: record_hist[str(x[0])]=record_hist.get(str(x[0]),0)+1
    if record_hist!=hist: raise RuntimeError('hist mismatch')
    all_records=sorted(all_records); dump=a.output/'packet-canonical.bin'; dump.write_bytes(MAGIC+b''.join(all_records)); locks=dict(zip(LOCK_KEYS,lock))
    out={'schema':'STAGE32_18O_D16_B14_PACKET_PILOT_V1','status':'COMPLETE','bound':14,'packet_id':a.packet_id,'tier':packet['tier'],'residues':residues,'residue_count':len(residues),
        'manifest_sha256':manifest_sha,'hybrid_risk_sum':packet['hybrid_risk_sum'],'p50_probe_prefix_sum':packet['p50_probe_prefix_sum'],'p48_probe_prefix_sum':packet['p48_probe_prefix_sum'],
        'canonical_survivors_including_zero':len(all_records),'canonical_nonzero_survivors':len(all_records)-hist.get('0',0),'canonical_norm_histogram':hist,
        'canonical_dump_sha256':hashlib.sha256(dump.read_bytes()).hexdigest(),'packet_residue_partition_complete':True,'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,'execution_work_counters_are_sum_of_independent_residue_runs_with_repeated_presplit_work':True,
        'execution_work_totals':totals,'per_residue':per,'parallel_residue_workers':workers,'carried_residues':sorted(carried),'computed_residues':sorted(missing),**locks,
        'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False}
    (a.output/'packet-certificate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'packet_id':a.packet_id,'status':'COMPLETE','residues':residues,'carried':sorted(carried),'computed':sorted(missing),'canonical':len(all_records)},sort_keys=True))
if __name__=='__main__':
    try: main()
    except Exception as e: print(f'ERROR: {e}',file=sys.stderr); raise
