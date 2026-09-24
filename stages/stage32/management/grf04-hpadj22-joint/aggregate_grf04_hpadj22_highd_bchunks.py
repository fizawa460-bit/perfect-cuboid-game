#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

SCHEMA_CHUNK="STAGE32_MAIN_V46_GRF04_HPADJ22_HIGHD_BCHUNK_V1"
SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_HIGHD_BCHUNK_AGGREGATE_V1"
EXPECTED=[(84,87),(88,90),(91,93),(94,96)]
BASELINE=236901807892797077

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--chunks-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    found={}
    for p in sorted(a.chunks_root.rglob("*.json")):
        d=json.loads(p.read_text())
        if d.get("schema")!=SCHEMA_CHUNK:continue
        req(d.get("canonical_sha256_without_this_field")==canon(d),f"chunk canonical drift {p}")
        t=d["target"]
        req((int(t["row_index"]),int(t["g"]),int(t["d"]),int(t["band_position"]))==(177,1,190,7),"target drift")
        key=tuple(int(x) for x in t["b_chunk"])
        req(key in EXPECTED and key not in found,f"chunk coverage/duplicate drift {key}")
        req(d["exactness"]["partial_b_partition_only"] is True,"partition semantics drift")
        req(d["exactness"]["hpadj22_partial_exact"] is True,"partial baseline exactness drift")
        req(d["exactness"]["x4_intersection_exact"] is True,"x4 exactness drift")
        req(d["exactness"]["e_independence_used"] is True,"e-independence drift")
        req(d["exactness"]["min_of_counts_used"] is False,"min-of-counts drift")
        req(d["exactness"]["additive_subtraction"] is False,"additive drift")
        req(d["firewalls"]["main_pruning_credit"] is False and d["firewalls"]["merge_authorized"] is False,"credit firewall drift")
        found[key]=d
    req(set(found)==set(EXPECTED),f"incomplete chunks {sorted(found)}")

    baseline=joint=0;summaries=[]
    for key in EXPECTED:
        d=found[key];r=d["result"]
        b=int(r["partial_hpadj22_exact_survivors"]);j=int(r["partial_joint_exact_survivors"])
        req(j<=b,f"chunk weakened baseline {key}")
        baseline+=b;joint+=j
        summaries.append({"b_chunk":list(key),"baseline":str(b),"joint":str(j),
          "improvement":str(b-j),"strict":bool(r["strict"]),
          "canonical":d["canonical_sha256_without_this_field"],"timing_seconds":d["timing_seconds"]})
    req(baseline==BASELINE,f"row177 HPADJ22 baseline mismatch {baseline}!={BASELINE}")
    req(joint<=baseline,"aggregate joint weakened baseline")

    out={
      "schema":SCHEMA,"stage":32,"status":"HIGHD_EXACT_FULL_BAND_AGGREGATE_ZERO_CREDIT",
      "target":{"row_index":177,"row_id":"g1-d190","g":1,"d":190,"band_position":7,"b_interval":[84,96]},
      "coverage":{"chunk_count":4,"expected_chunks":[list(x) for x in EXPECTED],"gaps":0,"overlaps":0},
      "result":{"hpadj22_exact_survivors":baseline,"joint_exact_survivors":joint,
        "exact_improvement":baseline-joint,"strict":joint<baseline,
        "relative_improvement_num":baseline-joint,"relative_improvement_den":baseline},
      "chunks":summaries,
      "decision":{"full178_scaleout_candidate":joint<baseline,
        "if_strict":"retain this exact execution gate, then prepare a separate resume-first FULL178 active-cell scaleout with zero MAIN credit until aggregate plus hostile audit",
        "if_not_strict":"stop this route"},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"effectivity_credit":False,
        "receiver_credit":False,"route_credit":False,"theorem_credit":False,"endpoint_credit":False,
        "stage32_closed":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("GRF04_HPADJ22_HIGHD_BCHUNK_AGG="+json.dumps({"baseline":baseline,"joint":joint,
      "improvement":baseline-joint,"strict":joint<baseline,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":main()
