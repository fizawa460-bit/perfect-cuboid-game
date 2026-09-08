#!/usr/bin/env python3
"""Replay the aggregate six-rank3 node-ramification coupling at O266.

Scratch-only diagnostic. No endpoint or MAIN credit.
"""

from math import ceil

TOTAL_RANK3_RH = 6 * 186 - 266  # sum_j (186-M_j)
assert TOTAL_RANK3_RH == 850

EXPECTED_FAILURE_FLOORS_AT_E0 = {
    2: 0,
    3: 0,
    4: 0,
    5: 16,
    6: 45,
    7: 65,
}

EXPECTED_FAILURE_FLOORS_AT_E80 = {
    2: 0,
    3: 0,
    4: 54,
    5: 96,
    6: 125,
    7: 145,
}


def aggregate_failure_floor(r: int, E: int) -> int:
    """Minimum rank3-r-flat failures among minimal branches.

    Q=80-E, L<=Q, M=266-L. A nonminimal branch with q-charge b
    contributes b-1 to its assigned rank3 pencil, so total nonminimal
    node ramification is Q-L. If F minimal branches fail r-flatness, then

        r*(M-F) + (Q-L) <= 850.

    The smallest possible F is obtained at the largest allowed L=Q.
    """
    Q = 80 - E
    L = Q
    M = 266 - L
    numerator = r * M + (Q - L) - TOTAL_RANK3_RH
    return max(0, ceil(numerator / r))


def main() -> None:
    for r in range(2, 8):
        assert aggregate_failure_floor(r, 0) == EXPECTED_FAILURE_FLOORS_AT_E0[r]
        assert aggregate_failure_floor(r, 80) == EXPECTED_FAILURE_FLOORS_AT_E80[r]

    for E in range(81):
        assert aggregate_failure_floor(4, E) == max(0, E - 26)
        assert aggregate_failure_floor(5, E) == 16 + E
        assert aggregate_failure_floor(6, E) == 45 + E
        assert aggregate_failure_floor(7, E) == 65 + E

    # Cross-check with the finite six-block minima previously replayed.
    min_required_nonminimal = {4: 54, 5: 96, 6: 125, 7: 145}
    for E in range(81):
        Q = 80 - E
        for r, required in min_required_nonminimal.items():
            block_floor = max(0, required - Q)
            assert aggregate_failure_floor(r, E) == block_floor

    print("PASS scratch rank3 nonminimal ramification coupling")
    print("total six-rank3 RH degree = 850")
    print("nonminimal node ramification = Q-L")
    print("failure floors: r4=max(0,E-26), r5=16+E, r6=45+E, r7=65+E")


if __name__ == "__main__":
    main()
