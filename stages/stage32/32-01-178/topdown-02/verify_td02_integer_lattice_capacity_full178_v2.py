#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_td02_integer_lattice_capacity_full178.py"
EXPECTED_BASE_BLOB = "e4adb6fd92d88f4d9c10923627cac9424425e467"
EXPECTED_INTERIORS = 893_856
EXPECTED_ZERO_SECOND = 282_104
EXPECTED_POSITIVE_SECOND = 611_752


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_base():
    raw = BASE.read_bytes()
    req(git_blob(raw) == EXPECTED_BASE_BLOB, "FULL178 V1 source drift")
    mod = types.ModuleType("td02_integer_full178_v1")
    mod.__file__ = str(BASE)
    exec(compile(raw, str(BASE), "exec"), mod.__dict__)
    return mod


def corrected_convexity(mod, kernel):
    interiors = zero = positive = 0
    minimum = None
    for b in range(mod.FULL_HMAX + 1):
        for c in range(mod.FULL_HMAX + 1):
            f = mod.fixed_t_profile(kernel, b, c)
            for t in range(1, len(f) - 1):
                second = f[t - 1] - 2 * f[t] + f[t + 1]
                req(second >= 0, f"fixed-t discrete convexity {(b,c,t,second)}")
                interiors += 1
                if second == 0:
                    zero += 1
                else:
                    positive += 1
                minimum = second if minimum is None else min(minimum, second)
    req(interiors == EXPECTED_INTERIORS, f"fixed-t interior count {interiors}")
    req(zero == EXPECTED_ZERO_SECOND, f"fixed-t zero-second count {zero}")
    req(positive == EXPECTED_POSITIVE_SECOND, f"fixed-t positive-second count {positive}")
    req(minimum == 0, f"fixed-t minimum second difference {minimum}")
    return {
        "interiors": interiors,
        "zero_second_difference": zero,
        "positive_second_difference": positive,
        "min_second_difference": minimum,
    }


def install_cached_interval_cap(mod):
    # capacity_scaleout calls the interval routine repeatedly with the same vals
    # object while varying a. Cache only the immediately preceding object; this
    # is exact, bounded-memory, and prevents Python id reuse from becoming a
    # correctness issue because the previous list is retained by last_obj.
    last_obj = None
    last_m = None
    last_left_neg = None
    last_right = None

    def interval_cap(vals: list[int], threshold: int) -> int:
        nonlocal last_obj, last_m, last_left_neg, last_right
        if vals is not last_obj:
            m = min(range(len(vals)), key=vals.__getitem__)
            left_neg = [-v for v in vals[: m + 1]]
            right = vals[m:]
            last_obj, last_m, last_left_neg, last_right = vals, m, left_neg, right
        else:
            m, left_neg, right = last_m, last_left_neg, last_right
        if vals[m] > threshold:
            return 0
        L = bisect.bisect_left(left_neg, -threshold)
        R = m + bisect.bisect_right(right, threshold) - 1
        req(0 <= L <= m <= R < len(vals), f"sublevel interval {(L,m,R,len(vals))}")
        return (R - L + 2) // 2

    mod.interval_cap_from_convex_values = interval_cap


def main() -> None:
    mod = load_base()

    def check_fixed_t_convexity(kernel):
        return corrected_convexity(mod, kernel)

    mod.check_fixed_t_convexity = check_fixed_t_convexity
    install_cached_interval_cap(mod)
    mod.main()


if __name__ == "__main__":
    main()
