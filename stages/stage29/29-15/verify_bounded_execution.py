from fractions import Fraction


def verify_beauville_v4_swap():
    # Gamma = (Z/2)^2, and the deck group of
    # (C x C)/Delta(Gamma) -> (C/Gamma) x (C/Gamma)
    # is (Gamma x Gamma)/Delta(Gamma) ~= Gamma via [(g,h)] -> g+h.
    gamma = [(a, b) for a in (0, 1) for b in (0, 1)]

    def add(g, h):
        return (g[0] ^ h[0], g[1] ^ h[1])

    # Factor swap sends [(g,h)] to [(h,g)].  Under the quotient
    # identification both have the same image because Gamma has exponent 2
    # (indeed here addition is commutative).
    for g in gamma:
        for h in gamma:
            assert add(g, h) == add(h, g)


def verify_q2_density():
    # Conditional on one coordinate being the unique odd coordinate, let X,Z
    # be the two even affine ratios.  For X and 1+X to be Q_2-squares,
    # v2(X)=2a with a>=2 and the odd unit part must be 1 mod 8.
    # Conditional mass w_a = 2^(-2a-2).
    w2 = Fraction(1, 64)
    ratio = Fraction(1, 4)
    S = w2 / (1 - ratio)  # sum_{a>=2} w_a = 1/48
    assert S == Fraction(1, 48)

    # X+Z fails exactly when the square valuations are equal or differ by 2,
    # i.e. |a-b| is 0 or 1.  Equal and adjacent masses are geometric series.
    equal = (w2 * w2) / (1 - Fraction(1, 16))
    adjacent_ordered = 2 * (w2 * (w2 * ratio)) / (1 - Fraction(1, 16))
    assert equal == Fraction(1, 3840)
    assert adjacent_ordered == Fraction(1, 7680)

    conditional_pair = S * S - equal - adjacent_ordered
    assert conditional_pair == Fraction(1, 23040)

    # P^2(F_2) has seven primitive parity cylinders of equal Haar mass.
    # Exactly the three cylinders with a unique odd coordinate survive.
    delta2 = Fraction(3, 7) * conditional_pair
    assert delta2 == Fraction(1, 53760)


if __name__ == "__main__":
    verify_beauville_v4_swap()
    verify_q2_density()
    print("R29-BEAU2A: PASS")
    print("R29-KUM-LOC2-2: PASS; Delta_2 = 1/53760")
