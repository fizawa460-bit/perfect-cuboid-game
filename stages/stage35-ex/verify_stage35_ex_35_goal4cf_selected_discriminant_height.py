#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages" / "stage35-ex" / "35ex-35"
CERT_PATH = BASE / "goal4cf-selected-direction-minimal-discriminant-height.json"
SOURCE_PATH = BASE / "goal4cf-selected-direction-minimal-discriminant-height-source-lock.md"

EXPECTED_CANONICAL = "46207a23fc54745851db52e9090fe147772dfb22eff49875d01d42d3fab9667d"
EXPECTED_PARENT = "70520b10e7db7063b1d7a7b75485533c131fe9f5"
EXPECTED_SOURCE_LF = "5e3dc56dc751795095f142765e0b4d4dd31e95c7f9a348a5176ea17f3e9cb88b"


def lf_bytes(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def sha256_lf(path: Path) -> str:
    return hashlib.sha256(lf_bytes(path)).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    head = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(head + raw).hexdigest()


def canonical_sha(data: dict) -> str:
    payload = dict(data)
    payload.pop("canonical_sha256", None)
    raw = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


# Tiny exact polynomial ring for symbolic identities.
# Monomials are tuples of nonnegative exponents.
def p_const(nvars: int, q) -> dict[tuple[int, ...], Fraction]:
    q = Fraction(q)
    return {} if q == 0 else {(0,) * nvars: q}


def p_var(nvars: int, idx: int) -> dict[tuple[int, ...], Fraction]:
    e = [0] * nvars
    e[idx] = 1
    return {tuple(e): Fraction(1)}


def p_add(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Fraction(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def p_neg(a):
    return {m: -c for m, c in a.items()}


def p_sub(a, b):
    return p_add(a, p_neg(b))


def p_scale(a, q):
    q = Fraction(q)
    return {m: c * q for m, c in a.items() if c * q}


def p_mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, Fraction(0)) + ca * cb
            if out[m] == 0:
                del out[m]
    return out


def p_pow(a, n: int):
    nvars = len(next(iter(a))) if a else 1
    out = p_const(nvars, 1)
    base = a
    while n:
        if n & 1:
            out = p_mul(out, base)
        base = p_mul(base, base)
        n >>= 1
    return out


def symbolic_checks() -> None:
    # R=r^2, S=s^2. General Weierstrass invariants of CF-2.
    R, S = p_var(2, 0), p_var(2, 1)
    one = p_const(2, 1)
    a1 = one
    a2 = p_scale(p_sub(p_sub(R, S), one), Fraction(1, 4))
    a3 = p_const(2, 0)
    a4 = p_scale(p_mul(R, S), Fraction(-1, 16))
    a6 = p_const(2, 0)

    b2 = p_add(p_pow(a1, 2), p_scale(a2, 4))
    b4 = p_add(p_scale(a4, 2), p_mul(a1, a3))
    b6 = p_add(p_pow(a3, 2), p_scale(a6, 4))
    b8 = p_add(
        p_add(p_mul(p_pow(a1, 2), a6), p_scale(p_mul(a2, a6), 4)),
        p_add(
            p_add(p_neg(p_mul(p_mul(a1, a3), a4)), p_mul(a2, p_pow(a3, 2))),
            p_neg(p_pow(a4, 2)),
        ),
    )
    c4 = p_sub(p_pow(b2, 2), p_scale(b4, 24))
    delta = p_add(
        p_add(p_neg(p_mul(p_pow(b2, 2), b8)), p_scale(p_pow(b4, 3), -8)),
        p_add(p_scale(p_pow(b6, 2), -27), p_scale(p_mul(p_mul(b2, b4), b6), 9)),
    )

    target_c4 = p_add(p_add(p_pow(R, 2), p_mul(R, S)), p_pow(S, 2))
    target_delta = p_scale(
        p_mul(p_mul(p_pow(R, 2), p_pow(S, 2)), p_pow(p_add(R, S), 2)),
        Fraction(1, 256),
    )
    assert c4 == target_c4
    assert delta == target_delta

    # Explicit x=4u, y=8v+4u transformation.
    # Variables U,V,R,S.
    U, V, R4, S4 = [p_var(4, i) for i in range(4)]
    lhs_raw = p_pow(p_add(p_scale(V, 8), p_scale(U, 4)), 2)
    rhs_raw = p_mul(
        p_scale(U, 4),
        p_mul(p_sub(p_scale(U, 4), S4), p_add(p_scale(U, 4), R4)),
    )
    transformed = p_sub(lhs_raw, rhs_raw)
    minimal64 = p_add(
        p_add(p_scale(p_pow(V, 2), 64), p_scale(p_mul(U, V), 64)),
        p_add(
            p_scale(p_pow(U, 3), -64),
            p_add(
                p_scale(
                    p_mul(p_add(p_sub(p_const(4, 1), R4), S4), p_pow(U, 2)),
                    16,
                ),
                p_scale(p_mul(p_mul(R4, S4), U), 4),
            ),
        ),
    )
    assert transformed == minimal64

    # Pythagorean parameter identity in b,c.
    B, C = p_var(2, 0), p_var(2, 1)
    r = p_sub(p_pow(C, 2), p_pow(B, 2))
    s = p_scale(p_mul(B, C), 2)
    t = p_add(p_pow(B, 2), p_pow(C, 2))
    assert p_add(p_pow(r, 2), p_pow(s, 2)) == p_pow(t, 2)

    # CF-4 factorization in h,k.
    H, K = p_var(2, 0), p_var(2, 1)
    left = p_sub(
        p_mul(K, p_sub(p_pow(H, 2), p_pow(K, 2))),
        p_sub(p_pow(H, 2), p_const(2, 1)),
    )
    right = p_mul(
        p_sub(K, p_const(2, 1)),
        p_sub(
            p_sub(p_sub(p_pow(H, 2), p_pow(K, 2)), K),
            p_const(2, 1),
        ),
    )
    assert left == right

    assert 12288 * (2 ** 10) == 12582912


def pair_height(a: int, b: int) -> int:
    return max(a, b) // math.gcd(a, b)


def selected_pair(A: int, B: int, C: int):
    items = [
        ("AB", "C", A, B, pair_height(A, B)),
        ("AC", "B", A, C, pair_height(A, C)),
        ("BC", "A", B, C, pair_height(B, C)),
    ]
    best = max(x[4] for x in items)
    # Fixed tie order is already AB, AC, BC.
    return next(x for x in items if x[4] == best), [x[4] for x in items]


def reduced_legs(a: int, b: int):
    g = math.gcd(a, b)
    return a // g, b // g


def model_data(b: int, c: int):
    assert math.gcd(b, c) == 1 and (b + c) % 2 == 1 and b != c
    r = c * c - b * b
    s = 2 * b * c
    t = b * b + c * c
    assert r * r + s * s == t * t
    assert r & 1 and t & 1 and s % 4 == 0
    assert math.gcd(abs(r), s) == 1
    assert math.gcd(abs(r), t) == 1
    assert math.gcd(s, t) == 1
    a2 = (r * r - s * s - 1) // 4
    a4 = -(r * r * s * s) // 16
    c4 = r**4 + r*r*s*s + s**4
    delta_num = (abs(r) * s * t) ** 4
    assert delta_num % 256 == 0
    delta = delta_num // 256
    # c4 is a unit at every bad prime; at 2 it is odd.
    assert c4 & 1
    assert math.gcd(c4, abs(r) * s * t) == 1
    # General Weierstrass formulas specialized numerically.
    b2 = 1 + 4 * a2
    b4 = 2 * a4
    b6 = 0
    b8 = -(a4 * a4)
    c4_check = b2*b2 - 24*b4
    delta_check = -(b2*b2)*b8 - 8*(b4**3) - 27*(b6**2) + 9*b2*b4*b6
    assert c4_check == c4
    assert delta_check == delta
    return r, s, t, [1, a2, 0, a4, 0], delta


def bounded_regressions(cert: dict) -> None:
    br = cert["bounded_regression"]

    triple_count = 0
    for A in range(1, 61):
        for B in range(A, 61):
            for C in range(B, 61):
                if math.gcd(math.gcd(A, B), C) != 1:
                    continue
                triple_count += 1
                (pair, orient, x, y, hstar), hs = selected_pair(A, B, C)
                M = C
                assert hstar * hstar >= M
                W2 = A*A + B*B + C*C
                assert W2 <= 3 * M * M
    assert triple_count == br["triple_count"] == 31079

    pair_count = 0
    for k in range(1, 501):
        for h in range(k + 1, 501):
            if math.gcd(k, h) != 1 or (k + h) % 2 != 1:
                continue
            pair_count += 1
            # CF-4 and positivity.
            assert k*(h*h-k*k) - (h*h-1) == (k-1)*(h*h-k*k-k-1)
            assert h*h-k*k-k-1 >= 1
            r, s, t, ainvs, delta = model_data(k, h)
            assert 4096 * delta >= 81 * (h ** 20)
    assert pair_count == br["pair_count"] == 50765

    for row in br["euler_brick_diagnostics"]:
        A, B, C = row["edges"]
        assert math.gcd(math.gcd(A, B), C) == 1
        # Verify all three face diagonals are integral.
        for x, y in ((A, B), (A, C), (B, C)):
            n = x*x + y*y
            z = math.isqrt(n)
            assert z*z == n
        W2 = A*A + B*B + C*C
        assert W2 == row["W_squared"]
        assert (math.isqrt(W2) ** 2 == W2) == row["W_is_integer"]

        selected, heights = selected_pair(A, B, C)
        pair, orient, x, y, hstar = selected
        assert heights == row["pair_heights"]
        assert pair == row["selected"]["pair"]
        assert orient == row["selected"]["orientation"]
        b, c = reduced_legs(x, y)
        assert max(b, c) == row["selected"]["height"]
        r, s, t, ainvs, delta = model_data(b, c)
        assert [abs(r), s, t] == row["selected"]["r_s_t"]
        assert ainvs == row["selected"]["minimal_ainvs"]
        assert delta == row["selected"]["minimal_discriminant"]
        assert 12288 * delta >= W2 ** 5

    # Primitive hypothesis is essential: reduced pair heights are scale-invariant
    # while max(A,B,C) grows under common scaling.
    A, B, C = br["euler_brick_diagnostics"][0]["edges"]
    selected, _ = selected_pair(A, B, C)
    hstar = selected[4]
    scale = hstar*hstar // max(A, B, C) + 1
    selected_scaled, _ = selected_pair(scale*A, scale*B, scale*C)
    assert selected_scaled[4] == hstar
    assert hstar*hstar < scale * max(A, B, C)


def verify_source_locks(cert: dict) -> None:
    locks = cert["source_locks"]
    for rel, lock in locks.items():
        path = ROOT / rel
        assert path.is_file(), f"missing source lock: {rel}"
        if "text_lf_sha256" in lock:
            actual = sha256_lf(path)
            assert actual == lock["text_lf_sha256"], (rel, actual, lock["text_lf_sha256"])
        if "parent_blob_sha1" in lock:
            actual_blob = git_blob_sha1(path)
            assert actual_blob == lock["parent_blob_sha1"], (
                rel,
                actual_blob,
                lock["parent_blob_sha1"],
            )


def verify_contract(cert: dict) -> None:
    assert cert["schema"] == "STAGE35_EX_GOAL4CF_SELECTED_DISCRIMINANT_HEIGHT_V1"
    assert cert["status"] == (
        "PROVISIONAL_EXACT_QUANTITATIVE_ADAPTER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT"
    )
    assert cert["parent_retained_head"] == EXPECTED_PARENT
    assert cert["authority"]["mathematical_state"] == "V74/Goal4AK"
    assert cert["authority"]["review"] == 5142248509
    assert cert["authority"]["intermediate_checkpoint"] == "Goal4BS"
    assert cert["authority"]["intermediate_review"] == 5151846948
    assert cert["authority"]["closed_unmerged_pr"] == 1723

    assert cert["canonical_sha256"] == EXPECTED_CANONICAL
    assert canonical_sha(cert) == EXPECTED_CANONICAL
    assert sha256_lf(SOURCE_PATH) == EXPECTED_SOURCE_LF

    r = cert["result"]
    assert r["exact_minimal_discriminant"] == "(r*s*t)^4/256"
    assert r["pair_lower_bound"] == "4096*abs(Delta_min)>=81*h^20"
    assert r["endpoint_bound"] == "12288*abs(Delta_min(E_*))>=W^10"
    assert r["new_global_minimal_model"] is True
    assert r["new_selected_direction_height_adapter"] is True

    cycle = cert["cycle"]
    assert cycle["route_status"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
    assert cycle["live_candidates"] == 1
    assert cycle["untested_candidates"] == 0
    assert cycle["parking_audit_complete"] is False
    assert cert["next"] == "SELECTED_PHYSICAL_MARKED_LOCAL_HEIGHT_COMPARISON_PREFLIGHT"

    fw = cert["credit_firewall"]
    required_false = [
        "fixed_direction_AW_C2_discharged",
        "arbitrary_cutoff_lower_bound",
        "explicit_canonical_height_upper_constant",
        "uniform_szpiro_bound",
        "strict_canonical_height_coefficient_win",
        "finite_height_reduction",
        "E1_proved",
        "R29_PESCH_E1_closed",
        "stage35_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "hostile_audit_pass",
        "merge_authorized",
    ]
    for key in required_false:
        assert fw[key] is False, key

    src = SOURCE_PATH.read_text(encoding="utf-8")
    required_snippets = [
        "|Delta_min(E_*)| >= (81/4096)*M^10",
        ">= W^10/12288",
        "FIXED_DIRECTION_AW_C2_DISCHARGED=false",
        "UNIFORM_SZPIRO_BOUND=false",
        "E1_proved=false",
        "No merge. MAIN-STATE remains V74 / Goal4AK.",
    ]
    for snippet in required_snippets:
        assert snippet in src, snippet


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    verify_contract(cert)
    verify_source_locks(cert)
    symbolic_checks()
    bounded_regressions(cert)
    print("PASS Goal4CF selected-direction minimal-discriminant height checkpoint")
    print("canonical_sha256", cert["canonical_sha256"])
    print("triple_count", cert["bounded_regression"]["triple_count"])
    print("pair_count", cert["bounded_regression"]["pair_count"])
    print("next", cert["next"])


if __name__ == "__main__":
    main()
