#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-29.

The asymptotic proof is in result.md.  This script checks the exact common-core
quadratic congruence and bad-coefficient peeling on finite physical packets,
verifies the primitive root-line spacing lemma exhaustively on small boxes, and
locks the exact exponent cancellation leading to 3/4.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


s28 = load_module(
    "stage14_s728_s729",
    SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py",
)
ch = s28.ch


def v2(n: int) -> int:
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def oddpart(n: int) -> int:
    return n >> v2(n)


def factor_prime_powers(n: int):
    assert n >= 1
    out = []
    x = n
    p = 3
    while p * p <= x:
        if x % p:
            p += 2
            continue
        e = 0
        pe = 1
        while x % p == 0:
            x //= p
            e += 1
            pe *= p
        out.append((p, e, pe))
        p += 2
    if x > 1:
        out.append((x, 1, x))
    return out


def omega(n: int) -> int:
    return len(factor_prime_powers(n))


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    d = s28.packet_data(a_state, b_state)
    s28.audit_reconstruction(d)

    C, u_res, v_res = d["triple"]
    r = int(d["r"])
    s = int(d["s"])
    U = int(d["lx_plus"])
    V = int(d["lx_minus"])
    a = int(d["cx_plus"])
    b = int(d["cx_minus"])
    hk_plus = int(d["hs"][0])

    assert gcd(U, V) == 1
    assert U * V == oddpart(int(d["X_ag"]))
    assert gcd(C, U * V) == 1
    assert hk_plus == (a * a * U * U + b * b * V * V) // 2
    assert (a * a * U * U + b * b * V * V) % C == 0

    g = gcd(a, b)
    assert oddpart(r * s) % oddpart(g) == 0
    a0 = a // g
    b0 = b // g
    assert gcd(a0, b0) == 1

    C_bad = gcd(C, g * g)
    C0 = C // C_bad
    assert C_bad <= g * g
    assert (a0 * a0 * U * U + b0 * b0 * V * V) % C0 == 0
    assert gcd(C0, a0 * b0 * U * V) == 1

    # The observed primitive pair lies on one of the Gaussian CRT root lines.
    if C0 > 1:
        rho = (U * pow(V, -1, C0)) % C0
        assert (a0 * a0 * rho * rho + b0 * b0) % C0 == 0
        for p, e, pe in factor_prime_powers(C0):
            assert p % 4 == 1
            z = (a0 * U * pow((b0 * V) % pe, -1, pe)) % pe
            assert (z * z + 1) % pe == 0

    return C, C0, U, V, u_res, v_res


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    nontrivial_C0 = 0
    max_bad = 1
    max_root_count = 1

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                C, C0, U, V, u_res, v_res = audit_packet(a_state, b_state)
                nontrivial_C0 += int(C0 > 1)
                max_bad = max(max_bad, C // C0)
                max_root_count = max(max_root_count, 2 ** omega(C0))
                checked += 1

    assert checked > 0
    return checked, nontrivial_C0, max_bad, max_root_count


def primitive_line_box_bound_audit() -> None:
    # Synthetic exhaustive regression of the exact dyadic spacing lemma.
    # The proof itself is the determinant-spacing argument in result.md.
    for q in range(1, 80, 2):
        for rho in range(q):
            if gcd(rho, q) != 1:
                continue
            for U0 in range(1, 11):
                for V0 in range(1, 11):
                    count = 0
                    for U in range(U0 + 1, 2 * U0 + 1):
                        for V in range(V0 + 1, 2 * V0 + 1):
                            if gcd(U, V) != 1:
                                continue
                            if (U - rho * V) % q == 0:
                                count += 1
                    # count <= 1 + 6 U0 V0/q, written without floats.
                    assert count * q <= q + 6 * U0 * V0


def exponent_ledger_audit() -> None:
    # Exact Fraction ledger over the whole surviving 4cg balanced grid.
    vals = [Fraction(n, 64) for n in range(8, 21)]
    saw = 0
    for theta in vals:
        if not (Fraction(3, 16) <= theta <= Fraction(5, 16)):
            continue
        for phi in vals:
            if not (Fraction(1, 8) <= phi <= Fraction(1, 4)):
                continue
            if theta < phi:
                continue
            if theta - phi > Fraction(1, 8):
                continue
            if theta + phi < Fraction(3, 8):
                continue

            cmax = 2 * theta + 2 * phi - Fraction(3, 4)
            assert cmax >= 0
            # Worst c is enough: 2phi-c is minimized at cmax.
            assert 2 * phi - cmax == Fraction(3, 4) - 2 * theta
            assert 2 * phi - cmax >= Fraction(1, 8)

            residual = cmax + Fraction(1, 4)
            primitive_pair = 2 * phi - cmax
            total = residual + primitive_pair
            assert total == 2 * phi + Fraction(1, 4)
            assert total <= Fraction(3, 4)
            saw += 1
    assert saw > 0


def boundary_audit() -> None:
    root = HERE.parents[4]
    cg = (root / "stages/stage14/14-4cg/result.md").read_text()
    s27 = (root / "stages/stage14/14-s7-27/result.md").read_text()
    s28_text = (root / "stages/stage14/14-s7-28/result.md").read_text()
    cn = (root / "stages/stage14/14-4cn/result.md").read_text()
    t66 = (root / "stages/stage14/14-t66/result.md").read_text()

    assert "gcd(C, oddpart(Xi_agree))=1" in cg
    assert "REDUCED_RESIDUAL_PRODUCT_MAX_EXPONENT=1/4" in cg
    assert "FIXED_RESIDUAL_FULL_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1" in s27
    assert "STAGE14_S7_28=COMPLETE_RATIO_SINGULAR_CLASSIFICATION_AND_PRIMITIVE_MODULUS_PAIR_RECONSTRUCTION" in s28_text
    assert "ABSOLUTE_MODULUS_SCALE_DEFECT=1" in s28_text
    assert "XI_SWITCH_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true" in s28_text
    assert "MAINLINE_H_REQUESTED_OBJECT=PhysicalReciprocalEdwardsGenusOneAverageIncidence" in cn
    assert "TH18_REQUESTED_OBJECT=CanonicalPrimeTaggedOppositeSignQuadraticRootLargeSieve" in t66


def main() -> None:
    boundary_audit()
    primitive_line_box_bound_audit()
    exponent_ledger_audit()
    checked, nontrivial, max_bad, max_roots = finite_physical_audit()

    print("Stage14-s7-29 common-core primitive root-line audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite packets with nontrivial good common-core modulus: {nontrivial}")
    print(f"max finite peeled bad common-core factor: {max_bad}")
    print(f"max finite Gaussian CRT root-line count: {max_roots}")
    print("common core -> Gaussian primitive root lines: exact")
    print("primitive dyadic root-line count <= 1+6UV/q: exhaustive regression PASS")
    print("residual exponent c+1/4 plus primitive-pair exponent 2phi-c: exact cancellation")
    print("uniform surviving-block exponent <= 3/4")
    print("new whole-family physical upper-bound exponent: 3/4")
    print("s7-29 auxiliary H needed: false")


if __name__ == "__main__":
    main()
