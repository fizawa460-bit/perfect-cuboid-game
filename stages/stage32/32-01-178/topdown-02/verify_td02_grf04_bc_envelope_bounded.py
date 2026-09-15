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
    "compressed_family": ("stages/stage32/residual-32-01-production/compressed_terminal_family.py", "90ff82ed312dcc0cb32cf207935945f550e29170"),
    "prefix_checkpoint": ("stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json", "eb823cc2f99d74456d5701b4673f848f18ba3151"),
    "corrected_adjunction": ("stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json", "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e"),
    "grf04": ("stages/stage32/management/global-residual-feasibility/GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json", "f7c1073edbf895f498fd9923e59eedf5a4e981c8"),
}
MAX_D = 32
H = 16
EXPECTED_PANEL = 37_302_011_598_273
EXPECTED_HPADJ08_REJECTED = 25_770_706_503_487
EXPECTED_HPADJ08_SURVIVORS = 11_531_305_094_786


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
    return min(13, d - a, d - 2*a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2*b, d - 2*c + 1)


def allowed_es(d: int, lower: int, upper: int, excluded: set[int]) -> list[int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return []
    return [e for e in range(lo, hi + 1, 2) if e not in excluded]


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
                                        dst[q01 + ql + qr] += vl*vr

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
                            vals = (t,t,x5,x6,x8,x9,x10)
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
                        vals = (t,t,x5,x6,x8,x9,x10)
                        BC[b][c][sum(v > 0 for v in vals)][sum(v*v for v in vals)] += 1
    return BC


def envelope_x4_survivors(*, d: int, g: int, b: int, c: int, q: int, n: int) -> int:
    # Exact full GRF04 has rho=q/2+(d/2-2*x4-t)^2/12 with
    # t=x0+x1+x6+x9. Nonnegativity gives 0 <= t <= b+c, hence
    # rho >= q/2 + dist(d/2-2*x4,[0,b+c])^2/12.
    # Keeping this lower envelope is weaker than exact-t GRF04 but requires no
    # histogram state beyond the retained HPADJ08 (b,c,q) statistics.
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*q
    if rem < 0:
        return 0
    r = math.isqrt(rem // 4)
    lo = max(0, ceil_div(d//2 - (b+c+r), 2))
    hi = min(n, (d//2 + r) // 2)
    return max(0, hi-lo+1)


def convolved_q_distribution(A, BC, *, a: int, sa: int, b: int, c: int, sbc: int) -> dict[int, int]:
    out = defaultdict(int)
    for qa, va in A[a][sa].items():
        for qb, vb in BC[b][c][sbc].items():
            out[qa + qb] += va * vb
    return out


def census() -> dict:
    A = build_a_q()
    BC = build_bc_q()
    qcache: dict[tuple[int, int, int, int, int], dict[int, int]] = {}
    panel = hpbad = envbad = 0
    rows = []
    for g in (0,1):
        for d in range(8, MAX_D+1, 2):
            h = d//2
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16*g + 16, 4)
            hp8 = d*d + 16*d + (32 if g == 0 else 0)
            rp = rh = re = 0
            for b in range(h+1):
                for c in range(h+1):
                    c3 = component3(d,b,c)
                    if c3 < 0 or not any(BC[b][c]):
                        continue
                    for a in range(h+1):
                        ca = component_a(d,a)
                        if ca < 0 or not any(A[a]):
                            continue
                        M = a+b+c
                        srem = min(16,d) + ca + c3
                        for sbc in range(8):
                            if not BC[b][c][sbc]:
                                continue
                            for sa in range(4):
                                if not A[a][sa]:
                                    continue
                                support = sbc+sa
                                qneed = K-support
                                if qneed > 0 and srem < qneed:
                                    continue
                                lower = max(legacy,K,d-4*g+4,M,M+max(0,qneed))
                                upper = min((19*d)//5,3*d,3*d-(b-c))
                                if lower > upper:
                                    continue
                                excluded = set()
                                en = 3*d-(b-c)
                                if b <= h-5 and support+srem == K and en-M >= srem:
                                    excluded.add(en)
                                if g == 1 and d == 8:
                                    excluded.add(8)
                                es = allowed_es(d,lower,upper,excluded)
                                if not es:
                                    continue

                                # Every allowed e satisfies e<=3d, hence
                                # n=19d-5e >= 4d. Also rem/4 <=
                                # (3d^2+48d+96)/4 <= 4d^2 for d>=8, so
                                # r<=2d and the raw GRF04 x4 upper endpoint is
                                # at most 5d/4 < 4d. Therefore the n-clipping
                                # in envelope_x4_survivors is inactive for all
                                # e in this bounded domain. We may sum the
                                # affine total_x4=n+1 exactly over e while
                                # evaluating the survivor count only once.
                                req(max(es) <= 3*d, f"e upper-bound regression {(g,d,a,b,c)}")
                                min_n = 19*d - 5*max(es)
                                req(min_n >= 4*d, f"normal-budget lower-bound regression {(g,d,a,b,c)}")
                                ecount = len(es)
                                total_x4_sum = sum(19*d - 5*e + 1 for e in es)

                                key = (a, sa, b, c, sbc)
                                qdist = qcache.get(key)
                                if qdist is None:
                                    qdist = convolved_q_distribution(A, BC, a=a, sa=sa, b=b, c=c, sbc=sbc)
                                    qcache[key] = qdist

                                for q, mult in qdist.items():
                                    rhs = 3*d*d + 48*d + 96 - 96*g
                                    rem = rhs - 24*q
                                    if rem >= 0:
                                        r = math.isqrt(rem // 4)
                                        req(r <= 2*d, f"GRF04 radius bound regression {(g,d,q)}")
                                        raw_hi = (d//2 + r) // 2
                                        req(raw_hi <= min_n, f"x4 n-clip unexpectedly active {(g,d,q,min_n,raw_hi)}")
                                    survive = envelope_x4_survivors(d=d,g=g,b=b,c=c,q=q,n=min_n)
                                    hp_all = 8*q > hp8
                                    rp += mult * total_x4_sum
                                    rh += mult * (total_x4_sum if hp_all else 0)
                                    re += mult * (total_x4_sum - ecount*survive)

            rows.append({"g":g,"d":d,"panel_terminals":rp,"hpadj08_rejected":rh,"bc_envelope_rejected":re,"incremental_over_hpadj08":re-rh,"bc_envelope_survivors":rp-re})
            panel += rp
            hpbad += rh
            envbad += re

    req(panel == EXPECTED_PANEL, f"panel baseline drift {panel}")
    req(hpbad == EXPECTED_HPADJ08_REJECTED, f"HPADJ08 baseline drift {hpbad}")
    req(panel-hpbad == EXPECTED_HPADJ08_SURVIVORS, "HPADJ08 survivor baseline drift")
    req(envbad > hpbad, "BC-envelope strict gain missing")
    stream = hashlib.sha256()
    for r in rows:
        stream.update(json.dumps(r,sort_keys=True,separators=(",",":")).encode()+b"\n")
    return {
        "schema":"STAGE32_32_01_178_TD02_GRF04_BC_ENVELOPE_BOUNDED_V1",
        "domain":{"g":[0,1],"d_even":[8,32],"hmax":H},
        "panel_terminals":panel,
        "hpadj08_rejected":hpbad,
        "hpadj08_survivors":panel-hpbad,
        "bc_envelope_rejected":envbad,
        "bc_envelope_survivors":panel-envbad,
        "incremental_over_hpadj08":envbad-hpbad,
        "row_stream_sha256":stream.hexdigest(),
        "rows":rows,
        "credit":{"main":False,"theorem":False,"effectivity":False,"endpoint":False,"merge":False},
    }


def main() -> None:
    for name,(rel,sha) in LOCKS.items():
        p=ROOT/rel
        req(p.is_file(), f"missing source {name}")
        req(git_blob(p)==sha, f"source drift {name}")
    prefix=json.loads((ROOT/LOCKS["prefix_checkpoint"][0]).read_text())
    req(prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] == [95,99,103,102,49,97,94,101,93,98,96], "FULL178 label order")
    # Concrete strict-gain witness inside the retained bounded domain.
    req(envelope_x4_survivors(d=8,g=0,b=0,c=0,q=0,n=92) == 9, "d8 witness survivor count")
    result=census()
    (HERE/"TD02-GRF04-BC-ENVELOPE-BOUNDED-RESULT.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:result[k] for k in ("panel_terminals","hpadj08_rejected","hpadj08_survivors","bc_envelope_rejected","bc_envelope_survivors","incremental_over_hpadj08","row_stream_sha256")},indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
