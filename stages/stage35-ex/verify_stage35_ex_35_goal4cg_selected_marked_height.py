#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages" / "stage35-ex" / "35ex-35"
CERT_PATH = BASE / "goal4cg-selected-physical-marked-local-height-comparison.json"
SOURCE_PATH = BASE / "goal4cg-selected-physical-marked-local-height-comparison-source-lock.md"

EXPECTED_CANONICAL = "d7eb73b45871c66e2c0ded5c566ae2c6f5e914483419d31823ab2f99e6ad13de"
EXPECTED_SOURCE_LF = "8528b2b818dd505c277372dd44a313e60399e7361503d753376d2899a7010e44"
EXPECTED_PARENT = "2ffe07f31d56caf78261d032b7e5a78d500dd146"


def lf_bytes(path: Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def sha256_lf(path: Path) -> str:
    return hashlib.sha256(lf_bytes(path)).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def canonical_sha(data: dict) -> str:
    payload = dict(data)
    payload.pop("canonical_sha256", None)
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def diag(x: int, y: int) -> int:
    n = x * x + y * y
    d = math.isqrt(n)
    assert d * d == n, (x, y, n)
    return d


def pair_height(x: int, y: int) -> int:
    return max(x, y) // math.gcd(x, y)


def selected_pair(A: int, B: int, C: int):
    rows = [
        ("AB", "C", A, B, pair_height(A, B)),
        ("AC", "B", A, C, pair_height(A, C)),
        ("BC", "A", B, C, pair_height(B, C)),
    ]
    best = max(row[4] for row in rows)
    return next(row for row in rows if row[4] == best)


def oriented_data(A: int, B: int, C: int, pair: str):
    if pair == "AB":
        g = math.gcd(A, B)
        m, n, K = A // g, B // g, C
        dm, dn = diag(A, C), diag(B, C)
    elif pair == "AC":
        g = math.gcd(A, C)
        m, n, K = C // g, A // g, B
        dm, dn = diag(C, B), diag(A, B)
    elif pair == "BC":
        g = math.gcd(B, C)
        m, n, K = B // g, C // g, A
        dm, dn = diag(B, A), diag(C, A)
    else:
        raise AssertionError(pair)
    assert math.gcd(m, n) == 1
    assert (m + n) % 2 == 1
    return g, m, n, K, dm, dn


def marked_u(g: int, m: int, n: int, K: int, dm: int, dn: int) -> Fraction:
    r = n * n - m * m
    denominator = 2 * (m * dm - n * dn)
    assert denominator != 0
    return Fraction(-m * n * r * (n * dm + m * dn), denominator)


def rad_odd(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    out = 1
    p = 3
    while p * p <= n:
        if n % p == 0:
            out *= p
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out *= n
    return out


def v2(n: int) -> int:
    n = abs(n)
    e = 0
    while n and n % 2 == 0:
        e += 1
        n //= 2
    return e


def verify_source_locks(cert: dict) -> None:
    for rel, lock in cert["source_locks"].items():
        path = ROOT / rel
        assert path.is_file(), f"missing source lock: {rel}"
        if "parent_blob_sha1" in lock:
            actual = git_blob_sha1(path)
            assert actual == lock["parent_blob_sha1"], (rel, actual, lock["parent_blob_sha1"])
        if "text_lf_sha256" in lock:
            actual = sha256_lf(path)
            assert actual == lock["text_lf_sha256"], (rel, actual, lock["text_lf_sha256"])


def verify_bricks(cert: dict) -> None:
    for row in cert["bounded_regression"]["euler_brick_diagnostics"]:
        A, B, C = row["edges"]
        pair, orient, _, _, _ = selected_pair(A, B, C)
        assert pair == row["selected_pair"]
        assert orient == row["orientation"]
        g, m, n, K, dm, dn = oriented_data(A, B, C, pair)
        assert [m, n] == row["oriented_legs"]

        r, s, t = n * n - m * m, 2 * m * n, m * m + n * n
        assert r * r + s * s == t * t
        p = Fraction(-m, n)
        assert (p * p - 1) / (2 * p) == Fraction(r, s)

        W2 = A * A + B * B + C * C
        assert W2 == row["W_squared"]
        assert (m * dm - n * dn) * (m * dm + n * dn) == -r * W2

        u = marked_u(g, m, n, K, dm, dn)
        assert u == Fraction(row["u_num"], row["u_den"])
        H = max(abs(u.numerator), u.denominator)
        assert H <= W2 ** 3

        z = Fraction(dm, dn)
        c0 = (p * p - 1) / (2 * p * p)
        X = c0 * (z - p) / (z + 1 / p)
        X_formula = Fraction(-r, 2 * m * n) * Fraction(n * dm + m * dn, m * dm - n * dn)
        assert X == X_formula
        assert Fraction(s * s, 4) * X == u

        b2 = r * r - s * s
        b4 = Fraction(-r * r * s * s, 8)
        assert b2 == 1 + 4 * ((r * r - s * s - 1) // 4)
        assert b4 == 2 * Fraction(-r * r * s * s, 16)
        C1 = Fraction(1) + Fraction(r * r * s * s, 8) + Fraction(r ** 4 * s ** 4, 256)
        C2 = 4 + abs(r * r - s * s) + Fraction(r * r * s * s, 4)
        assert max(C1, C2) <= W2 ** 8


def verify_conductor_panel(cert: dict) -> None:
    count = 0
    for m in range(1, 99):
        for n in range(m + 1, 100):
            if math.gcd(m, n) != 1 or (m + n) % 2 != 1:
                continue
            count += 1
            r = n * n - m * m
            s = 2 * m * n
            t = m * m + n * n
            assert r & 1 and t & 1 and s % 4 == 0
            R = abs(r * s * t)
            e = v2(s)
            assert e >= 2 and R % 4 == 0
            c4 = r ** 4 + r * r * s * s + s ** 4
            assert c4 & 1
            assert math.gcd(c4, R) == 1
            N = rad_odd(R) if e == 2 else 2 * rad_odd(R)
            assert 1 < N <= R // 4
            delta = (R // 4) ** 4
            assert math.log(delta) / math.log(N) >= 4 - 1e-12
    expected = cert["bounded_regression"]["conductor_pair_panel"]["pair_count"]
    assert count == expected == 2000


def verify_contract(cert: dict) -> None:
    assert cert["schema"] == "STAGE35_EX_GOAL4CG_SELECTED_MARKED_HEIGHT_V1"
    assert cert["status"] == "PROVISIONAL_EXACT_EXPLICIT_UPPER_AND_PETSCHE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT"
    assert cert["parent_goal4cf_head"] == EXPECTED_PARENT
    assert cert["canonical_sha256"] == EXPECTED_CANONICAL
    assert canonical_sha(cert) == EXPECTED_CANONICAL
    assert sha256_lf(SOURCE_PATH) == EXPECTED_SOURCE_LF

    assert cert["height_upper"]["naive_x"] == "h_x(P_*)<=6 log W"
    assert cert["height_upper"]["canonical"] == "hhat(P_*)<=17/3 log W"
    assert abs(cert["height_upper"]["explicit_upper_coefficient"] - 17 / 3) < 1e-15

    pc = cert["petsche_comparison"]
    best = 10 / (10 ** 15 * 4 ** 6 * math.log(104613 * 16) ** 2)
    assert abs(pc["best_case_logW_coefficient"] - best) < 1e-35
    assert best < 1.19e-20
    assert best < 17 / 3
    assert pc["strict_coefficient_win"] is False

    assert cert["semistable_conductor"]["szpiro_lower"] == "sigma(E_*)>=4"
    assert cert["semistable_conductor"]["uniform_szpiro_upper_obtained"] is False
    assert cert["local_component_blocker"]["name"] == "UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL"
    assert cert["result"]["route_status"] == "BLOCKED_EXPLICIT_UPPER_OBTAINED_NO_LOWER_COEFFICIENT_WIN"
    assert cert["cycle"]["active_receiver"] == "NONE_PENDING_HOSTILE_AUDIT"
    assert cert["cycle"]["next"] == "HOSTILE_AUDIT_GOAL4CG_THEN_BREADTH_REOPEN"

    fw = cert["credit_firewall"]
    assert all(fw[k] is False for k in (
        "E1_proved", "R29_PESCH_E1_closed", "stage35_closed",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
        "hostile_audit_pass", "merge_authorized",
    ))


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    verify_contract(cert)
    verify_source_locks(cert)
    verify_bricks(cert)
    verify_conductor_panel(cert)
    print("PASS Stage35-EX Goal4CG selected marked-height audit checkpoint")
    print(f"canonical_sha256={EXPECTED_CANONICAL}")
    print("explicit_upper=hhat(P_*)<=17/3 log W")
    print("petsche_cf_strict_coefficient_win=false")
    print("next=HOSTILE_AUDIT_GOAL4CG_THEN_BREADTH_REOPEN")


if __name__ == "__main__":
    main()
