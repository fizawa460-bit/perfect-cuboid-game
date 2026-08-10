#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-11.

Checks:
- merged s7-10 / 4by current 13/14 boundaries;
- exact 3-cell -> 2-cell quotient identity;
- exact 4-cell -> 2-cell quotient identity and torus kernels;
- exact finite-field Fourier-fiber formulas on the multiplicative torus;
- ideal d-cell square-sieve exponent ledger;
- exact 13/14 minimax barrier and optimistic 3/4-cell regressions;
- logical countermodel showing several bounds for one condition do not multiply.

No new external theorem is introduced here.
"""
from cmath import exp, pi
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
S710 = ROOT / "stages/stage14/14-s7-10/result.md"
R4BY = ROOT / "stages/stage14/14-4by/result.md"


def audit_merged_boundaries():
    s710 = S710.read_text()
    for flag in [
        "STAGE14_S7_10=COMPLETE_UNIFORM_ADJACENT_TWO_CELL_MIXED_FOURIER_AND_13_14_BOUND",
        "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true",
        "TWO_CELL_RECTANGLE_EXPONENT=2/3",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14",
    ]:
        assert flag in s710, flag

    r4by = R4BY.read_text()
    for flag in [
        "STAGE14_4BY=FU_GAUSS_LIFT_TWO_CELL_MIXED_TRANSFORM_AND_13_14_BOUND",
        "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true",
        "ADJACENT_TWO_CELL_RECTANGLE_EXPONENT=2/3",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14",
    ]:
        assert flag in r4by, flag
    return True


def H2_frac(R, Q):
    return (1 - R * R * Q * Q) * (Q * Q - R * R)


def G3_int(R, S, T):
    return (T*T - R*R*S*S) * (S*S - R*R*T*T)


def G4_int(r, s, t, j):
    return ((t*j)**2 - (r*s)**2) * ((s*j)**2 - (r*t)**2)


def audit_quotient_identities():
    samples = [
        (2, 3, 5),
        (3, 4, 7),
        (5, 2, 9),
        (7, 11, 13),
    ]
    for R, S, T in samples:
        q = Fraction(S, T)
        lhs = Fraction(G3_int(R, S, T), 1)
        rhs = T**4 * H2_frac(Fraction(R, 1), q)
        assert lhs == rhs
        for lam in [2, 3, 5]:
            assert G3_int(R, lam*S, lam*T) == lam**4 * G3_int(R, S, T)

    samples4 = [
        (2, 3, 5, 7),
        (3, 5, 7, 11),
        (5, 2, 11, 13),
        (7, 11, 13, 17),
    ]
    for r, s, t, j in samples4:
        alpha = Fraction(r, j)
        beta = Fraction(s, t)
        lhs = Fraction(G4_int(r, s, t, j), 1)
        rhs = (t*j)**4 * H2_frac(alpha, beta)
        assert lhs == rhs
        for a0, b0 in [(2, 3), (3, 5), (5, 2)]:
            scaled = G4_int(a0*r, b0*s, b0*t, a0*j)
            assert scaled == (a0*b0)**4 * G4_int(r, s, t, j)
    return len(samples), len(samples4)


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1


def e_p(x, p):
    return exp(2j*pi*(x % p)/p)


def H2_mod(R, Q, p):
    return ((1 - R*R*Q*Q) * (Q*Q - R*R)) % p


def G3_mod(R, S, T, p):
    return ((T*T - R*R*S*S) * (S*S - R*R*T*T)) % p


def G4_mod(r, s, t, j, p):
    return (((t*j)**2 - (r*s)**2) * ((s*j)**2 - (r*t)**2)) % p


def f2_partial(p, h):
    total = 0j
    for R in range(1, p):
        for q in range(1, p):
            total += chi(H2_mod(R, q, p), p) * e_p(h*R, p)
    return total


def f2_slice(p, h, q):
    total = 0j
    for R in range(1, p):
        total += chi(H2_mod(R, q, p), p) * e_p(h*R, p)
    return total


def t3_direct(p, h, k, ell):
    total = 0j
    for R in range(1, p):
        for S in range(1, p):
            for T in range(1, p):
                total += chi(G3_mod(R, S, T, p), p) * e_p(h*R+k*S+ell*T, p)
    return total


def t3_formula(p, h, k, ell):
    partial = f2_partial(p, h)
    if k % p:
        q0 = (-ell * pow(k, -1, p)) % p
        if q0:
            return p * f2_slice(p, h, q0) - partial
        return -partial
    if ell % p:
        return -partial
    return (p-1) * partial


def A(c, p):
    return (p-1) if c % p == 0 else -1


def t4_direct(p, hr, hs, ht, hj):
    total = 0j
    for r in range(1, p):
        for s in range(1, p):
            for t in range(1, p):
                for j in range(1, p):
                    total += chi(G4_mod(r, s, t, j, p), p) * e_p(hr*r+hs*s+ht*t+hj*j, p)
    return total


def t4_formula(p, hr, hs, ht, hj):
    total = 0j
    for alpha in range(1, p):
        for beta in range(1, p):
            f = chi(H2_mod(alpha, beta, p), p)
            total += f * A(hr*alpha+hj, p) * A(hs*beta+ht, p)
    return total


def audit_fourier_fibers():
    checks3 = 0
    checks4 = 0
    for p in [7, 11]:
        triples = [
            (1, 2, 3),
            (2, 0, 0),
            (3, 4, 0),
            (1, 0, 5),
        ]
        for h, k, ell in triples:
            got = t3_direct(p, h, k, ell)
            want = t3_formula(p, h, k, ell)
            assert abs(got-want) < 1e-7, (p, h, k, ell, got, want)
            checks3 += 1

        quads = [
            (1, 2, 3, 4),
            (1, 0, 2, 0),
            (0, 1, 2, 3),
            (2, 3, 0, 0),
        ]
        for hr, hs, ht, hj in quads:
            got = t4_direct(p, hr, hs, ht, hj)
            want = t4_formula(p, hr, hs, ht, hj)
            assert abs(got-want) < 1e-7, (p, hr, hs, ht, hj, got, want)
            checks4 += 1

    # The exact formula shows an entire torus-fiber multiplier on the
    # frequency plane k=ell=0. Verify the inherited two-cell axis is genuinely
    # nonzero on a finite regression sample; this is evidence of the visible
    # exceptional stratum, not an asymptotic lower-bound theorem.
    p = 7
    partial = f2_partial(p, 1)
    assert abs(partial) > 1e-6
    assert abs(t3_formula(p, 1, 0, 0) - (p-1)*partial) < 1e-7
    return checks3, checks4


def audit_ideal_square_sieve_ledger():
    out = {}
    for d in range(1, 5):
        saving = Fraction(1, d+1)
        count_exp = Fraction(d, d+1)
        assert count_exp + saving == 1
        out[d] = (count_exp, saving)
    assert out[1][1] == Fraction(1, 2)
    assert out[2][1] == Fraction(1, 3)
    assert out[3][1] == Fraction(1, 4)
    assert out[4][1] == Fraction(1, 5)
    assert out[2][1] > out[3][1] > out[4][1]
    return out


def minimax_lower_bound(gamma):
    # Thick exponent alpha=4/5. If all branches <=E, then
    # nu <= 3E/2-1,
    # tau >= 5/4(1-E),
    # nu >= 2tau + (1-E)/gamma.
    Acoef = Fraction(5, 2) + 1/gamma
    # Acoef*(1-E) <= 3E/2 - 1
    # => E >= (Acoef+1)/(Acoef+3/2)
    return (Acoef + 1) / (Acoef + Fraction(3, 2))


def audit_current_barrier():
    lam = Fraction(13, 28)
    nu = Fraction(11, 28)
    tau = Fraction(5, 56)
    target = Fraction(13, 14)

    E1 = 2*lam
    E2 = 1 + nu - lam
    E3 = 1 - Fraction(4, 5)*tau
    E4 = 1 - (nu - 2*tau)/3
    E5 = 1 - (lam - 2*tau)/3

    assert E1 == E2 == E3 == E4 == target
    assert E5 == Fraction(19, 21) < target
    assert minimax_lower_bound(Fraction(1, 3)) == target

    ideal3 = minimax_lower_bound(Fraction(1, 4))
    ideal4 = minimax_lower_bound(Fraction(1, 5))
    assert ideal3 == Fraction(15, 16)
    assert ideal4 == Fraction(17, 18)
    assert ideal3 > target and ideal4 > target

    assert target - Fraction(1, 2) == Fraction(3, 7)
    return target, ideal3, ideal4, E5


def audit_nonmultiplication_countermodel():
    # Several valid N^(2/3) upper bounds for the same condition can all be
    # saturated by one and the same subset. Hence their intersection need not
    # gain another power.
    N = 729
    M = 81  # N^(2/3)
    assert M**3 == N**2
    universe = set(range(N))
    exceptional = set(range(M))
    receiver_a = exceptional.copy()
    receiver_b = exceptional.copy()
    receiver_c = exceptional.copy()
    assert receiver_a <= universe
    assert len(receiver_a) == len(receiver_b) == len(receiver_c) == M
    assert len(receiver_a & receiver_b & receiver_c) == M
    return N, M


def main():
    assert audit_merged_boundaries()
    n3, n4 = audit_quotient_identities()
    f3, f4 = audit_fourier_fibers()
    ideal = audit_ideal_square_sieve_ledger()
    target, ideal3, ideal4, e5 = audit_current_barrier()
    N, M = audit_nonmultiplication_countermodel()

    print(f"THREE_CELL_QUOTIENT_IDENTITY_SAMPLES={n3}")
    print(f"FOUR_CELL_QUOTIENT_IDENTITY_SAMPLES={n4}")
    print(f"THREE_CELL_FOURIER_FORMULA_CHECKS={f3}")
    print(f"FOUR_CELL_FOURIER_FORMULA_CHECKS={f4}")
    print(f"IDEAL_TWO_CELL_RELATIVE_SAVING={ideal[2][1]}")
    print(f"IDEAL_THREE_CELL_RELATIVE_SAVING={ideal[3][1]}")
    print(f"IDEAL_FOUR_CELL_RELATIVE_SAVING={ideal[4][1]}")
    print(f"CURRENT_ARCHITECTURE_BARRIER={target}")
    print(f"OPTIMISTIC_THREE_CELL_BARRIER={ideal3}")
    print(f"OPTIMISTIC_FOUR_CELL_BARRIER={ideal4}")
    print(f"DENOMINATOR_THIN_EXPONENT={e5}")
    print(f"NONMULTIPLICATION_COUNTERMODEL_UNIVERSE={N}")
    print(f"NONMULTIPLICATION_COUNTERMODEL_INTERSECTION={M}")
    print("MERGED_S7_10_BOUNDARY_AUDIT=true")
    print("MERGED_4BY_BOUNDARY_AUDIT=true")
    print("THREE_CELL_DETECTOR_FACTORS_THROUGH_TWO_CELL_QUOTIENT=true")
    print("FOUR_CELL_DETECTOR_FACTORS_THROUGH_TWO_CELL_QUOTIENT=true")
    print("THREE_CELL_TORUS_KERNEL_DIMENSION=1")
    print("FOUR_CELL_TORUS_KERNEL_DIMENSION=2")
    print("THREE_CELL_FOURIER_FIBER_IDENTITY_EXACT=true")
    print("FOUR_CELL_FOURIER_FIBER_IDENTITY_EXACT=true")
    print("MULTICELL_IMPROVES_PROVED_TWO_CELL_SAVING=false")
    print("PAIRWISE_TWO_CELL_SAVINGS_MULTIPLY=false")
    print("NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
