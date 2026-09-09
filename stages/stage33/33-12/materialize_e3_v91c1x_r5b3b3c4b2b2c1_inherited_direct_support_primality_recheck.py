#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
D11 = HERE.parent / "33-11d" / "stage33-11d-prime-refinement-certificate.json"
E11 = HERE.parent / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
E11_VERIFY = HERE.parent / "33-11e" / "verify_stage33_11e_prime_galois_transport.py"
C3 = HERE / "e3-v91c1x-r5b3b3c3-c1-factor-to-strict-prime-and-exceptional-attachment.json"
C4B2B2C = HERE / "e3-v91c1x-r5b3b3c4b2b2c-unique-degree16-residue-norm-sweep.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2c1-inherited-direct-support-primality-recheck.json"

D11_SHA = "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d"
E11_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
E11_VERIFY_BLOB_SHA1 = "85fc05f4ba3513edab2ee740c77f387879878e0d"
C3_SHA = "d65be2f66b16c14ac230746ca0e832a627da611ceb7533b4766e1b13df23ae71"
C4B2B2C_SHA = "92fdf2bc96ff0f00c2200cef63a1270b96e6962a6022e0cd5fb2ed361ba8bb3a"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
LIN024_PROJECTIVE_SHA = "437ad2bc8c4c25e8a2078e663cbca3d5523efbdec3e06be6f2c1b8555c6c58f7"
LIN024_SUPPORT_TO_C3_ID = {
    "a1 + i*a3": "537ee4d04a103c9082958b087b663f1a1fa319ecd2c0ad7fbfface8a5cbe6767",
    "a1 - i*a3": "914b682af4aa0f52d029122538b95c9961e86eb738c567495947efbe21166c11",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def git_blob_sha1(path: Path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def pstr(expr):
    return str(sp.expand(expr)).replace("**", "^").replace("I", "i")


def nonprime_zero_divisor_witness(gens, left, right, variables):
    gb = sp.groebner(gens, *variables, order="grevlex", extension=sp.I)
    rl = sp.expand(gb.reduce(sp.expand(left))[1])
    rr = sp.expand(gb.reduce(sp.expand(right))[1])
    rp = sp.expand(gb.reduce(sp.expand(left * right))[1])
    if rl == 0 or rr == 0 or rp != 0:
        raise SystemExit(f"zero-divisor witness failed: left={rl} right={rr} product={rp}")
    return {
        "left_factor": pstr(left),
        "right_factor": pstr(right),
        "left_nonzero_mod_support_ideal": True,
        "right_nonzero_mod_support_ideal": True,
        "product_zero_mod_support_ideal": True,
        "left_remainder": pstr(rl),
        "right_remainder": pstr(rr),
    }


def parse_support(text, local):
    return sp.expand(sp.sympify(text.replace("^", "**"), locals=local))


def build():
    d11 = load(D11, D11_SHA)
    e11 = load(E11, E11_SHA)
    c3 = load(C3, C3_SHA)
    c = load(C4B2B2C, C4B2B2C_SHA)
    if git_blob_sha1(E11_VERIFY) != E11_VERIFY_BLOB_SHA1:
        raise SystemExit("33-11e verifier blob moved")
    if c["degree16_sweep"]["nonsquare_by_norm_count"] != 16 or c["degree16_sweep"]["inconclusive_count"] != 0:
        raise SystemExit("C4B2B2C degree16 gate moved")
    if c["next_exact_leaf"] != "V91C1X_R5B3B3C4B2B2C1_LIN024_TWO_DEGREE1_STRICT_PRIME_SQUARECLASS_TEST":
        raise SystemExit("C4B2B2C next-leaf gate moved")

    direct = d11["inherited_direct_refinements"]
    records = list(direct["records"])
    if int(direct["carrier_count"]) != 6 or len(records) != 6:
        raise SystemExit("33-11d inherited direct-carrier count moved")
    axis = [r for r in records if r["refinement_scout"]["type"].startswith("AXIS_")]
    diff = [r for r in records if r["refinement_scout"]["type"].startswith("DIFF_C_MINUS_")]
    if len(axis) != 3 or len(diff) != 3:
        raise SystemExit("33-11d inherited direct type partition moved")

    a1, a2, a3, b1, b2, b3, cv = variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    local = {str(v): v for v in variables} | {"i": sp.I}
    Q = [
        a1**2 + a2**2 - b3**2,
        a2**2 + a3**2 - b1**2,
        a1**2 + a3**2 - b2**2,
        a1**2 + a2**2 + a3**2 - cv**2,
    ]
    axis_data = {
        "AXIS_B1_ZERO": (b1, a1),
        "AXIS_B2_ZERO": (b2, a2),
        "AXIS_B3_ZERO": (b3, a3),
    }
    diff_data = {
        "DIFF_C_MINUS_B1": (cv - b1, a1, [(b2-a3, b2+a3), (b3-a2, b3+a2)]),
        "DIFF_C_MINUS_B2": (cv - b2, a2, [(b1-a3, b1+a3), (b3-a1, b3+a1)]),
        "DIFF_C_MINUS_B3": (cv - b3, a3, [(b1-a2, b1+a2), (b2-a1, b2+a1)]),
    }

    rows = []
    pseudo_support_count = 0
    lin024 = None
    for r in sorted(records, key=lambda x: x["carrier_id"]):
        scout = r["refinement_scout"]
        typ = scout["type"]
        if typ in axis_data:
            carrier, remaining_a = axis_data[typ]
            branches = list(scout["reduced_linear_branches_over_Qi"])
            if len(branches) != 2:
                raise SystemExit(f"axis branch count moved: {typ}")
            witnesses = []
            for text in branches:
                support = parse_support(text, local)
                w = nonprime_zero_divisor_witness(Q + [carrier, support], cv - remaining_a, cv + remaining_a, variables)
                w["recorded_support"] = text
                w["second_split_forced_by_surface"] = f"c^2-{remaining_a}^2=0"
                witnesses.append(w)
            pseudo_support_count += 2
            row = {
                "carrier_id": r["carrier_id"],
                "direct_type": typ,
                "recorded_support_count": 2,
                "all_recorded_support_quotients_are_non_domains": True,
                "support_zero_divisor_witnesses": witnesses,
                "minimum_additional_component_split_per_recorded_support": 2,
                "exact_four_component_refinement_certified_in_this_leaf": False,
            }
        elif typ in diff_data:
            carrier, reduced, pairs = diff_data[typ]
            recorded = parse_support(scout["reduced_support"].replace("=0", ""), local)
            if sp.expand(recorded - reduced) != 0:
                raise SystemExit(f"diff reduced support moved: {typ}")
            witnesses = [nonprime_zero_divisor_witness(Q + [carrier, reduced], l, rr, variables) for l, rr in pairs]
            pseudo_support_count += 1
            row = {
                "carrier_id": r["carrier_id"],
                "direct_type": typ,
                "recorded_support_count": 1,
                "recorded_scheme_multiplicity_signal": int(scout["scheme_multiplicity_signal"]),
                "recorded_support_quotient_is_non_domain": True,
                "independent_surface_square_difference_witnesses": witnesses,
                "four_component_candidate_grid_exposed": True,
                "exact_four_component_refinement_and_scheme_multiplicities_certified_in_this_leaf": False,
            }
        else:
            raise SystemExit(f"unexpected direct type: {typ}")
        rows.append(row)
        if r["carrier_id"] == LIN024_PROJECTIVE_SHA:
            lin024 = row

    if pseudo_support_count != 9:
        raise SystemExit(f"expected 9 inherited direct support pseudo-prime records, got {pseudo_support_count}")
    if lin024 is None or lin024["direct_type"] != "AXIS_B2_ZERO":
        raise SystemExit("LIN024/AXIS_B2 direct record binding moved")

    c3_lin = [r for r in c3["c1_factor_to_strict_prime_adapter"]["rows"] if r["carrier_id"] == "LIN_024"]
    if len(c3_lin) != 2:
        raise SystemExit("C3 LIN024 adapter row count moved")
    c3_map = {r["direct_support_Qi"]: r["strict_prime_ids"][0] for r in c3_lin}
    if c3_map != LIN024_SUPPORT_TO_C3_ID:
        raise SystemExit(f"C3 LIN024 direct-support id binding moved: {c3_map}")
    if any(r["prime_identifier_kind"] != "AUDITED_33_11D_DIRECT_PRIME_SUPPORT" for r in c3_lin):
        raise SystemExit("C3 LIN024 record kind moved")

    # The audited 33-11e certificate is source-locked, but the implementation path for
    # inherited direct carriers hashes a carrier/support label into prime_id without an
    # exact ideal/domain check.  The zero-divisor witnesses above show why this label must
    # not be consumed as an actual height-one prime ideal for residue-field arithmetic.
    if e11["summary"]["actual_distinct_prime_count"] != 44:
        raise SystemExit("33-11e recorded prime count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2b2c1.inherited_direct_support_primality_recheck.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2C1_INHERITED_DIRECT_SUPPORT_PRIMALITY_RECHECK",
        "role": "EXACT_NONCREDIT_PRIMALITY_RECHECK_SHOWING_THAT_THE_NINE_33_11D_INHERITED_DIRECT_SUPPORT_LABELS_CONSUMED_AS_PRIME_IDS_ARE_REDUCIBLE_SUPPORTS_ON_THE_FROZEN_SURFACE_AND_MUST_BE_REFINED_BEFORE_RESIDUE_FIELD_ARITHMETIC",
        "entry": {"authority": AUTHORITY, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "stage33_11d_prime_refinement_certificate_sha256": D11_SHA,
            "stage33_11e_prime_transport_certificate_sha256": E11_SHA,
            "stage33_11e_verifier_blob_sha1": E11_VERIFY_BLOB_SHA1,
            "r5b3b3c3_sha256": C3_SHA,
            "c4b2b2c_sha256": C4B2B2C_SHA,
        },
        "surface_model": {
            "base_field": "Q(i)",
            "equations": [pstr(q) for q in Q],
            "proof_method": "exact Groebner remainder: both displayed factors are nonzero modulo the recorded carrier/support ideal while their product is zero",
        },
        "inherited_direct_recheck": {
            "direct_carrier_count": 6,
            "recorded_support_pseudo_prime_count": 9,
            "axis_carrier_count": 3,
            "c_minus_b_carrier_count": 3,
            "all_nine_recorded_support_quotients_non_domains": True,
            "rows": rows,
        },
        "lin024_exact_boundary": {
            "projective_linear_form_Qi_sha256": LIN024_PROJECTIVE_SHA,
            "recorded_base_support_to_c3_id": LIN024_SUPPORT_TO_C3_ID,
            "recorded_base_support_count": 2,
            "each_recorded_base_support_splits_further_by": "c-a2 and c+a2",
            "the_two_C3_ids_are_not_prime_exact_residue_field_targets": True,
            "c4b2b2c_remaining_strict_prime_squareclass_debt_count_2_is_not_prime_exact": True,
            "replacement_debt_type": "REFINE_THE_TWO_LIN024_BASE_SUPPORT_RECORDS_TO_ACTUAL_HEIGHT_ONE_COMPONENT_PRIMES_THEN_RECOMPUTE_COMPONENTWISE_TAME_RESIDUE_SQUARECLASSES",
        },
        "upstream_scope": {
            "stage33_11e_recorded_actual_distinct_prime_count": 44,
            "stage33_11e_prime_level_transport_requires_replay_after_direct_support_refinement": True,
            "this_leaf_does_not_assert_the_replayed_prime_level_galois_difference_is_nonzero": True,
            "current_V91C1V_authority_is_not_demoted_by_this_noncredit_diagnostic": True,
            "f4_f14_and_c2c_degree16_nonsquare_certificates_are_not_refuted_by_this_direct_support_issue": True,
        },
        "exact_consequence": {
            "degree16_unique_targets_nonsquare_count_retained": 16,
            "f4_pair_and_f14_four_repeated_factor_nonsquare_results_retained": True,
            "lin024_two_recorded_supports_may_not_be_treated_as_two_actual_strict_primes": True,
            "offboundary_strict_prime_inventory_requires_direct_support_refinement_repair": True,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": "V91C1X_R5B3B3C4B2B2C2_LIN024_EXACT_FOUR_COMPONENT_PRIME_REFINEMENT_AND_COMPONENTWISE_RESIDUE_SQUARECLASS",
        "credit_firewall": {
            "authority_promotion": False,
            "authority_demotion_claim": False,
            "hostile_audit_credit": False,
            "marked_brauer_image_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "direct_support_pseudo_prime_count": 9,
            "all_nine_nonprime": True,
            "lin024_recorded_support_count": 2,
            "next_exact_leaf": cert["next_exact_leaf"],
            "certificate_sha256": cert["canonical_sha256"],
        }, sort_keys=True))
        return
    if not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2C1 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
