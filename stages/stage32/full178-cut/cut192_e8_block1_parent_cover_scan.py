#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from sympy import Matrix
from z3 import get_version_string, sat, unknown, unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

import cut102_finite_ring_direct_completion_v2 as cut102
import cut191_bc218_parent_cover_scan as cut191scan

SCHEMA = "STAGE32_FULL178_CUT192_E8_BLOCK1_PARENT_COVER_SCAN_V1"
HANDOFF = HERE / "CUT192-EX5-E8-HANDOFF.json"
EXPECTED_HANDOFF_BLOB = "011fe82cd97bfa192d4efbbafacb21b0ea724b44"
EXPECTED_HANDOFF_CANONICAL = "41405165f081554bf3089c0cb15f568d8515fe81202cf6c809914c9490479d1c"
EXPECTED_CUT102_BLOB = "fbdd1e65b509526d5198743208bff79bd2488673"
EXPECTED_CUT191_SCAN_BLOB = "d789e43a2440b4c1b4411e02b3f926b0653d8e8f"
EXPECTED_EX5_HEAD = "fd00531181228c9f367a49eb61ddc3af6ab84ab3"
EXPECTED_EX5_ADAPTER_BLOB = "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f"
EXPECTED_EX5_PREFLIGHT_BLOB = "b28539d9d0eafddc181d3bbf6d668261f2ff081e"
EXPECTED_EX5_VERIFIER_BLOB = "8fe802444ca8c92a80058555eaf431f0c1a52c76"
EXPECTED_PARENT_COUNT = 2360
EXPECTED_PARENT_STREAM = "4977be767465c69616288b54bc79e491b3f8ee29c94162ce089a6258b6fc00e0"
EXPECTED_FIXED = {93: 0, 94: 0, 95: 0, 96: 1, 97: 0, 98: 0, 99: 1, 101: 1, 102: 0, 103: 0}


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def load_json_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected and csha(body) == expected, f"canonical drift: {path}")
    return obj


def git_head(root: Path) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


def import_ex5_adapter(ex5_root: Path):
    adapter_path = ex5_root / "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py"
    preflight = ex5_root / "stages/stage32-ex5/cut-handoff/e8-terminal-population-preflight.json"
    verifier = ex5_root / "stages/stage32-ex5/cut-handoff/verify_e8_terminal_population_adapter.py"
    req(git_head(ex5_root) == EXPECTED_EX5_HEAD, "EX5 exact checkout head drift")
    req(blob(adapter_path) == EXPECTED_EX5_ADAPTER_BLOB, "EX5 adapter blob drift")
    req(blob(preflight) == EXPECTED_EX5_PREFLIGHT_BLOB, "EX5 preflight blob drift")
    req(blob(verifier) == EXPECTED_EX5_VERIFIER_BLOB, "EX5 adapter verifier blob drift")
    spec = importlib.util.spec_from_file_location("stage32ex5_e8_exact_adapter_fd005311", adapter_path)
    req(spec is not None and spec.loader is not None, "cannot import exact EX5 adapter")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_cut_geometry_from_exact_ex5(adapter_mod):
    # Use the exact producer's retained Picard dependency boundary, but build only
    # the CUT solver geometry. This avoids rebuilding terminal-to-Picard semantics.
    d18 = adapter_mod.d18
    bundle = d18.load_retained(d18.RETAINED, "s32cut192_block1_bundle")
    marking = d18.load_retained(d18.MARKING, "s32cut192_block1_marking")
    req(bundle.get("canonical_sha256") == d18.EXPECTED_BUNDLE_CANONICAL, "retained Picard bundle canonical drift")
    req(marking.get("canonical_sha256") == d18.EXPECTED_MARKING_CANONICAL, "retained Picard marking canonical drift")
    pic = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(pic.pairing_matrix)
    coords = Matrix(pic.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    req(P.shape == (140, 64) and coords.shape == (140, 64) and gram.shape == (64, 64), "Picard matrix shape drift")
    full = coords * gram * coords.T
    blocks = []
    fibre_coeffs = []
    for factor_index, pack in enumerate(cut102.PACKS, start=1):
        seen = []
        factor_blocks = []
        funcs = []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            req(len(inc) == 8, f"incidence regression boundary {boundary}")
            seen.extend(inc)
            factor_blocks.append(inc)
            funcs.append(2 * P.row(boundary - 1) + cut102.row_sum(P, inc))
        req(sorted(seen) == list(range(93, 141)), f"factor partition regression {factor_index}")
        req(all(f == funcs[0] for f in funcs[1:]), f"fibre functional regression {factor_index}")
        blocks.append(factor_blocks)
        fibre_coeffs.append(funcs[0])
    req(19 * (fibre_coeffs[0] + fibre_coeffs[1]) == cut102.row_sum(P, list(range(1, 93))) + 5 * cut102.row_sum(P, list(range(93, 141))), "degree-sum functional regression")
    return P, blocks


def parent_stream(adapter_mod):
    geometry = adapter_mod.load_geometry()
    records = list(adapter_mod.iter_parent_population(1, geometry))
    req(len(records) == EXPECTED_PARENT_COUNT, f"block1 HNF parent count drift: {len(records)}")
    h = hashlib.sha256()
    for rec in records:
        adapter_mod.stream_update(h, rec)
    req(h.hexdigest() == EXPECTED_PARENT_STREAM, "block1 HNF parent stream drift")
    return geometry, records


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ex5-root", type=Path, required=True)
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--end", type=int, required=True)
    ap.add_argument("--weak-timeout-ms", type=int, default=300)
    ap.add_argument("--strong-timeout-ms", type=int, default=600)
    ap.add_argument("--mod2-timeout-ms", type=int, default=500)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    req(0 <= args.start < args.end <= EXPECTED_PARENT_COUNT, "invalid HNF parent range")
    req(min(args.weak_timeout_ms, args.strong_timeout_ms, args.mod2_timeout_ms) > 0, "timeouts must be positive")
    req(blob(HANDOFF) == EXPECTED_HANDOFF_BLOB, "CUT192 handoff receipt blob drift")
    req(blob(Path(cut102.__file__).resolve()) == EXPECTED_CUT102_BLOB, "CUT102 implementation drift")
    req(blob(Path(cut191scan.__file__).resolve()) == EXPECTED_CUT191_SCAN_BLOB, "CUT191 cover implementation drift")
    handoff = load_json_canonical(HANDOFF, EXPECTED_HANDOFF_CANONICAL)
    req(handoff["first_disjoint_block"]["hnf_feasible_parent_count"] == EXPECTED_PARENT_COUNT, "handoff HNF parent count drift")
    req(handoff["first_disjoint_block"]["hnf_parent_stream_sha256"] == EXPECTED_PARENT_STREAM, "handoff parent stream drift")

    ex5_root = args.ex5_root.resolve()
    adapter_mod = import_ex5_adapter(ex5_root)
    geometry, parents = parent_stream(adapter_mod)
    fixed = {int(k): int(v) for k, v in handoff["first_disjoint_block"]["fixed_exceptional_pairings"].items()}
    req(fixed == EXPECTED_FIXED, "block1 terminal fixed signature drift")
    exceptional_labels = [int(v) for v in geometry.exceptional_labels]
    P, blocks = load_cut_geometry_from_exact_ex5(adapter_mod)

    weak, weak_p = cut191scan.make_exact_solver(P, blocks, fixed, False, args.weak_timeout_ms)
    strong, strong_p = cut191scan.make_exact_solver(P, blocks, fixed, True, args.strong_timeout_ms)
    mod2, mod2_y, _n1, mod2_meta = cut102.make_solver(P, blocks, fixed, 2, args.mod2_timeout_ms)

    counts = {
        "weak_exact_unsat": 0,
        "strong_exact_unsat": 0,
        "mod2_unsat": 0,
        "residual_strong_sat": 0,
        "residual_mod2_sat": 0,
        "residual_unknown": 0,
    }
    residual = []
    status_stream = hashlib.sha256()
    for parent_index in range(args.start, args.end):
        rec = parents[parent_index]
        yE = [int(v) for v in rec["selected_exceptional_pairings"]]
        wr, wreason = cut191scan.check_parent(weak, weak_p, exceptional_labels, yE)
        if wr == unsat:
            counts["weak_exact_unsat"] += 1
            status_stream.update(f"{parent_index}:WEAK_EXACT_UNSAT\n".encode())
            continue
        sr, sreason = cut191scan.check_parent(strong, strong_p, exceptional_labels, yE)
        if sr == unsat:
            counts["strong_exact_unsat"] += 1
            status_stream.update(f"{parent_index}:STRONG_EXACT_UNSAT\n".encode())
            continue
        mod2.push()
        for label, value in zip(exceptional_labels, yE):
            mod2.add(mod2_y[label - 1] == value)
        mr = mod2.check()
        mreason = mod2.reason_unknown() if mr == unknown else None
        mod2.pop()
        if mr == unsat:
            counts["mod2_unsat"] += 1
            status_stream.update(f"{parent_index}:MOD2_UNSAT\n".encode())
            continue
        if sr == sat:
            kind = "residual_strong_sat"
        elif mr == sat:
            kind = "residual_mod2_sat"
        else:
            kind = "residual_unknown"
        counts[kind] += 1
        rr = {
            "parent_index": parent_index,
            "selected_residual_mass": int(rec["selected_residual_mass"]),
            "x4_allowed_residues_mod8": [int(v) for v in rec["x4_allowed_residues_mod8"]],
            "weak_exact": str(wr),
            "strong_exact": str(sr),
            "mod2": str(mr),
        }
        if wreason is not None:
            rr["weak_reason_unknown"] = wreason
        if sreason is not None:
            rr["strong_reason_unknown"] = sreason
        if mreason is not None:
            rr["mod2_reason_unknown"] = mreason
        residual.append(rr)
        status_stream.update(f"{parent_index}:RESIDUAL:{str(wr)}:{str(sr)}:{str(mr)}\n".encode())

    checked = args.end - args.start
    covered = counts["weak_exact_unsat"] + counts["strong_exact_unsat"] + counts["mod2_unsat"]
    req(covered + len(residual) == checked, "coverage accounting drift")
    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT192",
        "status": "PASS_SHARD_ALL_HNF_PARENTS_OBSTRUCTED" if not residual else "BLOCKED_SHARD_RESIDUAL_REMAINS",
        "source_locks": {
            "cut192_ex5_handoff_blob": EXPECTED_HANDOFF_BLOB,
            "cut192_ex5_handoff_canonical": EXPECTED_HANDOFF_CANONICAL,
            "ex5_exact_head": EXPECTED_EX5_HEAD,
            "ex5_adapter_blob": EXPECTED_EX5_ADAPTER_BLOB,
            "ex5_preflight_blob": EXPECTED_EX5_PREFLIGHT_BLOB,
            "ex5_verifier_blob": EXPECTED_EX5_VERIFIER_BLOB,
            "block1_hnf_parent_stream_sha256": EXPECTED_PARENT_STREAM,
            "cut102_implementation_blob": EXPECTED_CUT102_BLOB,
            "cut191_cover_implementation_blob": EXPECTED_CUT191_SCAN_BLOB,
            "coarse_block_screen_exact_head": "05daa3633b711f37d59dc14ae044404598106d8a",
            "coarse_block_screen_ci_run": 34604199491,
            "coarse_block_screen_canonical": "65082083a60b42780ae260a1a3464477881fcdb1496ceffb3bfc8e0c8c67a767",
            "coarse_block_screen_status": "BOUNDED_BLOCK1_FINITE_RING_SCREEN_NONEXCLUDING_NO_PRUNING_CREDIT",
        },
        "scope": {
            "block_index": 1,
            "terminal_rank_range": [113, 225],
            "terminal_count": 113,
            "hnf_parent_count": EXPECTED_PARENT_COUNT,
            "parent_index_start_inclusive": args.start,
            "parent_index_end_exclusive": args.end,
            "parents_checked": checked,
            "parent_semantics": "source-locked EX5 exact HNF-integrality-feasible selected-exceptional completions for the disjoint current-MAIN-surviving e8 block1",
        },
        "solver": {
            "z3_version": get_version_string(),
            "weak_timeout_ms": args.weak_timeout_ms,
            "strong_timeout_ms": args.strong_timeout_ms,
            "mod2_timeout_ms": args.mod2_timeout_ms,
            "mod2_rank": mod2_meta["rank_mod_p"],
            "mod2_left_kernel_dimension": mod2_meta["left_kernel_dimension"],
        },
        "methods": {
            "weak_exact": "exact Picard64 integer image plus all140 nonnegative/mass and source-locked block1 selected-exceptional parent pairings",
            "strong_exact": "weak exact plus fibre, n1+n2=8, exceptional diagonal and cross-factor block-sum necessary constraints",
            "mod2": "CUT102 left-kernel mod2 necessary image relaxation with the same strong bounded constraints",
            "soundness": "Only UNSAT covers a parent. SAT/UNKNOWN remains residual; no timeout is promoted.",
        },
        "result": {
            "counts": counts,
            "covered_parent_count": covered,
            "residual_parent_count": len(residual),
            "residual_records": residual,
            "status_stream_sha256": status_stream.hexdigest(),
        },
        "credit": {
            "shard_parent_cover_complete": not residual,
            "whole_block_parent_union_closed": args.start == 0 and args.end == EXPECTED_PARENT_COUNT and not residual,
            "cut192_pruning_candidate_terminals": 113 if args.start == 0 and args.end == EXPECTED_PARENT_COUNT and not residual else 0,
            "stage32_main_pruning_credit": False,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "firewalls": {
            "ex5_adapter_rebuilt_by_cut": False,
            "producer_exact_checkout_consumed_read_only": True,
            "sat_promoted_to_exact_feasibility": False,
            "unknown_promoted_to_unsat": False,
            "n357_duplicated": False,
            "main_authority_mutated": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": body["status"],
        "start": args.start,
        "end": args.end,
        "covered": covered,
        "residual": len(residual),
        "counts": counts,
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
