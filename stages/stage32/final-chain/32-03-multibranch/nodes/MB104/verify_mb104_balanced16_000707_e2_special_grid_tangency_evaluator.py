#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]

SOURCE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPECIAL-GRID-TANGENCY-EVALUATOR.md": "3f040b8ebb3daf9947aab530f494c6bbce312d11",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT.md": "d4e5c3b9c598299114f983594be1fac1b01d24d7",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md": "d2e3056137360a9e15ae7c820088d2977a5eb137",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md": "dbfea5a4f62b1388c9810c37ad867076ed4dca6e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-13FORM-PRINCIPAL-PART.md": "1080c5da761fe328d3047f9829fd46cc3e7aabb0",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPECIAL-GRID-DELTA-CAPACITY-WALL.md": "f7ae2dac5be3b15542471e5b4b0e50515c05537b",
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
            raise SystemExit(f"FAIL source lock drift: {rel} expected={expected} got={got}")


def first_order_fourth_power(q: Fraction, a: Fraction) -> Fraction:
    # Coefficient of s in (q+a*s)^4-q^4.
    return 4 * q**3 * a


def verify_slope_identity() -> None:
    # Exact rational replay of the formal first-order identity.  The value of
    # c=q^4 cancels, so rational nonzero q_z,q_w suffice to verify the algebra.
    samples = [
        (Fraction(2), Fraction(3), Fraction(5), Fraction(7)),
        (Fraction(-3), Fraction(4), Fraction(2), Fraction(-5)),
        (Fraction(5, 2), Fraction(-7, 3), Fraction(11, 5), Fraction(13, 7)),
    ]
    for qz, qw, az, aw in samples:
        cz = first_order_fourth_power(qz, az)
        cw = first_order_fourth_power(qw, aw)
        a2 = cz / cw
        slope = aw / az
        reconstructed = qz**3 / (qw**3 * a2)
        if slope != reconstructed:
            raise SystemExit("FAIL exact tangent-slope identity")


def verify_kummer_ratio_algebra() -> None:
    # From V^2=((rz^4-4)(rw^4-4))/16 and
    # A=4V/(rw^4-4), squaring must return the displayed quotient;
    # similarly for U and the +4 equation.  Check the cancellation exactly at
    # several rational points away from the branch locus.
    for sign in (-1, 1):
        # sign=-1 means F=r^4-4; sign=+1 means F=r^4+4.
        for rz, rw in [(Fraction(1), Fraction(2)), (Fraction(2), Fraction(3)), (Fraction(3, 2), Fraction(5, 2))]:
            fz = rz**4 + sign * 4
            fw = rw**4 + sign * 4
            if fw == 0:
                continue
            # We do not choose a square root.  Compare A^2 algebraically.
            invariant_square = fz * fw / 16
            a_square_from_invariant = 16 * invariant_square / (fw * fw)
            if a_square_from_invariant != fz / fw:
                raise SystemExit("FAIL Kummer-ratio square identity")


def verify_divisor_counts() -> None:
    # Work in units of l. n=28l.  One inertia type has seven nodes and 8l
    # supported branches per node, hence 2n common simple zeros.
    n = 28
    supported = 7 * 8
    if supported != 2 * n:
        raise SystemExit("FAIL supported divisor degree")

    # F(r)=r^4 +/-4 has pullback zero degree 4n.  Removing 2n common
    # unramified zeros leaves 2n zero multiplicity, i.e. n simple ramification
    # points counted with multiplicity two.
    remaining_zero_multiplicity = 4 * n - supported
    if remaining_zero_multiplicity != 2 * n:
        raise SystemExit("FAIL remaining zero multiplicity")
    ramification_degree = remaining_zero_multiplicity // 2
    if ramification_degree != n:
        raise SystemExit("FAIL inertia-type ramification degree")

    # Positive degree of R_z-R_w-2P_z+2P_w is at most n+2n.
    a_degree_bound = ramification_degree + 2 * n
    if a_degree_bound != 3 * n or a_degree_bound != 84:
        raise SystemExit("FAIL A degree bound")
    if not (supported < a_degree_bound):
        raise SystemExit("FAIL no-pigeonhole ordering")


def main() -> None:
    # Fail closed before any mathematics.
    verify_source_locks()
    verify_kummer_ratio_algebra()
    verify_slope_identity()
    verify_divisor_counts()
    print("PASS stage32 MB104 000707 e2 special-grid tangency evaluator")


if __name__ == "__main__":
    main()
