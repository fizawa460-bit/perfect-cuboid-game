#!/usr/bin/env python3
"""Replay the six-rank3 simultaneous O266 RH integer budget.

Scratch-only diagnostic.  This does not grant endpoint or MAIN credit.
"""

from functools import lru_cache

TOTAL_EXCEPTIONAL_MASS = 266
BLOCK_COUNT = 6
BLOCK_MIN = 8
BLOCK_MAX = 184

EXPECTED_MIN_NONMINIMAL = {
    2: 0,
    3: 0,
    4: 54,
    5: 96,
    6: 125,
    7: 145,
}


def block_required_nonminimal(M: int, r: int) -> int:
    """Minimum nonminimal branches needed in a mass-M block if all minimal
    branches are rank3-r-flat, given RH degree 186-M.
    """
    return max(0, M - (186 - M) // r)


def minimize_required_nonminimal(r: int):
    values = tuple(range(BLOCK_MIN, BLOCK_MAX + 1, 2))

    @lru_cache(None)
    def dp(k: int, remaining: int):
        if k == 0:
            return (0, ()) if remaining == 0 else None
        best = None
        for M in values:
            if M > remaining:
                break
            tail = dp(k - 1, remaining - M)
            if tail is None:
                continue
            val = block_required_nonminimal(M, r) + tail[0]
            cand = (val, (M,) + tail[1])
            if best is None or cand[0] < best[0]:
                best = cand
        return best

    return dp(BLOCK_COUNT, TOTAL_EXCEPTIONAL_MASS)


def failure_floor(r: int, E: int) -> int:
    """Lower bound for rank3-r-flat failures among minimal branches.

    O266 gives L_nonminimal <= Q = 80-E, where E=Eta+Rrho.
    If all but F minimal branches are r-flat, then L+F must be at least
    the six-block minimum required_nonminimal.
    """
    min_required = EXPECTED_MIN_NONMINIMAL[r]
    return max(0, min_required - (80 - E))


def main() -> None:
    witnesses = {}
    for r, expected in EXPECTED_MIN_NONMINIMAL.items():
        result = minimize_required_nonminimal(r)
        assert result is not None
        value, masses = result
        assert value == expected, (r, value, masses)
        assert len(masses) == 6
        assert sum(masses) == 266
        assert all(8 <= M <= 184 and M % 2 == 0 for M in masses)
        witnesses[r] = masses

    # Canonical symbolic forms at E>=0.
    assert failure_floor(4, 0) == 0
    assert failure_floor(4, 26) == 0
    assert failure_floor(4, 27) == 1
    assert failure_floor(5, 0) == 16
    assert failure_floor(6, 0) == 45
    assert failure_floor(7, 0) == 65

    # Check formulas over the full allowed scalar interval 0<=E<=80.
    for E in range(81):
        assert failure_floor(4, E) == max(0, E - 26)
        assert failure_floor(5, E) == 16 + E
        assert failure_floor(6, E) == 45 + E
        assert failure_floor(7, E) == 65 + E

    print("PASS scratch six-rank3 simultaneous RH budget")
    for r in sorted(witnesses):
        print(f"r={r}: min_nonminimal={EXPECTED_MIN_NONMINIMAL[r]}, witness={list(witnesses[r])}")
    print("failure floors: r4=max(0,E-26), r5=16+E, r6=45+E, r7=65+E")


if __name__ == "__main__":
    main()
