#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
import sys
from pathlib import Path

from z3 import unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"

EXPECTED_BLOBS = {
    "hperp_integral_adapter": (RESIDUAL / "hperp_integral_adapter.py", "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"),
    "pairing_prefix_engine": (RESIDUAL / "pairing_prefix_engine.py", "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"),
    "bc2_18_enumerator": (EX5 / "bc2_18_n354_survivor_exceptional_mod8_decomposition.py", "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"),
    "bc2_17_evidence": (EX5 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json", "28c4b762c7f96a4898c62751062648cad066578c"),
    "bc2_18_checkpoint": (EX5 / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json", "0e269d5ec6da24b9b887b6dd40f4b4f33242e154"),
    "bc2_19_checkpoint": (EX5 / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json", "7d75a46a3dc0f54b60b0d70aa2240882b516de59"),
    "retained_picard_bundle": (ROOT / "stages/stage33/33-07/picard_base_rows_retained.py", "82e4d450a1d852e34f6615440fb88a029c6e54eb"),
    "retained_marking": (ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py", "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"),
    "cut102": (HERE / "cut102_finite_ring_direct_completion_v2.py", "fbdd1e65b509526d5198743208bff79bd2488673"),
    "cut191_cover": (HERE / "cut191_bc218_parent_cover_scan.py", "d789e43a2440b4c1b4411e02b3f926b0653d8e8f"),
    "cut102_final": (HERE / "CUT102-final-checkpoint.json", "d7ab957618d366c17b9d68029649de4f6823a9a7"),
    "cut191_closure": (HERE / "CUT191-first-block-closure-checkpoint.json", "a90042ec931cb487ae6be852524db5a4537862f4"),
    "main_state": (ROOT / "stages/stage32/MAIN-STATE.json", "9981889309c833a1834eaadddce73e52c0aa0176"),
}

EXPECTED_CLOSURE_CANONICAL = "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd"
EXPECTED_BC217_CANONICAL = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BC218_EMBEDDED_CANONICAL = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_BC219_CANONICAL = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_PARENT_STREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
EXPECTED_PARENT_COUNT = 7336


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def strict_canonical(path: Path, expected: str) -> dict:
    value = load_json(path)
    if value.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field moved: {path}")
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    if csha(body) != expected:
        raise ValueError(f"canonical replay moved: {path}")
    return value


def assert_repo_import_boundary() -> None:
    def roots(path: Path) -> set[str]:
        tree = ast.parse(path.read_text(), filename=str(path))
        out: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                out.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                out.add(node.module.split(".")[0])
        return out

    hroots = roots(RESIDUAL / "hperp_integral_adapter.py")
    proots = roots(RESIDUAL / "pairing_prefix_engine.py")
    allowed_h = {"__future__", "hashlib", "json", "dataclasses", "sympy", "pairing_prefix_engine"}
    allowed_p = {"__future__", "hashlib", "json", "math", "dataclasses", "typing", "sympy"}
    if hroots - allowed_h:
        raise ValueError(f"new unpinned hperp import boundary: {sorted(hroots - allowed_h)}")
    if proots - allowed_p:
        raise ValueError(f"new unpinned pairing-prefix import boundary: {sorted(proots - allowed_p)}")
    if "pairing_prefix_engine" not in hroots:
        raise ValueError("hperp no longer imports pairing_prefix_engine as expected")


def verify_retained_boundary() -> tuple[dict, dict]:
    closure = strict_canonical(HERE / "CUT191-first-block-closure-checkpoint.json", EXPECTED_CLOSURE_CANONICAL)
    bc217 = strict_canonical(EX5 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json", EXPECTED_BC217_CANONICAL)
    bc218 = load_json(EX5 / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json")
    if bc218.get("canonical_sha256_without_this_field") != EXPECTED_BC218_EMBEDDED_CANONICAL:
        raise ValueError("BC2-18 embedded historical canonical moved")
    strict_canonical(EX5 / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json", EXPECTED_BC219_CANONICAL)

    broad = closure["broad_cover_run"]
    shards = broad["shards"]
    cursor = 0
    residuals: list[int] = []
    totals = {"weak_exact_unsat": 0, "strong_exact_unsat": 0, "mod2_unsat": 0}
    for shard in shards:
        start, end = map(int, shard["range"])
        if start != cursor or end <= start:
            raise ValueError("CUT191 shard partition has a gap/overlap")
        cursor = end
        counts = shard["counts"]
        if sum(int(v) for v in counts.values()) != end - start:
            raise ValueError("CUT191 shard accounting regression")
        for key in totals:
            totals[key] += int(counts[key])
        residuals.extend(int(v) for v in shard["residual_parent_indices"])
    if cursor != EXPECTED_PARENT_COUNT:
        raise ValueError("CUT191 shard partition does not cover 0..7335")
    if totals != {"weak_exact_unsat": 7061, "strong_exact_unsat": 154, "mod2_unsat": 119}:
        raise ValueError(f"CUT191 broad-cover totals moved: {totals}")
    if sorted(residuals) != [1030, 3182]:
        raise ValueError(f"CUT191 residual set moved: {sorted(residuals)}")
    agg = broad["aggregate_counts"]
    if int(agg["covered_parent_count"]) != 7334 or int(agg["residual_parent_count"]) != 2:
        raise ValueError("CUT191 aggregate cover count moved")
    if bool(broad["timeouts_relabelled_unsat"]):
        raise ValueError("timeout-to-UNSAT promotion detected")

    cert = closure["coverage_certificate"]
    if not cert["bc2_18_parent_union_exhaustive"] or int(cert["covered_parent_count"]) != EXPECTED_PARENT_COUNT:
        raise ValueError("CUT191 exhaustive parent-union certificate moved")
    if int(cert["sat_parent_count"]) != 0 or int(cert["unknown_parent_count"]) != 0:
        raise ValueError("CUT191 retained boundary no longer SAT=0/UNKNOWN=0")
    if not cert["whole_bc2_18_parent_union_closed"] or not cert["whole_first_block_picard64_unsat"]:
        raise ValueError("CUT191 closure flags moved")

    retarget = bc217["retarget"]
    if retarget["first_block"] != [0, 112] or int(retarget["first_block_width"]) != 113:
        raise ValueError("BC2-17 first block moved")
    if int(retarget["rank_unrank_replay_count"]) != 113:
        raise ValueError("BC2-17 rank/unrank replay count moved")
    if retarget["replay_stream_sha256"] != "c7ba2038f06494cdcd02c9906ddcdecb938ff82c29eb1af3fce60a5ff79f409c":
        raise ValueError("BC2-17 rank/unrank replay stream moved")
    fixed = {int(k): int(v) for k, v in retarget["fixed_exceptional_pairings"].items()}
    groups = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
    sums = [sum(fixed[label] for label in group) for group in groups]
    if sums != [0, 1, 1] or max(sums) > 4:
        raise ValueError(f"N355 preservation replay moved: {sums}")

    credit = closure["credit"]
    if not credit["stage32_main_pruning_candidate"] or int(credit["stage32_main_pruning_candidate_terminals"]) != 113:
        raise ValueError("CUT191 113-terminal candidate moved")
    if credit["stage32_main_pruning_credit"] or credit["hostile_audit_passed"]:
        raise ValueError("CUT191 self-promotion detected")
    if credit["whole_stratum_closed"] or credit["full178_complete"] or credit["theorem_credit"] or credit["endpoint_credit"]:
        raise ValueError("CUT191 credit ceiling violated")

    main = strict_canonical(ROOT / "stages/stage32/MAIN-STATE.json", "6143a95a0fb380e3c30c6a464722b350666cec5f018318adefdae15800a676b3")
    frontier = main["current_exact_frontier"]
    if not frontier["n355_main_pruning_credit"] or frontier["n356_main_pruning_credit"]:
        raise ValueError("MAIN N355/N356 authority boundary moved")
    if int(frontier["n355_remaining_terminals"]) != 66462870551188628549910:
        raise ValueError("MAIN retained terminal authority moved")
    if int(closure["population_preimage"]["candidate_remaining_terminals_if_consumed"]) != int(frontier["n355_remaining_terminals"]) - 113:
        raise ValueError("CUT191 candidate terminal subtraction regression")
    if closure["population_preimage"]["n356_applied"]:
        raise ValueError("CUT191 silently applied N356")
    return closure, bc217


def fresh_residual_replay() -> dict:
    sys.path.insert(0, str(HERE))
    import cut102_finite_ring_direct_completion_v2 as cut102
    import cut191_bc218_parent_cover_scan as cover

    P, blocks, exceptional_labels, parents, fixed = cut102.load_interface()
    if len(parents) != EXPECTED_PARENT_COUNT or cut102.EXPECTED_STREAM != EXPECTED_PARENT_STREAM:
        raise ValueError("BC2-18 exact parent stream replay moved")

    yE1030, _ = parents[1030]
    branch_results = []
    for degree in range(9):
        s, y, n1, _meta = cut102.make_solver(P, blocks, fixed, 2, 30000)
        for label, value in zip(exceptional_labels, yE1030):
            s.add(y[label - 1] == int(value))
        s.add(n1 == degree)
        r = s.check()
        branch_results.append(str(r))
        if r != unsat:
            raise ValueError(f"parent 1030 n1={degree} exact-head mod2 replay not UNSAT: {r}; reason={s.reason_unknown()}")

    yE3182, _ = parents[3182]
    weak, weak_p = cover.make_exact_solver(P, blocks, fixed, False, 30000)
    r3182, reason3182 = cover.check_parent(weak, weak_p, exceptional_labels, yE3182)
    if r3182 != unsat:
        raise ValueError(f"parent 3182 exact-head weak replay not UNSAT: {r3182}; reason={reason3182}")

    return {
        "parent_1030_n1_branches": branch_results,
        "parent_3182_weak_exact": str(r3182),
        "bc2_18_parent_count": len(parents),
    }


def main() -> None:
    observed = {}
    for name, (path, expected) in EXPECTED_BLOBS.items():
        actual = git_blob_sha(path)
        observed[name] = actual
        if actual != expected:
            raise ValueError(f"source lock moved for {name}: expected {expected}, got {actual}")
    assert_repo_import_boundary()
    verify_retained_boundary()
    replay = fresh_residual_replay()
    print(json.dumps({
        "status": "PASS_CUT191_EXACT_HEAD_AUDIT_VERIFIER",
        "transitive_executable_source_locks": {
            "hperp_integral_adapter.py": observed["hperp_integral_adapter"],
            "pairing_prefix_engine.py": observed["pairing_prefix_engine"],
        },
        "fresh_replay": replay,
        "stage32_main_pruning_credit": False,
        "candidate_terminals": 113,
        "n356_consumed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
