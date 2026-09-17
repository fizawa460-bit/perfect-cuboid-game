#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "compressed_family": (
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "grf04": (
        "stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json",
        "f7c1073edbf895f498fd9923e59eedf5a4e981c8",
    ),
}

MAX_D = 20
H = MAX_D // 2
EXPECTED_PANEL = 204_729_820_492
EXPECTED_HPADJ08_REJECTED = 108_290_859_347
EXPECTED_BC_ENVELOPE_REJECTED = 198_808_166_494
EXPECTED_PROJECTION_REJECTED = 199_725_549_465
EXPECTED_INCREMENTAL_OVER_BC_ENVELOPE = 917_382_971
EXPECTED_ROW_STREAM = "c0544548f5f7ef5d83e4fecf55f77ab5c3aa70934b51a796c73f292da8c5aa93"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def allowed_es(d: int, lower: int, upper: int, excluded: set[int]) -> list[int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return []
    return [e for e in range(lo, hi + 1, 2) if e not in excluded]


def verify_sos_identity() -> None:
    # Integer SOS identity behind the new projection:
    # 60*qBC - 20*b^2 - 15*c^2 - (6*t-4*b-3*c)^2
    # = 30[(x1-x9)^2+(x0-x6)^2+(x8-x10)^2]
    #   + 6(5*u-2*b-2*t+c)^2 >= 0, u=x1+x9.
    # Exhaustive bounded substitution is a regression check; the displayed
    # identity itself is an exact polynomial identity over Z.
    for x0 in range(4):
        for x1 in range(4):
            for x5 in range(4):
                for x6 in range(4):
                    for x8 in range(4):
                        for x9 in range(4):
                            for x10 in range(4):
                                b = x1 + x5 + x9
                                c = x0 + x8 + x6 + x10
                                u = x1 + x9
                                t = u + x0 + x6
                                qbc = sum(v * v for v in (x0, x1, x5, x6, x8, x9, x10))
                                lhs = 60*qbc - 20*b*b - 15*c*c - (6*t - 4*b - 3*c)**2
                                rhs = 30*((x1-x9)**2 + (x0-x6)**2 + (x8-x10)**2) + 6*(5*u - 2*b - 2*t + c)**2
                                req(lhs == rhs and lhs >= 0, "BC q-t SOS identity regression")


def build_a_q():
    out = [[defaultdict(int) for _ in range(4)] for __ in range(H + 1)]
    for a in range(H + 1):
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                s = sum(v > 0 for v in (x2, x3, x7))
                out[a][s][x2*x2 + x3*x3 + x7*x7] += 1
    return out


def build_bc_q():
    B = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][x5*x5 + x9*x9] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8+x10) & 1][x6*x6 + x8*x8 + x10*x10] += 1

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
                                dst = BC[b][c][sb + sc + extra]
                                for ql, vl in left.items():
                                    for qr, vr in right.items():
                                        dst[q01 + ql + qr] += vl * vr

    for t in range(H + 1):
        parity = t & 1
        cap = H - t
        for x5 in range(cap + 1):
            for x8 in range(x5 + 1, cap + 1):
                for x9 in range(cap - x5 + 1):
                    b = t + x5 + x9
                    for x6 in range(cap - x8 + 1):
                        for x10 in range(cap - x8 - x6 + 1):
                            c = t + x8 + x6 + x10
                            if ((x8+x9+x10) & 1) != parity:
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
                        if ((x8+x9+x10) & 1) != parity:
                            continue
                        vals = (t, t, x5, x6, x8, x9, x10)
                        BC[b][c][sum(v > 0 for v in vals)][sum(v*v for v in vals)] += 1
    return BC


def bc_envelope_x4_survivors(*, d: int, g: int, b: int, c: int, q: int, n: int) -> int:
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*q
    if rem < 0:
        return 0
    r = math.isqrt(rem // 4)
    lo = max(0, ceil_div(d//2 - (b+c+r), 2))
    hi = min(n, (d//2 + r) // 2)
    return max(0, hi-lo+1)


def projected_t_interval(*, b: int, c: int, qbc: int) -> tuple[int, int] | None:
    # Necessary consequence of the SOS identity.
    radius_sq = 60*qbc - 20*b*b - 15*c*c
    if radius_sq < 0:
        return None
    r = math.isqrt(radius_sq)
    lo = max(0, ceil_div(4*b + 3*c - r, 6))
    hi = min(b+c, (4*b + 3*c + r) // 6)
    if lo > hi:
        return None
    return lo, hi


def projection_x4_survivors(*, d: int, g: int, b: int, c: int, qbc: int, q: int, n: int) -> int:
    interval = projected_t_interval(b=b, c=c, qbc=qbc)
    if interval is None:
        return 0
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*q
    if rem < 0:
        return 0
    r = math.isqrt(rem // 4)
    tlo, thi = interval
    lo = max(0, ceil_div(d//2 - thi - r, 2))
    hi = min(n, (d//2 - tlo + r) // 2)
    return max(0, hi-lo+1)


def census() -> dict:
    A = build_a_q()
    BC = build_bc_q()
    panel = hpbad = envbad = projbad = 0
    strict_cells = 0
    rows = []
    for g in (0, 1):
        for d in range(8, MAX_D + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16*g + 16, 4)
            hp8 = d*d + 16*d + (32 if g == 0 else 0)
            rp = rh = re = rproj = 0
            for b in range(h + 1):
                for c in range(h + 1):
                    c3 = component3(d, b, c)
                    if c3 < 0 or not any(BC[b][c]):
                        continue
                    for a in range(h + 1):
                        ca = component_a(d, a)
                        if ca < 0 or not any(A[a]):
                            continue
                        M = a+b+c
                        srem = min(16, d) + ca + c3
                        for sbc in range(8):
                            bd = BC[b][c][sbc]
                            if not bd:
                                continue
                            for sa in range(4):
                                ad = A[a][sa]
                                if not ad:
                                    continue
                                support = sbc + sa
                                qneed = K - support
                                if qneed > 0 and srem < qneed:
                                    continue
                                lower = max(legacy, K, d-4*g+4, M, M+max(0, qneed))
                                upper = min((19*d)//5, 3*d, 3*d-(b-c))
                                if lower > upper:
                                    continue
                                excluded = set()
                                en = 3*d-(b-c)
                                if b <= h-5 and support+srem == K and en-M >= srem:
                                    excluded.add(en)
                                if g == 1 and d == 8:
                                    excluded.add(8)
                                es = allowed_es(d, lower, upper, excluded)
                                if not es:
                                    continue
                                for qbc, vb in bd.items():
                                    for qa, va in ad.items():
                                        q = qa + qbc
                                        mult = va * vb
                                        hp_all = 8*q > hp8
                                        for e in es:
                                            n = 19*d - 5*e
                                            total = n + 1
                                            env = bc_envelope_x4_survivors(d=d, g=g, b=b, c=c, q=q, n=n)
                                            proj = projection_x4_survivors(d=d, g=g, b=b, c=c, qbc=qbc, q=q, n=n)
                                            req(proj <= env, f"projection dominance regression {(g,d,e,a,b,c,qbc,q)}")
                                            strict_cells += int(proj < env)
                                            rp += mult * total
                                            rh += mult * (total if hp_all else 0)
                                            re += mult * (total - env)
                                            rproj += mult * (total - proj)
            row = {
                "g": g,
                "d": d,
                "panel_terminals": rp,
                "hpadj08_rejected": rh,
                "bc_envelope_rejected": re,
                "bc_qt_projection_rejected": rproj,
                "bc_envelope_survivors": rp-re,
                "bc_qt_projection_survivors": rp-rproj,
                "incremental_over_bc_envelope": rproj-re,
            }
            rows.append(row)
            panel += rp
            hpbad += rh
            envbad += re
            projbad += rproj

    req(panel == EXPECTED_PANEL, f"panel drift {panel}")
    req(hpbad == EXPECTED_HPADJ08_REJECTED, f"HPADJ08 drift {hpbad}")
    req(envbad == EXPECTED_BC_ENVELOPE_REJECTED, f"BC envelope drift {envbad}")
    req(projbad == EXPECTED_PROJECTION_REJECTED, f"projection drift {projbad}")
    req(projbad-envbad == EXPECTED_INCREMENTAL_OVER_BC_ENVELOPE, "incremental projection gain drift")
    req(projbad > envbad, "strict aggregate gain missing")
    req(strict_cells > 0, "strict cell gain missing")
    stream = hashlib.sha256()
    for row in rows:
        stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    req(stream.hexdigest() == EXPECTED_ROW_STREAM, "row stream drift")
    return {
        "schema": "STAGE32_MAIN_GRF04_BC_QT_PROJECTION_PREFLIGHT_V1",
        "domain": {"g": [0, 1], "d_even": [8, MAX_D], "hmax": H},
        "panel_terminals": panel,
        "hpadj08_rejected": hpbad,
        "bc_envelope_rejected": envbad,
        "bc_envelope_survivors": panel-envbad,
        "bc_qt_projection_rejected": projbad,
        "bc_qt_projection_survivors": panel-projbad,
        "incremental_over_bc_envelope": projbad-envbad,
        "relative_reduction_of_bc_envelope_survivors": (projbad-envbad)/(panel-envbad),
        "strict_aggregate_cells": strict_cells,
        "row_stream_sha256": stream.hexdigest(),
        "credit": {"main": False, "theorem": False, "effectivity": False, "endpoint": False, "merge": False},
    }


def main() -> None:
    for name, (rel, sha) in LOCKS.items():
        p = ROOT / rel
        req(p.is_file(), f"missing source {name}")
        req(git_blob(p) == sha, f"source drift {name}")
    verify_sos_identity()
    result = census()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
