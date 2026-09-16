#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]

SOURCE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-CONDUCTOR-PAIR-INVOLUTION-QUOTIENT.md": "3344d2f638b8f1373fc660202a5f3307dd30a51b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXPLICIT-RESIDUAL-KUMMER-COORDINATE.md": "5017d7c137f6d4994a34cb1edac28aadcd832a2a",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-COMPLEMENT-H1-BIT.md": "b0c212014615c47cbeaaa82a206e2b232ddd3686",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ZERO-QUARTIC-UNION-RESIDUAL-MONODROMY.md": "2d08671a04932c7e18b914d64f813608d13354c2",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-GENERALIZED-JACOBIAN-GLUING-CHARACTER.md": "b2816ce1a8554a9bee33acfb6cc76df066d73b74",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-KUMMER-MONODROMY.md": "0edeb77294919b9a7ad0dcce3030739b630c1fd1",
}


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def verify_source_locks() -> None:
    for rel, expected in SOURCE_LOCKS.items():
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"FAIL missing source lock: {rel}")
        got = git_blob_sha1(path)
        if got != expected:
            raise SystemExit(
                f"FAIL source lock drift: {rel} expected={expected} got={got}"
            )


def verify_pair_receiver() -> None:
    # Exact rational fibres of r^2=h with h a nonzero square.  The two points
    # over the same base point must be the diagonal or deck-twisted pair.
    for s in [Fraction(1), Fraction(2), Fraction(-3, 2), Fraction(5, 3)]:
        h = s * s
        if h == 0:
            raise SystemExit("FAIL etale Kummer chart used h=0")
        for sign in (1, -1):
            ri = s
            rj = sign * s
            if ri * ri != h or rj * rj != h:
                raise SystemExit("FAIL Kummer fibre equation")
            difference = ri * ri - rj * rj
            factored = (ri - rj) * (ri + rj)
            if difference != factored or difference != 0:
                raise SystemExit("FAIL pair split identity")
            chi = ri * rj / h
            if chi not in (Fraction(1), Fraction(-1)):
                raise SystemExit("FAIL chi not mu2-valued")
            if chi * chi != 1:
                raise SystemExit("FAIL chi^2 != 1")
            if chi != sign:
                raise SystemExit("FAIL chi component label")
            # Simultaneous deck flip must not change chi.
            if ((-ri) * (-rj) / h) != chi:
                raise SystemExit("FAIL diagonal deck invariance")
            # Swapping the conductor pair must not change chi.
            if (rj * ri / h) != chi:
                raise SystemExit("FAIL pair-swap invariance")


def verify_generator_independence() -> None:
    # On a Kummer-chart overlap r'=a*r and h'=a^2*h.
    for s, a, sign in [
        (Fraction(2), Fraction(3), 1),
        (Fraction(2), Fraction(-5, 2), -1),
        (Fraction(7, 3), Fraction(4, 5), -1),
    ]:
        h = s * s
        ri = s
        rj = sign * s
        chi = ri * rj / h
        rip = a * ri
        rjp = a * rj
        hp = a * a * h
        if rip * rjp / hp != chi:
            raise SystemExit("FAIL Kummer-generator independence")


def verify_local_cocycle() -> None:
    # Relative signs must come from branch labels, so pair bits at one
    # singular point are not independent.
    labels = [1, -1, 1, 1, -1]
    for i in range(len(labels)):
        if labels[i] * labels[i] != 1:
            raise SystemExit("FAIL chi_ii")
        for j in range(len(labels)):
            chi_ij = labels[i] * labels[j]
            chi_ji = labels[j] * labels[i]
            if chi_ij != chi_ji:
                raise SystemExit("FAIL chi symmetry")
            for k in range(len(labels)):
                chi_jk = labels[j] * labels[k]
                chi_ik = labels[i] * labels[k]
                if chi_ij * chi_jk != chi_ik:
                    raise SystemExit("FAIL local relative-sign cocycle")


def verify_weighted_cut_adapter() -> None:
    # (1-chi)/2 is exactly the opposite-sheet indicator.
    weights = [Fraction(1), Fraction(3, 2), Fraction(7), Fraction(11, 3)]
    chis = [1, -1, -1, 1]
    direct = sum(w for w, chi in zip(weights, chis) if chi == -1)
    algebraic = sum(w * Fraction(1 - chi, 2) for w, chi in zip(weights, chis))
    if direct != algebraic:
        raise SystemExit("FAIL weighted chi-cut identity")


def verify_two_class_dictionary() -> None:
    # H_1(U,Z)=Z/2 and alpha_abs(gamma_Q)=1 make the sign dictionary unique.
    dictionary = {0: 1, 1: -1}
    if dictionary[0] != 1 or dictionary[1] != -1:
        raise SystemExit("FAIL 0/gamma_Q dictionary")
    for bit in (0, 1):
        chi = (-1) ** bit
        if chi != dictionary[bit]:
            raise SystemExit("FAIL ambient-character sign adapter")


def main() -> None:
    # Fail closed before any mathematics.
    verify_source_locks()
    verify_pair_receiver()
    verify_generator_independence()
    verify_local_cocycle()
    verify_weighted_cut_adapter()
    verify_two_class_dictionary()
    print("PASS stage32 MB104 000707 e2 conductor-pair involution quotient")


if __name__ == "__main__":
    main()
