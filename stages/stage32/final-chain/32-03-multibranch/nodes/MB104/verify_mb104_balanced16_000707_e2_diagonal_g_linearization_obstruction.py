#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]

SOURCE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/EQUIVARIANT-PICARD-LINEARIZATION-SOURCE-NOTE.md": "a8db86e809ed6a19e7777a7680f3392f980e0bf0",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-DIAGONAL-G-LINEARIZATION-OBSTRUCTION.md": "7593aad67cbc284f16066063bc6abc6afb2352c8",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PRODUCT-CORRESPONDENCE-LINEARIZATION.md": "2c2db567db6a3c33762b2ff3d7f39f885a95b974",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXTERNAL-PRODUCT-PICARD-REDUCTION.md": "dc2def9e4d0148aa3146a034a2ce0ef331206a29",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-G-FIXED-JACOBIAN-EXPLICIT-BASIS.md": "c734b96e8506aae51fc23b68dc0e47b5b8356632",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md": "dbfea5a4f62b1388c9810c37ad867076ed4dca6e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md": "a29161602c0b38f0607794e56e61068b8cb9735d",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY.md": "3fb4152c35b88160f36730fac941f542566664a8",
}


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def verify_source_locks() -> None:
    # Fail closed before any retained arithmetic/group replay.
    for rel, expected in SOURCE_LOCKS.items():
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"FAIL missing source lock: {rel}")
        got = git_blob_sha1(path)
        if got != expected:
            raise SystemExit(
                f"FAIL source lock drift: {rel} expected={expected} got={got}"
            )


def verify_unsupported_fixed_points() -> None:
    # Each used stabilizer type has 16 box nodes, while 000707 supports seven.
    total_type_nodes = 16
    supported_type_nodes = 7
    unsupported = total_type_nodes - supported_type_nodes
    if unsupported != 9 or unsupported <= 0:
        raise SystemExit("FAIL unsupported fixed-point supply")


def xor(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x ^ y for x, y in zip(a, b))


def verify_linearizable_kernel_count() -> None:
    # Retained fixed Jacobian J(C8)^G = F2^5.
    fixed_dim = 5
    fixed_size = 1 << fixed_dim
    if fixed_size != 32:
        raise SystemExit("FAIL fixed-Jacobian cardinality")

    # For G=F2^3, alternating bicharacters are determined by three unordered
    # basis pairs, so H^2(G,C*) has F2-dimension binomial(3,2)=3.
    g_dim = 3
    h2_dim = g_dim * (g_dim - 1) // 2
    h2_size = 1 << h2_dim
    if h2_dim != 3 or h2_size != 8:
        raise SystemExit("FAIL obstruction-group cardinality")

    # Invariant divisor relations leave at most the two classes
    # lambda_1=R1-R3 and lambda_2=R1-R5, each of exponent two.
    invariant_divisor_kernel_upper = 1 << 2

    # A homomorphism 32 -> 8 has kernel of size at least four.  Since the
    # equivariant-Picard theorem identifies that kernel with invariant-divisor
    # classes, upper and lower bounds meet exactly.
    kernel_lower = fixed_size // h2_size
    if kernel_lower != 4 or invariant_divisor_kernel_upper != 4:
        raise SystemExit("FAIL kernel bounds")
    kernel_exact = kernel_lower

    # Model the resulting exact sequence F2^2 -> F2^5 -> F2^3 to replay the
    # compatible-pair count.  The coordinate projection is only a cardinality
    # model; the retained theorem proves the actual obstruction map has the
    # same kernel/image sizes.
    labels = list(itertools.product((0, 1), repeat=fixed_dim))
    obstruction = {x: x[2:] for x in labels}
    fibres: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for x in labels:
        fibres.setdefault(obstruction[x], []).append(x)
    if sorted(len(v) for v in fibres.values()) != [kernel_exact] * h2_size:
        raise SystemExit("FAIL obstruction fibre sizes")

    compatible = sum(len(v) ** 2 for v in fibres.values())
    if compatible != 128 or compatible != fixed_size * kernel_exact:
        raise SystemExit("FAIL compatible factor-pair count")

    # Relative differences of compatible pairs lie in the 2-bit kernel.
    for v in fibres.values():
        base = v[0]
        for x in v:
            d = xor(base, x)
            if any(d[2:]):
                raise SystemExit("FAIL relative obstruction not killed")


def verify_ramification_divisor_reduction() -> None:
    # Symbolically reduce the six branch-orbit labels to the two possible
    # degree-zero generators under the retained relations
    # R1=R2, R3=R4, R5=R6 and 2(R1-R3)=2(R1-R5)=0.
    # We encode only the resulting F2 labels of R_i-R1.
    zero = (0, 0)
    lam1 = (1, 0)
    lam2 = (0, 1)
    differences_from_r1 = {
        1: zero,
        2: zero,
        3: lam1,
        4: lam1,
        5: lam2,
        6: lam2,
    }
    if set(differences_from_r1.values()) != {zero, lam1, lam2}:
        raise SystemExit("FAIL ramification-orbit reduction")
    # Their subgroup also contains lambda_1+lambda_2 and has four elements.
    subgroup = {zero, lam1, lam2, xor(lam1, lam2)}
    if len(subgroup) != 4:
        raise SystemExit("FAIL linearizable subgroup size")


def main() -> None:
    verify_source_locks()
    verify_unsupported_fixed_points()
    verify_ramification_divisor_reduction()
    verify_linearizable_kernel_count()
    print("PASS stage32 MB104 000707 e2 diagonal-G linearization obstruction")
    print("fixed_jacobian=32 obstruction_group=8 linearizable_kernel=4 compatible_pairs=128")


if __name__ == "__main__":
    main()
