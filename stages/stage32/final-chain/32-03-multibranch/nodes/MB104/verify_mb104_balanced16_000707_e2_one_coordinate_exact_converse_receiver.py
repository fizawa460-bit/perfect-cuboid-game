#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]

SOURCE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md": "d2e3056137360a9e15ae7c820088d2977a5eb137",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-CONDUCTOR-PAIR-INVOLUTION-QUOTIENT.md": "3344d2f638b8f1373fc660202a5f3307dd30a51b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md": "ce9554bc047159baf7640db50aa5daf1f0c67f74",
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


def verify_one_coordinate_exact_converse() -> None:
    cases = [
        (Fraction(1), Fraction(2), 1),
        (Fraction(2), Fraction(3), -1),
        (Fraction(-3, 2), Fraction(5, 4), 1),
        (Fraction(5, 3), Fraction(-7, 2), -1),
    ]
    for rzi, m, expected_delta in cases:
        if rzi == 0:
            raise SystemExit("FAIL non-etale r_z chart")
        A = rzi * rzi
        rzj = expected_delta * rzi
        rwi = m / rzi
        rwj = m / rzj

        if rzj * rzj != A:
            raise SystemExit("FAIL common base square")
        if rzi * rwi != m or rzj * rwj != m:
            raise SystemExit("FAIL common base product")

        delta = rzj / rzi
        if delta * delta != 1 or delta != expected_delta:
            raise SystemExit("FAIL delta not exact mu2 coordinate")
        if rwj != delta * rwi:
            raise SystemExit("FAIL r_w converse reconstruction")

        pair_i = (rzi, rwi)
        pair_j = (rzj, rwj)
        if delta == 1 and pair_j != pair_i:
            raise SystemExit("FAIL +1 converse component")
        if delta == -1 and pair_j != (-rzi, -rwi):
            raise SystemExit("FAIL -1 converse component")

        chi = rzi * rzj / A
        if chi != delta:
            raise SystemExit("FAIL chi != delta")


def verify_generator_rescaling_invariance() -> None:
    for rzi, delta, a in [
        (Fraction(2), 1, Fraction(3)),
        (Fraction(2), -1, Fraction(-5, 2)),
        (Fraction(-7, 3), -1, Fraction(4, 5)),
    ]:
        rzj = delta * rzi
        if a == 0:
            raise SystemExit("FAIL zero Kummer rescaling")
        original = rzj / rzi
        rescaled = (a * rzj) / (a * rzi)
        if rescaled != original:
            raise SystemExit("FAIL generator-rescaling invariance")


def verify_symmetry_and_cocycle() -> None:
    labels = [1, -1, 1, 1, -1]
    for i in range(len(labels)):
        for j in range(len(labels)):
            delta_ij = Fraction(labels[j], labels[i])
            delta_ji = Fraction(labels[i], labels[j])
            if delta_ij != delta_ji:
                raise SystemExit("FAIL pair symmetry")
            for k in range(len(labels)):
                delta_jk = Fraction(labels[k], labels[j])
                delta_ik = Fraction(labels[k], labels[i])
                if delta_ij * delta_jk != delta_ik:
                    raise SystemExit("FAIL local delta cocycle")


def verify_weighted_cut_adapter() -> None:
    weights = [Fraction(1), Fraction(3, 2), Fraction(7), Fraction(11, 3)]
    deltas = [1, -1, -1, 1]
    direct = sum(w for w, delta in zip(weights, deltas) if delta == -1)
    algebraic = sum(
        w * Fraction(1 - delta, 2) for w, delta in zip(weights, deltas)
    )
    if direct != algebraic:
        raise SystemExit("FAIL weighted delta-cut identity")


def main() -> None:
    # Fail closed before any mathematical replay.
    verify_source_locks()
    verify_one_coordinate_exact_converse()
    verify_generator_rescaling_invariance()
    verify_symmetry_and_cocycle()
    verify_weighted_cut_adapter()
    print("PASS stage32 MB104 000707 e2 one-coordinate exact-converse receiver")


if __name__ == "__main__":
    main()
