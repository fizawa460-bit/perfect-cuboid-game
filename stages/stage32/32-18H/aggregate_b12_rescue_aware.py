#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

M=140
MAGIC=b"S32D16C1"
SCHEMA="STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
EXPECTED_AUT="7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3"
EXPECTED_HPERP="7cd24466752b21a30b4f523c04892215d5ad0f33d1cc61bc09fa8f6dc815edd3"
EXPECTED_B10_DUMP_SHA="186085d4824e8752f11fa81c5f538e54fe724268defe288e5c2e004613bb474a"
EXPECTED_B10_COUNT=1430
EXPECTED_B10_HIST={"0":1,"2":1,"4":7,"6":28,"8":223,"10":1170}
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


def validate(d:dict,sid:int,count:int):
    if d.get('schema')!=SCHEMA or d.get('status')!='COMPLETE' or d.get('bound')!=12:
        raise RuntimeError(f"bad status/schema for {sid}/{count}")
    if d.get('shard_id')!=sid or d.get('shard_count')!=count:
        raise RuntimeError(f"bad shard metadata for {sid}/{count}")
    if d.get('stable_aut_content_sha256')!=EXPECTED_AUT or d.get('prepared_input_sha256')!=EXPECTED_HPERP:
        raise RuntimeError(f"source lock mismatch for {sid}/{count}")
    if d.get('aut_group_order')!=1536 or d.get('dfs_symmetry_breaker_count')!=256:
        raise RuntimeError(f"group/breaker mismatch for {sid}/{count}")
    if d.get('split_coordinate')!=54:
        raise RuntimeError(f"split mismatch for {sid}/{count}")
    if d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is not True:
        raise RuntimeError(f"missing traversal certificate for {sid}/{count}")
    if d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is not True:
        raise RuntimeError(f"missing exact symmetry certificate for {sid}/{count}")


def load_standard(root:pathlib.Path,sid:int,count:int,prefix:str):
    jp=root/f"{prefix}-{sid}-of{count}.json" if count!=64 else root/f"d16-b12-exact-shard-{sid}.json"
    bp=root/f"{prefix}-{sid}-of{count}.bin" if count!=64 else root/f"d16-b12-exact-shard-{sid}.bin"
    if not jp.exists() or not bp.exists():
        return None
    d=json.loads(jp.read_text()); validate(d,sid,count)
    rs=read_records(bp)
    if len(rs)!=int(d.get('canonical_survivors_including_zero',-1)):
        raise RuntimeError(f"record count mismatch {sid}/{count}")
    return d,rs


def add_exec(total:dict,d:dict):
    for k in EXEC_KEYS: total[k]+=int(d.get(k,0))


def hist_of(records):
    h={}
    for r in records: h[str(r[0])]=h.get(str(r[0]),0)+1
    return h


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ordinary',type=pathlib.Path,required=True)
    ap.add_argument('--rescue256',type=pathlib.Path,required=True)
    ap.add_argument('--deep1024',type=pathlib.Path,required=True)
    ap.add_argument('--audited-b10-dump',type=pathlib.Path,required=True)
    ap.add_argument('--output-json',type=pathlib.Path,required=True)
    ap.add_argument('--output-dump',type=pathlib.Path,required=True)
    ap.add_argument('--certificate',type=pathlib.Path,required=True)
    args=ap.parse_args()

    ordinary_ids=set(range(64))-{26}
    ordinary_records=[]; ordinary_exec={k:0 for k in EXEC_KEYS}; bundle=None
    found=set()
    for sid in sorted(ordinary_ids):
        item=load_standard(args.ordinary,sid,64,'unused')
        if item is None: raise RuntimeError(f"missing ordinary shard {sid}")
        d,rs=item; found.add(sid); ordinary_records.extend(rs); add_exec(ordinary_exec,d)
        if bundle is None: bundle=d.get('canonical_bundle_sha256')
        if d.get('canonical_bundle_sha256')!=bundle: raise RuntimeError('bundle mismatch')
    if found!=ordinary_ids: raise RuntimeError('ordinary residue coverage mismatch')
    if len(ordinary_records)!=len(set(ordinary_records)):
        raise RuntimeError('duplicate records across ordinary shards')

    rescue_exec={k:0 for k in EXEC_KEYS}; rescue_records={}; rescue_json={}
    for sid in [90,154,218]:
        item=load_standard(args.rescue256,sid,256,'d16-b12-exact-subshard')
        if item is None: raise RuntimeError(f"missing 256-way rescue shard {sid}")
        d,rs=item; rescue_json[sid]=d; rescue_records[sid]=rs; add_exec(rescue_exec,d)
        if d.get('canonical_bundle_sha256')!=bundle: raise RuntimeError('rescue bundle mismatch')

    direct26=load_standard(args.rescue256,26,256,'d16-b12-exact-subshard')
    direct26_exec={k:0 for k in EXEC_KEYS}
    if direct26 is not None:
        d26,r26=direct26; add_exec(direct26_exec,d26)
        if d26.get('canonical_bundle_sha256')!=bundle: raise RuntimeError('direct26 bundle mismatch')
    else:
        r26=None

    deep_exec={k:0 for k in EXEC_KEYS}; deep_records=[]; split_seen=[]
    for sid in [26,282,538,794]:
        item=load_standard(args.deep1024,sid,1024,'d16-b12-exact-subshard')
        if item is None: raise RuntimeError(f"missing deep 1024-way shard {sid}")
        d,rs=item; add_exec(deep_exec,d); deep_records.extend(rs)
        split_seen.append(int(d.get('split_prefixes_seen',-1)))
        if d.get('canonical_bundle_sha256')!=bundle: raise RuntimeError('deep bundle mismatch')
    if len(set(split_seen))!=1: raise RuntimeError(f"deep pre-split traversal mismatch {split_seen}")
    if len(deep_records)!=len(set(deep_records)):
        raise RuntimeError('duplicate canonical records across deep children')
    deep_records=sorted(deep_records)
    direct_vs_deep=None
    if r26 is not None:
        direct_vs_deep=(sorted(r26)==deep_records)
        if not direct_vs_deep: raise RuntimeError('direct 26/256 differs from exact 1024-way rescue union')

    parent26_records=list(deep_records)
    for sid in [90,154,218]: parent26_records.extend(rescue_records[sid])
    if len(parent26_records)!=len(set(parent26_records)):
        raise RuntimeError('duplicate canonical records inside rescued parent 26/64')
    parent26_records=sorted(parent26_records)

    # Exact nested partition proof by residue arithmetic, independent of observed records.
    if sorted(r for r in range(256) if r%64==26)!=[26,90,154,218]:
        raise RuntimeError('64->256 residue partition identity failed')
    if sorted(r for r in range(1024) if r%256==26)!=[26,282,538,794]:
        raise RuntimeError('256->1024 residue partition identity failed')

    records=ordinary_records+parent26_records
    if len(records)!=len(set(records)):
        raise RuntimeError('duplicate canonical records in global aggregate')
    records=sorted(records); hist=hist_of(records)

    audited_raw=args.audited_b10_dump.read_bytes()
    if hashlib.sha256(audited_raw).hexdigest()!=EXPECTED_B10_DUMP_SHA:
        raise RuntimeError('audited b10 dump sha mismatch')
    audited=sorted(read_records(args.audited_b10_dump))
    if len(audited)!=EXPECTED_B10_COUNT: raise RuntimeError('audited b10 count mismatch')
    predecessor=sorted(r for r in records if r[0]<=10)
    if predecessor!=audited: raise RuntimeError('b12 <=10 predecessor set differs from hostile-audited b10')
    lower={k:v for k,v in hist.items() if int(k)<=10}
    if lower!=EXPECTED_B10_HIST: raise RuntimeError(f"b10 histogram mismatch {lower}")

    args.output_dump.parent.mkdir(parents=True,exist_ok=True)
    args.output_dump.write_bytes(MAGIC+b''.join(records))
    dump_sha=hashlib.sha256(args.output_dump.read_bytes()).hexdigest()
    zero=hist.get('0',0)
    summary={
        'schema':'STAGE32_18H_D16_B12_RESCUE_AWARE_AGGREGATE_V1','status':'COMPLETE','bound':12,
        'aut_group_order':1536,'stable_aut_content_sha256':EXPECTED_AUT,'prepared_input_sha256':EXPECTED_HPERP,
        'canonical_bundle_sha256':bundle,'breaker_count':256,'split_coordinate':54,
        'canonical_survivors_including_zero':len(records),'canonical_nonzero_survivors':len(records)-zero,
        'canonical_norm_histogram':hist,'canonical_dump_sha256':dump_sha,
        'ordinary_64way_shard_ids':sorted(ordinary_ids),'rescued_parent_64way_shard_id':26,
        'rescue_256way_residues':[26,90,154,218],'deep_1024way_residues':[26,282,538,794],
        'nested_residue_partition_exact':True,'direct_26_of256_available':r26 is not None,
        'direct_26_of256_equals_deep_rescue_union':direct_vs_deep,
        'audited_b10_predecessor_set_identical':True,'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'telemetry_semantics':'execution_work counters describe the real shard/rescue runs and include repeated work above split coordinate 54; no hypothetical single-run global node/trial total is claimed',
        'execution_work':{
            'ordinary_63_shards':ordinary_exec,
            'rescue_256way_non26_children':rescue_exec,
            'deep_1024way_children_for_26_of256':deep_exec,
            'optional_direct_26_of256_crosscheck':direct26_exec if r26 is not None else None,
            'deep_logical_parent_split_prefixes_seen':split_seen[0]
        },
        'D16_B12_NUMERICAL_CREDIT':False,'AUDIT_STATUS':'PENDING','FULL_D16_G0_ROW_COMPLETE':False,
        'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
    }
    args.output_json.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    cert={
        'schema':'STAGE32_18H_D16_B12_EXACT_PRODUCTION_CERTIFICATE_V1',
        'verdict':'PASS_EXACT_RESCUE_AWARE_D16_B12_PRODUCTION_PENDING_HOSTILE_AUDIT',
        'AUDIT_STATUS':'PENDING','bound':12,'breaker_count':256,'split_coordinate':54,
        'nested_residue_partition_exact':True,'canonical_survivors_including_zero':len(records),
        'canonical_nonzero_survivors':len(records)-zero,'canonical_norm_histogram':hist,
        'new_norm12_canonical_survivors':hist.get('12',0),'canonical_dump_sha256':dump_sha,
        'canonical_bundle_sha256':bundle,'audited_b10_predecessor_set_identical':True,
        'direct_26_of256_available':r26 is not None,'direct_26_of256_equals_deep_rescue_union':direct_vs_deep,
        'TRAVERSAL_COMPLETENESS_CERTIFICATE':True,
        'D16_B12_NUMERICAL_CREDIT':False,'D16_B12_NUMERICAL_CREDIT_PENDING_HOSTILE_AUDIT':True,
        'FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED':False,'SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED':False,
        'FULL_D16_G0_ROW_COMPLETE':False,'THEOREM_CREDIT':False,'RECEIVER_CREDIT':False
    }
    args.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps(cert,sort_keys=True))


if __name__=='__main__': main()
