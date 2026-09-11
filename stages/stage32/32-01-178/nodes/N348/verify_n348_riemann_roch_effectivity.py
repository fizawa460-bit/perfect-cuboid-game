#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

N342_RESULT = ROOT / "stages/stage32/32-01-178/nodes/N342/RESULT.json"
N342_V2 = ROOT / "stages/stage32/32-01-178/nodes/N342/verify_n342_n341_sat_to_59d_node_support_v2.py"
N347_RESULT = ROOT / "stages/stage32/32-01-178/nodes/N347/RESULT.json"
SOURCE_LOCK = ROOT / "stages/stage29/29-02a/source-lock.md"
HIST_PICARD = ROOT / "stages/stage32/32-21/post-21bl-picard64-witness-adapter.json"
HIST_RR = ROOT / "stages/stage32/32-21/post-21bl-riemann-roch-divisor-effectivity.json"
HIST_AUDIT = ROOT / "stages/stage32/residual-32-01-production/audit_stage32_post21bl_divisor_effectivity.py"

EXPECTED_N342_CANONICAL = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
EXPECTED_N347_CANONICAL = "ccafa29bdbc2f9463fe3a0ef16eb328319214574440074365f35d2a1761b6f80"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_HIST_PICARD_CANONICAL = "ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038"
EXPECTED_HIST_RR_CANONICAL = "6e02dfa2f29ebdd218aa869e1994776abc6bd068be9f138e1dd1980789e2483b"
EXPECTED_N345_CANONICAL = "0b5eb496404395574f85e0f5cbf47101691566ea6e153b43e75a71fbecbb672d"
EXPECTED_N347_RUN_CANONICAL = "e297436081dcac730d5cacb8edba166ea3ba53f5937d8cdbb9eb3c5de172578c"

# These are exact SAT witnesses already observed in the source-locked N345/N347
# Actions runs.  N348 does not solve for a new Picard class; it only applies the
# audited surface Riemann--Roch calculation to the already exact classes.
ROWS = [
    # N345 exact kernel14 QF_NIA SAT rows.
    ("N345", "g0-d176", 0, 176, 11, 900, "ff854a2d"),
    ("N345", "g0-d176", 0, 176, 19, 1044, "917581bc"),
    ("N345", "g0-d176", 0, 176, 23, 776, "3472cea7"),
    ("N345", "g0-d176", 0, 176, 31, 440, "26fe9bb1"),
    ("N345", "g0-d176", 0, 176, 35, 996, "0251f254"),
    ("N345", "g1-d192", 1, 192, 23, 1072, "f6c3b93e"),
    ("N345", "g1-d192", 1, 192, 39, 892, "a62c0d37"),
    ("N345", "g1-d192", 1, 192, 43, 1364, "1d8ec666"),
    # N347 deterministic center-nearest QF_LIA + exact replay SAT rows.
    ("N347", "g0-d176", 0, 176, 3, 1064, "853d79a7"),
    ("N347", "g0-d176", 0, 176, 7, 1372, "3f1a4f04"),
    ("N347", "g0-d176", 0, 176, 15, 828, "31ce8773"),
    ("N347", "g0-d176", 0, 176, 27, 1520, "1cc7dd7a"),
    ("N347", "g0-d176", 0, 176, 39, 876, "f356dadb"),
    ("N347", "g1-d192", 1, 192, 3, 1324, "9fed234f"),
    ("N347", "g1-d192", 1, 192, 7, 1604, "0d13a9d7"),
    ("N347", "g1-d192", 1, 192, 11, 1284, "6495eb6c"),
    ("N347", "g1-d192", 1, 192, 15, 1640, "9a70a98f"),
    ("N347", "g1-d192", 1, 192, 19, 1824, "1ecf81bc"),
    ("N347", "g1-d192", 1, 192, 27, 1072, "cbcfa8bd"),
    ("N347", "g1-d192", 1, 192, 31, 1824, "c5d4c660"),
    ("N347", "g1-d192", 1, 192, 35, 1468, "059ae9db"),
]


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
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    n342 = load_canonical(N342_RESULT, EXPECTED_N342_CANONICAL)
    n347 = load_canonical(N347_RESULT, EXPECTED_N347_CANONICAL)
    hist_picard = load_canonical(HIST_PICARD, EXPECTED_HIST_PICARD_CANONICAL)
    hist_rr = load_canonical(HIST_RR, EXPECTED_HIST_RR_CANONICAL)

    if n342["aggregate"]["sat_terminal_count"] != 21:
        raise ValueError("N342 terminal-count regression")
    if n347["aggregate"]["combined_exact_sat_threshold_count"] != 21:
        raise ValueError("N347 exact SAT threshold-count regression")
    if n347["aggregate"]["combined_unresolved_count"] != 0:
        raise ValueError("N347 unresolved-count regression")
    locks = n347["source_locks"]
    if locks["n345_canonical_sha256"] != EXPECTED_N345_CANONICAL:
        raise ValueError("N345 canonical regression")
    if locks["n347_canonical_sha256"] != EXPECTED_N347_RUN_CANONICAL:
        raise ValueError("N347 run canonical regression")

    # Lock the current 21-terminal adapter to the same retained Picard64 bundle
    # used by the historical Stage32 Riemann--Roch effectivity audit.
    n342_text = N342_V2.read_text()
    if f'EXPECTED_BUNDLE_CANONICAL = "{EXPECTED_BUNDLE_CANONICAL}"' not in n342_text:
        raise ValueError("current N342 retained-bundle lock drift")
    if hist_picard["source"]["retained_bundle_sha256"] != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("historical Picard retained-bundle lock drift")
    expected_targets = [
        '("g0-d176", 0, 176, 48, 3104, [3,7,11,15,19,23,27,31,35,39])',
        '("g1-d192", 1, 192, 48, 3408, [3,7,11,15,19,23,27,31,35,39,43])',
    ]
    for target in expected_targets:
        if target not in n342_text:
            raise ValueError(f"current canonical-degree target drift: {target}")

    source = SOURCE_LOCK.read_text()
    for required in ["SOURCE_AUDIT=PASS", "K^2=16", "p_g=7", "q=0", "canonical divisor big and nef"]:
        if required not in source:
            raise ValueError(f"surface source-lock regression: {required}")

    if hist_rr["source_locks"]["surface_invariants"] != {
        "K_big": True,
        "K_nef": True,
        "K_square": 16,
        "chi_O": 8,
        "p_g": 7,
        "q": 0,
    }:
        raise ValueError("historical RR surface-invariant lock drift")

    # The merged historical fresh audit explicitly identifies Stage32 target
    # degree with K.C.  Require that exact semantic bridge to remain present.
    hist_audit_text = HIST_AUDIT.read_text()
    for required in [
        'degree = int(picard["target"]["degree"])',
        '"K_dot_C": degree',
        'K_K_minus_C = K2 - degree',
    ]:
        if required not in hist_audit_text:
            raise ValueError(f"historical K.C adapter regression: {required}")

    K2, pg, q = 16, 7, 0
    chi_O = 1 - q + pg
    out_rows = []
    for source_node, row_id, genus, degree, x4, square, witness_prefix in ROWS:
        if degree not in (176, 192):
            raise ValueError("unexpected canonical degree")
        if (square - degree) % 2:
            raise ValueError(f"RR parity regression {row_id}/x4={x4}")
        chi_C = chi_O + (square - degree) // 2
        K_K_minus_C = K2 - degree
        if K_K_minus_C >= 0:
            raise ValueError(f"K.(K-C) not negative {row_id}/x4={x4}")
        # K is nef by the audited source lock.  Therefore K-C cannot be
        # effective when K.(K-C)<0.  Serre duality gives h2(O(C))=0, hence
        # h0(O(C)) = chi(O(C)) + h1(O(C)) >= chi(O(C)).
        if chi_C <= 0:
            raise ValueError(f"nonpositive RR lower bound {row_id}/x4={x4}")
        out_rows.append({
            "source_node": source_node,
            "row_id": row_id,
            "target_geometric_genus": genus,
            "K_dot_C": degree,
            "x4": x4,
            "C_square": square,
            "observed_witness_sha256_prefix": witness_prefix,
            "chi_O_C": chi_C,
            "K_dot_K_minus_C": K_K_minus_C,
            "h2_O_C": 0,
            "h0_lower_bound": chi_C,
            "geometric_effective_divisor_representative_exists": True,
        })

    expected_partition = {
        ("g0-d176", x) for x in [3,7,11,15,19,23,27,31,35,39]
    } | {
        ("g1-d192", x) for x in [3,7,11,15,19,23,27,31,35,39,43]
    }
    actual_partition = {(r["row_id"], r["x4"]) for r in out_rows}
    if actual_partition != expected_partition or len(out_rows) != 21:
        raise ValueError("21-terminal partition regression")

    result = {
        "schema": "STAGE32_32_01_178_N348_RIEMANN_ROCH_EFFECTIVITY_V1",
        "node_id": "N348",
        "source_locks": {
            "n342_checkpoint_canonical": EXPECTED_N342_CANONICAL,
            "n347_checkpoint_canonical": EXPECTED_N347_CANONICAL,
            "n345_run_id": 34429852662,
            "n345_verify_job_id": 102722838215,
            "n345_canonical_sha256": EXPECTED_N345_CANONICAL,
            "n347_run_id": 34431789914,
            "n347_verify_job_id": 102728645720,
            "n347_canonical_sha256": EXPECTED_N347_RUN_CANONICAL,
            "retained_picard64_bundle_sha256": EXPECTED_BUNDLE_CANONICAL,
            "historical_picard_adapter_canonical": EXPECTED_HIST_PICARD_CANONICAL,
            "historical_rr_canonical": EXPECTED_HIST_RR_CANONICAL,
            "historical_merged_effectivity_pr": 1471,
            "historical_merge_commit": "d6acf27fe9c3ba2fb3fad63a49f39668bb52118d",
            "surface_source_lock": "stages/stage29/29-02a/source-lock.md",
            "surface_source_audit": "PASS",
        },
        "surface_invariants": {
            "K_square": K2,
            "p_g": pg,
            "q": q,
            "chi_O": chi_O,
            "K_nef": True,
        },
        "rows": out_rows,
        "aggregate": {
            "input_exact_picard_class_count": len(out_rows),
            "geometric_effective_divisor_representative_count": sum(
                1 for r in out_rows if r["geometric_effective_divisor_representative_exists"]
            ),
            "nonpositive_chi_count": sum(1 for r in out_rows if r["chi_O_C"] <= 0),
            "minimum_h0_lower_bound": min(r["h0_lower_bound"] for r in out_rows),
            "maximum_h0_lower_bound": max(r["h0_lower_bound"] for r in out_rows),
        },
        "conclusion": {
            "riemann_roch_geometric_divisor_effectivity_closed_for_all_21_locked_classes": True,
            "next_gap": "INTEGRAL_IRREDUCIBLE_LOW_GENUS_CARRIER_AND_NORMALIZATION_BRANCH_COMPATIBILITY",
        },
        "semantics": {
            "geometric_effective_divisor_is_not_integral_irreducible_curve": True,
            "target_normalization_genus_0_or_1_not_proved": True,
            "q_defined_effective_member_not_proved": True,
            "production_leaf_credit": False,
            "n350_producer_registry_unchanged": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "hostile_audit_required_before_main_credit": True,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N348_RIEMANN_ROCH_GEOMETRIC_DIVISOR_EFFECTIVITY_21_OF_21",
        "effective": result["aggregate"]["geometric_effective_divisor_representative_count"],
        "nonpositive": result["aggregate"]["nonpositive_chi_count"],
        "min_h0": result["aggregate"]["minimum_h0_lower_bound"],
        "max_h0": result["aggregate"]["maximum_h0_lower_bound"],
        "canonical": result["canonical_sha256_without_this_field"],
        "integral_irreducible_low_genus_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
