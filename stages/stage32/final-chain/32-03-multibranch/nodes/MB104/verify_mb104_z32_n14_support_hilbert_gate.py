#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
W5 = HERE / "MB104-W5-SOLO-ORDER2-ACTIVE-SUPPORT-CERTIFICATE.json"


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def blob_sha1(path):
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def residual_cost(c):
    # Leading local A1 non-extension coefficient after q~c*m
    # hyperplane vanishing. c is Fraction.
    if c <= Fraction(1, 6):
        return Fraction(11, 108) - c*c
    return c**3 - c*c/Fraction(2,1) - c/Fraction(4,1) + Fraction(1,8)


def supply(c):
    # Product-cover invariant leading coefficient after twist -qH.
    return Fraction(4,3) * (1 - 2*c)**3


def lower(c):
    return supply(c) - 14*residual_cost(c)


def main():
    req(W5.is_file(), "missing W5 certificate")
    w5 = json.loads(W5.read_text())
    req(w5["schema"] == "STAGE32_MB104_W5_SOLO_ORDER2_ACTIVE_SUPPORT_V1", "W5 schema")
    req(w5["source_space"]["dimension"] == 13, "W5 source dimension")
    req(w5["stacked_active_support_conditions"]["nominal_rows"] == 42, "W5 nominal rows")
    req(w5["stacked_active_support_conditions"]["exact_rank"] == 12, "W5 exact rank")
    req(w5["stacked_active_support_conditions"]["kernel_dimension"] == 1, "W5 kernel dimension")
    req(w5["unique_regular_form"]["homogeneous"] == "(z-x1-x2-i*x3)*eta", "W5 hyperplane form")

    # BTVA N=14 cubic deficit.
    req(Fraction(4,3) - 14*Fraction(11,108) == -Fraction(5,54), "N14 deficit")

    # Local residual interpolation endpoints.
    req(residual_cost(Fraction(0)) == Fraction(11,108), "C(0)")
    req(residual_cost(Fraction(1,2)) == 0, "C(1/2)")
    req(residual_cost(Fraction(1,6)) == Fraction(2,27), "C(1/6) continuity low")
    high_at_boundary = Fraction(1,6)**3 - Fraction(1,6)**2/Fraction(2,1) - Fraction(1,6)/Fraction(4,1) + Fraction(1,8)
    req(high_at_boundary == Fraction(2,27), "C(1/6) continuity high")

    # Exact factorization checks on a dense rational grid.
    for k in range(0, 101):
        c = Fraction(k, 600)  # [0,1/6]
        lhs = lower(c)
        rhs = -(576*c**3 - 1620*c**2 + 432*c + 5) / 54
        req(lhs == rhs, f"low factor identity c={c}")
        req(lhs < 0, f"low negativity c={c}")

    for k in range(100, 301):
        c = Fraction(k, 600)  # [1/6,1/2]
        lhs = lower(c)
        rhs = -(2*c-1)**2 * (74*c+5) / 12
        req(lhs == rhs, f"high factor identity c={c}")
        if c < Fraction(1,2):
            req(lhs < 0, f"high negativity c={c}")
        else:
            req(lhs == 0, "endpoint zero")

    # Product-cover twisted supply sanity:
    # q=0 -> 4/3; q=m/2 -> cubic supply 0.
    req(supply(Fraction(0)) == Fraction(4,3), "untwisted supply")
    req(supply(Fraction(1,2)) == 0, "half-twist supply")

    print("PASS: Z32 N14 support-Hilbert arithmetic")
    print("W5 balanced support: dim13, rank12, kernel1 = support-hyperplane form")
    print("N14 independent cubic deficit = -5/54")
    print("uniform proportional hyperplane twist lower coefficient <0 for 0<=c<1/2")


if __name__ == "__main__":
    main()
