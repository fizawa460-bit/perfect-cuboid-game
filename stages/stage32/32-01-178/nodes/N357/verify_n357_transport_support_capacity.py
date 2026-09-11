#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
N355 = HERE.parent / "N355"
N356 = HERE.parent / "N356"
N355_FULL = N355 / "verify_n355_full_prefix_block_sum_census.py"
N356_CONTRACT = N356 / "OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CAP_CONTRACT.md"
N356_RESULT = N356 / "RESULT.json"

EXPECTED_N355_FULL_BLOB = "ccc00d1536cdf5e27965465dd5e40163e2fcb91c"
EXPECTED_N356_CONTRACT_BLOB = "d2353cab9c175a680067c7ad4c24759b6dd15df3"
EXPECTED_N356_RESULT_BLOB = "677b1ae2bab910db0805d20ee489d922522919ed"
EXPECTED_N356_RESULT_CANONICAL = "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31"

WITNESS_G = 0
WITNESS_D = 100
WITNESS_E = 200
WITNESS_K = 29
WITNESS_THRESHOLD = 100
EXPECTED_N356_EXCEPTIONAL = 49_048_088_431_446
EXPECTED_N357_EXCEPTIONAL = 49_030_556_814_634
EXPECTED_INCREMENTAL_EXCEPTIONAL = 17_531_616_812
EXPECTED_NORMAL_BLOCK = 901
EXPECTED_INCREMENTAL_TERMINALS = 15_795_986_747_612


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def component0_formula(d: int) -> int:
    return min(16, d)


def component_a_formula(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3_formula(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def support_suffix_capacity(d: int, a: int, b: int, c: int) -> int:
    return component0_formula(d) + component_a_formula(d, a) + component3_formula(d, b, c)


def brute_component_a(n1: int, n2: int, a: int) -> int:
    if min(n1, n2) < a:
        return -1
    best = -1
    for z in range(2):  # one omitted slot in the fixed-a cell
        if z > min(n1 - a, n2 - a):
            continue
        for x in range(5):
            if z + x > n1 - a:
                continue
            for y in range(5):
                if z + y > n2 - a:
                    continue
                w = min(4, n1 - y, n2 - x)
                if w >= 0:
                    best = max(best, z + x + y + w)
    return best


def brute_component3(n1: int, n2: int, b: int, c: int) -> int:
    if min(n1, n2) < max(b, c):
        return -1
    best = -1
    for z in range(2):  # the single omitted label in the b cell
        if n1 - b - z < 0 or n2 - b - z < 0:
            continue
        x = min(4, n1 - c, n2 - b - z)
        y = min(4, n1 - b - z, n2 - c)
        if min(x, y) >= 0:
            best = max(best, x + y + z)
    return best


def brute_component0(n1: int, n2: int) -> int:
    return min(16, 2 * n1, 2 * n2)


def validate_flow_formulas() -> None:
    # Exact balanced formulas and balanced fixed-sum maximization on hostile small domains.
    for d in range(0, 26, 2):
        h = d // 2
        for a in range(h + 1):
            got = brute_component_a(h, h, a)
            want = component_a_formula(d, a)
            if got != want:
                raise ValueError(f"component A formula regression {(d,a)}: {got}!={want}")
        for b in range(h + 1):
            for c in range(h + 1):
                got = brute_component3(h, h, b, c)
                want = component3_formula(d, b, c)
                if got != want:
                    raise ValueError(f"component3 formula regression {(d,b,c)}: {got}!={want}")

        for a in range(h + 1):
            for b in range(h + 1):
                for c in range(h + 1):
                    balanced = (
                        brute_component0(h, h)
                        + brute_component_a(h, h, a)
                        + brute_component3(h, h, b, c)
                    )
                    best = -1
                    for n1 in range(d + 1):
                        n2 = d - n1
                        if min(n1, n2) < max(a, b, c):
                            continue
                        val = (
                            brute_component0(n1, n2)
                            + brute_component_a(n1, n2, a)
                            + brute_component3(n1, n2, b, c)
                        )
                        best = max(best, val)
                    if best != balanced:
                        raise ValueError(
                            f"balanced support maximum regression {(d,a,b,c)}: {best}!={balanced}"
                        )


def s3_ge_interval(h: int, x0: int, x1: int, r: int, t: int, lo: int, hi: int):
    # b=x1+g2, c=x0+(r-g2), d=2h.  S3>=t is an interval in g2.
    if t <= 0:
        return lo, hi
    if t > 9:
        return 1, 0
    d = 2 * h
    if t > d - x0 - x1 - r:
        return 1, 0
    hi = min(hi, (d - 2 * x1 - t) // 2)
    lo = max(lo, ceil_div(t - d + 2 * x0 + 2 * r - 1, 2))
    return lo, hi


def build_support_exact(h: int, threshold: int, fullmod):
    d = 2 * h
    bc_pref = fullmod.build_bc_prefix(h)
    lex_pref = fullmod.build_lex_prefix(h)
    mid = [[[0] * 10 for _ in range(8)] for __ in range(2 * h + 1)]

    def accumulate(pref, x0, x1, r, lo0, hi0, m0, s0, parity):
        for support in range(6):
            ge = [0] * 11
            for t in range(10):
                lo, hi = s3_ge_interval(h, x0, x1, r, t, lo0, hi0)
                if lo <= hi:
                    ge[t] = fullmod.interval_query(pref, r, lo, hi, support, parity)
            for t in range(10):
                value = ge[t] - ge[t + 1]
                if value:
                    mid[m0 + r][s0 + support][t] += value

    for x0 in range(h + 1):
        for x1 in range(x0 + 1, h + 1):
            c2 = h - x1
            c3 = h - x0
            m0 = x0 + x1
            s0 = 1 + int(x0 > 0)
            parity = x1 & 1
            for r in range(c2 + c3 + 1):
                lo = max(0, r - c3)
                hi = min(c2, r, (threshold - x1 + x0 + r) // 2)
                if lo <= hi:
                    accumulate(bc_pref, x0, x1, r, lo, hi, m0, s0, parity)

    for x0 in range(h + 1):
        ccap = h - x0
        m0 = 2 * x0
        s0 = 0 if x0 == 0 else 2
        parity = x0 & 1
        for r in range(2 * ccap + 1):
            lo = max(0, r - ccap)
            hi = min(ccap, r, (threshold + r) // 2)
            if lo <= hi:
                accumulate(lex_pref, x0, x0, r, lo, hi, m0, s0, parity)

    s0_capacity = component0_formula(d)
    out = [[[0] * 39 for _ in range(11)] for __ in range(3 * h + 1)]
    for m0, row in enumerate(mid):
        for s0, by_s3 in enumerate(row):
            if not any(by_s3):
                continue
            for a in range(h + 1):
                sa = component_a_formula(d, a)
                for support_a in range(4):
                    right = fullmod.triple_free_count(a, support_a)
                    if not right:
                        continue
                    for s3, left in enumerate(by_s3):
                        if left:
                            srem = s0_capacity + sa + s3
                            out[m0 + a][s0 + support_a][srem] += left * right
    return out


def count_witness_stratum(table):
    old = 0
    new = 0
    for mass, row in enumerate(table):
        if mass > WITNESS_E:
            break
        for support, by_srem in enumerate(row):
            for srem, count in enumerate(by_srem):
                if not count:
                    continue
                if support + min(38, WITNESS_E - mass) >= WITNESS_K:
                    old += count
                if support + min(srem, WITNESS_E - mass) >= WITNESS_K:
                    new += count
    return old, new


def validate_strict_witness() -> None:
    v = (0, 50, 50, 0, 0, 0, 0, 0, 0, 0)
    x0, x1, x2, x3, x5, x6, x7, x8, x9, x10 = v
    a = x2 + x3 + x7
    b = x1 + x5 + x9
    c = x0 + x6 + x8 + x10
    mass = sum(v)
    support = sum(int(x > 0) for x in v)
    h = WITNESS_D // 2
    if not (x0 < x1 and ((x1 + x8 + x9 + x10) & 1) == 0):
        raise ValueError("strict witness canonical/parity regression")
    if max(a, b, c) > h or b - c > WITNESS_THRESHOLD:
        raise ValueError("strict witness no longer survives N355/N356 prefix cuts")
    if support + min(38, WITNESS_E - mass) < WITNESS_K:
        raise ValueError("strict witness no longer survives N220")
    srem = support_suffix_capacity(WITNESS_D, a, b, c)
    if (a, b, c, mass, support, srem) != (50, 50, 0, 100, 2, 20):
        raise ValueError("strict witness invariant regression")
    if support + min(WITNESS_E - mass, srem) >= WITNESS_K:
        raise ValueError("strict witness is not rejected by N357")


def main() -> None:
    for path, expected in [
        (N355_FULL, EXPECTED_N355_FULL_BLOB),
        (N356_CONTRACT, EXPECTED_N356_CONTRACT_BLOB),
        (N356_RESULT, EXPECTED_N356_RESULT_BLOB),
    ]:
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual}!={expected}")

    result = json.loads(N356_RESULT.read_text())
    if result.get("canonical_sha256_without_this_field") != EXPECTED_N356_RESULT_CANONICAL:
        raise ValueError("N356 result canonical regression")
    if result.get("semantics", {}).get("main_pruning_credit") is not False:
        raise ValueError("N356 must remain no-credit at this N357 checkpoint")
    if result.get("status") != "AUDIT_CANDIDATE_TRANSPORT_NECESSARY_CUT_NO_MAIN_CREDIT":
        raise ValueError("N356 audit-candidate status regression")

    validate_flow_formulas()
    validate_strict_witness()

    fullmod = load_module(N355_FULL, "s32_n357_n355_full")
    table = build_support_exact(WITNESS_D // 2, WITNESS_THRESHOLD, fullmod)
    old, new = count_witness_stratum(table)
    if old != EXPECTED_N356_EXCEPTIONAL:
        raise ValueError(f"N356 witness-stratum count regression {old}")
    if new != EXPECTED_N357_EXCEPTIONAL:
        raise ValueError(f"N357 witness-stratum count regression {new}")
    diff = old - new
    if diff != EXPECTED_INCREMENTAL_EXCEPTIONAL:
        raise ValueError("N357 strict incremental exceptional count regression")
    normal = 19 * WITNESS_D - 5 * WITNESS_E + 1
    if normal != EXPECTED_NORMAL_BLOCK or diff * normal != EXPECTED_INCREMENTAL_TERMINALS:
        raise ValueError("N357 witness terminal multiplication regression")

    # K=48 boundary simplification.
    for d, expected in [
        (176, (83, 83, 84, 167)),
        (192, (91, 91, 92, 183)),
    ]:
        h = d // 2
        got = (h - 5, h - 5, h - 4, d - 9)
        if got != expected:
            raise ValueError("K=48 boundary corollary regression")

    print(json.dumps({
        "verdict": "PASS_N357_TRANSPORT_SUPPORT_CAPACITY_RESEARCH_CHECKPOINT",
        "n356_external_audit_still_required": True,
        "main_pruning_credit": False,
        "witness_stratum": [WITNESS_G, WITNESS_D, WITNESS_E],
        "n356_exceptional": old,
        "n357_exceptional": new,
        "incremental_exceptional_reject": diff,
        "incremental_terminal_reject": diff * normal,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
