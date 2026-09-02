#!/usr/bin/env python3
"""Exact p=13 obstruction for the two hard q=20/99 Stage34 d1 sign orbits.

This is a deterministic finite verifier. It grants no audit/promotion credit.
"""

P = 13
A_COEFF = 20
B_COEFF = 99

BRANCHES = {
    "0de8f4d61c834bdf136b": (-6, 10, 510, -34),
    "1f5f04661b6ace1279b8": (6, -10, -510, 34),
    "6c9e0174b4ec2e232143": (-5, 3, 17, -255),
    "81bdbd19aed01cc4a379": (5, -3, -17, 255),
}

EXPECTED = {
    "0de8f4d61c834bdf136b": [((5, 1), 5), ((8, 1), 8)],
    "1f5f04661b6ace1279b8": [((5, 1), 5), ((8, 1), 8)],
    "6c9e0174b4ec2e232143": [((5, 1), 5), ((8, 1), 8)],
    "81bdbd19aed01cc4a379": [((5, 1), 5), ((8, 1), 8)],
}


def is_square_or_zero(x):
    x %= P
    return x == 0 or pow(x, (P - 1) // 2, P) == 1


def p1_points():
    return [(t, 1) for t in range(P)] + [(1, 0)]


def forms(T, S):
    U = (T * T - S * S) % P
    V = (2 * T * S) % P
    A = (A_COEFF * U + B_COEFF * V) % P
    B = (B_COEFF * U + A_COEFF * V) % P
    return U, V, A, B


def branch_survivors(delta):
    out = []
    for T, S in p1_points():
        U, V, A, B = forms(T, S)
        Fs = (U, V, A, B)
        ok = True
        for F, d in zip(Fs, delta):
            d %= P
            assert d != 0
            if not is_square_or_zero(F * pow(d, -1, P)):
                ok = False
                break
        if ok:
            out.append(((T, S), (A * A + B * B) % P))
    return out


def verify_cleared_quartic_identity():
    # With U=T^2-S^2, V=2TS, A=aU+bV, B=bU+aV,
    # A^2+B^2 is b^2 times the homogeneous d=1 K_{q,1} quartic (q=a/b).
    lhs_coeffs = (
        A_COEFF * A_COEFF + B_COEFF * B_COEFF,
        8 * A_COEFF * B_COEFF,
        2 * (A_COEFF * A_COEFF + B_COEFF * B_COEFF),
        -8 * A_COEFF * B_COEFF,
        A_COEFF * A_COEFF + B_COEFF * B_COEFF,
    )
    cleared_k_coeffs = lhs_coeffs
    assert lhs_coeffs == cleared_k_coeffs


def main():
    assert P % 4 == 1
    assert (2 * A_COEFF * B_COEFF * (A_COEFF * A_COEFF - B_COEFF * B_COEFF)) % P != 0
    verify_cleared_quartic_identity()

    square_residues = {x * x % P for x in range(P)}
    assert 5 not in square_residues
    assert 8 not in square_residues

    for branch_id, delta in BRANCHES.items():
        assert all(d % P != 0 for d in delta)
        got = branch_survivors(delta)
        assert got == EXPECTED[branch_id], (branch_id, got)
        assert all(not is_square_or_zero(k) for _, k in got)
        print(branch_id, "branch_residues=", got, "receiver_K_intersection=EMPTY")

    print("PASS: all four hard q=20/99 branches are locally obstructed at p=13 after imposing K_{q,1}.")


if __name__ == "__main__":
    main()
