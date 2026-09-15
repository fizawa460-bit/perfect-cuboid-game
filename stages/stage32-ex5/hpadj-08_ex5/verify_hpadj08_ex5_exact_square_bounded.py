#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFLIGHT = HERE / "HPADJ08-EX5-EXACT-SQUARE-PREFLIGHT.json"
PREFLIGHT_CANON = "9867898a32d34f470ec421fef560527dcbcc5579453a0dab8454553a142cf953"
LOCKS = {
    "compressed_family": ("stages/stage32/residual-32-01-production/compressed_terminal_family.py", "90ff82ed312dcc0cb32cf207935945f550e29170"),
    "prefix_checkpoint": ("stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json", "eb823cc2f99d74456d5701b4673f848f18ba3151"),
    "corrected_adjunction": ("stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json", "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e"),
    "hpadj_v22_replay": ("stages/stage32/management/hpadj-01/verify_hpadj01_current_v22_lower_bound.py", "b0253975ddf28c99b9d9898f54ada9a6842b2386"),
}
MAX_D = 32
H = 16
EXPECTED_OLD = 3257761571005
EXPECTED_EXACT = 25770706503487
EXPECTED_INCREMENTAL = 22512944932482
EXPECTED_STREAM = "8c416e9424439780202522a5cba88f19b2681ba1352e0e0470498922cfcd40ac"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def even_interval_normal_sum(d: int, lower: int, upper: int, excluded: set[int]) -> tuple[int, int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return 0, 0
    n = (hi - lo) // 2 + 1
    total = n * (19 * d + 1) - 5 * (n * (lo + hi) // 2)
    count = n
    for e in sorted(excluded):
        if lo <= e <= hi and e % 2 == 0:
            total -= 19 * d - 5 * e + 1
            count -= 1
    return count, total


def build_a_q(H: int):
    A = [[defaultdict(int) for _ in range(4)] for __ in range(H + 1)]
    for a in range(H + 1):
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                s = sum(v > 0 for v in (x2, x3, x7))
                A[a][s][x2*x2 + x3*x3 + x7*x7] += 1
    return A


def build_bc_q(H: int):
    B = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][x5*x5 + x9*x9] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1][x6*x6 + x8*x8 + x10*x10] += 1

    BC = [[[defaultdict(int) for _ in range(8)] for __ in range(H + 1)] for ___ in range(H + 1)]
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        for x1 in range(x0 + 1, H + 1):
            parity = x1 & 1
            q01 = x0*x0 + x1*x1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    for sb in range(3):
                        for pb in (0, 1):
                            left = B[g2][sb][pb]
                            if not left:
                                continue
                            for sc in range(4):
                                right = C[g3][sc][pb ^ parity]
                                if not right:
                                    continue
                                for ql, vl in left.items():
                                    for qr, vr in right.items():
                                        BC[b][c][sb + sc + extra][q01 + ql + qr] += vl * vr

    for t in range(H + 1):
        extra = 2 * int(t > 0)
        parity = t & 1
        cap = H - t
        for x5 in range(cap + 1):
            for x8 in range(x5 + 1, cap + 1):
                for x9 in range(cap - x5 + 1):
                    b = t + x5 + x9
                    for x6 in range(cap - x8 + 1):
                        for x10 in range(cap - x8 - x6 + 1):
                            c = t + x8 + x6 + x10
                            if ((x8 + x9 + x10) & 1) != parity:
                                continue
                            vals = (t, t, x5, x6, x8, x9, x10)
                            BC[b][c][sum(v > 0 for v in vals)][sum(v*v for v in vals)] += 1
        for x5 in range(cap + 1):
            x8 = x5
            for x6 in range(cap - x8 + 1):
                for x9 in range(x6, cap - x5 + 1):
                    b = t + x5 + x9
                    for x10 in range(cap - x8 - x6 + 1):
                        c = t + x8 + x6 + x10
                        if ((x8 + x9 + x10) & 1) != parity:
                            continue
                        vals = (t, t, x5, x6, x8, x9, x10)
                        BC[b][c][sum(v > 0 for v in vals)][sum(v*v for v in vals)] += 1
    return BC


def brute_bc_q(H: int):
    out = [[[defaultdict(int) for _ in range(8)] for __ in range(H + 1)] for ___ in range(H + 1)]
    for x0 in range(H + 1):
        for x1 in range(x0, H + 1):
            for x5 in range(H + 1):
                for x6 in range(H + 1):
                    for x8 in range(H + 1):
                        for x9 in range(H + 1):
                            if x0 == x1 and (x5, x6) > (x8, x9):
                                continue
                            b = x1 + x5 + x9
                            if b > H:
                                continue
                            for x10 in range(H + 1):
                                c = x0 + x6 + x8 + x10
                                if c > H or (x1 + x8 + x9 + x10) & 1:
                                    continue
                                vals = (x0, x1, x5, x6, x8, x9, x10)
                                out[b][c][sum(v > 0 for v in vals)][sum(v*v for v in vals)] += 1
    return out


def semantic_crosscheck() -> None:
    fast = build_bc_q(4)
    brute = brute_bc_q(4)
    for b in range(5):
        for c in range(5):
            for s in range(8):
                req(dict(fast[b][c][s]) == dict(brute[b][c][s]), f"q-refined BC mismatch {(b,c,s)}")


def bounded_census() -> dict:
    A = build_a_q(H)
    BC = build_bc_q(H)
    records = []
    old_total = 0
    exact_total = 0
    for g in (0, 1):
        for d in range(8, MAX_D + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16 * g + 16, 4)
            threshold8 = d*d + 16*d + (32 if g == 0 else 0)
            row_old = 0
            row_exact = 0
            for b in range(h + 1):
                for c in range(h + 1):
                    if not any(BC[b][c]):
                        continue
                    c3 = component3(d, b, c)
                    if c3 < 0:
                        continue
                    for a in range(h + 1):
                        if not any(A[a]):
                            continue
                        M = a + b + c
                        ca = component_a(d, a)
                        if ca < 0:
                            continue
                        srem = min(16, d) + ca + c3
                        old_reject = 8*a*a + 8*b*b + 6*c*c > 3*d*d + 48*d + (96 if g == 0 else 0)
                        for sbc in range(8):
                            if not BC[b][c][sbc]:
                                continue
                            for sa in range(4):
                                if not A[a][sa]:
                                    continue
                                support = sbc + sa
                                qneed = K - support
                                if qneed > 0 and srem < qneed:
                                    continue
                                lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                                upper = min((19*d)//5, 3*d, 3*d - (b - c))
                                if lower > upper:
                                    continue
                                excluded = set()
                                e_n358 = 3*d - (b - c)
                                if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                    excluded.add(e_n358)
                                if g == 1 and d == 8:
                                    excluded.add(8)
                                ne, normal_sum = even_interval_normal_sum(d, lower, upper, excluded)
                                if ne <= 0:
                                    continue
                                bc_total = sum(BC[b][c][sbc].values())
                                a_total = sum(A[a][sa].values())
                                exact_reject = 0
                                for qb, vb in BC[b][c][sbc].items():
                                    for qa, va in A[a][sa].items():
                                        if 8 * (qa + qb) > threshold8:
                                            exact_reject += vb * va
                                if old_reject:
                                    req(exact_reject == bc_total * a_total, f"Cauchy not subset {(g,d,a,b,c,sa,sbc)}")
                                    row_old += bc_total * a_total * normal_sum
                                row_exact += exact_reject * normal_sum
            rec = {
                "g": g,
                "d": d,
                "old_group_cauchy_candidate_rejected_terminals": row_old,
                "stored_exact_square_candidate_rejected_terminals": row_exact,
                "incremental_candidate_over_group_cauchy": row_exact - row_old,
            }
            req(rec["incremental_candidate_over_group_cauchy"] >= 0, f"negative gain {(g,d)}")
            records.append(rec)
            old_total += row_old
            exact_total += row_exact

    stream = hashlib.sha256()
    for rec in records:
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    req(old_total == EXPECTED_OLD, "old bounded total drift")
    req(exact_total == EXPECTED_EXACT, "exact bounded total drift")
    req(exact_total - old_total == EXPECTED_INCREMENTAL, "incremental bounded total drift")
    req(stream.hexdigest() == EXPECTED_STREAM, "row stream drift")
    req(any(r["old_group_cauchy_candidate_rejected_terminals"] == 0 and r["stored_exact_square_candidate_rejected_terminals"] > 0 for r in records), "strict low-degree witness missing")
    return {"old": old_total, "exact": exact_total, "incremental": exact_total - old_total, "rows": len(records), "stream": stream.hexdigest()}


def main() -> None:
    for name, (rel, expected) in LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), f"missing source {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    p = json.loads(PREFLIGHT.read_text())
    req(p["canonical_sha256_without_this_field"] == PREFLIGHT_CANON, "stored preflight canonical")
    req(canonical(p) == PREFLIGHT_CANON, "preflight canonical drift")
    req(p["route_id"] == "HPADJ-08_ex5", "route id")
    req(all(v is False for v in p["firewalls"].values()), "credit firewall")

    correction = json.loads((ROOT / LOCKS["corrected_adjunction"][0]).read_text())
    c = correction["corrected_general_type_adjunction"]
    req(c["g0_exact_exceptional_square_necessary_condition"] == "8*sum(y_i^2)<=d^2+16*d+32", "g0 condition")
    req(c["g1_exact_exceptional_square_necessary_condition"] == "8*sum(y_i^2)<=d^2+16*d", "g1 condition")

    prefix = json.loads((ROOT / LOCKS["prefix_checkpoint"][0]).read_text())
    labels = prefix["exact_terminal_family"]["assignment_order_known_labels_1based"]
    req(labels == [95,99,103,102,49,97,94,101,93,98,96], "terminal labels")
    req(labels[4] == 49 and all(93 <= x <= 140 for i, x in enumerate(labels) if i != 4), "stored exceptional identity")

    semantic_crosscheck()
    result = bounded_census()
    req(result["old"] == p["bounded_diagnostic"]["old_group_cauchy_candidate_rejected_terminals"], "preflight old count")
    req(result["exact"] == p["bounded_diagnostic"]["stored_exact_square_candidate_rejected_terminals"], "preflight exact count")
    req(result["incremental"] == p["bounded_diagnostic"]["incremental_candidate_over_group_cauchy"], "preflight incremental count")
    print("PASS HPADJ-08_ex5 bounded exact-square strict-gain diagnostic", json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
