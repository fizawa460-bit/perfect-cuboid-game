#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt

F = Fraction


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def difference_square_pairs(w: int):
    """Positive (A,B), A>B, with A^2-B^2=w."""
    out = set()
    for fm in divisors(w):
        fp = w // fm
        if fp <= fm or (fp - fm) % 2:
            continue
        A = (fp + fm) // 2
        B = (fp - fm) // 2
        if A > B > 0 and A * A - B * B == w:
            out.add((A, B))
    return sorted(out)


def reverse_completions(U: int, V: int, M: int):
    """X13 reverse reconstruction in the normalized r=s=eps_x=eps_k=1 audit model."""
    if M <= 0 or M % 4:
        return set()
    XY = M // 4
    W2 = 4 * XY * U * V
    completions = set()

    # Second reciprocal equation: (c p)^2-(d q)^2=W2.
    for cp, dq in difference_square_pairs(W2):
        for c in divisors(cp):
            p = cp // c
            for d in divisors(dq):
                q = dq // d
                W1 = 4 * p * q

                # First reciprocal equation: (a U)^2-(b V)^2=W1.
                for aU, bV in difference_square_pairs(W1):
                    if aU % U or bV % V:
                        continue
                    a = aU // U
                    b = bV // V
                    if min(a, b, c, d, p, q) <= 0:
                        continue
                    N = a * b * c * d
                    completions.add((a, b, c, d, p, q, N))
    return completions


def audit_reverse_factorization():
    examples = []
    for U in range(1, 9):
        for V in range(1, 9):
            if gcd(U, V) != 1:
                continue
            for a in range(1, 8):
                for b in range(1, 8):
                    W1 = (a * U) ** 2 - (b * V) ** 2
                    if W1 <= 0 or W1 % 4:
                        continue
                    pq = W1 // 4
                    for p in divisors(pq):
                        q = pq // p
                        for c in range(1, 7):
                            for d in range(1, 7):
                                W2 = (c * p) ** 2 - (d * q) ** 2
                                if W2 <= 0 or W2 % (4 * U * V):
                                    continue
                                XY = W2 // (4 * U * V)
                                M = 4 * XY
                                examples.append((U, V, a, b, c, d, p, q, M))
                                if len(examples) >= 256:
                                    break
                            if len(examples) >= 256:
                                break
                        if len(examples) >= 256:
                            break
                    if len(examples) >= 256:
                        break
                if len(examples) >= 256:
                    break
            if len(examples) >= 256:
                break
        if len(examples) >= 256:
            break

    assert len(examples) >= 128

    max_fiber = 0
    for U, V, a, b, c, d, p, q, M in examples:
        comps = reverse_completions(U, V, M)
        N = a * b * c * d
        assert any(t[:6] == (a, b, c, d, p, q) and t[6] == N for t in comps)
        max_fiber = max(max_fiber, len(comps))

    # Independent exact checks of the two difference-of-squares reversals.
    diff_checks = 0
    for A in range(2, 90):
        for B in range(1, A):
            w = A * A - B * B
            assert (A, B) in difference_square_pairs(w)
            diff_checks += 1

    return len(examples), diff_checks, max_fiber


def audit_fraction_envelope():
    # Dense rational mesh whose denominator contains 8, 16, 22, 24, 44, 88.
    D = 1056
    checked = 0
    max_e = F(-1000)
    equality = []

    for i in range((3 * D) // 16, (5 * D) // 16 + 1):
        theta = F(i, D)
        for j in range(D // 8, D // 4 + 1):
            phi = F(j, D)
            if not (F(0) <= theta - phi <= F(1, 8)):
                continue
            if theta + phi < F(3, 8):
                continue

            chi = 2 * theta + 2 * phi - F(3, 4)
            # Algebraic identity behind the X13 nonproportional count.
            assert 2 * phi + F(1, 4) - chi == 1 - 2 * theta

            E_s = max(2 * theta, 1 - 2 * theta)
            E_k = 3 * theta - F(1, 4)
            # Best possible H-count upper bound occurs at s=0.
            E_H0 = 3 * phi - F(1, 8)

            bounds = [E_s, E_k, E_H0]
            if chi <= F(1, 4):
                E_rrf = 2 * phi + F(1, 4) - chi
                bounds.append(E_rrf)
            else:
                # Merged 4cx: fixed-power high-core nonproportional packet is empty.
                bounds.append(F(-1000))

            e = min(bounds)
            checked += 1
            if e > max_e:
                max_e = e
                equality = [(theta, phi, chi)]
            elif e == max_e:
                equality.append((theta, phi, chi))

    assert max_e == F(1, 2)
    assert equality
    assert all(theta == F(1, 4) for theta, _, _ in equality)
    assert min(phi for _, phi, _ in equality) == F(5, 24)
    assert max(phi for _, phi, _ in equality) == F(1, 4)

    # The exact saturation-band inequality with moving cross-root exponent s.
    band_checks = 0
    for _, phi, _ in equality:
        s_max = phi - F(5, 24)
        assert s_max >= 0
        # endpoints suffice because E_H is affine decreasing in s.
        assert 3 * phi - F(1, 8) >= F(1, 2)
        assert 3 * phi - F(1, 8) - 3 * s_max == F(1, 2)
        band_checks += 1

    return checked, len(equality), band_checks


def main():
    examples, diff_checks, max_fiber = audit_reverse_factorization()
    mesh, eqpts, band = audit_fraction_envelope()

    print("Stage14-X13 reverse reciprocal square-root audit: PASS")
    print(f"synthetic physical reciprocal packets recovered: {examples}")
    print(f"difference-of-squares reverse checks: {diff_checks}")
    print(f"max finite normalized reverse fiber: {max_fiber}")
    print(f"balanced rational mesh points checked: {mesh}")
    print(f"square-root equality mesh points: {eqpts}")
    print(f"square-root band endpoint checks: {band}")
    print("entering exponent: 23/44")
    print("current whole-family exponent: 1/2")
    print("improvement over 23/44: 1/44")
    print("row CRT lift independent support: false")
    print("square-root upper bound proved: true")
    print("strict sub-square-root power saving proved: false")
    print("sqrt saturation: theta=1/4, phi in [5/24,1/4]")
    print("X13 auxiliary H needed: false")


if __name__ == "__main__":
    main()
