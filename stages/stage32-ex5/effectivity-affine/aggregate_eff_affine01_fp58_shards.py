#!/usr/bin/env python3
"""Fail-closed aggregator for exact EFF-AFFINE01 FP58 shards."""
import argparse, hashlib, json
from pathlib import Path

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

ap=argparse.ArgumentParser()
ap.add_argument("--inputs",type=Path,nargs="+",required=True)
ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args()
rows=[json.loads(p.read_text()) for p in a.inputs]
if not rows: raise SystemExit("FAIL: no shards")
for r in rows:
    claimed=r.get("canonical_sha256_without_this_field")
    u=dict(r); u.pop("canonical_sha256_without_this_field",None)
    if claimed!=csha(u): raise SystemExit("FAIL: shard canonical mismatch")
base4=rows[0]["base4"]; count=rows[0]["shard"]["count"]; split=rows[0]["shard"]["split_index"]
EXPECTED_SCHEMA="STAGE32EX5_EFF_AFFINE01_FP58_KEY_V1"
EXPECTED_PARTITION="SHA256_REPR_PREFIX_MOD_COUNT_V1"
EXPECTED_BAD_SHELL=[-20,3]
EXPECTED_KERNEL_DIMENSION=58
for r in rows:
    if r.get("schema")!=EXPECTED_SCHEMA: raise SystemExit("FAIL: shard schema")
    if r.get("complete") is not True: raise SystemExit("FAIL: incomplete shard")
    if r.get("base4")!=base4 or r.get("bad_shell")!=EXPECTED_BAD_SHELL: raise SystemExit("FAIL: population mismatch")
    if r.get("kernel_dimension")!=EXPECTED_KERNEL_DIMENSION or r.get("all140_pruning") is not True: raise SystemExit("FAIL: engine semantics")
    if r.get("credit")!={"effectivity":False,"main":False}: raise SystemExit("FAIL: credit firewall")
    s=r.get("shard",{})
    if s.get("count")!=count or s.get("split_index")!=split or s.get("partition")!=EXPECTED_PARTITION: raise SystemExit("FAIL: shard partition")
    cls=r.get("classification"); wit=r.get("witness")
    if cls=="BAD_SHELL_SAT_WITNESS":
        if not isinstance(wit,dict) or not (EXPECTED_BAD_SHELL[0] <= wit.get("C2",10**9) <= EXPECTED_BAD_SHELL[1]): raise SystemExit("FAIL: witness/classification")
    elif cls=="BAD_SHELL_UNSAT_EXACT":
        if wit is not None: raise SystemExit("FAIL: UNSAT carries witness")
    else: raise SystemExit("FAIL: unexpected shard classification")
ids=sorted(r["shard"]["id"] for r in rows)
if ids!=list(range(count)): raise SystemExit("FAIL: shard coverage")
w=[r["witness"] for r in rows if r.get("witness") is not None]
classification="BAD_SHELL_SAT_WITNESS" if w else "BAD_SHELL_UNSAT_EXACT"
out={"schema":"STAGE32EX5_EFF_AFFINE01_FP58_AGGREGATE_V1","base4":base4,
     "classification":classification,"complete":True,"shard_count":count,
     "split_index":split,"partition":"SHA256_REPR_PREFIX_MOD_COUNT_V1",
     "total_nodes":sum(r.get("node_count",0) for r in rows),
     "total_intersection_prunes":sum(r.get("intersection_prune_count",0) for r in rows),
     "witness":w[0] if w else None,"credit":{"effectivity":False,"main":False}}
out["canonical_sha256_without_this_field"]=csha(out)
a.output.parent.mkdir(parents=True,exist_ok=True)
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print("EFF_AFFINE01_FP58_AGGREGATE="+classification)
print("CANONICAL="+out["canonical_sha256_without_this_field"])
