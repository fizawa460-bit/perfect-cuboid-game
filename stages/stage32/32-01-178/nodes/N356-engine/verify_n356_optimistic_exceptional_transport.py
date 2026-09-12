#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N355 = HERE.parent / "N355"
CONTRACT = HERE / "OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CAP_CONTRACT.md"
N355_FULL = N355 / "verify_n355_full_prefix_block_sum_census.py"
N355_PREFLIGHT = N355 / "verify_n355_special_fibre_prefix_max_cut.py"
N355_FULL_RECEIPT = N355 / "FULL-PREFIX-HOSTILE-AUDIT-PASS.json"

EXPECTED_CONTRACT_BLOB = "d2353cab9c175a680067c7ad4c24759b6dd15df3"
EXPECTED_N355_FULL_BLOB = "ccc00d1536cdf5e27965465dd5e40163e2fcb91c"
EXPECTED_N355_PREFLIGHT_BLOB = "c6214fb274992a874899c563d83cbb7a5a29ba89"
EXPECTED_N355_FULL_RECEIPT_BLOB = "033294f56fb86d81b7aa43758a51a39747ccc082"
EXPECTED_N355_FULL_RECEIPT_CANONICAL = "d6bda89f94eb57bf021f0acbbc5000e198f1805c09da3e5f9a531d20b70ce004"
EXPECTED_N355_FULL_REVIEW = 5165895301
EXPECTED_N355_FULL_HEAD = "3f3aadd2e5ada2a0a02a69490d6d659c02762682"
AUDITED_N355_STRATA = 17128
AUDITED_N355_TERMINALS = 66462870551188628549910

MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def component3_extra_capacity(n1: int, n2: int, b: int, c: int) -> int:
    if min(n1, n2) < max(b, c):
        return -1
    return min(2 * n1 - b - c, 2 * n2 - b - c, n1 + n2 - 2 * b)


def optimistic_total_capacity(d: int, b: int, c: int) -> int:
    h = d // 2
    if max(b, c) > h:
        return -1
    return min(6 * h, 4 * h + d + c - b)


def brute_component3_extra_capacity(n1: int, n2: int, b: int, c: int) -> int:
    if min(n1, n2) < max(b, c):
        return -1
    r1 = n1 - c
    r2 = n1 - b
    c1 = n2 - b
    c2 = n2 - c
    best = 0
    for x11 in range(min(r1, c1) + 1):
        for x21 in range(min(r2, c1 - x11) + 1):
            x22 = min(r2 - x21, c2)
            best = max(best, x11 + x21 + x22)
    return best


def validate_transport_formula() -> None:
    for n1 in range(5):
        for n2 in range(5):
            for b in range(min(n1, n2) + 1):
                for c in range(min(n1, n2) + 1):
                    got = brute_component3_extra_capacity(n1, n2, b, c)
                    want = component3_extra_capacity(n1, n2, b, c)
                    if got != want:
                        raise ValueError(
                            f"component3 max-flow formula regression {(n1,n2,b,c)}: {got}!={want}"
                        )

    for d in range(1, 9):
        h = d // 2
        for a in range(h + 1):
            for b in range(h + 1):
                for c in range(h + 1):
                    best = -1
                    for n1 in range(d + 1):
                        n2 = d - n1
                        if min(n1, n2) < max(a, b, c):
                            continue
                        m = min(n1, n2)
                        extra3 = component3_extra_capacity(n1, n2, b, c)
                        total = 4 * m + b + c + extra3
                        best = max(best, total)
                    want = optimistic_total_capacity(d, b, c)
                    if best != want:
                        raise ValueError(
                            f"balanced transport capacity regression {(d,a,b,c)}: {best}!={want}"
                        )


def reconstruct_cell_geometry(pre):
    n345 = pre.load_module(pre.N345_PATH, "s32_n356_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n356_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n356_marking")
    if bundle.get("canonical_sha256") != pre.EXPECTED_BUNDLE:
        raise ValueError("retained Picard bundle regression")
    if marking.get("canonical_sha256") != pre.EXPECTED_MARKING:
        raise ValueError("retained marking regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    partitions = []
    for pack in pre.BOUNDARY_PACKS:
        blocks = []
        seen = []
        for boundary in pack:
            inc = tuple(j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1)
            if len(inc) != 8:
                raise ValueError(f"boundary incidence regression {boundary}")
            seen.extend(inc)
            blocks.append(inc)
        if sorted(seen) != list(range(93, 141)):
            raise ValueError("exceptional partition regression")
        partitions.append(blocks)

    cells = {}
    for i, row in enumerate(partitions[0]):
        for j, col in enumerate(partitions[1]):
            cell = tuple(sorted(set(row).intersection(col)))
            if cell:
                cells[(i, j)] = cell
    if len(cells) != 12 or any(len(cell) != 4 for cell in cells.values()):
        raise ValueError(f"2x2-component cell structure regression: {cells}")

    row_neighbors = {i: set() for i in range(6)}
    col_neighbors = {j: set() for j in range(6)}
    for i, j in cells:
        row_neighbors[i].add(j)
        col_neighbors[j].add(i)
    if any(len(v) != 2 for v in row_neighbors.values()) or any(len(v) != 2 for v in col_neighbors.values()):
        raise ValueError("transport graph degree regression")

    known = set(pre.KNOWN_EXCEPTIONAL)
    known_cells = {}
    no_missing_cells = []
    for key, cell in cells.items():
        k = tuple(x for x in cell if x in known)
        if k:
            known_cells[key] = k
        if not set(cell) - known:
            no_missing_cells.append((key, cell))

    expected_known_sets = {
        (101, 102, 103),
        (97, 98, 99),
        (93, 94, 95, 96),
    }
    if set(known_cells.values()) != expected_known_sets:
        raise ValueError(f"known-cell occupancy regression: {known_cells}")
    if len(no_missing_cells) != 1 or no_missing_cells[0][1] != (93, 94, 95, 96):
        raise ValueError(f"unique saturated cell regression: {no_missing_cells}")

    return {
        "cells": {f"{i},{j}": list(v) for (i, j), v in sorted(cells.items())},
        "known_cells": {f"{i},{j}": list(v) for (i, j), v in sorted(known_cells.items())},
        "unique_no_missing_cell": {
            "cell": list(no_missing_cells[0][0]),
            "labels": list(no_missing_cells[0][1]),
        },
    }


def build_transport_exact(h: int, threshold: int, bc_pref, lex_pref, fullmod):
    h = int(h)
    mid = [[0] * 8 for _ in range(2 * h + 1)]

    for x0 in range(h + 1):
        for x1 in range(x0 + 1, h + 1):
            c2 = h - x1
            c3 = h - x0
            m0 = x0 + x1
            s0 = 1 + int(x0 > 0)
            parity = x1 & 1
            for r in range(c2 + c3 + 1):
                lo = max(0, r - c3)
                hi = min(c2, r, (threshold - x1 + x0 + r) // 2)
                if lo > hi:
                    continue
                for support in range(6):
                    value = fullmod.interval_query(bc_pref, r, lo, hi, support, parity)
                    if value:
                        mid[m0 + r][s0 + support] += value

    for a in range(h + 1):
        ccap = h - a
        m0 = 2 * a
        s0 = 0 if a == 0 else 2
        parity = a & 1
        for r in range(2 * ccap + 1):
            lo = max(0, r - ccap)
            hi = min(ccap, r, (threshold + r) // 2)
            if lo > hi:
                continue
            for support in range(6):
                value = fullmod.interval_query(lex_pref, r, lo, hi, support, parity)
                if value:
                    mid[m0 + r][s0 + support] += value

    out = [[0] * 11 for _ in range(3 * h + 1)]
    for m0, row in enumerate(mid):
        for s0, left in enumerate(row):
            if not left:
                continue
            for q in range(h + 1):
                for sq in range(4):
                    right = fullmod.triple_free_count(q, sq)
                    if right:
                        out[m0 + q][s0 + sq] += left * right
    return out


def brute_small_transport(h: int, threshold: int):
    out = [[0] * 11 for _ in range(3 * h + 1)]
    for v in itertools.product(range(h + 1), repeat=10):
        x0, x1, x2, x3, x5, x6, x7, x8, x9, x10 = v
        if x0 > x1:
            continue
        if x0 == x1 and (x5, x6) > (x8, x9):
            continue
        if (x1 + x8 + x9 + x10) & 1:
            continue
        a = x2 + x3 + x7
        b = x1 + x5 + x9
        c = x0 + x6 + x8 + x10
        if max(a, b, c) > h:
            continue
        if b - c > threshold:
            continue
        mass = sum(v)
        support = sum(int(x > 0) for x in v)
        out[mass][support] += 1
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    for path, expected in [
        (CONTRACT, EXPECTED_CONTRACT_BLOB),
        (N355_FULL, EXPECTED_N355_FULL_BLOB),
        (N355_PREFLIGHT, EXPECTED_N355_PREFLIGHT_BLOB),
        (N355_FULL_RECEIPT, EXPECTED_N355_FULL_RECEIPT_BLOB),
    ]:
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual}!={expected}")

    receipt = json.loads(N355_FULL_RECEIPT.read_text())
    body = dict(receipt)
    receipt_canonical = body.pop("canonical_sha256_without_this_field")
    if receipt_canonical != EXPECTED_N355_FULL_RECEIPT_CANONICAL or csha(body) != receipt_canonical:
        raise ValueError("N355 full-prefix receipt canonical regression")
    if receipt["status"] != "PASS" or receipt["review_id"] != EXPECTED_N355_FULL_REVIEW:
        raise ValueError("N355 full-prefix hostile-audit PASS regression")
    if receipt["audited_exact_head"] != EXPECTED_N355_FULL_HEAD:
        raise ValueError("N355 full-prefix audited exact-head regression")
    if receipt["consumed_counts"]["remaining_strata"] != AUDITED_N355_STRATA:
        raise ValueError("N355 full-prefix residual strata regression")
    if receipt["consumed_counts"]["remaining_terminals"] != AUDITED_N355_TERMINALS:
        raise ValueError("N355 full-prefix residual terminal regression")

    fullmod = load_module(N355_FULL, "s32_n356_n355_full")
    pre = load_module(N355_PREFLIGHT, "s32_n356_n355_preflight")
    geometry = reconstruct_cell_geometry(pre)
    validate_transport_formula()

    manifest = fullmod.base.load_canonical(MANIFEST, fullmod.base.EXPECTED_MANIFEST_CANONICAL)
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")
    parsed = [fullmod.base.parse_row_id(row_id) for row_id in rows]
    H = max(d // 2 for _, d in parsed)
    all_degrees_even = all((d & 1) == 0 for _, d in parsed)

    bc_pref = fullmod.build_bc_prefix(H)
    lex_pref = fullmod.build_lex_prefix(H)

    for h in (0, 1, 2):
        for threshold in range(-2, 3):
            got = build_transport_exact(h, threshold, bc_pref, lex_pref, fullmod)
            want = brute_small_transport(h, threshold)
            if got != want:
                raise ValueError(f"transport prefix DP brute regression h={h} t={threshold}")

    total_exact = fullmod.base.build_exceptional_exact_mass_support()
    support_lt = fullmod.fast.build_support_lt(total_exact)
    cumulative = []
    running = 0
    for e in range(fullmod.base.MAX_E + 1):
        running += sum(total_exact[e])
        cumulative.append(running)

    capped_cache = {}
    transport_cache = {}
    records = []
    replay_n355_terminals = 0
    incremental_rejected_terminals = 0
    remaining_terminals = 0
    remaining_strata = 0
    affected_strata = 0
    genus_reject = {0: 0, 1: 0}
    genus_remaining = {0: 0, 1: 0}

    for row_id in rows:
        g, d = fullmod.base.parse_row_id(row_id)
        h = d // 2
        if h not in capped_cache:
            capped_cache[h] = fullmod.build_capped_exact(h, bc_pref, lex_pref)
        capped = capped_cache[h]

        legacy_emin = 8 if g == 0 else 4
        K = fullmod.ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * d) // 5

        for e in range(effective_emin, emax + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * fullmod.ceil_div(e, 6):
                continue

            threshold = 4 * h + d - e
            key = (h, threshold)
            if key not in transport_cache:
                transport_cache[key] = build_transport_exact(h, threshold, bc_pref, lex_pref, fullmod)
            transport = transport_cache[key]

            n355_exceptional = fullmod.n220_accept_from_exact(capped, e=e, required=K)
            n356_exceptional = fullmod.n220_accept_from_exact(transport, e=e, required=K)
            if not 0 <= n356_exceptional <= n355_exceptional:
                raise ValueError(f"N356 count outside audited N355 residual {(g,d,e)}")

            normal_block = 19 * d - 5 * e + 1
            n355_t = n355_exceptional * normal_block
            remain_t = n356_exceptional * normal_block
            reject_t = n355_t - remain_t

            replay_n355_terminals += n355_t
            incremental_rejected_terminals += reject_t
            remaining_terminals += remain_t
            genus_reject[g] += reject_t
            genus_remaining[g] += remain_t
            if reject_t:
                affected_strata += 1
            if remain_t:
                remaining_strata += 1

            records.append({
                "g": g,
                "d": d,
                "e": e,
                "h": h,
                "threshold_b_minus_c": threshold,
                "n355_full_prefix_terminals": n355_t,
                "n356_transport_rejected_terminals": reject_t,
                "n356_transport_remaining_terminals": remain_t,
            })

    if replay_n355_terminals != AUDITED_N355_TERMINALS:
        raise ValueError(f"audited N355 full-prefix replay regression {replay_n355_terminals}")
    if incremental_rejected_terminals <= 0:
        raise ValueError("N356 transport cut is not incrementally strict")
    if AUDITED_N355_TERMINALS - incremental_rejected_terminals != remaining_terminals:
        raise ValueError("N356 partition identity regression")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    result = {
        "schema": "STAGE32_32_01_178_N356_OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CENSUS_V1",
        "node_id": "N356",
        "status": "AUDIT_CANDIDATE_TRANSPORT_NECESSARY_CUT_NO_MAIN_CREDIT",
        "audited_input": {
            "review_id": EXPECTED_N355_FULL_REVIEW,
            "audited_exact_head": EXPECTED_N355_FULL_HEAD,
            "remaining_strata": AUDITED_N355_STRATA,
            "remaining_terminals": AUDITED_N355_TERMINALS,
        },
        "geometry": geometry,
        "transport_contract": {
            "h": "floor(d/2)",
            "known_cell_masses": {
                "a": "E101+E102+E103",
                "b": "E97+E98+E99",
                "c": "E93+E94+E95+E96",
            },
            "balanced_max_capacity": "min(6*h,4*h+d+c-b)",
            "prefix_sensitive_necessary_cut": "b-c<=4*h+d-e",
            "even_degree_specialization": "b-c<=3*d-e",
            "all_full178_degrees_even": all_degrees_even,
            "relaxation": "omitted exceptional mass may be distributed arbitrarily among cells containing at least one omitted label",
        },
        "aggregate": {
            "source_strata_replayed": len(records),
            "source_terminals_replayed": replay_n355_terminals,
            "affected_strata": affected_strata,
            "candidate_incremental_rejected_terminals": incremental_rejected_terminals,
            "candidate_remaining_strata": remaining_strata,
            "candidate_remaining_terminals": remaining_terminals,
            "genus0_rejected_terminals": genus_reject[0],
            "genus1_rejected_terminals": genus_reject[1],
            "genus0_remaining_terminals": genus_remaining[0],
            "genus1_remaining_terminals": genus_remaining[1],
            "per_stratum_stream_sha256": stream.hexdigest(),
        },
        "verification": {
            "component3_small_maxflow_brute": True,
            "balanced_capacity_small_split_brute": True,
            "prefix_dp_small_brute_h0_h1_h2": True,
            "audited_n355_replayed_exactly": True,
            "partition_identity": True,
            "max_h": H,
        },
        "semantics": {
            "main_pruning_credit": False,
            "external_hostile_audit_required": True,
            "n350_producer_registered": False,
            "production_complete": False,
            "n104_release": False,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "heavy_compute_authorized": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)

    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    print(json.dumps({
        "verdict": "PASS_N356_OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CENSUS",
        "incremental_rejected_terminals": incremental_rejected_terminals,
        "remaining_strata": remaining_strata,
        "remaining_terminals": remaining_terminals,
        "affected_strata": affected_strata,
        "stream": stream.hexdigest(),
        "canonical": result["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
