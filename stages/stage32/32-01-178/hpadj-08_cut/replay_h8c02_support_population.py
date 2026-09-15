#!/usr/bin/env python3
from __future__ import annotations

import argparse
import functools
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
HPADJ07 = REPO / "stages/stage32/management/hpadj-07/proof-chain/verify_general_type_adjunction_correction.py"
N358_REL = Path("stages/stage32/32-01-178/nodes/N358/verify_n358_exact_incremental_census.py")
N358_AUDITED_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
N358_BLOB = "c07a7e358a6253919194189377d6ed56f95e047a"
HPADJ07_BLOB = "e3efa7c27c1cb37324d588bac270d53f2b21620f"
EXPECTED_OLD = 20713268924714183714810
EXPECTED_NEW = 22291592385308320124345
EXPECTED_INCREMENT = 1578323460594136409535
EXPECTED_ROWS = 178
EXPECTED_STREAM = "6ab0ab20dc346bd704c6d3421f0301aeadeb3598d9d7b93e446586f646741a92"


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
        return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("FAIL: cannot resolve audited N358 checkout head: " + exc.output.strip()) from exc


def min_integer_square_sum(total: int, slots: int) -> int:
    q, r = divmod(int(total), int(slots))
    return (slots - r) * q * q + r * (q + 1) * (q + 1)


def h8c01_scaled24(a: int, b: int, c: int) -> int:
    return 24 * (min_integer_square_sum(a, 3) + min_integer_square_sum(b, 3) + min_integer_square_sum(c, 4))


@functools.lru_cache(maxsize=None)
def min_square_given_support(total: int, slots: int, support: int):
    total = int(total); slots = int(slots); support = int(support)
    if support < 0 or support > slots:
        return None
    if support == 0:
        return 0 if total == 0 else None
    if total < support:
        return None
    q, r = divmod(total, support)
    return (support - r) * q * q + r * (q + 1) * (q + 1)


@functools.lru_cache(maxsize=None)
def min_square_total_support_groups(a: int, b: int, c: int, support: int):
    best = None
    for sa in range(4):
        ma = min_square_given_support(a, 3, sa)
        if ma is None:
            continue
        for sb in range(4):
            sc = support - sa - sb
            if not 0 <= sc <= 4:
                continue
            mb = min_square_given_support(b, 3, sb)
            mc = min_square_given_support(c, 4, sc)
            if mb is None or mc is None:
                continue
            value = ma + mb + mc
            if best is None or value < best:
                best = value
    return best


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-n358-root", required=True, type=Path)
    args = ap.parse_args()

    req(HPADJ07.is_file(), "missing HPADJ07 verifier")
    req(git_blob(HPADJ07) == HPADJ07_BLOB, "HPADJ07 verifier source-lock drift")
    h7 = load_module(HPADJ07, "stage32_hpadj08_cut_h7_support")

    audited = args.audited_n358_root.resolve()
    req(audited.is_dir(), "missing audited N358 checkout")
    req(exact_head(audited) == N358_AUDITED_HEAD, "audited N358 exact head drift")
    n358_path = audited / N358_REL
    req(n358_path.is_file(), "missing audited N358 replay source")
    req(git_blob(n358_path) == N358_BLOB, "audited N358 blob drift")
    n358 = load_module(n358_path, "stage32_hpadj08_cut_n358_support")

    BC = n358.build_bc_exact(n358.HMAX)
    req(n358.n357_count_witness(BC) == n358.EXPECTED_N357_WITNESS, "N357 semantic witness drift")

    old_total = new_total = 0
    affected_rows = 0
    row_stream = hashlib.sha256()

    for g in (0, 1):
        dmax = 176 if g == 0 else 192
        for d in range(8, dmax + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = n358.ceil_div(d - 16 * g + 16, 4)
            threshold = 3 * d * d + 48 * d + 96 - 96 * g
            A = [[n358.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
            row_old = row_new = 0

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
                        old_reject = 8 * a * a + 8 * b * b + 6 * c * c > threshold
                        h8c01_reject = h8c01_scaled24(a, b, c) > threshold

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
                            excluded = set()
                            e_n358 = 3 * d - (b - c)
                            if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                excluded.add(e_n358)
                            if g == 1 and d == 8:
                                excluded.add(8)
                            ne, normal_sum = h7.even_interval_normal_sum(d, lower, upper, excluded)
                            if ne <= 0:
                                continue
                            if old_reject:
                                row_old += count * normal_sum
                            sq = min_square_total_support_groups(a, b, c, support)
                            req(sq is not None, "support/mass feasibility drift")
                            h8c02_reject = 24 * sq > threshold
                            req(not old_reject or h8c02_reject, "HPADJ07 monotonicity regression")
                            req(not h8c01_reject or h8c02_reject, "H8C01 monotonicity regression")
                            if h8c02_reject:
                                row_new += count * normal_sum

            inc = row_new - row_old
            if inc:
                affected_rows += 1
            old_total += row_old
            new_total += row_new
            row_stream.update(json.dumps({
                "g": g,
                "d": d,
                "old_terms": row_old,
                "h8c02_terms": row_new,
                "incremental_vs_hpadj07": inc,
            }, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    increment = new_total - old_total
    req(old_total == EXPECTED_OLD == h7.EXPECTED_TERMS, "HPADJ07 replay drift")
    req(new_total == EXPECTED_NEW, "H8C02 total drift")
    req(increment == EXPECTED_INCREMENT, "H8C02 increment drift")
    req(affected_rows == EXPECTED_ROWS, "H8C02 affected-row drift")
    req(row_stream.hexdigest() == EXPECTED_STREAM, "H8C02 row stream drift")

    print(json.dumps({
        "status": "PASS_HPADJ08_CUT_H8C02_SUPPORT_POPULATION_REPLAY_CANDIDATE",
        "hpadj07_rejected_terminals": old_total,
        "h8c02_rejected_terminals": new_total,
        "incremental_candidate_rejected_terminals": increment,
        "affected_incremental_rows": affected_rows,
        "row_stream_sha256": row_stream.hexdigest(),
        "main_pruning_credit": False,
        "hostile_audit_required": True,
        "overlap_accounting_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
