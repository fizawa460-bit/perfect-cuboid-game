#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

M=140
MAGIC=b"S32D16C1"
EXPECTED_SCHEMA="STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
TOTAL_KEYS=[
    'nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes',
    'exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves',
    'leaf_cap_survivors_after_branch_symmetry','precanonical_survivors',
    'canonical_rejects','canonical_survivors_including_zero',
    'canonical_nonzero_survivors','owned_prefixes'
]

def read_records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=MAGIC:
        raise RuntimeError(f"bad dump magic {path}")
    body=raw[8:]
    size=M+1
    if len(body)%size:
        raise RuntimeError(f"truncated dump {path}")
    return [body[i:i+size] for i in range(0,len(body),size)]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=pathlib.Path,required=True)
    ap.add_argument('--output-json',type=pathlib.Path,required=True)
    ap.add_argument('--output-dump',type=pathlib.Path,required=True)
    ap.add_argument('--certificate',type=pathlib.Path,required=True)
    ap.add_argument('--parent-shard-id',type=int,required=True)
    ap.add_argument('--parent-shard-count',type=int,required=True)
    ap.add_argument('--rescue-shard-count',type=int,required=True)
    ap.add_argument('--rescue-shard-ids',required=True)
    args=ap.parse_args()

    rescue_ids=sorted(int(x) for x in args.rescue_shard_ids.split(',') if x!='')
    expected=sorted(r for r in range(args.rescue_shard_count)
                    if r%args.parent_shard_count==args.parent_shard_id)
    if rescue_ids!=expected:
        raise RuntimeError(f"residue partition mismatch: got {rescue_ids}, expected {expected}")

    jsons=[]
    bins=[]
    for sid in rescue_ids:
        jp=args.input/f'd16-b12-exact-subshard-{sid}-of{args.rescue_shard_count}.json'
        bp=args.input/f'd16-b12-exact-subshard-{sid}-of{args.rescue_shard_count}.bin'
        if not jp.exists() or not bp.exists():
            raise RuntimeError(f"missing rescue subshard {sid}")
        jsons.append((sid,json.loads(jp.read_text())))
        bins.append((sid,bp))

    totals={k:0 for k in TOTAL_KEYS}
    hist={}
    split_prefixes_seen=0
    records=[]
    lock=None
    for sid,d in jsons:
        if d.get('schema')!=EXPECTED_SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=12:
            raise RuntimeError(f"bad status/schema for rescue subshard {sid}")
        if d.get('shard_id')!=sid or d.get('shard_count')!=args.rescue_shard_count:
            raise RuntimeError(f"bad shard metadata for {sid}")
        if d.get('split_coordinate')!=54 or d.get('dfs_symmetry_breaker_count')!=256:
            raise RuntimeError(f"bad split/breaker metadata for {sid}")
        if d.get('aut_group_order')!=1536:
            raise RuntimeError(f"bad Aut order for {sid}")
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True:
            raise RuntimeError(f"missing traversal certificate for {sid}")
        if d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True:
            raise RuntimeError(f"missing exact symmetry certificate for {sid}")
        here=(d.get('stable_aut_content_sha256'),d.get('prepared_input_sha256'),d.get('canonical_bundle_sha256'))
        if lock is None: lock=here
        if here!=lock:
            raise RuntimeError(f"source/bundle lock mismatch for {sid}")
        for k in TOTAL_KEYS:
            totals[k]+=int(d.get(k,0))
        split_prefixes_seen+=int(d.get('split_prefixes_seen',0))
        for k,v in d.get('canonical_norm_histogram',{}).items():
            hist[str(k)]=hist.get(str(k),0)+int(v)

    for sid,bp in bins:
        rs=read_records(bp)
        if len(rs)!=int(dict(jsons)[sid].get('canonical_survivors_including_zero',0)):
            raise RuntimeError(f"record count mismatch for {sid}")
        records.extend(rs)
    if len(records)!=len(set(records)):
        raise RuntimeError('duplicate canonical records across rescue subshards')
    if len(records)!=totals['canonical_survivors_including_zero']:
        raise RuntimeError('synthetic parent record count mismatch')
    records=sorted(records)
    record_hist={}
    for r in records:
        record_hist[str(r[0])]=record_hist.get(str(r[0]),0)+1
    if record_hist!=hist:
        raise RuntimeError(f"histogram mismatch records={record_hist} json={hist}")

    args.output_dump.parent.mkdir(parents=True,exist_ok=True)
    args.output_dump.write_bytes(MAGIC+b''.join(records))
    dump_sha=hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    stable_aut,prepared_input,bundle_sha=lock
    out={
        'schema':EXPECTED_SCHEMA,'status':'COMPLETE','bound':12,
        'aut_group_order':1536,'stable_aut_content_sha256':stable_aut,
        'prepared_input_sha256':prepared_input,'canonical_bundle_sha256':bundle_sha,
        'dfs_symmetry_breaker_count':256,'shard_id':args.parent_shard_id,
        'shard_count':args.parent_shard_count,'split_coordinate':54,
        'split_prefixes_seen':split_prefixes_seen,**totals,
        'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'all_symmetry_branch_rejections_exact_rational_cauchy_schwarz':True,
        'rescue_subshard_partition_certificate':True,
        'rescue_parent_residue_equivalence':f'h%{args.parent_shard_count}=={args.parent_shard_id} iff h%{args.rescue_shard_count} in {rescue_ids}',
        'rescue_subshard_count':len(rescue_ids),'rescue_shard_count':args.rescue_shard_count,
        'rescue_subshard_ids':rescue_ids,
        'D16_B12_NUMERICAL_CREDIT':False,'AUDIT_STATUS':'PENDING',
        'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,
    }
    args.output_json.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    cert={
        'schema':'STAGE32_18F_D16_B12_SHARD_RESCUE_CERTIFICATE_V1',
        'verdict':'PASS_EXACT_RESCUE_SYNTHETIC_PARENT_SHARD_PENDING_GLOBAL_AGGREGATION_AND_HOSTILE_AUDIT',
        'parent_shard_id':args.parent_shard_id,'parent_shard_count':args.parent_shard_count,
        'rescue_shard_count':args.rescue_shard_count,'rescue_subshard_ids':rescue_ids,
        'residue_partition_exact':True,'canonical_survivors_including_zero':totals['canonical_survivors_including_zero'],
        'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'D16_B12_NUMERICAL_CREDIT':False,'D16_B12_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':False,
        'GLOBAL_B12_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING',
        'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,
    }
    args.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps(cert,sort_keys=True))

if __name__=='__main__':
    main()
