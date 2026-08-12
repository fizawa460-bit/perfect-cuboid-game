from __future__ import annotations

from math import isqrt


def support_receiver(F1: int, F2: int, B: int) -> dict[str, int | bool]:
    prod = F1 * F2
    S = isqrt(prod)
    return {
        "product_is_square": S * S == prod,
        "S": S,
        "inside_physical_cutoff": S <= 2 * B,
    }


def audit_flags() -> dict[str, bool]:
    return {
        "chan_direct_reuse": False,
        "choi_direct_reuse": False,
        "alpoge_ho_direct_reuse": False,
        "fixed_S_fiber_closed": True,
        "weighted_twist_second_moment_gate_superseded": True,
        "admissible_diagonal_support_bound_proved": False,
    }


def witness() -> dict[str, object]:
    return {
        "receiver": support_receiver(13690, 250, 1000),
        "flags": audit_flags(),
    }


if __name__ == "__main__":
    print(witness())
