#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED_PICARD_CANONICAL = "ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038"
EXPECTED_RR_CANONICAL = "6e02dfa2f29ebdd218aa869e1994776abc6bd068be9f138e1dd1980789e2483b"
EXPECTED_GAP_CANONICAL = "4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc"
EXPECTED_GENUS_CANONICAL = "e59e23b2aefb1a3b622f3f3ed4eb0f83fd7bb335125fa3254c7e4e737caaa96c"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    data = json.loads(path.read_text())
    claimed = data.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(data) != claimed:
        raise ValueError(f"canonical regression: {path}")
    data["canonical_sha256_without_this_field"] = claimed
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--picard", type=Path, required=True)
    ap.add_argument("--rr", type=Path, required=True)
    ap.add_argument("--gap", type=Path, required=True)
    ap.add_argument("--genus", type=Path, required=True)
    ap.add_argument("--source-lock", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    picard = load_canonical(args.picard, EXPECTED_PICARD_CANONICAL)
    rr = load_canonical(args.rr, EXPECTED_RR_CANONICAL)
    gap = load_canonical(args.gap, EXPECTED_GAP_CANONICAL)
    genus = load_canonical(args.genus, EXPECTED_GENUS_CANONICAL)
    source = args.source_lock.read_text()

    required_source_strings = [
        "K^2=16",
        "p_g=7",
        "q=0",
        "canonical divisor big and nef",
        "SOURCE_AUDIT=PASS",
    ]
    missing = [s for s in required_source_strings if s not in source]
    if missing:
        raise ValueError(f"Testa-Stoll source-lock regression: {missing}")

    if picard.get("status") != "PASS_POST21BL_EXACT_PICARD64_SLICE_WITNESS":
        raise ValueError("Picard64 source status regression")
    degree = int(picard["target"]["degree"])
    square = int(picard["quadratic"]["picard_self_square"])
    if (degree, square) != (186, 858):
        raise ValueError(f"representative invariant regression: {(degree, square)}")
    if not picard["all140"]["all_pairings_integral"] or not picard["all140"]["all_pairings_nonnegative"]:
        raise ValueError("all140 pairing regression")

    K2, pg, q = 16, 7, 0
    chi_O = 1 - q + pg
    chi_C = chi_O + (square - degree) // 2
    if (square - degree) % 2:
        raise ValueError("Riemann-Roch parity regression")
    K_K_minus_C = K2 - degree
    if K_K_minus_C >= 0:
        raise ValueError("K.(K-C) must be negative")

    # K is nef by the audited source lock. Hence a nonzero effective divisor D
    # must satisfy K.D >= 0. Since K.(K-C)=-170, K-C is not effective.
    # Serre duality gives h^2(O(C))=h^0(O(K-C))=0.
    h2 = 0
    h0_lower = chi_C

    exact = rr["exact_riemann_roch"]
    expected_rr = {
        "chi_O_C": chi_C,
        "K_dot_K_minus_C": K_K_minus_C,
        "h2_O_C": h2,
        "h0_lower_bound": h0_lower,
        "effective_divisor_exists_in_class_C": True,
    }
    for key, value in expected_rr.items():
        if exact.get(key) != value:
            raise ValueError(f"RR evidence mismatch {key}: {exact.get(key)} != {value}")

    if genus["exact_numerical_data"]["arithmetic_genus"] != (square + degree) // 2 + 1:
        raise ValueError("adjunction arithmetic genus regression")
    if genus["exact_numerical_data"]["required_total_normalization_genus_defect"] != 522:
        raise ValueError("genus-defect regression")
    if gap["exact_gap_result"]["r29_lg2_eff_receiver_closed"]:
        raise ValueError("gap file illegally closes R29-LG2-EFF")

    audit = {
        "schema": "STAGE32_POST21BL_DIVISOR_EFFECTIVITY_FRESH_AUDIT_V1",
        "stage": 32,
        "verdict": "PASS_STAGE32_POST21BL_FRESH_RIEMANN_ROCH_DIVISOR_EFFECTIVITY_AUDIT",
        "source_canonicals": {
            "picard64": EXPECTED_PICARD_CANONICAL,
            "rr": EXPECTED_RR_CANONICAL,
            "gap": EXPECTED_GAP_CANONICAL,
            "genus": EXPECTED_GENUS_CANONICAL,
        },
        "independent_recomputation": {
            "K_square": K2,
            "p_g": pg,
            "q": q,
            "chi_O": chi_O,
            "K_dot_C": degree,
            "C_square": square,
            "chi_O_C": chi_C,
            "K_dot_K_minus_C": K_K_minus_C,
            "h2_O_C": h2,
            "h0_lower_bound": h0_lower,
            "effective_divisor_exists": True,
            "arithmetic_genus": 523,
            "required_normalization_genus_defect_for_g1": 522,
        },
        "firewalls": {
            "effective_divisor_is_not_integral_irreducible_curve": True,
            "effective_divisor_is_not_normalization_genus1": True,
            "r29_lg2_eff_receiver_closed": False,
            "full178_numerical_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    audit["canonical_sha256_without_this_field"] = csha(audit)
    args.output.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": audit["verdict"],
        "canonical": audit["canonical_sha256_without_this_field"],
        "h0_lower_bound": h0_lower,
        "carrier_receiver_closed": False,
    }))


if __name__ == "__main__":
    main()
