#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
EXPECTED="e876c51a45e8d534d134ea9deb13716327953522f89ac865d12ad7aec6bdbeb0"
NOTE_BLOB="2245de9920e4f685bf5ebc6784b43469302f2143"
LOCKS={
"v6":("stages/stage32/32-21/post1473-v6-witness-body-recovered.json","d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"),
"gap":("stages/stage32/32-21/post-21bl-effectivity-gap-separation.json","4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc"),
"node":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-relative-h-marked-node-action.json","d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"),
"mult":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-local-multiplicity-adapter.json","919f8bed23fc07a8bd39907c1d348f7e3b7535cee0dd64642aa600ab793f633b"),
"bound":("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-marked-multiplicity-only-boundary.json","29afae4e789522162374baeaca89c860a1c6dac21ce77059e7fe06988e43bfcf"),
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
    note=HERE/"post1490-o210-q4-bolza-marked-tangent-information-boundary-source-note.md"
    if blobsha(note)!=NOTE_BLOB: raise SystemExit("source note blob moved")
    w=data["v6"]["witness"]
    forbidden={"curve_equation","defining_equations","local_branch_parametrization","tangent_direction","tangent_cone","infinitely_near_cluster"}
    if forbidden.intersection(w): raise SystemExit("V6 witness unexpectedly acquired local-geometry fields; boundary must be re-audited")
    g=data["gap"]["exact_gap_result"]
    if any(g[k] for k in ("actual_effective_curve_certificate_present","integral_irreducible_curve_certificate_present","geometric_genus1_normalization_certificate_present")): raise SystemExit("effectivity gap changed; tangent boundary must be re-audited")
    if len(data["node"]["marked_node_action"]["nonidentity_permutations_images_of_93_to_140"])!=3: raise SystemExit("named deck-node action moved")
    if len(data["mult"]["exact_multiplicity_vector"]["values"])!=48: raise SystemExit("local multiplicity vector moved")
    b=data["bound"]
    if b["combined_marked_budget_lower_bound"]!=3350 or b["unforced_budget_after_marked_multiplicity_only"]!=5236: raise SystemExit("multiplicity-only boundary moved")
    cert,claimed=load_rel(str(a.check.relative_to(ROOT)) if a.check.is_absolute() else str(a.check))
    if claimed!=EXPECTED: raise SystemExit("tangent information-boundary canonical moved")
    inv=cert["retained_information_inventory"]
    if inv["tangent_direction_record_present"] or inv["branch_direction_pairing_present"] or inv["infinitely_near_multiplicity_cluster_present"]: raise SystemExit("certificate overstates retained local geometry")
    dec=cert["decision"]
    if dec["O210_excluded"] or dec["new_tangent_compute_from_picard64_authorized"]: raise SystemExit("information boundary overpromoted")
    print(json.dumps({"verdict":"PASS_EXACT_RETAINED_TANGENT_INFORMATION_BOUNDARY","canonical_sha256":claimed,"unforced_budget":5236,"O210_excluded":False,"next_exact_leaf":dec["next_exact_leaf"]},sort_keys=True))
if __name__=="__main__": main()
