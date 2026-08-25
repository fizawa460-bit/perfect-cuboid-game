#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

MAGIC=b"S32D16C1"
M=140
EXPECTED_BASELINE_MISSING={"0":1,"4":2,"8":19}


def records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=MAGIC: raise RuntimeError(f"bad dump magic {path}")
    body=raw[8:]; size=M+1
    if len(body)%size: raise RuntimeError(f"truncated dump {path}")
    return [body[i:i+size] for i in range(0,len(body),size)]


def hist(rs):
    out={}
    for r in rs:
        k=str(r[0]); out[k]=out.get(k,0)+1
    return dict(sorted(out.items(), key=lambda kv:int(kv[0])))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",required=True)
    ap.add_argument("--audited-b8",type=pathlib.Path,required=True)
    ap.add_argument("--baseline-b10",type=pathlib.Path,required=True)
    ap.add_argument("--variant-b10",type=pathlib.Path,required=True)
    ap.add_argument("--variant-json",type=pathlib.Path,required=True)
    ap.add_argument("--output",type=pathlib.Path,required=True)
    args=ap.parse_args()

    b8=records(args.audited_b8)
    baseline=records(args.baseline_b10)
    variant=records(args.variant_b10)
    vjson=json.loads(args.variant_json.read_text())
    if len(b8)!=260: raise RuntimeError(f"audited b8 count {len(b8)} != 260")
    if vjson.get("status")!="COMPLETE" or vjson.get("bound")!=10:
        raise RuntimeError("variant did not complete b10")

    s8=set(b8); sb=set(baseline); sv=set(variant)
    base_missing=sorted(s8-sb)
    variant_missing=sorted(s8-sv)
    if len(base_missing)!=22 or hist(base_missing)!=EXPECTED_BASELINE_MISSING:
        raise RuntimeError(f"baseline b10 regression changed: {len(base_missing)} {hist(base_missing)}")

    missing_blob=b"".join(base_missing)
    recovered=[r for r in base_missing if r in sv]
    added=sorted(sv-sb)
    removed=sorted(sb-sv)
    lower_variant=[r for r in variant if r[0]<=8]
    out={
      "schema":"STAGE32_SCOUT2_FAST_STATE_DRIFT_VARIANT_V1",
      "mode":args.mode,
      "SCOUT_ONLY":True,
      "AUDIT_STATUS":"NOT_APPLICABLE_SCOUT",
      "audited_b8_count":len(b8),
      "baseline_b10_count":len(baseline),
      "baseline_missing_audited_b8_count":len(base_missing),
      "baseline_missing_audited_b8_histogram":hist(base_missing),
      "baseline_missing_records_sha256":hashlib.sha256(missing_blob).hexdigest(),
      "variant_b10_count":len(variant),
      "variant_b10_histogram":hist(variant),
      "variant_lower_le8_count":len(lower_variant),
      "variant_missing_audited_b8_count":len(variant_missing),
      "variant_missing_audited_b8_histogram":hist(variant_missing),
      "recovered_of_baseline_22_count":len(recovered),
      "added_vs_baseline_count":len(added),
      "added_vs_baseline_histogram":hist(added),
      "removed_vs_baseline_count":len(removed),
      "removed_vs_baseline_histogram":hist(removed),
      "variant_nodes":vjson.get("nodes"),
      "variant_coordinate_trials":vjson.get("coordinate_trials"),
      "variant_constraint_prunes":vjson.get("constraint_prunes"),
      "variant_symmetry_prunes":vjson.get("symmetry_prunes"),
      "variant_elapsed_seconds":vjson.get("elapsed_seconds"),
      "audited_b8_subset_restored":len(variant_missing)==0,
      "FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED":False,
      "THEOREM_CREDIT":False,
      "RECEIVER_CREDIT":False,
      "FULL_D16_G0_ROW_COMPLETE":False
    }
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))

if __name__=="__main__": main()
