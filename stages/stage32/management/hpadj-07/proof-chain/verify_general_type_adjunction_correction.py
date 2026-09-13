#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESULT = HERE / "GENERAL-TYPE-ADJUNCTION-CORRECTION.json"
SURFACE = ROOT / "stages/stage32/final-chain/32-02-effectivity/SURFACE-INVARIANT-SOURCE-LOCK.json"
STAGE29 = ROOT / "stages/stage29/29-02c-LG2/result.md"
HPADJ01 = ROOT / "stages/stage32/management/hpadj-01/verify_hpadj01_current_v22_lower_bound.py"
N358_REL = Path("stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py")
N358_AUDITED_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
N358_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"

LOCKS = {
    SURFACE: "07b7fae35a23f403898d33e5dc75baa24f631dcf",
    STAGE29: "820ed4e1b1a53db14085678de6f186b59ae0ea48",
    HPADJ01: "b0253975ddf28c99b9d9898f54ada9a6842b2386",
}
EXPECTED_CANON = "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa"
EXPECTED_ROWS = 165
EXPECTED_PREFIX = 15196542371901641344
EXPECTED_TERMS = 20713268924714183714810
EXPECTED_G0 = 4629288543122194904265
EXPECTED_G1 = 16083980381591988810545
EXPECTED_OVERCOUNT = 6391052402591515560677
EXPECTED_STREAM = "3bf1ab5cb3c46f42ab2c6178936cd965bd635823cfb54d2d82b24fee541ee27a"
OLD_INVALID_TERMS = 27104321327305699275487


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def exact_checkout_head(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.STDOUT,
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("FAIL: cannot resolve audited N358 checkout head: " + exc.output.strip()) from exc


def even_interval_normal_sum(d: int, lower: int, upper: int, excluded: set[int]) -> tuple[int, int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return 0, 0
    n = (hi - lo) // 2 + 1
    total_e = n * (lo + hi) // 2
    total = n * (19 * d + 1) - 5 * total_e
    count = n
    for e in sorted(excluded):
        if lo <= e <= hi and e % 2 == 0:
            total -= 19 * d - 5 * e + 1
            count -= 1
    return count, total


def replay(n358) -> dict:
    BC = n358.build_bc_exact(n358.HMAX)
    req(n358.n357_count_witness(BC) == n358.EXPECTED_N357_WITNESS, "N357 semantic witness drift")
    total_prefix = 0
    total_terms = 0
    by_g = {0: 0, 1: 0}
    affected_rows = 0
    per_row = []

    for g in (0, 1):
        dmax = 176 if g == 0 else 192
        for d in range(8, dmax + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = n358.ceil_div(d - 16 * g + 16, 4)
            row_prefix = 0
            row_terms = 0
            A = [[n358.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
            threshold = 3 * d * d + 48 * d + 96 - 96 * g

            for b in range(h + 1):
                for c in range(h + 1):
                    bcv = BC[b][c]
                    if not any(bcv):
                        continue
                    c3 = n358.component3(d, b, c)
                    if c3 < 0:
                        continue
                    for a in range(h + 1):
                        avec = A[a]
                        if not any(avec):
                            continue
                        if 8 * a * a + 8 * b * b + 6 * c * c <= threshold:
                            continue
                        M = a + b + c
                        ca = n358.component_a(d, a)
                        if ca < 0:
                            continue
                        srem = min(16, d) + ca + c3
                        scount = [0] * 11
                        for sbc, left in enumerate(bcv):
                            if not left:
                                continue
                            for sa, right in enumerate(avec):
                                if right:
                                    scount[sbc + sa] += left * right
                        for support, count in enumerate(scount):
                            if not count:
                                continue
                            qneed = K - support
                            if qneed > 0 and srem < qneed:
                                continue
                            lower = max(legacy, K, d - 4 * g + 4, M, M + max(0, qneed))
                            upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                            if lower > upper:
                                continue
                            excluded: set[int] = set()
                            e_n358 = 3 * d - (b - c)
                            if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                excluded.add(e_n358)
                            if g == 1 and d == 8:
                                excluded.add(8)
                            ne, normal_sum = even_interval_normal_sum(d, lower, upper, excluded)
                            if ne <= 0:
                                continue
                            row_prefix += count * ne
                            row_terms += count * normal_sum

            if row_terms:
                affected_rows += 1
            total_prefix += row_prefix
            total_terms += row_terms
            by_g[g] += row_terms
            per_row.append({"g": g, "d": d, "candidate_hodge_endpoint_terms": row_terms})

    stream = hashlib.sha256()
    for rec in sorted(per_row, key=lambda r: (r["g"], r["d"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return {
        "affected_rows_with_nonzero_rejection": affected_rows,
        "exceptional_prefix_stratum_instances": total_prefix,
        "candidate_rejected_terminals_lower_bound": total_terms,
        "genus0_candidate_rejected_terminals": by_g[0],
        "genus1_candidate_rejected_terminals": by_g[1],
        "invalid_overcount_removed": OLD_INVALID_TERMS - total_terms,
        "per_row_stream_sha256": stream.hexdigest(),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-n358-root", required=True, type=Path)
    args = ap.parse_args()

    for path, expected in LOCKS.items():
        req(path.is_file(), f"missing source {path}")
        req(git_blob(path) == expected, f"source-lock drift {path}")

    audited_n358_root = args.audited_n358_root.resolve()
    req(audited_n358_root.is_dir(), "missing hostile-audited N358 checkout")
    req(exact_checkout_head(audited_n358_root) == N358_AUDITED_HEAD, "hostile-audited N358 exact head drift")
    n358_path = audited_n358_root / N358_REL
    req(n358_path.is_file(), f"missing hostile-audited N358 replay source {N358_REL}")
    req(git_blob(n358_path) == N358_BLOB, "hostile-audited N358 replay source blob drift")

    surface = json.loads(SURFACE.read_text(encoding="utf-8"))
    inv = surface["surface_invariants"]
    req(inv["K_square"] == 16 and inv["p_g"] == 7 and inv["q"] == 0 and inv["chi_O"] == 8,
        "cuboid surface invariant drift")
    req(surface["applicability"]["stage32_target_degree_semantics"] == "degree=K.C", "degree semantics drift")

    stage29 = STAGE29.read_text(encoding="utf-8")
    for needle in ("C^2 + d = 2 p_a(C) - 2", "C^2 >= -d-2", "C^2 >= -d"):
        req(needle in stage29, f"Stage29 adjunction source drift: {needle}")

    result = json.loads(RESULT.read_text(encoding="utf-8"))
    req(result.get("canonical_sha256_without_this_field") == EXPECTED_CANON, "stored result canonical")
    req(canon(result) == EXPECTED_CANON, "result canonical")
    req(result["status"].startswith("PREDECESSOR_HPADJ_ADJUNCTION_INVALID"), "correction status")
    req(result["firewalls"]["main_pruning_credit"] is False, "premature pruning credit")

    n358 = load_module(n358_path, "stage32_hpadj07_n358")
    got = replay(n358)
    expected = result["corrected_v22_conservative_replay"]
    for key, value in got.items():
        req(expected[key] == value, f"corrected replay drift {key}: {value}")
    req(got["affected_rows_with_nonzero_rejection"] == EXPECTED_ROWS, "affected-row count")
    req(got["exceptional_prefix_stratum_instances"] == EXPECTED_PREFIX, "prefix count")
    req(got["candidate_rejected_terminals_lower_bound"] == EXPECTED_TERMS, "terminal count")
    req(got["genus0_candidate_rejected_terminals"] == EXPECTED_G0, "g0 subtotal")
    req(got["genus1_candidate_rejected_terminals"] == EXPECTED_G1, "g1 subtotal")
    req(got["invalid_overcount_removed"] == EXPECTED_OVERCOUNT, "old invalid overcount")
    req(got["per_row_stream_sha256"] == EXPECTED_STREAM, "row stream")

    print(json.dumps({
        "verdict": "PASS_HPADJ07_GENERAL_TYPE_ADJUNCTION_CORRECTION_CANDIDATE",
        **got,
        "audited_n358_head": N358_AUDITED_HEAD,
        "main_pruning_credit": False,
        "hostile_audit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
