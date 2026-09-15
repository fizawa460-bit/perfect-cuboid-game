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
ROOT = HERE.parents[3]
HPADJ07 = ROOT / "management/hpadj-07/proof-chain/verify_general_type_adjunction_correction.py"
N358_REL = Path("stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py")
N358_AUDITED_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
N358_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"
HPADJ07_BLOB = "e3efa7c27c1cb37324d588bac270d53f2b21620f"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def exact_head(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.STDOUT,
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("FAIL: cannot resolve audited N358 checkout head: " + exc.output.strip()) from exc


def min_integer_square_sum(total: int, slots: int) -> int:
    q, r = divmod(int(total), int(slots))
    return (slots - r) * q * q + r * (q + 1) * (q + 1)


def old_scaled24(a: int, b: int, c: int) -> int:
    return 8 * a * a + 8 * b * b + 6 * c * c


def new_scaled24(a: int, b: int, c: int) -> int:
    return 24 * (
        min_integer_square_sum(a, 3)
        + min_integer_square_sum(b, 3)
        + min_integer_square_sum(c, 4)
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-n358-root", required=True, type=Path)
    args = ap.parse_args()

    req(HPADJ07.is_file(), "missing HPADJ07 verifier")
    req(git_blob(HPADJ07) == HPADJ07_BLOB, "HPADJ07 verifier source-lock drift")
    h7 = load_module(HPADJ07, "stage32_hpadj08_cut_h7")

    audited = args.audited_n358_root.resolve()
    req(audited.is_dir(), "missing audited N358 checkout")
    req(exact_head(audited) == N358_AUDITED_HEAD, "audited N358 exact head drift")
    n358_path = audited / N358_REL
    req(n358_path.is_file(), "missing audited N358 replay source")
    req(git_blob(n358_path) == N358_BLOB, "audited N358 blob drift")
    n358 = load_module(n358_path, "stage32_hpadj08_cut_n358")

    BC = n358.build_bc_exact(n358.HMAX)
    req(n358.n357_count_witness(BC) == n358.EXPECTED_N357_WITNESS, "N357 semantic witness drift")

    old_total = 0
    new_total = 0
    incremental = 0
    old_prefix = 0
    new_prefix = 0
    incremental_prefix = 0
    affected_incremental_rows = 0
    row_stream = hashlib.sha256()

    for g in (0, 1):
        dmax = 176 if g == 0 else 192
        for d in range(8, dmax + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = n358.ceil_div(d - 16 * g + 16, 4)
            threshold = 3 * d * d + 48 * d + 96 - 96 * g
            A = [[n358.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
            row_old = row_new = row_inc = 0
            row_old_prefix = row_new_prefix = row_inc_prefix = 0

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
                        old_reject = old_scaled24(a, b, c) > threshold
                        new_reject = new_scaled24(a, b, c) > threshold
                        if not new_reject:
                            continue
                        req(not old_reject or new_reject, "monotonicity regression")
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
                            ne, normal_sum = h7.even_interval_normal_sum(d, lower, upper, excluded)
                            if ne <= 0:
                                continue
                            row_new_prefix += count * ne
                            row_new += count * normal_sum
                            if old_reject:
                                row_old_prefix += count * ne
                                row_old += count * normal_sum
                            else:
                                row_inc_prefix += count * ne
                                row_inc += count * normal_sum

            if row_inc:
                affected_incremental_rows += 1
            old_total += row_old
            new_total += row_new
            incremental += row_inc
            old_prefix += row_old_prefix
            new_prefix += row_new_prefix
            incremental_prefix += row_inc_prefix
            row_stream.update(json.dumps({
                "g": g,
                "d": d,
                "old_terms": row_old,
                "new_terms": row_new,
                "incremental_terms": row_inc,
            }, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(old_total == h7.EXPECTED_TERMS, f"HPADJ07 replay drift: {old_total} != {h7.EXPECTED_TERMS}")
    req(new_total == old_total + incremental, "increment accounting drift")
    req(new_prefix == old_prefix + incremental_prefix, "prefix increment accounting drift")

    print(json.dumps({
        "status": "PASS_HPADJ08_CUT_H8C01_POPULATION_REPLAY_CANDIDATE",
        "hpadj07_rejected_terminals": old_total,
        "hpadj08_cut_integer_min_rejected_terminals": new_total,
        "incremental_candidate_rejected_terminals": incremental,
        "hpadj07_rejected_prefix_instances": old_prefix,
        "hpadj08_cut_integer_min_rejected_prefix_instances": new_prefix,
        "incremental_candidate_prefix_instances": incremental_prefix,
        "affected_incremental_rows": affected_incremental_rows,
        "row_stream_sha256": row_stream.hexdigest(),
        "main_pruning_credit": False,
        "hostile_audit_required": True,
        "overlap_accounting_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
