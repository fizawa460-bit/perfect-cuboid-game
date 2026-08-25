#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

M=140
MAGIC=b"S32D16C1"
EXPECTED_SCHEMA="STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
EXPECTED_AUT="7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3"
EXPECTED_HPERP="7cd24466752b21a30b4f523c04892215d5ad0f33d1cc61bc09fa8f6dc815edd3"
EXPECTED_B10_DUMP_SHA="186085d4824e8752f11fa81c5f538e54fe724268defe288e5c2e004613bb474a"
EXPECTED_B10_COUNT=1430
EXPECTED_B10_HIST={"0":1,"2":1,"4":7,"6":28,"8":223,"10":1170}


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
    ap.add_argument('--shards',type=pathlib.Path,required=True)
    ap.add_argument('--audited-b10-dump',type=pathlib.Path,required=True)
    ap.add_argument('--output-json',type=pathlib.Path,required=True)
    ap.add_argument('--output-dump',type=pathlib.Path,required=True)
    ap.add_argument('--certificate',type=pathlib.Path,required=True)
    ap.add_argument('--shard-count',type=int,default=64)
    ap.add_argument('--bound',type=int,default=12)
    ap.add_argument('--breaker-count',type=int,default=256)
    args=ap.parse_args()

    js=sorted(args.shards.glob('d16-b12-exact-shard-*.json'))
    bins=sorted(args.shards.glob('d16-b12-exact-shard-*.bin'))
    if len(js)!=args.shard_count or len(bins)!=args.shard_count:
        raise RuntimeError(f"expected {args.shard_count} shard json/bin files, got {len(js)}/{len(bins)}")

    totals={k:0 for k in [
        'nodes','coordinate_trials','exact_prune_checks','exact_constraint_prunes',
        'exact_symmetry_prune_checks','exact_symmetry_prunes','exact_norm_leaves',
        'leaf_cap_survivors_after_branch_symmetry','precanonical_survivors',
        'canonical_rejects','canonical_survivors_including_zero',
        'canonical_nonzero_survivors','owned_prefixes']}
    hist={}
    seen_ids=set(); split_coordinate=None; bundle_sha=None; records=[]
    for p in js:
        d=json.loads(p.read_text())
        if d.get('schema')!=EXPECTED_SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=args.bound:
            raise RuntimeError(f"bad shard status/schema {p}")
        if d.get('stable_aut_content_sha256')!=EXPECTED_AUT or d.get('prepared_input_sha256')!=EXPECTED_HPERP:
            raise RuntimeError(f"source lock mismatch {p}")
        if d.get('aut_group_order')!=1536 or d.get('dfs_symmetry_breaker_count')!=args.breaker_count:
            raise RuntimeError(f"group/breaker mismatch {p}")
        if d.get('shard_count')!=args.shard_count:
            raise RuntimeError(f"shard count mismatch {p}")
        if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True:
            raise RuntimeError(f"missing traversal certificate {p}")
        if d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True:
            raise RuntimeError(f"missing exact symmetry branch certificate {p}")
        sid=d.get('shard_id')
        if sid in seen_ids or not isinstance(sid,int) or not 0<=sid<args.shard_count:
            raise RuntimeError(f"bad/duplicate shard id {sid}")
        seen_ids.add(sid)
        sc=d.get('split_coordinate')
        if split_coordinate is None: split_coordinate=sc
        if sc!=split_coordinate: raise RuntimeError('split coordinate mismatch')
        bs=d.get('canonical_bundle_sha256')
        if bundle_sha is None: bundle_sha=bs
        if bs!=bundle_sha: raise RuntimeError('bundle sha mismatch')
        for k in totals: totals[k]+=int(d.get(k,0))
        for k,v in d.get('canonical_norm_histogram',{}).items(): hist[str(k)]=hist.get(str(k),0)+int(v)

    for p in bins: records.extend(read_records(p))
    if len(records)!=totals['canonical_survivors_including_zero']:
        raise RuntimeError('aggregate record count mismatch')
    if len(records)!=len(set(records)):
        raise RuntimeError('duplicate canonical records across exact shards')
    records=sorted(records)

    audited_raw=args.audited_b10_dump.read_bytes()
    if hashlib.sha256(audited_raw).hexdigest()!=EXPECTED_B10_DUMP_SHA:
        raise RuntimeError('audited b10 dump sha mismatch')
    audited=sorted(read_records(args.audited_b10_dump))
    if len(audited)!=EXPECTED_B10_COUNT:
        raise RuntimeError('audited b10 record count mismatch')
    predecessor=sorted(r for r in records if r[0]<=10)
    if predecessor!=audited:
        raise RuntimeError('exact b12 <=10 predecessor subset differs from hostile-audited exact b10 set')
    lower={k:v for k,v in hist.items() if int(k)<=10}
    if lower!=EXPECTED_B10_HIST:
        raise RuntimeError(f'b10 histogram regression mismatch {lower}')

    args.output_dump.write_bytes(MAGIC+b''.join(records))
    dump_sha=hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    summary={
        'schema':'STAGE32_18E_D16_B12_EXACT_SYMMETRY_SHARDED_AGGREGATE_V1',
        'status':'COMPLETE','bound':args.bound,'aut_group_order':1536,
        'stable_aut_content_sha256':EXPECTED_AUT,'prepared_input_sha256':EXPECTED_HPERP,
        'canonical_bundle_sha256':bundle_sha,'breaker_count':args.breaker_count,
        'shard_count':args.shard_count,'split_coordinate':split_coordinate,
        **totals,'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,
        'audited_b10_predecessor_set_identical':True,
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'D16_B12_NUMERICAL_CREDIT':False,'AUDIT_STATUS':'PENDING',
        'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,
    }
    args.output_json.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    cert={
        'schema':'STAGE32_18E_D16_B12_EXACT_PRODUCTION_CERTIFICATE_V1',
        'verdict':'PASS_EXACT_SYMMETRY_SHARDED_D16_B12_PRODUCTION_PENDING_HOSTILE_AUDIT',
        'AUDIT_STATUS':'PENDING','bound':args.bound,'shard_count':args.shard_count,
        'breaker_count':args.breaker_count,'split_coordinate':split_coordinate,
        'aggregate_nodes':totals['nodes'],'aggregate_coordinate_trials':totals['coordinate_trials'],
        'exact_cap_prunes':totals['exact_constraint_prunes'],'exact_symmetry_prunes':totals['exact_symmetry_prunes'],
        'canonical_survivors_including_zero':totals['canonical_survivors_including_zero'],
        'canonical_nonzero_survivors':totals['canonical_nonzero_survivors'],
        'canonical_norm_histogram':hist,'new_norm12_canonical_survivors':hist.get('12',0),
        'canonical_dump_sha256':dump_sha,'canonical_bundle_sha256':bundle_sha,
        'audited_b10_predecessor_set_identical':True,
        'D16_B12_NUMERICAL_CREDIT':False,
        'D16_B12_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':True,
        'FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED':False,
        'SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED':False,
        'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,
    }
    args.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps(cert,sort_keys=True))

if __name__=='__main__': main()
