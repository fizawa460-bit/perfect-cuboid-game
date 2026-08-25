#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

M=140
MAGIC=b"S32D16C1"
EXPECTED_SCHEMA="STAGE32_18C_D16_EXACT_SHARDED_TRAVERSAL_CERT_V1"
EXPECTED_AUT="7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3"
EXPECTED_HPERP="7cd24466752b21a30b4f523c04892215d5ad0f33d1cc61bc09fa8f6dc815edd3"
AUDITED_B8_HIST={"0":1,"2":1,"4":7,"6":28,"8":223}

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
    ap.add_argument("--shards",type=pathlib.Path,required=True)
    ap.add_argument("--fixed-fast-json",type=pathlib.Path,required=True)
    ap.add_argument("--fixed-fast-dump",type=pathlib.Path,required=True)
    ap.add_argument("--output-json",type=pathlib.Path,required=True)
    ap.add_argument("--output-dump",type=pathlib.Path,required=True)
    ap.add_argument("--certificate",type=pathlib.Path,required=True)
    ap.add_argument("--shard-count",type=int,default=16)
    ap.add_argument("--bound",type=int,default=10)
    args=ap.parse_args()

    js=sorted(args.shards.glob("d16-b10-exact-shard-*.json"))
    bins=sorted(args.shards.glob("d16-b10-exact-shard-*.bin"))
    if len(js)!=args.shard_count or len(bins)!=args.shard_count:
        raise RuntimeError(f"expected {args.shard_count} shard json/bin files, got {len(js)}/{len(bins)}")

    seen_ids=set()
    totals={k:0 for k in ["nodes","coordinate_trials","exact_prune_checks","exact_constraint_prunes","exact_norm_leaves",
                          "cap_survivors_before_symmetry","precanonical_survivors","canonical_rejects",
                          "canonical_survivors_including_zero","canonical_nonzero_survivors","owned_prefixes"]}
    hist={}
    records=[]
    split_coordinate=None
    for p in js:
        d=json.loads(p.read_text())
        if d.get("schema")!=EXPECTED_SCHEMA or d.get("status")!="COMPLETE" or d.get("bound")!=args.bound:
            raise RuntimeError(f"bad shard status/schema {p}")
        if d.get("stable_aut_content_sha256")!=EXPECTED_AUT or d.get("prepared_input_sha256")!=EXPECTED_HPERP:
            raise RuntimeError(f"source lock mismatch {p}")
        if d.get("aut_group_order")!=1536 or d.get("shard_count")!=args.shard_count:
            raise RuntimeError(f"group/shard count mismatch {p}")
        if d.get("TRAVERSAL_COMPLETENESS_CERTIFICATE") is not True:
            raise RuntimeError(f"missing traversal completeness certificate {p}")
        sid=d.get("shard_id")
        if sid in seen_ids or not isinstance(sid,int) or not 0<=sid<args.shard_count:
            raise RuntimeError(f"bad/duplicate shard id {sid}")
        seen_ids.add(sid)
        sc=d.get("split_coordinate")
        if split_coordinate is None: split_coordinate=sc
        if sc!=split_coordinate: raise RuntimeError("split coordinate mismatch")
        for k in totals: totals[k]+=int(d.get(k,0))
        for k,v in d.get("canonical_norm_histogram",{}).items(): hist[str(k)]=hist.get(str(k),0)+int(v)

    if seen_ids != set(range(args.shard_count)):
        raise RuntimeError(f"shard id coverage mismatch: {sorted(seen_ids)}")

    for p in bins: records.extend(read_records(p))
    if len(records)!=totals["canonical_survivors_including_zero"]:
        raise RuntimeError("aggregate record count mismatch")
    if len(records)!=len(set(records)):
        raise RuntimeError("duplicate canonical records across exact shards")
    records=sorted(records)

    lower={k:v for k,v in hist.items() if int(k)<=8}
    if lower!=AUDITED_B8_HIST or sum(lower.values())!=260:
        raise RuntimeError(f"audited b8 predecessor regression mismatch {lower}")

    args.output_dump.write_bytes(MAGIC+b"".join(records))
    dump_sha=hashlib.sha256(args.output_dump.read_bytes()).hexdigest()

    fixed=json.loads(args.fixed_fast_json.read_text())
    if fixed.get("bound")!=args.bound or fixed.get("status")!="COMPLETE":
        raise RuntimeError("snapshot-fixed fast b10 incomplete")
    fixed_records=sorted(read_records(args.fixed_fast_dump))
    fixed_equal=(records==fixed_records)

    exact_summary={
      "schema":"STAGE32_18C_D16_B10_SHARDED_EXACT_AGGREGATE_V2",
      "status":"COMPLETE","bound":args.bound,"aut_group_order":1536,
      "stable_aut_content_sha256":EXPECTED_AUT,"prepared_input_sha256":EXPECTED_HPERP,
      "shard_count":args.shard_count,"split_coordinate":split_coordinate,**totals,
      "canonical_norm_histogram":hist,"canonical_dump_sha256":dump_sha,
      "audited_b8_predecessor_regression_pass":True,
      "snapshot_fixed_fast_set_identical":fixed_equal,
      "TRAVERSAL_COMPLETENESS_CERTIFICATE":True,
      "THEOREM_CREDIT":False,"RECEIVER_CREDIT":False,"FULL_D16_G0_ROW_COMPLETE":False
    }
    args.output_json.write_text(json.dumps(exact_summary,indent=2,sort_keys=True)+"\n")

    cap=totals["cap_survivors_before_symmetry"]
    canon=totals["canonical_survivors_including_zero"]
    cert={
      "schema":"STAGE32_18C_D16_B10_EXACT_ONLY_RECOVERY_CERTIFICATE_V1",
      "verdict":"PASS_EXACT_SHARDED_D16_B10_WITH_SNAPSHOT_FAST_CROSSCHECK" if fixed_equal else "PASS_EXACT_SHARDED_D16_B10_FAST_CROSSCHECK_MISMATCH",
      "AUDIT_STATUS":"PENDING","bound":args.bound,"shard_count":args.shard_count,
      "split_coordinate":split_coordinate,"aggregate_shard_nodes":totals["nodes"],
      "aggregate_shard_coordinate_trials":totals["coordinate_trials"],
      "aggregate_shard_exact_cap_prunes":totals["exact_constraint_prunes"],
      "cap_survivors_before_symmetry":cap,
      "symmetry_breaker_survivors":totals["precanonical_survivors"],
      "canonical_survivors_including_zero":canon,
      "canonical_nonzero_survivors":totals["canonical_nonzero_survivors"],
      "canonical_norm_histogram":hist,"new_norm10_canonical_survivors":hist.get("10",0),
      "cap_to_canonical_compression_ratio":cap/canon if canon else None,
      "audited_b8_predecessor_regression_pass":True,
      "snapshot_fixed_fast_set_identical":fixed_equal,
      "canonical_dump_sha256":dump_sha,"stable_aut_content_sha256":EXPECTED_AUT,
      "FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED":False,
      "SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED":False,
      "D16_B10_NUMERICAL_CREDIT_READY_FOR_AUDIT":True,
      "D16_PRODUCTION_EXACT_OR_CROSS_CERTIFICATE_REQUIRED":True,
      "FULL_D16_G0_ROW_COMPLETE":False,"THEOREM_CREDIT":False,"RECEIVER_CREDIT":False
    }
    args.certificate.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
    print(json.dumps(cert,sort_keys=True))

if __name__=="__main__": main()
