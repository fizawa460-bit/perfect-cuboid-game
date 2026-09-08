#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
C1 = HERE / "e3-v91c1x-r5b3b3c1-offboundary-norm-factorization.json"
C2C = HERE / "e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
B2A = HERE / "e3-v91c1x-r5b3b3c4b2a-strict-prime-cross-carrier-geometric-incidence.json"
B2B1 = HERE / "e3-v91c1x-r5b3b3c4b2b1-explicit-a1-boundary-residue-field-squareclass.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2-remaining24-strict-prime-squareclass-partition.json"

C1_SHA = "5c092fcec6720d0097d6e7509ce37b1506d7a099015a1a6a004250513d0f29f3"
C2C_SHA = "01fc321272106a1ce7c382783c4dcb128c164d21ee4deedf4060137ef9ed971a"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
B2A_SHA = "ae207b31329f8248859dc96893243c4259e4d92d05beda1df8e65f2aac290d33"
B2B1_SHA = "bc13cb417addcfbd05616c9cff1f8ae73ba286071b2f6ebbda9144ec0eeb9de3"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
A1 = "44afff33ba591a11904229fe7936cb41caa700bd759cda0a5106218250561491"
F14 = "da9c1c762b7deb1ac7c630325bcfa1ee9b1a44916f5bd9df410bf16c9effd5b4"
F4 = "69623aeb5f2dab057c7c435c9f72d85b6670e7716c1a64d2a2b8ea3b9ec1be1b"
SPECIAL = ["LIN_008", "LIN_015", "LIN_020", "LIN_025"]
PAIR = ["LIN_013", "LIN_019"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256", None); actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def build_certificate():
    c1 = load_locked(C1, C1_SHA)
    c2c = load_locked(C2C, C2C_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    b2a = load_locked(B2A, B2A_SHA)
    b2b1 = load_locked(B2B1, B2B1_SHA)
    if b2b1["exact_consequence"]["remaining_C4B2B_strict_prime_squareclass_context_count"] != 24 or not b2b1["exact_consequence"]["all_four_are_nonsquare"]:
        raise SystemExit("B2B1 negative checkpoint moved")
    if b2a["strict_prime_tame_parity_after_incidence"]["total_targeted_strict_prime_residue_field_squareclass_rows_for_C4B2B"] != 28:
        raise SystemExit("B2A target count moved")

    rows = list(c4a["strict_prime_preflight"]["rows"])
    if len(rows) != 28:
        raise SystemExit("C4A strict row count moved")
    repeated = {g["c1_normalized_factor_sha256"]: g for g in b2a["cross_carrier_incidence"]["group_rows"]}
    if set(repeated) != {A1, F14, F4}:
        raise SystemExit("B2A repeated group identity set moved")

    boundary_keys = {(A1, cid) for cid in SPECIAL}
    remaining = [r for r in rows if (r["c1_normalized_factor_sha256"], r["carrier_id"]) not in boundary_keys]
    if len(remaining) != 24:
        raise SystemExit(f"remaining row count moved: {len(remaining)}")

    c1rows = {r["carrier_id"]: r for r in c1["exact_factorization"]["carrier_rows"]}
    degree_counter = Counter()
    def row_out(r, bucket):
        cid, fsha = r["carrier_id"], r["c1_normalized_factor_sha256"]
        ms = [f for f in c1rows[cid]["factors"] if f["normalized_factor_sha256"] == fsha]
        if len(ms) != 1: raise SystemExit(f"C1 factor lookup failed {cid}/{fsha}")
        f = ms[0]; degree = int(f["factor_total_degree"]); degree_counter[degree] += 1
        odd = list(r["combined_tame_residue_odd_linear_carrier_ids_under_single_carrier_valuation"])
        if not odd or r["combined_tame_residue_carrier_parity_zero_under_single_carrier_valuation"]:
            raise SystemExit(f"remaining row unexpectedly zero parity {cid}/{fsha}")
        return {"bucket": bucket, "carrier_id": cid, "c1_normalized_factor_sha256": fsha,
                "c1_factor_total_degree": degree, "c1_factor_multiplicity_in_full_sign_norm": int(f["multiplicity"]),
                "c4a_strict_prime_ids": list(r["strict_prime_ids"]),
                "combined_tame_residue_odd_linear_carrier_ids": odd,
                "odd_linear_carrier_count": len(odd), "residue_field_squareclass_status": "OPEN_TARGETED_REDUCTION_REQUIRED"}

    f14 = [r for r in remaining if r["c1_normalized_factor_sha256"] == F14]
    f4 = [r for r in remaining if r["c1_normalized_factor_sha256"] == F4]
    unique = [r for r in remaining if not r["c1_factor_repeated_across_carrier_contexts"]]
    if sorted(r["carrier_id"] for r in f14) != SPECIAL: raise SystemExit("F14 target set moved")
    if sorted(r["carrier_id"] for r in f4) != PAIR: raise SystemExit("F4 target set moved")
    if len(unique) != 18: raise SystemExit("unique target count moved")

    buckets = [
      {"bucket":"F14_RESIDUAL_REPEATED_FACTOR_STRICT_PRIMES","target_count":4,"base_factor_degree":14,"carrier_ids":SPECIAL,
       "rows":[row_out(r,"F14_RESIDUAL_REPEATED_FACTOR_STRICT_PRIMES") for r in sorted(f14,key=lambda x:x["carrier_id"])],
       "recommended_reducer":"use the C2C unique residual prime over irreducible F14; seek a norm/valuation witness before full quotient-field computation"},
      {"bucket":"F4_REPEATED_FACTOR_PAIR_STRICT_PRIMES","target_count":2,"base_factor_degree":4,"carrier_ids":PAIR,
       "rows":[row_out(r,"F4_REPEATED_FACTOR_PAIR_STRICT_PRIMES") for r in sorted(f4,key=lambda x:x["carrier_id"])],
       "recommended_reducer":"use explicit LIN_013/LIN_019 equations with the four surface quadrics to build a low-degree multiquadratic norm witness"},
      {"bucket":"UNIQUE_C1_FACTOR_STRICT_PRIMES","target_count":18,
       "rows":[row_out(r,"UNIQUE_C1_FACTOR_STRICT_PRIMES") for r in sorted(unique,key=lambda x:(x["carrier_id"],x["c1_normalized_factor_sha256"]))],
       "recommended_reducer":"retain each source-bound C4A strict-prime id and unique C1 contraction; use low-cost residue norm/odd-valuation witnesses first"}
    ]

    # C2C is used only where it literally exposes the four special representative rows.
    reps = {r["carrier_id"]: r for r in c2c["representative_strict_prime_decompositions"]["rows"]}
    for cid in SPECIAL:
        q = reps[cid]["special_reducible_norm_prime_decomposition_certificate"]["residual_prime"]
        if q["base_factor"] != "F14" or not q["unique_minimal_prime_above_factor"]:
            raise SystemExit(f"C2C F14 residual contract moved {cid}")
    # LIN_013/LIN_019 are not literal keys in this representative-only table; their F4
    # contexts are source-locked through C1 + C4A and geometrically separated in B2A.

    cert = {
      "schema":"stage33.e3.v91c1x_r5b3b3c4b2b2.remaining24_strict_prime_squareclass_partition.v2","stage":"33-12",
      "candidate":"V91C1X_R5B3B3C4B2B2_REMAINING_24_STRICT_PRIME_RESIDUE_FIELD_SQUARECLASS_PARTITION",
      "role":"EXACT_NONCREDIT_PARTITION_OF_THE_24_STRICT_PRIME_SQUARECLASS_DEBTS_REMAINING_AFTER_THE_FOUR_EXPLICIT_A1_BOUNDARY_NONSQUARE_CERTIFICATES",
      "entry":{"authority":AUTHORITY,"stage33_progress":"6/11","successor_pr":1722},
      "source_locks":{"r5b3b3c1_sha256":C1_SHA,"r5b3b3c2c_sha256":C2C_SHA,"c4a_sha256":C4A_SHA,"c4b2a_sha256":B2A_SHA,"c4b2b1_sha256":B2B1_SHA},
      "frozen_negative_checkpoint":{"already_audited_explicit_a1_boundary_prime_count":4,"already_audited_nonsquare_count":4,
        "current_literal_eight_symbol_candidate_already_known_ramified":True,"this_does_not_negate_stage33_endpoint_or_other_representatives":True},
      "remaining24_partition":{"target_count":24,"bucket_count":3,
        "bucket_sizes":{"F14_RESIDUAL_REPEATED_FACTOR_STRICT_PRIMES":4,"F4_REPEATED_FACTOR_PAIR_STRICT_PRIMES":2,"UNIQUE_C1_FACTOR_STRICT_PRIMES":18},
        "c1_factor_degree_distribution":{str(k):int(v) for k,v in sorted(degree_counter.items())},"rows_by_bucket":buckets,"all_24_remain_open_squareclass_debts":True},
      "exact_consequence":{"all_28_C4B2B_targets_accounted_for_as_4_audited_plus_24_partitioned":True,"remaining_strict_prime_squareclass_debt_count":24,
        "F4_pair_is_the_smallest_nontrivial_next_exact_residue_field_target":True,"offboundary_codimension_one_residue_cancellation_verified":False,"unramifiedness_verified":False},
      "next_exact_leaf":"V91C1X_R5B3B3C4B2B2A_F4_PAIR_MULTIQUEADRATIC_RESIDUE_NORM_WITNESS",
      "next_exact_step":"construct the two F4 strict-prime function fields from LIN_013/LIN_019 and test the combined odd-carrier residue by exact multiquadratic norm to Q(i)(x); nonsquare norm proves nonsquare residue, square norm is inconclusive",
      "credit_firewall":{"authority_promotion":False,"hostile_audit_credit":False,"h2_fixedness_credit":False,"marked_brauer_image_credit":False,
        "genuine_full_surface_h2_mu2_lift_credit":False,"offboundary_cancellation_credit":False,"unramifiedness_credit":False,"stage33_close_credit":False,
        "stage33_release_credit":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"merge_allowed":False}}
    cert["canonical_sha256"] = csha(cert); return cert


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); cert=build_certificate()
    text=json.dumps(cert,indent=2,sort_keys=True)+"\n"
    if args.write:
        OUT.write_text(text,encoding="utf-8"); p=cert["remaining24_partition"]
        print(json.dumps({"success":True,"marker":cert["candidate"],"target_count":24,"bucket_sizes":p["bucket_sizes"],
          "degree_distribution":p["c1_factor_degree_distribution"],"certificate_sha256":cert["canonical_sha256"],"next_exact_leaf":cert["next_exact_leaf"]},sort_keys=True)); return
    if not OUT.exists(): raise SystemExit(f"missing materialized certificate: {OUT}")
    if json.loads(OUT.read_text(encoding="utf-8")) != cert: raise SystemExit("materialized C4B2B2 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])

if __name__ == "__main__": main()
