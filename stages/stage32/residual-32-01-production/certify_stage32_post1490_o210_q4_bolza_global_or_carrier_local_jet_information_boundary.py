#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
EXPECTED="96e28e71b6b8236a62d221e3a5082d31a51ef8880851fa9c095123fe569cfed0"
NOTE_BLOB="72819bf6df1c6b2d3eacee051994d424acf5c43b"
LOCKS={
"gap":("stages/stage32/32-21/post-21bl-effectivity-gap-separation.json","4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc"),
"mult":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-marked-multiplicity-only-boundary.json","29afae4e789522162374baeaca89c860a1c6dac21ce77059e7fe06988e43bfcf"),
"tangent":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-marked-tangent-information-boundary.json","e876c51a45e8d534d134ea9deb13716327953522f89ac865d12ad7aec6bdbeb0"),
}

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load_rel(rel):
    p=ROOT/rel; x=json.loads(p.read_text()); claimed=x.pop("canonical_sha256_without_this_field")
    if csha(x)!=claimed: raise SystemExit(f"canonical mismatch: {rel}")
    return x,claimed
def blobsha(p):
    b=p.read_bytes(); return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",type=Path,required=True); a=ap.parse_args()
    data={}
    for k,(p,h) in LOCKS.items():
        x,ch=load_rel(p)
        if ch!=h: raise SystemExit(f"source lock moved: {k}")
        data[k]=x
    note=HERE/"post1490-o210-q4-bolza-global-or-carrier-local-jet-information-boundary-source-note.md"
    if blobsha(note)!=NOTE_BLOB: raise SystemExit("source note blob moved")
    g=data["gap"]["exact_gap_result"]
    for k in ("actual_effective_curve_certificate_present","integral_irreducible_curve_certificate_present","geometric_genus1_normalization_certificate_present"):
        if g[k]: raise SystemExit(f"effectivity gap changed: {k}")
    if not data["gap"]["strategy_selection"]["effectivity_gap"]=="OPEN_PRIMARY": raise SystemExit("effectivity gap no longer open")
    t=data["tangent"]
    if t["decision"]["O210_excluded"] or not t["decision"]["tangent_route_closed_from_existing_retained_data"]: raise SystemExit("tangent boundary moved")
    inv=t["retained_information_inventory"]
    if inv["tangent_direction_record_present"] or inv["branch_direction_pairing_present"] or inv["infinitely_near_multiplicity_cluster_present"] or inv["v6_has_actual_curve_equation"]: raise SystemExit("retained local-geometry inventory changed")
    b=data["mult"]
    if b["combined_marked_budget_lower_bound"]!=3350 or b["unforced_budget_after_marked_multiplicity_only"]!=5236: raise SystemExit("multiplicity-only budget moved")
    rel=str(a.check.relative_to(ROOT)) if a.check.is_absolute() else str(a.check)
    cert,claimed=load_rel(rel)
    if claimed!=EXPECTED: raise SystemExit("global/carrier information-boundary canonical moved")
    if cert["fixed_target"]!={"row_id":"g1-d186","d":186,"e":266,"genus":1,"O":210,"qprime":4}: raise SystemExit("fixed target moved")
    s=cert["bounded_existing_asset_search"]
    if s["independent_global_constraint_closing_remaining_defect_found"] or s["effective_carrier_with_local_equation_or_jet_found"]: raise SystemExit("boundary contradicts its search result")
    eb=cert["exact_boundary"]
    if eb["remaining_defect_budget"]!=5236 or eb["independent_global_constraint_found"] or eb["effective_carrier_equation_found"] or eb["carrier_local_jet_found"] or eb["new_tangent_or_infinitely_near_contribution_certifiable"]: raise SystemExit("exact boundary overpromoted")
    dec=cert["decision"]
    if dec["O210_excluded"] or not dec["information_boundary_locked_exactly"] or not dec["retained_source_search_for_this_leaf_exhausted"]: raise SystemExit("decision overpromoted or incomplete")
    fw=cert["firewalls"]
    if fw["full178_authorized"] or fw["receiver_credit"] or fw["route_credit"] or fw["theorem_credit"] or fw["endpoint_credit"] or fw["perfect_cuboid_claim"]: raise SystemExit("credit firewall violated")
    print(json.dumps({"verdict":"PASS_EXACT_GLOBAL_OR_CARRIER_LOCAL_JET_INFORMATION_BOUNDARY","canonical_sha256":claimed,"unforced_budget":5236,"O210_excluded":False,"next_exact_leaf":dec["next_exact_leaf"]},sort_keys=True))
if __name__=="__main__": main()
