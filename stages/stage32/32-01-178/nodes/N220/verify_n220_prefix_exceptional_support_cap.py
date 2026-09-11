#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_family import terminal_predicate

EXPECTED_MANIFEST_CANONICAL = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PREFIX_CANONICAL = "65a5ab43e44ebb33341c250a8fa2c5ece09999203893f9a76ca46fb037df558f"
EXPECTED_ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_EXCEPTIONAL_POSITIONS = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10]
FREE_CONCENTRATION_POSITIONS = (2, 3, 7)
EXPECTED_COARSE_BEFORE = 64111
EXPECTED_COARSE_AFTER_NODE_MASS = 60491
EXPECTED_COARSE_ELIMINATED = 3620
EXPECTED_AFFECTED_ROWS = 168
EXPECTED_EXPLICIT_PREFIX_CONFIGS = 24876258
EXPECTED_EXPLICIT_TERMINAL_LOWER_BOUND = 26206770933


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    body = dict(raw)
    body.pop("canonical_sha256_without_this_field", None)
    if claimed != expected or csha(body) != expected:
        raise ValueError(f"canonical hash regression: {path}")
    return raw


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = str(row_id).split("-d")
    return int(g[1:]), int(d)


def ceil_div(a: int, b: int) -> int:
    if b <= 0:
        raise ValueError("positive denominator required")
    return -((-a) // b)


def support_required(*, genus: int, degree: int) -> int:
    return ceil_div(degree - 16 * genus + 16, 4)


def prefix_support_upper_bound(values: list[int], *, e: int) -> int:
    if len(values) != 11:
        raise ValueError("expected 11 indexed-terminal prefix values")
    known_mass = sum(int(values[i]) for i in EXPECTED_EXCEPTIONAL_POSITIONS)
    if known_mass > int(e):
        return -1
    known_support = sum(int(values[i]) > 0 for i in EXPECTED_EXCEPTIONAL_POSITIONS)
    remaining_mass = int(e) - known_mass
    return known_support + min(38, remaining_mass)


def explicit_family_count(*, e: int, required: int) -> int:
    # One all-zero exceptional prefix, plus three symmetry/parity-free one-slot
    # concentration families x2=s, x3=s, x7=s.  Counts only members whose
    # support upper bound is already below the required support.
    zero = int(min(38, e) < required)
    if required <= 1:
        positive_s = 0
    elif required <= 39:
        positive_s = min(e, required - 1)
    else:
        positive_s = e
    return zero + len(FREE_CONCENTRATION_POSITIONS) * positive_s


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    args = ap.parse_args()

    manifest = load_canonical(args.manifest, EXPECTED_MANIFEST_CANONICAL)
    prefix = load_canonical(args.prefix_checkpoint, EXPECTED_PREFIX_CANONICAL)
    order = prefix["exact_terminal_family"]["assignment_order_known_labels_1based"]
    if order != EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("indexed-terminal assignment order regression")
    exceptional_positions = [i for i, label in enumerate(order) if int(label) > 92]
    if exceptional_positions != EXPECTED_EXCEPTIONAL_POSITIONS or order[4] != 49:
        raise ValueError("ten-exceptional/one-normal prefix layout regression")

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    coarse_before = 0
    coarse_after = 0
    coarse_eliminated = 0
    affected_rows = 0
    prunable_strata = 0
    explicit_prefix_configs = 0
    explicit_terminal_lower_bound = 0

    for row_id in rows:
        genus, degree = parse_row_id(row_id)
        legacy_emin = 8 if genus == 0 else 4
        emax = (19 * degree) // 5
        required = support_required(genus=genus, degree=degree)
        effective_emin = max(legacy_emin, required)

        row_before = max(0, emax - legacy_emin + 1)
        row_after = max(0, emax - effective_emin + 1)
        row_eliminated = row_before - row_after
        coarse_before += row_before
        coarse_after += row_after
        coarse_eliminated += row_eliminated
        if row_eliminated:
            affected_rows += 1

        for e in range(effective_emin, emax + 1):
            # A universal explicit witness that the new cut is nontrivial in
            # every post-node-mass stratum: concentrate all known exceptional
            # mass in x2.  It satisfies every current indexed-prefix rule, but
            # can attain at most one positive exceptional slot in total.
            witness = [0] * 11
            witness[2] = e
            if not terminal_predicate(witness, e=e, d=degree):
                raise ValueError(f"concentrated prefix stopped being terminal-valid: {row_id}, e={e}")
            if prefix_support_upper_bound(witness, e=e) >= required:
                raise ValueError(f"concentrated prefix stopped being support-cap rejected: {row_id}, e={e}")
            prunable_strata += 1

            family_count = explicit_family_count(e=e, required=required)
            if family_count <= 0:
                raise ValueError(f"explicit rejected family unexpectedly empty: {row_id}, e={e}")
            explicit_prefix_configs += family_count
            normal_budget = 19 * degree - 5 * e
            if normal_budget < 0:
                raise ValueError("negative normal budget inside manifest stratum")
            explicit_terminal_lower_bound += family_count * (normal_budget + 1)

    observed = {
        "coarse_before": coarse_before,
        "coarse_after_node_mass": coarse_after,
        "coarse_eliminated_by_node_mass": coarse_eliminated,
        "affected_rows_by_node_mass": affected_rows,
        "post_node_mass_prunable_strata": prunable_strata,
        "explicit_rejected_exceptional_prefix_configs": explicit_prefix_configs,
        "explicit_rejected_terminal_tuple_lower_bound": explicit_terminal_lower_bound,
    }
    expected = {
        "coarse_before": EXPECTED_COARSE_BEFORE,
        "coarse_after_node_mass": EXPECTED_COARSE_AFTER_NODE_MASS,
        "coarse_eliminated_by_node_mass": EXPECTED_COARSE_ELIMINATED,
        "affected_rows_by_node_mass": EXPECTED_AFFECTED_ROWS,
        "post_node_mass_prunable_strata": EXPECTED_COARSE_AFTER_NODE_MASS,
        "explicit_rejected_exceptional_prefix_configs": EXPECTED_EXPLICIT_PREFIX_CONFIGS,
        "explicit_rejected_terminal_tuple_lower_bound": EXPECTED_EXPLICIT_TERMINAL_LOWER_BOUND,
    }
    if observed != expected:
        raise ValueError(f"N220 exact-count regression: {observed} != {expected}")

    print(json.dumps({
        "verdict": "PASS_N220_PREFIX_EXCEPTIONAL_SUPPORT_CAP_NONTRIVIAL",
        "formula": "S10 + min(38, e-M10) >= ceil((d-16g+16)/4)",
        **observed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
