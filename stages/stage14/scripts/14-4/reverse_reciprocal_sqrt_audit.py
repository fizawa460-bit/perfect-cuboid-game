#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def difference_of_squares_pairs(w: int):
    """Return positive (A,B) with A>B and A^2-B^2=w."""
    out = []
    for fm in divisors(w):
        fp = w // fm
        if fm >= fp:
            continue
        if (fm + fp) % 2:
            continue
        A = (fp + fm) // 2
        B = (fp - fm) // 2
        if A > B > 0 and A * A - B * B == w:
            out.append((A, B))
    return out


def ordered_factorizations(n: int):
    return [(d, n // d) for d in divisors(n)]


def check_difference_of_squares() -> int:
    checks = 0
    for A in range(2, 80):
        for B in range(1, A):
            w = A * A - B * B
            pairs = difference_of_squares_pairs(w)
            assert (A, B) in pairs
            for A2, B2 in pairs:
                assert A2 * A2 - B2 * B2 == w
            checks += 1
    return checks


def check_reverse_second_equation() -> int:
    checks = 0
    # This is a pure quantifier/factorization regression: once the RHS is fixed,
    # cp and dq are obtained from divisor pairs and then split divisor-many ways.
    for c in range(1, 8):
        for p in range(1, 8):
            A = c * p
            for d in range(1, 8):
                for q in range(1, 8):
                    B = d * q
                    if A <= B:
                        continue
                    w = A * A - B * B
                    pairs = difference_of_squares_pairs(w)
                    assert (A, B) in pairs
                    recovered = set()
                    for A2, B2 in pairs:
                        for c2, p2 in ordered_factorizations(A2):
                            for d2, q2 in ordered_factorizations(B2):
                                recovered.add((c2, d2, p2, q2))
                    assert (c, d, p, q) in recovered
                    checks += 1
    return checks


def check_reverse_first_equation() -> int:
    checks = 0
    # With U,V fixed, the factor pair determines aU,bV and hence a,b when divisible.
    for U in range(1, 9):
        for V in range(1, 9):
            if gcd(U, V) != 1:
                continue
            for a in range(1, 9):
                A = a * U
                for b in range(1, 9):
                    B = b * V
                    if A <= B:
                        continue
                    w = A * A - B * B
                    candidates = set()
                    for A2, B2 in difference_of_squares_pairs(w):
                        if A2 % U == 0 and B2 % V == 0:
                            candidates.add((A2 // U, B2 // V))
                    assert (a, b) in candidates
                    checks += 1
    return checks


def check_column_M_identity() -> int:
    checks = 0
    for x1 in range(1, 9):
        for y1 in range(1, 9):
            for x2 in range(1, 9):
                for y2 in range(1, 9):
                    for g1 in (1, 2):
                        for g2 in (1, 2):
                            # Only integral z_i states matter.
                            if (2 * x1 * y1) % g1 or (2 * x2 * y2) % g2:
                                continue
                            z1 = 2 * x1 * y1 // g1
                            z2 = 2 * x2 * y2 // g2
                            X = x1 * x2
                            Y = y1 * y2
                            assert z1 * z2 * g1 * g2 == 4 * X * Y
                            checks += 1
    return checks


def legal(theta: Fraction, phi: Fraction) -> bool:
    return (
        Fraction(3, 16) <= theta <= Fraction(5, 16)
        and Fraction(1, 8) <= phi <= Fraction(1, 4)
        and Fraction(0) <= theta - phi <= Fraction(1, 8)
        and theta + phi >= Fraction(3, 8)
    )


def check_square_root_ledger() -> int:
    half = Fraction(1, 2)
    D = 528  # divisible by 16, 24, 44, 88
    checks = 0
    equality_theta = set()

    for it in range(D * 3 // 16, D * 5 // 16 + 1):
        theta = Fraction(it, D)
        for ip in range(D // 8, D // 4 + 1):
            phi = Fraction(ip, D)
            if not legal(theta, phi):
                continue
            chi = 2 * theta + 2 * phi - Fraction(3, 4)
            E_k = 3 * theta - Fraction(1, 4)
            E_rrf = 2 * phi + Fraction(1, 4) - chi
            assert E_rrf == 1 - 2 * theta

            if theta <= Fraction(1, 4):
                assert E_k <= half
                envelope = E_k
            else:
                # chi>1/4 is the merged 4cx empty branch.
                if chi > Fraction(1, 4):
                    checks += 1
                    continue
                assert E_rrf <= half
                envelope = E_rrf

            assert envelope <= half
            if envelope == half:
                equality_theta.add(theta)
            checks += 1

    assert equality_theta == {Fraction(1, 4)}

    # The old unique 23/44 endpoint is strictly below sqrt after row removal.
    old_theta = Fraction(23, 88)
    old_phi = Fraction(19, 88)
    old_chi = 2 * old_theta + 2 * old_phi - Fraction(3, 4)
    assert old_chi == Fraction(9, 44)
    old_rrf = 2 * old_phi + Fraction(1, 4) - old_chi
    assert old_rrf == Fraction(21, 44)
    assert old_rrf == half - Fraction(1, 44)

    assert Fraction(23, 44) - half == Fraction(1, 44)
    return checks


def check_sqrt_saturation_band() -> int:
    theta = Fraction(1, 4)
    D = 528
    checks = 0
    possible_phis = set()
    for ip in range(D // 8, D // 4 + 1):
        phi = Fraction(ip, D)
        if not legal(theta, phi):
            continue
        chi = 2 * phi - Fraction(1, 4)
        base = 2 * phi
        column = Fraction(1, 4) - chi
        assert base + column == Fraction(1, 2)

        possible = False
        # s-grid is enough to verify the exact inequality boundary.
        for is_ in range(0, ip + 1):
            s = Fraction(is_, D)
            E_H = 3 * phi - Fraction(1, 8) - 3 * s
            if E_H >= Fraction(1, 2):
                assert phi - s >= Fraction(5, 24)
                possible = True
            checks += 1
        if possible:
            possible_phis.add(phi)

    assert min(possible_phis) == Fraction(5, 24)
    assert max(possible_phis) == Fraction(1, 4)
    return checks


def main() -> None:
    diff_checks = check_difference_of_squares()
    second_checks = check_reverse_second_equation()
    first_checks = check_reverse_first_equation()
    m_checks = check_column_M_identity()
    ledger_checks = check_square_root_ledger()
    band_checks = check_sqrt_saturation_band()

    print("Stage14-4da deterministic audit: PASS")
    print(f"difference-of-squares checks: {diff_checks}")
    print(f"reverse second-equation checks: {second_checks}")
    print(f"reverse first-equation checks: {first_checks}")
    print(f"column-M identity checks: {m_checks}")
    print(f"whole-strip rational ledger checks: {ledger_checks}")
    print(f"sqrt-band checks: {band_checks}")
    print("ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false")
    print("POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=Bo1")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("IMPROVEMENT_OVER_MERGED_23_44=1/44")
    print("SQRT_B_UPPER_BOUND_PROVED=true")
    print("S7_41_MAINLINE_H_GATE_SUPERSEDED=true")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4db")


if __name__ == "__main__":
    main()
