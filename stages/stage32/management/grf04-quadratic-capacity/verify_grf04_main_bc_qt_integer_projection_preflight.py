#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_grf04_main_bc_qt_projection_preflight.py"
PARENT_BLOB = "66dfd1082c119f86ec8d249389e039358277daa6"
ARTIFACT = HERE / "GRF04-MAIN-BC-QT-INTEGER-PROJECTION-PREFLIGHT.json"
ARTIFACT_BLOB = "45e1f112a8df9e34087a161a219c82323bbc4635"
ARTIFACT_CANON = "08c4fd287d4630ff786994cf29e866c816a3e8668cce3cf46c7a11e8bd6c739f"

EXPECTED_PANEL = 204_729_820_492
EXPECTED_ENV_REJECTED = 198_808_166_494
EXPECTED_REAL_REJECTED = 199_725_549_465
EXPECTED_INTEGER_REJECTED = 199_744_626_374
EXPECTED_INCREMENTAL = 19_076_909
EXPECTED_STRICT_CELLS = 530_964
EXPECTED_ROW_STREAM = "90e547ecb1999e7f660843a8c3fd8c549f35202c9ea86520d64398bb43956e44"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_parent():
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "parent BC-QT verifier blob drift")
    spec = importlib.util.spec_from_file_location("bc_qt_parent_locked", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load parent BC-QT verifier")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qmin_bruteforce(b: int, c: int, t: int) -> int | None:
    lo = max(0, t - c)
    hi = min(b, t)
    if lo > hi:
        return None
    best = None
    for u in range(lo, hi + 1):
        v = t - u
        val = (
            (u*u + 1)//2
            + (b-u)*(b-u)
            + (v*v + 1)//2
            + ((c-v)*(c-v) + 1)//2
        )
        best = val if best is None else min(best, val)
    return best


@lru_cache(maxsize=None)
def qmin_fast(b: int, c: int, t: int) -> int | None:
    lo = max(0, t - c)
    hi = min(b, t)
    if lo > hi:
        return None
    A = 2*b + 2*t - c
    C = 2*b*b + t*t + (c-t)*(c-t)
    best = None
    for p in (0, 1):
        lp = lo if lo % 2 == p else lo + 1
        up = hi if hi % 2 == p else hi - 1
        if lp > up:
            continue
        # On one parity class the ceiling corrections are constant and the
        # remaining quadratic is strictly convex with vertex A/5.  The exact
        # minimizer is therefore the admissible parity point nearest A/5.
        base = A // 5
        candidates = {lp, up}
        for z in range(base - 4, base + 5):
            if lp <= z <= up and z % 2 == p:
                candidates.add(z)
        eps = p + ((t-p) & 1) + ((c-t+p) & 1)
        for u in candidates:
            num = 5*u*u - 2*A*u + C + eps
            req(num % 2 == 0, "parity quadratic nonintegral")
            val = num // 2
            best = val if best is None else min(best, val)
    return best


@lru_cache(maxsize=None)
def integer_t_interval(b: int, c: int, qbc: int) -> tuple[int, int] | None:
    vals = [t for t in range(b + c + 1) if qmin_fast(b, c, t) <= qbc]
    if not vals:
        return None
    req(vals == list(range(vals[0], vals[-1] + 1)), "integer projected t-set not contiguous")
    return vals[0], vals[-1]


def integer_projection_x4_survivors(parent, *, d: int, g: int, b: int, c: int,
                                    qbc: int, q: int, n: int) -> int:
    interval = integer_t_interval(b, c, qbc)
    if interval is None:
        return 0
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*q
    if rem < 0:
        return 0
    r = parent.math.isqrt(rem // 4)
    tlo, thi = interval
    lo = max(0, parent.ceil_div(d//2 - thi - r, 2))
    hi = min(n, (d//2 - tlo + r) // 2)
    return max(0, hi-lo+1)


def census(parent) -> dict:
    A = parent.build_a_q()
    BC = parent.build_bc_q()
    panel = envbad = realbad = intbad = 0
    strict_cells = 0
    rows = []

    for b in range(parent.H + 1):
        for c in range(parent.H + 1):
            for t in range(b + c + 1):
                req(qmin_fast(b, c, t) == qmin_bruteforce(b, c, t),
                    f"exact integer qBC minimum mismatch {(b,c,t)}")

    for g in (0, 1):
        for d in range(8, parent.MAX_D + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = parent.ceil_div(d - 16*g + 16, 4)
            rp = re = rr = ri = 0
            for b in range(h + 1):
                for c in range(h + 1):
                    c3 = parent.component3(d, b, c)
                    if c3 < 0 or not any(BC[b][c]):
                        continue
                    for a in range(h + 1):
                        ca = parent.component_a(d, a)
                        if ca < 0 or not any(A[a]):
                            continue
                        M = a + b + c
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
                                es = parent.allowed_es(d, lower, upper, excluded)
                                if not es:
                                    continue
                                for qbc, vb in bd.items():
                                    intv = integer_t_interval(b, c, qbc)
                                    real_intv = parent.projected_t_interval(b=b, c=c, qbc=qbc)
                                    if intv is not None and real_intv is not None:
                                        req(intv[0] >= real_intv[0] and intv[1] <= real_intv[1],
                                            f"integer projection escaped real projection {(b,c,qbc)}")
                                    elif intv is not None:
                                        req(False, f"integer projection exists outside real projection {(b,c,qbc)}")
                                    for qa, va in ad.items():
                                        q = qa + qbc
                                        mult = va * vb
                                        for e in es:
                                            n = 19*d - 5*e
                                            total = n + 1
                                            env = parent.bc_envelope_x4_survivors(
                                                d=d, g=g, b=b, c=c, q=q, n=n)
                                            real = parent.projection_x4_survivors(
                                                d=d, g=g, b=b, c=c, qbc=qbc, q=q, n=n)
                                            inte = integer_projection_x4_survivors(
                                                parent, d=d, g=g, b=b, c=c, qbc=qbc, q=q, n=n)
                                            req(inte <= real <= env,
                                                f"integer/real/envelope dominance regression {(g,d,e,a,b,c,qbc,q)}")
                                            strict_cells += int(inte < real)
                                            rp += mult * total
                                            re += mult * (total - env)
                                            rr += mult * (total - real)
                                            ri += mult * (total - inte)
            row = {
                "g": g,
                "d": d,
                "panel_terminals": rp,
                "bc_envelope_rejected": re,
                "bc_qt_projection_rejected": rr,
                "bc_qt_integer_projection_rejected": ri,
                "bc_qt_projection_survivors": rp-rr,
                "bc_qt_integer_projection_survivors": rp-ri,
                "incremental_integer_over_real_projection": ri-rr,
            }
            rows.append(row)
            panel += rp
            envbad += re
            realbad += rr
            intbad += ri

    req(panel == EXPECTED_PANEL, f"panel drift {panel}")
    req(envbad == EXPECTED_ENV_REJECTED, f"BC envelope drift {envbad}")
    req(realbad == EXPECTED_REAL_REJECTED, f"real projection drift {realbad}")
    req(intbad == EXPECTED_INTEGER_REJECTED, f"integer projection drift {intbad}")
    req(intbad-realbad == EXPECTED_INCREMENTAL, "integer projection incremental drift")
    req(strict_cells == EXPECTED_STRICT_CELLS, f"strict cell count drift {strict_cells}")
    stream = hashlib.sha256()
    for row in rows:
        stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    req(stream.hexdigest() == EXPECTED_ROW_STREAM, "row stream drift")
    return {
        "panel_terminals": panel,
        "bc_envelope_rejected": envbad,
        "bc_qt_real_projection_rejected": realbad,
        "bc_qt_integer_projection_rejected": intbad,
        "bc_qt_real_projection_survivors": panel-realbad,
        "bc_qt_integer_projection_survivors": panel-intbad,
        "incremental_rejected_over_real_projection": intbad-realbad,
        "strict_projection_cells": strict_cells,
        "row_stream_sha256": stream.hexdigest(),
    }


def main() -> None:
    parent = load_parent()
    req(ARTIFACT.is_file() and git_blob(ARTIFACT) == ARTIFACT_BLOB, "integer preflight artifact blob drift")
    art = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    req(art.get("canonical_sha256_without_this_field") == ARTIFACT_CANON, "stored artifact canonical drift")
    req(canon(art) == ARTIFACT_CANON, "artifact canonical drift")
    got = census(parent)
    bounded = art["bounded_preflight"]
    for key, value in got.items():
        req(bounded[key] == value, f"artifact bounded result mismatch {key}")
    req(art["research_interpretation"]["full178_scaleout_not_run"] is True,
        "preflight overclaims FULL178 scaleout")
    req(art["research_interpretation"]["current_main_numerical_authority_changed"] is False,
        "preflight overclaims MAIN authority")
    for key, value in art["credit"].items():
        req(value is False, f"credit firewall {key}")
    print("PASS: exact integer BC q-t projection formula matches bounded brute force")
    print("PASS: integer projection is a subset of the prior real BC-QT projection")
    print("PASS: bounded panel adds 19076909 exact necessary-condition rejections with zero MAIN credit")


if __name__ == "__main__":
    main()
