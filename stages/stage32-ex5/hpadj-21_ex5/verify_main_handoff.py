#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
HANDOFF=HERE/"MAIN-HANDOFF.json"
HANDOFF_BLOB="c0a27ff6fdc78fba8e530d340bf4774be1f5341f"
HANDOFF_CANON="b574fe4c48ac7f525063dfbcc7f9b43aeb0a40877a559e696159d16851ce6416"
CHECKPOINT_BLOB="2161c2dedf94fa2124231453dd56e4047ebd8707"
CHECKPOINT_CANON="f92ccd5296ef9f5ee041baac44cd4933662d9413ea17b4ca1f59a18bf219a961"
PREFLIGHT_BLOB="b8b7dacad95d5b0cfbebbf908d7adfbb78385ef1"
PREFLIGHT_CANON="ff2b20f5e654f45b367a46e893529982014b04215641d1321d57a174d037fae2"
AUDITED_HEAD="265fbef0a67014494fcf773af6c3a9f1b095ef95"
AUDIT_REVIEW=5242670540
MAIN_HEAD="37bb811b95399d73cc46fe899badcfa8eb5fca7d"
OLD=179119009547804181594
NEW=157570677819451133507
GAIN=21548331728353048087

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p):
    raw=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(obj):
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def lock_json(p,b,c,label):
    req(p.is_file(),"missing "+label)
    req(blob(p)==b,label+" blob drift")
    obj=json.loads(p.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field")==c,label+" stored canonical drift")
    req(canon(obj)==c,label+" canonical drift")
    return obj

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--main-root",type=Path); args=ap.parse_args()
    h=lock_json(HANDOFF,HANDOFF_BLOB,HANDOFF_CANON,"HPADJ21 MAIN handoff")
    cp=lock_json(HERE/"FULL178-CHECKPOINT.json",CHECKPOINT_BLOB,CHECKPOINT_CANON,"HPADJ21 checkpoint")
    pf=lock_json(HERE/"MAIN-HANDOFF-PREFLIGHT.json",PREFLIGHT_BLOB,PREFLIGHT_CANON,"HPADJ21 handoff preflight")
    req(h["status"]=="HOSTILE_AUDITED_PRODUCER_READY_FOR_MAIN_NONADDITIVE_REPLACEMENT__ZERO_MAIN_CREDIT","handoff status")
    p=h["producer"]
    req(p["audited_exact_head"]==AUDITED_HEAD and p["hostile_audit_review_id"]==AUDIT_REVIEW and p["hostile_audit_verdict"]=="PASS","audit identity")
    req(p["audit_current_main"]==MAIN_HEAD and p["merge_ready_freshness"]=="PENDING","audit freshness record")
    req(p["checkpoint"]["blob_sha1"]==CHECKPOINT_BLOB and p["checkpoint"]["canonical_sha256"]==CHECKPOINT_CANON,"checkpoint identity")
    req(p["handoff_preflight"]["blob_sha1"]==PREFLIGHT_BLOB and p["handoff_preflight"]["canonical_sha256"]==PREFLIGHT_CANON,"preflight identity")
    heavy=p["heavy_run"]
    req(heavy["run_id"]==35279651998 and heavy["conclusion"]=="success" and heavy["full178_rows"]==178,"heavy result")
    req(heavy["row_gap_count"]==0 and heavy["row_overlap_count"]==0,"heavy coverage")
    req(cp["totals"]["hpadj20_cellwise_floor_sum"]==OLD and cp["totals"]["hpadj21_cellwise_floor_sum"]==NEW,"checkpoint totals")
    t=h["candidate_transition"]
    req(t["current_main_v41_upper_bound"]==OLD and t["hpadj21_candidate_upper_bound"]==NEW,"candidate bounds")
    req(t["strict_improvement_vs_current_main_v41"]==GAIN and OLD-NEW==GAIN,"candidate arithmetic")
    req(t["composition_rule"]=="DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION","composition")
    req(t["recommended_main_composition_rule"]=="MIN_OF_CERTIFIED_UPPER_BOUNDS__HPADJ21_SAME_POPULATION_REFINEMENT__NO_ADDITIVE_STACKING","MAIN composition")
    req(t["same_hpadj20_pre_domain_population"] and t["same_hpadj20_post_mass_constraints"] and t["ordered_triple_population_preserved_exactly"],"population semantics")
    req(not t["additive_subtraction_authorized"] and not t["ex5_main_authority_mutation_performed"] and not t["stage32_full178_numerical_census_complete"],"transition firewalls")
    for k,v in h["firewalls"].items(): req(v is False,"firewall "+k)
    req(pf["producer"]["hostile_audit_status"]=="PENDING_REQUIRED","preflight historical status must remain pre-audit")
    if args.main_root:
        target=h["target_main"]
        s=lock_json(args.main_root/target["main_state_path"],target["main_state_blob_sha1"],target["main_state_canonical_sha256"],"MAIN V41 state")
        r=lock_json(args.main_root/target["v41_audit_sync_receipt_path"],target["v41_audit_sync_receipt_blob_sha1"],target["v41_audit_sync_receipt_canonical_sha256"],"MAIN V41 audit sync")
        q=lock_json(args.main_root/target["existing_full_qA_preflight_path"],target["existing_full_qA_preflight_blob_sha1"],target["existing_full_qA_preflight_canonical_sha256"],"MAIN full-qA preflight")
        req(s["current_exact_frontier"]["authoritative_remaining_terminals"]==OLD,"MAIN bound")
        req(s["current_exact_frontier"]["authoritative_remaining_strata"]==17128,"MAIN strata")
        req(s["current_exact_frontier"]["v40_replacement_head_hostile_audited"] is True,"MAIN V40 audit sync")
        req(r["hostile_audit"]["status"]=="PASS","MAIN V41 audit receipt")
        req(q["structural_dominance"]["full_histogram_cell_objective_no_larger_than_hpadj20"] is True,"MAIN structural preflight")
        print("PASS: audited HPADJ21 handoff targets exact MAIN V41 authority")
    print("PASS: HPADJ21 producer hostile-audit PASS review 5242670540 source-bound into MAIN handoff")
    print("PASS: 179119009547804181594 -> 157570677819451133507 by non-additive same-population replacement candidate")
    print("PASS: EX5 grants zero MAIN credit; MAIN replacement requires its own hostile audit")

if __name__=="__main__": main()
