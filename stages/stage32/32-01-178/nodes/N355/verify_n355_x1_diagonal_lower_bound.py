#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N220 = HERE.parent / "N220"
sys.path.insert(0, str(N220))
import verify_n220_exact_symbolic_count as base

MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
N354_RECEIPT = HERE.parent / "N354/HOSTILE-AUDIT-PASS.json"
CONTRACT = HERE / "SPECIAL_FIBRE_PREFIX_MAX_CUT_CONTRACT.md"

EXPECTED_N220_VERIFIER_BLOB = "5855ae0835a828ab56b7a6e93a42f6788b6f676a"
EXPECTED_CONTRACT_BLOB = "8a20e8f02c36907e0d3370d1cbd5250b86440932"
EXPECTED_N354_RECEIPT_BLOB = "0394b088349780b6cddf7bcb9d207b3889679e1e"
EXPECTED_N354_REVIEW = 5164850548
EXPECTED_N354_STRATA = 17128
EXPECTED_N354_TERMINALS = 38560956534397137634780102


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parity_counts(lo: int, hi: int) -> tuple[int, int]:
    """Return counts of even, odd integers in inclusive [lo,hi]."""
    if lo > hi:
        return (0, 0)
    n = hi - lo + 1
    evens = n // 2
    odds = n // 2
    if n & 1:
        if lo & 1:
            odds += 1
        else:
            evens += 1
    return evens, odds


def build_suffix_capacity_table(max_required: int = 64):
    """Count eight-variable unequal suffixes by N220 optimistic support capacity.

    For fixed rem=e-x0-x1 and parity p=x1 mod2, the remaining eight known
    exceptional variables consist of five parity-free and three parity-marked
    variables.  The table answers the exact count whose final N220 optimistic
    support capacity is >=K, for base support 1 (x0=0) or 2 (x0>0).
    """
    free8 = base.build_free_distribution(unmarked=5, marked=3)
    out = {
        1: [[[0] * (max_required + 1) for _ in range(2)] for __ in range(base.MAX_E + 1)],
        2: [[[0] * (max_required + 1) for _ in range(2)] for __ in range(base.MAX_E + 1)],
    }
    for rem in range(base.MAX_E + 1):
        for base_support in (1, 2):
            by_parity_capacity = [[0] * (max_required + 40) for _ in range(2)]
            for mass in range(rem + 1):
                slack = rem - mass
                optimistic_suffix = min(38, slack)
                row = free8[mass]
                for support in range(len(row)):
                    cap = base_support + support + optimistic_suffix
                    for parity in (0, 1):
                        count = row[support][parity]
                        if count:
                            by_parity_capacity[parity][min(cap, len(by_parity_capacity[parity]) - 1)] += count
            for parity in (0, 1):
                running = 0
                capacities = by_parity_capacity[parity]
                for k in range(len(capacities) - 1, -1, -1):
                    running += capacities[k]
                    if k <= max_required:
                        out[base_support][rem][parity][k] = running
    return out


def unequal_x1_gt_half_count(*, genus: int, degree: int, e: int, table) -> int:
    """Exact exceptional-prefix count for x0<x1 and x1>floor(d/2), after N220."""
    required = ceil_div(degree - 16 * genus + 16, 4)
    h = degree // 2
    total = 0
    for u in range(1, e + 1):
        max_x0 = min((u - 1) // 2, u - h - 1)
        if max_x0 < 0:
            continue
        rem = e - u

        # x0=0 is the unique base-support-one pair when allowed.
        if max_x0 >= 0:
            x1 = u
            total += table[1][rem][x1 & 1][required]

        # x0=1..max_x0 have base support two. Group only by x1 parity.
        if max_x0 >= 1:
            even_x0, odd_x0 = parity_counts(1, max_x0)
            # x1 parity = u parity xor x0 parity.
            total += even_x0 * table[2][rem][u & 1][required]
            total += odd_x0 * table[2][rem][(u ^ 1) & 1][required]
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    if git_blob_sha1(Path(base.__file__)) != EXPECTED_N220_VERIFIER_BLOB:
        raise ValueError("N220 symbolic verifier source-lock regression")
    if git_blob_sha1(CONTRACT) != EXPECTED_CONTRACT_BLOB:
        raise ValueError("N355 contract source-lock regression")
    if git_blob_sha1(N354_RECEIPT) != EXPECTED_N354_RECEIPT_BLOB:
        raise ValueError("N354 receipt source-lock regression")

    receipt = json.loads(N354_RECEIPT.read_text())
    if receipt["status"] != "PASS" or receipt["review_id"] != EXPECTED_N354_REVIEW:
        raise ValueError("N354 audit authority regression")
    if receipt["consumed_counts"]["remaining_strata"] != EXPECTED_N354_STRATA:
        raise ValueError("N354 survivor-strata regression")
    if receipt["consumed_counts"]["remaining_terminals"] != EXPECTED_N354_TERMINALS:
        raise ValueError("N354 survivor-terminal regression")

    manifest = base.load_canonical(MANIFEST, base.EXPECTED_MANIFEST_CANONICAL)
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    table = build_suffix_capacity_table()
    records = []
    total_subset_rejected = 0
    affected_strata = 0
    by_genus = {0: [0, 0], 1: [0, 0]}

    for row_id in rows:
        g, d = base.parse_row_id(row_id)
        legacy_emin = 8 if g == 0 else 4
        K = ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * d) // 5
        for e in range(effective_emin, emax + 1):
            # Exact N354 survivor predicate after N353.
            if d > e + 4 * g - 4:
                continue
            if e & 1:
                continue
            if d < 2 * ceil_div(e, 6):
                continue

            exceptional_reject = unequal_x1_gt_half_count(
                genus=g, degree=d, e=e, table=table
            )
            normal_block = 19 * d - 5 * e + 1
            terminal_reject = exceptional_reject * normal_block
            if terminal_reject:
                affected_strata += 1
                by_genus[g][0] += 1
            by_genus[g][1] += terminal_reject
            total_subset_rejected += terminal_reject
            records.append({
                "g": g,
                "d": d,
                "e": e,
                "x1_label": 99,
                "threshold": d // 2,
                "unequal_x1_gt_half_n220_exceptional_prefixes": exceptional_reject,
                "normal_block": normal_block,
                "certified_rejected_terminals": terminal_reject,
            })

    if len(records) != EXPECTED_N354_STRATA:
        raise ValueError(f"N354 survivor record count regression: {len(records)}")
    if total_subset_rejected <= 0:
        raise ValueError("N355 diagonal subset unexpectedly empty")
    if total_subset_rejected >= EXPECTED_N354_TERMINALS:
        raise ValueError("N355 subset lower bound exceeds source population")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    result = {
        "schema": "STAGE32_32_01_178_N355_X1_DIAGONAL_CERTIFIED_LOWER_BOUND_V1",
        "node_id": "N355",
        "status": "AUDIT_CANDIDATE_CERTIFIED_SUBSET_LOWER_BOUND_NO_AUTHORITY_DECREMENT",
        "source_population": {
            "n354_audited_strata": EXPECTED_N354_STRATA,
            "n354_audited_terminals": EXPECTED_N354_TERMINALS,
        },
        "subset_definition": {
            "branch": "x0<x1",
            "assignment_label": 99,
            "condition": "x1>floor(d/2)",
            "why_rejected": "N355 diagonal consequence requires every known exceptional pairing <= floor(d/2)",
            "n220_filter_counted_exactly": True,
            "normal_x4_block_multiplied_exactly": True,
        },
        "aggregate": {
            "survivor_strata_replayed": len(records),
            "affected_strata": affected_strata,
            "certified_subset_rejected_terminals": total_subset_rejected,
            "certified_fraction_of_n354_terminal_mass": f"{total_subset_rejected}/{EXPECTED_N354_TERMINALS}",
            "genus0_affected_strata": by_genus[0][0],
            "genus0_rejected_terminals": by_genus[0][1],
            "genus1_affected_strata": by_genus[1][0],
            "genus1_rejected_terminals": by_genus[1][1],
            "per_stratum_stream_sha256": stream.hexdigest(),
        },
        "scope_warning": {
            "this_is_not_full_n355_count": True,
            "equal_x0_eq_x1_branch_not_counted": True,
            "other_nine_diagonal_violations_not_counted": True,
            "stronger_A1_plus_A2_violations_not_counted": True,
            "therefore_total_is_certified_lower_bound_only": True,
        },
        "semantics": {
            "main_pruning_count_credit": False,
            "authoritative_n354_aggregate_unchanged": True,
            "heavy_compute_authorized": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N355_X1_DIAGONAL_CERTIFIED_LOWER_BOUND",
        "affected_strata": affected_strata,
        "certified_subset_rejected_terminals": total_subset_rejected,
        "stream": stream.hexdigest(),
        "canonical": result["canonical_sha256_without_this_field"],
        "authority_decrement": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
