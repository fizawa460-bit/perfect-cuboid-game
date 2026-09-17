#!/usr/bin/env python3
"""Zero-credit regression checks for RR norm quantization research.

This verifier does not award Stage32 credit.  The universal argument is the
algebra in RR-NORM-QUANTIZATION-RESEARCH.md; these finite checks are only a
regression guard against sign/modulus mistakes.
"""

from math import gcd


def params(d: int) -> tuple[int, int, int]:
    r = gcd(d, 16)
    return r, 16 // r, d // r


def norm_from_c2(d: int, c2: int) -> int:
    _, m, n = params(d)
    return 16 * n * n - m * m * c2


def rr_boundary_norm(d: int) -> int:
    _, m, n = params(d)
    return 16 * n * n - m * m * d + 14 * m * m


def admissible_residue(d: int) -> tuple[int, int]:
    _, m, n = params(d)
    modulus = 2 * m * m
    residue = (16 * n * n - m * m * d) % modulus
    return modulus, residue


def main() -> None:
    checked_pairs = 0

    for d in range(1, 4097):
        _, m, _ = params(d)
        modulus, residue = admissible_residue(d)
        threshold = rr_boundary_norm(d)

        assert modulus == 2 * m * m
        assert threshold % modulus == residue
        assert norm_from_c2(d, d - 14) == threshold
        assert norm_from_c2(d, d - 16) == threshold + modulus

        # Parity-compatible integral self-intersections C^2 = d + 2k.
        for k in range(-32, 33):
            c2 = d + 2 * k
            norm = norm_from_c2(d, c2)
            assert norm % modulus == residue

            # Exact equivalence with the already source-locked RR gate.
            rhs = m * m * (d * d - 16 * d + 224)
            assert (16 * norm <= rhs) == (c2 >= d - 14)
            checked_pairs += 1

    # Even-degree residue classes used as a compact human-readable checksum.
    expected = {
        2: (128, 16),  # d == 2 mod 4
        4: (32, 16),   # d == 4 mod 8
        8: (8, 0),     # d == 8 mod 16
        16: (2, 0),    # d == 0 mod 16
    }
    for d, want in expected.items():
        assert admissible_residue(d) == want

    print(
        "PASS: RR norm quantization regression; "
        f"degrees=4096 parity-compatible-pairs={checked_pairs} credit=NONE"
    )


if __name__ == "__main__":
    main()
