#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib
M=140
EXPECTED_STABLE="7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3"

def records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=b"S32D16C1": raise RuntimeError("bad dump magic")
    body=raw[8:]; size=M+1
    if len(body)%size: raise RuntimeError("truncated dump")
    return [(body[o],bytes(body[o+1:o+size])) for o in range(0,len(body),size)]

def sha(p:pathlib.Path): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    for n in ("exact_json","exact_dump","exact_verify","fast_json","fast_dump","fast_verify","provenance","output"):
        ap.add_argument("--"+n.replace("_","-"),dest=n,type=pathlib.Path,required=True)
    ap.add_argument("--bound",type=int,required=True)
    a=ap.parse_args()
    e=json.loads(a.exact_json.read_text()); f=json.loads(a.fast_json.read_text())
    ev=json.loads(a.exact_verify.read_text()); fv=json.loads(a.fast_verify.read_text())
    p=json.loads(a.provenance.read_text())
    er=records(a.exact_dump); fr=records(a.fast_dump)
    if e.get("schema")!="STAGE32_18B_D16_EXACT_BOUNDED_TRAVERSAL_CERT_V1": raise RuntimeError("bad exact schema")
    if e.get("bound")!=a.bound or f.get("bound")!=a.bound: raise RuntimeError("bound mismatch")
    if e.get("status")!="COMPLETE" or f.get("status")!="COMPLETE": raise RuntimeError("incomplete traversal")
    if e.get("TRAVERSAL_COMPLETENESS_CERTIFICATE") is not True: raise RuntimeError("missing exact completeness certificate")
    if e.get("floating_arithmetic_used_for_traversal_pruning") is not False: raise RuntimeError("unsafe exact traversal flag")
    if p.get("stable_aut_content_sha256")!=EXPECTED_STABLE or e.get("stable_aut_content_sha256")!=EXPECTED_STABLE: raise RuntimeError("stable Aut mismatch")
    if len(er)!=len(set(er)) or len(fr)!=len(set(fr)): raise RuntimeError("duplicate records")
    if set(er)!=set(fr): raise RuntimeError(f"exact/fast canonical sets differ exact={len(er)} fast={len(fr)}")
    if ev.get("every_emitted_pairing_is_full_group_score_then_lex_minimum") is not True: raise RuntimeError("exact full-group verify failed")
    if fv.get("every_emitted_pairing_is_full_group_score_then_lex_minimum") is not True: raise RuntimeError("fast full-group verify failed")
    caps=int(e["cap_survivors_before_symmetry"]); pre=int(e["precanonical_survivors"]); canon=int(e["canonical_survivors_including_zero"])
    if canon<=0 or pre<canon or caps<pre: raise RuntimeError("invalid survivor monotonicity")
    out={
      "schema":"STAGE32_18B_D16_BOUNDED_PRODUCTION_CERTIFICATE_V1",
      "verdict":"PASS_EXACT_CROSS_CERTIFIED_D16_BOUNDED_PRODUCTION",
      "bound":a.bound,
      "exact_nodes":e["nodes"],
      "exact_coordinate_trials":e["coordinate_trials"],
      "exact_cap_prunes":e["exact_constraint_prunes"],
      "cap_survivors_before_symmetry":caps,
      "symmetry_breaker_survivors":pre,
      "canonical_survivors_including_zero":canon,
      "canonical_nonzero_survivors":e["canonical_nonzero_survivors"],
      "cap_to_canonical_compression_ratio":caps/canon,
      "breaker_to_canonical_compression_ratio":pre/canon,
      "exact_and_fast_canonical_sets_identical":True,
      "canonical_dump_sha256":sha(a.exact_dump),
      "stable_aut_content_sha256":EXPECTED_STABLE,
      "AUDIT_STATUS":"PENDING",
      "THEOREM_CREDIT":False,"RECEIVER_CREDIT":False,"FULL_D16_G0_ROW_COMPLETE":False,
      "FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED":False,
      "D16_PRODUCTION_EXACT_OR_CROSS_CERTIFICATE_REQUIRED":True
    }
    if sha(a.exact_dump)!=sha(a.fast_dump): raise RuntimeError("byte-level canonical dump mismatch")
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
