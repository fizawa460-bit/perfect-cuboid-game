#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from collections import defaultdict
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N355_FULL = HERE.parent / "N355" / "verify_n355_full_prefix_block_sum_census.py"
N357_ENGINE = HERE.parent / "N357-engine" / "verify_n357_transport_support_capacity.py"
N356_RECEIPT = HERE.parent / "N356" / "HOSTILE-AUDIT-PASS.json"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"

EXPECTED_N355_FULL_BLOB = "ccc00d1536cdf5e27965465dd5e40163e2fcb91c"
EXPECTED_N357_ENGINE_BLOB = "479c783cb42d0952cc310708106787147b499240"
EXPECTED_N356_RECEIPT_BLOB = "4966d57f61624c1cfd313ae5d1fe5e33bb25e569"
EXPECTED_MANIFEST_BLOB = "0a46b34e278688240656b4977e9cb7f589e90e06"
EXPECTED_N356_REVIEW = 5176607630
EXPECTED_N356_HEAD = "0cd222d4824e65ea122bc90ac0d48686ddae38f2"
EXPECTED_N356_STRATA = 17128
EXPECTED_N356_TERMINALS = 65396964990500233636214

_ENGINE = None
_FULLMOD = None


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


def count_table(table, e: int, required: int) -> tuple[int, int]:
    old = 0
    new = 0
    for mass, row in enumerate(table):
        if mass > e:
            break
        omitted = e - mass
        for support, by_srem in enumerate(row):
            old_accept = support + min(38, omitted) >= required
            for srem, count in enumerate(by_srem):
                if not count:
                    continue
                if old_accept:
                    old += count
                if support + min(srem, omitted) >= required:
                    new += count
    return old, new


def _compute_group(item):
    (h, threshold), strata = item
    table = _ENGINE.build_support_exact(h, threshold, _FULLMOD)
    out = []
    for row_id, g, d, e, required, normal_block in strata:
        old, new = count_table(table, e, required)
        if not 0 <= new <= old:
            raise ValueError(f"N357 count outside N356 residual {(g,d,e)}: {new}>{old}")
        old_t = old * normal_block
        new_t = new * normal_block
        out.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "e": e,
            "h": h,
            "threshold_b_minus_c": threshold,
            "required_support": required,
            "n356_transport_remaining_terminals": old_t,
            "n357_support_capacity_rejected_terminals": old_t - new_t,
            "n357_support_capacity_remaining_terminals": new_t,
        })
    return out


def main() -> None:
    global _ENGINE, _FULLMOD
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--workers", type=int, default=0)
    args = ap.parse_args()

    for path, expected in [
        (N355_FULL, EXPECTED_N355_FULL_BLOB),
        (N357_ENGINE, EXPECTED_N357_ENGINE_BLOB),
        (N356_RECEIPT, EXPECTED_N356_RECEIPT_BLOB),
        (MANIFEST, EXPECTED_MANIFEST_BLOB),
    ]:
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual}!={expected}")

    receipt = json.loads(N356_RECEIPT.read_text())
    if receipt.get("status") != "PASS" or receipt.get("review_id") != EXPECTED_N356_REVIEW:
        raise ValueError("N356 hostile-audit PASS regression")
    if receipt.get("audited_exact_head") != EXPECTED_N356_HEAD:
        raise ValueError("N356 hostile-audit exact-head regression")
    counts = receipt.get("consumed_counts", {})
    if counts.get("remaining_strata") != EXPECTED_N356_STRATA:
        raise ValueError("N356 authoritative remaining-strata regression")
    if counts.get("remaining_terminals") != EXPECTED_N356_TERMINALS:
        raise ValueError("N356 authoritative remaining-terminal regression")

    fullmod = load_module(N355_FULL, "s32_n357_all178_n355_full")
    engine = load_module(N357_ENGINE, "s32_n357_all178_engine")
    manifest = fullmod.base.load_canonical(MANIFEST, fullmod.base.EXPECTED_MANIFEST_CANONICAL)

    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")
    parsed = [fullmod.base.parse_row_id(row_id) for row_id in rows]
    if not all((d & 1) == 0 for _, d in parsed):
        raise ValueError("N357 all178 census currently requires verified even FULL178 degrees")
    H = max(d // 2 for _, d in parsed)

    # Build the expensive prefix tables once at the maximum retained h.  The
    # N355 interval-query representation is prefix-stable when queried on any
    # smaller h; this is the same acceleration used by the audited N356 replay.
    original_bc = fullmod.build_bc_prefix
    original_lex = fullmod.build_lex_prefix
    bc_pref = original_bc(H)
    lex_pref = original_lex(H)
    fullmod.build_bc_prefix = lambda _h: bc_pref
    fullmod.build_lex_prefix = lambda _h: lex_pref

    groups = defaultdict(list)
    structural_records = 0
    for row_id in rows:
        g, d = fullmod.base.parse_row_id(row_id)
        h = d // 2
        legacy_emin = 8 if g == 0 else 4
        required = fullmod.ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, required)
        emax = (19 * d) // 5
        for e in range(effective_emin, emax + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * fullmod.ceil_div(e, 6):
                continue
            threshold = 4 * h + d - e
            normal_block = 19 * d - 5 * e + 1
            if normal_block <= 0:
                raise ValueError(f"nonpositive normal block {(g,d,e)}")
            groups[(h, threshold)].append((row_id, g, d, e, required, normal_block))
            structural_records += 1

    ordered = sorted(groups.items())
    workers = args.workers or min(4, max(1, os.cpu_count() or 1), max(1, len(ordered)))
    _ENGINE = engine
    _FULLMOD = fullmod
    if workers == 1:
        batches = [_compute_group(item) for item in ordered]
    else:
        ctx = get_context("fork")
        chunksize = max(1, len(ordered) // (workers * 8))
        with ctx.Pool(processes=workers) as pool:
            batches = pool.map(_compute_group, ordered, chunksize=chunksize)

    records = [rec for batch in batches for rec in batch]
    if len(records) != structural_records:
        raise ValueError("N357 stratum record-count regression")

    source_terminals = sum(r["n356_transport_remaining_terminals"] for r in records)
    source_strata = sum(r["n356_transport_remaining_terminals"] > 0 for r in records)
    rejected = sum(r["n357_support_capacity_rejected_terminals"] for r in records)
    remaining = sum(r["n357_support_capacity_remaining_terminals"] for r in records)
    remaining_strata = sum(r["n357_support_capacity_remaining_terminals"] > 0 for r in records)
    affected_strata = sum(r["n357_support_capacity_rejected_terminals"] > 0 for r in records)

    # Hard authority replay gate: the old side of the N357 partition must
    # reconstruct the hostile-audited and already-consumed N356 residual exactly.
    if source_strata != EXPECTED_N356_STRATA:
        raise ValueError(f"N356 source-strata replay regression {source_strata}")
    if source_terminals != EXPECTED_N356_TERMINALS:
        raise ValueError(f"N356 source-terminal replay regression {source_terminals}")
    if rejected <= 0:
        raise ValueError("N357 all178 support-capacity cut is not incrementally strict")
    if source_terminals - rejected != remaining:
        raise ValueError("N357 partition identity regression")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"], r["row_id"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    result = {
        "schema": "STAGE32_32_01_178_N357_ALL178_SUPPORT_SUFFIX_CAPACITY_CENSUS_V1",
        "node_id": "N357",
        "status": "RESEARCH_CANDIDATE_ALL178_N357_NO_MAIN_CREDIT",
        "audited_input": {
            "node": "N356",
            "review_id": EXPECTED_N356_REVIEW,
            "audited_exact_head": EXPECTED_N356_HEAD,
            "remaining_strata": EXPECTED_N356_STRATA,
            "remaining_terminals": EXPECTED_N356_TERMINALS,
        },
        "necessary_condition": "s + min(e-M,Srem) >= K",
        "aggregate": {
            "source_strata_replayed": source_strata,
            "source_terminals_replayed": source_terminals,
            "affected_strata": affected_strata,
            "candidate_incremental_rejected_terminals": rejected,
            "candidate_remaining_strata": remaining_strata,
            "candidate_remaining_terminals": remaining,
            "per_stratum_stream_sha256": stream.hexdigest(),
        },
        "verification": {
            "full178_rows": len(rows),
            "structural_strata_replayed": len(records),
            "n356_authority_replayed_exactly": True,
            "partition_identity": True,
            "max_h": H,
            "workers": workers,
        },
        "semantics": {
            "main_pruning_credit": False,
            "external_hostile_audit_required_before_credit": True,
            "full178_complete": False,
            "n350_producer_registered": False,
            "production_complete": False,
            "n104_release": False,
            "receiver_credit": False,
            "theorem_credit": False,
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
        "verdict": "PASS_N357_ALL178_SUPPORT_SUFFIX_CAPACITY_CANDIDATE",
        "source_strata": source_strata,
        "source_terminals": source_terminals,
        "affected_strata": affected_strata,
        "incremental_rejected_terminals": rejected,
        "remaining_strata": remaining_strata,
        "remaining_terminals": remaining,
        "stream": stream.hexdigest(),
        "canonical": result["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
