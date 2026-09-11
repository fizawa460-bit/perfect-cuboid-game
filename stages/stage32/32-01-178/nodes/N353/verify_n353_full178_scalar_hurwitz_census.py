#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N250_PATH = HERE.parent / "N250/verify_n250_post_n220_block_census.py"
N351_CONTRACT = HERE.parent / "N351/GENERAL_FACTOR_HURWITZ_MASS_CAP_CONTRACT.md"
N352_CONTRACT = HERE.parent / "N352/DEGREE_SUM_SCALAR_HURWITZ_CONTRACT.md"
N352_VERIFIER = HERE.parent / "N352/verify_n352_degree_sum_scalar_hurwitz.py"

EXPECTED_N250_BLOB = "a2aceacca94e446df96835f76ddae14fbc815f22"
EXPECTED_N351_CONTRACT_BLOB = "377c2c43b3c80644c5913586cee42e9a6ec1138d"
EXPECTED_N352_CONTRACT_BLOB = "60295a86297330d83370cf32016c75a8244a2aa4"
EXPECTED_N352_VERIFIER_BLOB = "2462f3e45c0a47044b94c71c0eac3b984585e7ea"
EXPECTED_STRATA = 60491
EXPECTED_POST_N220 = 346053707902916587089896969
EXPECTED_FULL178_ROWS = 178
EXPECTED_GENUS_SET = {0, 1}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    locks = {
        str(N250_PATH.relative_to(ROOT)): EXPECTED_N250_BLOB,
        str(N351_CONTRACT.relative_to(ROOT)): EXPECTED_N351_CONTRACT_BLOB,
        str(N352_CONTRACT.relative_to(ROOT)): EXPECTED_N352_CONTRACT_BLOB,
        str(N352_VERIFIER.relative_to(ROOT)): EXPECTED_N352_VERIFIER_BLOB,
    }
    for rel, expected in locks.items():
        got = git_blob_sha1(ROOT / rel)
        if got != expected:
            raise ValueError(f"source-lock regression {rel}: {got} != {expected}")

    n250 = load_module(N250_PATH, "s32_n353_n250")
    base = n250.base
    fast = n250.fast
    manifest = base.load_canonical(n250.MANIFEST, base.EXPECTED_MANIFEST_CANONICAL)
    prefix = base.load_canonical(n250.PREFIX, base.EXPECTED_PREFIX_CANONICAL)
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != base.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("indexed-terminal assignment-order regression")

    row_ids: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        row_ids.extend(str(v) for v in ids)
    if len(row_ids) != EXPECTED_FULL178_ROWS or len(set(row_ids)) != EXPECTED_FULL178_ROWS:
        raise ValueError("FULL178 row population regression")
    genera = {base.parse_row_id(row_id)[0] for row_id in row_ids}
    if genera != EXPECTED_GENUS_SET:
        raise ValueError(f"N351 genus scope does not cover FULL178: {sorted(genera)}")

    exact = base.build_exceptional_exact_mass_support()
    support_lt = fast.build_support_lt(exact)
    cumulative_exceptional: list[int] = []
    running = 0
    for e in range(base.MAX_E + 1):
        running += sum(exact[e])
        cumulative_exceptional.append(running)

    records = []
    total_post_n220 = 0
    candidate_rejected_terminals = 0
    candidate_remaining_terminals = 0
    candidate_rejected_exceptional_blocks = 0
    candidate_remaining_exceptional_blocks = 0
    contradicted_strata = 0
    not_contradicted_strata = 0
    by_genus = {
        0: {"strata": 0, "contradicted_strata": 0, "post_n220_terminals": 0, "candidate_rejected_terminals": 0, "candidate_remaining_terminals": 0},
        1: {"strata": 0, "contradicted_strata": 0, "post_n220_terminals": 0, "candidate_rejected_terminals": 0, "candidate_remaining_terminals": 0},
    }

    for row_id in row_ids:
        genus, degree = base.parse_row_id(row_id)
        legacy_emin = 8 if genus == 0 else 4
        required = base.ceil_div(degree - 16 * genus + 16, 4)
        effective_emin = max(legacy_emin, required)
        emax = (19 * degree) // 5
        for e in range(effective_emin, emax + 1):
            old_exceptional = cumulative_exceptional[e]
            rejected_exceptional = fast.rejected_fast(exact, support_lt, e=e, required=required)
            survivor_exceptional = old_exceptional - rejected_exceptional
            if survivor_exceptional <= 0:
                raise ValueError("unexpected zero-survivor post-N220 stratum")
            normal_block = 19 * degree - 5 * e + 1
            survivor_terminal = survivor_exceptional * normal_block
            total_post_n220 += survivor_terminal

            scalar_cap = e + 4 * genus - 4
            contradiction = degree > scalar_cap
            if contradiction:
                contradicted_strata += 1
                candidate_rejected_terminals += survivor_terminal
                candidate_rejected_exceptional_blocks += survivor_exceptional
            else:
                not_contradicted_strata += 1
                candidate_remaining_terminals += survivor_terminal
                candidate_remaining_exceptional_blocks += survivor_exceptional

            g = by_genus[genus]
            g["strata"] += 1
            g["post_n220_terminals"] += survivor_terminal
            if contradiction:
                g["contradicted_strata"] += 1
                g["candidate_rejected_terminals"] += survivor_terminal
            else:
                g["candidate_remaining_terminals"] += survivor_terminal

            records.append({
                "row_id": row_id,
                "g": genus,
                "d": degree,
                "e": e,
                "K": required,
                "normal_block": normal_block,
                "survivor_exceptional_blocks": survivor_exceptional,
                "post_n220_terminals": survivor_terminal,
                "scalar_cap": scalar_cap,
                "contradiction": contradiction,
            })

    if len(records) != EXPECTED_STRATA:
        raise ValueError(f"post-N220 stratum count regression: {len(records)}")
    if total_post_n220 != EXPECTED_POST_N220:
        raise ValueError(f"post-N220 terminal-total regression: {total_post_n220}")
    if candidate_rejected_terminals + candidate_remaining_terminals != total_post_n220:
        raise ValueError("terminal partition regression")
    if contradicted_strata + not_contradicted_strata != EXPECTED_STRATA:
        raise ValueError("stratum partition regression")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    frontier = []
    for genus in (0, 1):
        survivors = [r for r in records if r["g"] == genus and not r["contradiction"]]
        if survivors:
            first = min(survivors, key=lambda r: (r["d"], r["e"]))
            min_slack = min(r["scalar_cap"] - r["d"] for r in survivors)
            frontier.append({"g": genus, "first_not_contradicted": first, "minimum_scalar_slack": min_slack})

    body = {
        "schema": "STAGE32_32_01_178_N353_FULL178_SCALAR_HURWITZ_CENSUS_V1",
        "node_id": "N353",
        "status": "AUDIT_CANDIDATE_DIAGNOSTIC_NO_MAIN_CREDIT",
        "population": {
            "full178_rows": EXPECTED_FULL178_ROWS,
            "genus_set": sorted(genera),
            "post_n220_strata": len(records),
            "post_n220_terminals": total_post_n220,
        },
        "source_locks": locks,
        "candidate_scalar_rule": {
            "necessary_condition": "d <= e+4g-4",
            "candidate_reject_when": "d > e+4g-4",
            "n351_scope_covers_full178_genus_set": True,
            "n351_hostile_audit_required": True,
            "n352_hostile_audit_required": True,
        },
        "aggregate": {
            "contradicted_strata": contradicted_strata,
            "not_contradicted_strata": not_contradicted_strata,
            "candidate_rejected_terminals": candidate_rejected_terminals,
            "candidate_remaining_terminals": candidate_remaining_terminals,
            "candidate_rejected_exceptional_blocks": candidate_rejected_exceptional_blocks,
            "candidate_remaining_exceptional_blocks": candidate_remaining_exceptional_blocks,
            "candidate_rejected_terminal_fraction_num": candidate_rejected_terminals,
            "candidate_rejected_terminal_fraction_den": total_post_n220,
            "per_stratum_stream_sha256": stream.hexdigest(),
        },
        "by_genus": {str(k): v for k, v in by_genus.items()},
        "frontier": frontier,
        "semantics": {
            "diagnostic_census_only_until_external_audit": True,
            "main_pruning_credit": False,
            "production_leaf_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N353_FULL178_SCALAR_HURWITZ_CENSUS",
        "contradicted_strata": contradicted_strata,
        "remaining_strata": not_contradicted_strata,
        "candidate_rejected_terminals": str(candidate_rejected_terminals),
        "candidate_remaining_terminals": str(candidate_remaining_terminals),
        "stream": stream.hexdigest(),
        "canonical": body["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
