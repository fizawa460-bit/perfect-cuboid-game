#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path
import sympy as sp

H = Path(__file__).resolve().parent
D11 = H.parent / "33-11d" / "stage33-11d-prime-refinement-certificate.json"
E11 = H.parent / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
E11V = H.parent / "33-11e" / "verify_stage33_11e_prime_galois_transport.py"
C3 = H / "e3-v91c1x-r5b3b3c3-c1-factor-to-strict-prime-and-exceptional-attachment.json"
C = H / "e3-v91c1x-r5b3b3c4b2b2c-unique-degree16-residue-norm-sweep.json"
OUT = H / "e3-v91c1x-r5b3b3c4b2b2c1-inherited-direct-support-primality-recheck.json"
LOCKS = {
    D11: "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d",
    E11: "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426",
    C3: "d65be2f66b16c14ac230746ca0e832a627da611ceb7533b4766e1b13df23ae71",
    C: "92fdf2bc96ff0f00c2200cef63a1270b96e6962a6022e0cd5fb2ed361ba8bb3a",
}
E11V_BLOB = "85fc05f4ba3513edab2ee740c77f387879878e0d"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
LIN024 = "437ad2bc8c4c25e8a2078e663cbca3d5523efbdec3e06be6f2c1b8555c6c58f7"
LIN024_IDS = {
    "a1 + i*a3": "537ee4d04a103c9082958b087b663f1a1fa319ecd2c0ad7fbfface8a5cbe6767",
    "a1 - i*a3": "914b682af4aa0f52d029122538b95c9961e86eb738c567495947efbe21166c11",
}

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def load(p):
    o = json.loads(p.read_text(encoding="utf-8")); b = dict(o); claimed = b.pop("canonical_sha256", None)
    if claimed != LOCKS[p] or csha(b) != LOCKS[p]:
        raise SystemExit(f"canonical lock moved: {p.name}")
    return o

def blobsha(p):
    d = p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode() + d).hexdigest()

def ps(e):
    return str(sp.expand(e)).replace("**", "^").replace("I", "i")

def zdiv(gens, left, right, vv):
    G = sp.groebner(gens, *vv, order="grevlex", extension=sp.I)
    l = sp.expand(G.reduce(sp.expand(left))[1]); r = sp.expand(G.reduce(sp.expand(right))[1]); p = sp.expand(G.reduce(sp.expand(left*right))[1])
    if l == 0 or r == 0 or p != 0:
        raise SystemExit(f"zero-divisor witness failed: {l=} {r=} {p=}")
    return {"left": ps(left), "right": ps(right), "left_nonzero": True, "right_nonzero": True,
            "product_zero": True, "left_remainder": ps(l), "right_remainder": ps(r)}

def build():
    d11, e11, c3, c = (load(D11), load(E11), load(C3), load(C))
    if blobsha(E11V) != E11V_BLOB: raise SystemExit("33-11e verifier blob moved")
    if e11["prime_inventory"]["distinct_prime_ids"] != 44: raise SystemExit("33-11e prime inventory count moved")
    if c["degree16_sweep"]["nonsquare_by_norm_count"] != 16 or c["degree16_sweep"]["inconclusive_count"] != 0:
        raise SystemExit("degree16 sweep gate moved")

    direct = d11["inherited_direct_refinements"]; recs = direct["records"]
    if direct["carrier_count"] != 6 or len(recs) != 6: raise SystemExit("direct carrier count moved")
    a1,a2,a3,b1,b2,b3,cv = vv = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    loc = {str(v):v for v in vv} | {"i":sp.I}
    Q = [a1**2+a2**2-b3**2, a2**2+a3**2-b1**2, a1**2+a3**2-b2**2, a1**2+a2**2+a3**2-cv**2]
    axis = {"AXIS_B1_ZERO":(b1,a1), "AXIS_B2_ZERO":(b2,a2), "AXIS_B3_ZERO":(b3,a3)}
    diff = {
      "DIFF_C_MINUS_B1":(cv-b1,a1,[(b2-a3,b2+a3),(b3-a2,b3+a2)]),
      "DIFF_C_MINUS_B2":(cv-b2,a2,[(b1-a3,b1+a3),(b3-a1,b3+a1)]),
      "DIFF_C_MINUS_B3":(cv-b3,a3,[(b1-a2,b1+a2),(b2-a1,b2+a1)]),
    }
    rows=[]; n=0; lin=None
    for r in sorted(recs, key=lambda x:x["carrier_id"]):
        s=r["refinement_scout"]; t=s["type"]
        if t in axis:
            carrier, rem = axis[t]; ws=[]
            if len(s["reduced_linear_branches_over_Qi"]) != 2: raise SystemExit(f"axis branches moved: {t}")
            for text in s["reduced_linear_branches_over_Qi"]:
                sup=sp.expand(sp.sympify(text.replace("^","**"), locals=loc)); w=zdiv(Q+[carrier,sup],cv-rem,cv+rem,vv); w["recorded_support"]=text; ws.append(w)
            row={"carrier_id":r["carrier_id"],"direct_type":t,"recorded_support_count":2,
                 "all_recorded_support_quotients_non_domains":True,"support_zero_divisor_witnesses":ws,
                 "minimum_additional_component_split_per_recorded_support":2}; n+=2
        elif t in diff:
            carrier, red, pairs=diff[t]; parsed=sp.expand(sp.sympify(s["reduced_support"].replace("=0", ""),locals=loc))
            if sp.expand(parsed-red)!=0: raise SystemExit(f"reduced support moved: {t}")
            ws=[zdiv(Q+[carrier,red],x,y,vv) for x,y in pairs]
            row={"carrier_id":r["carrier_id"],"direct_type":t,"recorded_support_count":1,
                 "recorded_scheme_multiplicity_signal":int(s["scheme_multiplicity_signal"]),
                 "recorded_support_quotient_is_non_domain":True,"independent_square_difference_witnesses":ws,
                 "four_component_candidate_grid_exposed":True}; n+=1
        else: raise SystemExit(f"unexpected direct type: {t}")
        rows.append(row)
        if r["carrier_id"]==LIN024: lin=row
    if n!=9 or lin is None or lin["direct_type"]!="AXIS_B2_ZERO": raise SystemExit("nine-support/LIN024 binding moved")

    c3rows=[r for r in c3["c1_factor_to_strict_prime_adapter"]["rows"] if r["carrier_id"]=="LIN_024"]
    if len(c3rows)!=2 or any(r["prime_identifier_kind"]!="AUDITED_33_11D_DIRECT_PRIME_SUPPORT" for r in c3rows):
        raise SystemExit("C3 LIN024 record-kind contract moved")
    m={r["direct_support_Qi"]:r["strict_prime_ids"][0] for r in c3rows}
    if m!=LIN024_IDS: raise SystemExit(f"C3 LIN024 id binding moved: {m}")

    cert={
      "schema":"stage33.e3.v91c1x_r5b3b3c4b2b2c1.inherited_direct_support_primality_recheck.v1","stage":"33-12",
      "candidate":"V91C1X_R5B3B3C4B2B2C1_INHERITED_DIRECT_SUPPORT_PRIMALITY_RECHECK",
      "role":"EXACT_NONCREDIT_RECHECK_PROVING_THE_NINE_INHERITED_33_11D_DIRECT_SUPPORT_LABELS_USED_AS_PRIME_IDS_HAVE_NONDOMAIN_SUPPORT_QUOTIENTS_AND_REQUIRE_ACTUAL_COMPONENT_REFINEMENT_BEFORE_RESIDUE_FIELD_ARITHMETIC",
      "entry":{"authority":AUTH,"stage33_progress":"6/11","successor_pr":1722},
      "source_locks":{"stage33_11d_sha256":LOCKS[D11],"stage33_11e_sha256":LOCKS[E11],"stage33_11e_verifier_blob_sha1":E11V_BLOB,"c3_sha256":LOCKS[C3],"c4b2b2c_sha256":LOCKS[C]},
      "surface_model":{"base_field":"Q(i)","equations":[ps(q) for q in Q],"proof_method":"exact Groebner remainders exhibit nonzero zero-divisor factors on every recorded direct support quotient"},
      "inherited_direct_recheck":{"direct_carrier_count":6,"recorded_support_pseudo_prime_count":9,"all_nine_recorded_support_quotients_non_domains":True,"rows":rows},
      "lin024_exact_boundary":{"projective_linear_form_Qi_sha256":LIN024,"recorded_base_support_to_c3_id":LIN024_IDS,"recorded_base_support_count":2,
        "each_recorded_base_support_splits_further_by":"c-a2 and c+a2","the_two_C3_ids_are_not_prime_exact_residue_field_targets":True,
        "c4b2b2c_remaining_strict_prime_squareclass_debt_count_2_is_not_prime_exact":True,
        "replacement_debt_type":"REFINE_LIN024_TO_ACTUAL_HEIGHT_ONE_COMPONENT_PRIMES_THEN_RECOMPUTE_COMPONENTWISE_TAME_RESIDUE_SQUARECLASSES"},
      "upstream_scope":{"stage33_11e_recorded_distinct_support_or_prime_ids":44,"stage33_11e_prime_level_transport_requires_replay_after_direct_support_refinement":True,
        "this_leaf_does_not_assert_replayed_prime_level_galois_difference_is_nonzero":True,"current_V91C1V_authority_is_not_demoted_by_this_noncredit_diagnostic":True,
        "f4_f14_and_c2c_degree16_nonsquare_certificates_are_not_refuted":True},
      "exact_consequence":{"degree16_unique_targets_nonsquare_count_retained":16,"f4_pair_and_f14_four_repeated_factor_nonsquare_results_retained":True,
        "lin024_two_recorded_supports_may_not_be_treated_as_two_actual_strict_primes":True,"offboundary_strict_prime_inventory_requires_direct_support_refinement_repair":True,
        "offboundary_codimension_one_residue_cancellation_verified":False,"unramifiedness_verified":False},
      "next_exact_leaf":"V91C1X_R5B3B3C4B2B2C2_LIN024_EXACT_FOUR_COMPONENT_PRIME_REFINEMENT_AND_COMPONENTWISE_RESIDUE_SQUARECLASS",
      "credit_firewall":{"authority_promotion":False,"authority_demotion_claim":False,"hostile_audit_credit":False,"marked_brauer_image_credit":False,
        "offboundary_cancellation_credit":False,"unramifiedness_credit":False,"stage33_close_credit":False,"stage33_release_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"merge_allowed":False}}
    cert["canonical_sha256"]=csha(cert); return cert

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); cert=build(); text=json.dumps(cert,indent=2,sort_keys=True)+"\n"
    if args.write:
        OUT.write_text(text,encoding="utf-8"); print(json.dumps({"success":True,"marker":cert["candidate"],"nonprime_support_count":9,"lin024_support_count":2,"certificate_sha256":cert["canonical_sha256"],"next_exact_leaf":cert["next_exact_leaf"]},sort_keys=True)); return
    if not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8"))!=cert: raise SystemExit("materialized C4B2B2C1 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])

if __name__=="__main__": main()
