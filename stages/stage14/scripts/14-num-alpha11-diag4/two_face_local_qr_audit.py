#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction

PRIMES = (3, 7, 11, 19, 23)


def main():
    rows = []
    for p in PRIMES:
        qr = {x * x % p for x in range(p)}
        ambient = 0
        pass3 = 0
        for x in range(p):
            x2 = x * x % p
            for y in range(p):
                y2 = y * y % p
                if (x2 + y2) % p not in qr:
                    continue
                for z in range(p):
                    z2 = z * z % p
                    if (x2 + z2) % p not in qr:
                        continue
                    space = (x2 + y2 + z2) % p
                    # Primitive Stage14 diagonals are units at inert p, so the
                    # physical local universe keeps only nonzero square space diagonals.
                    if space == 0 or space not in qr:
                        continue
                    ambient += 1
                    if (y2 + z2) % p in qr:
                        pass3 += 1
        frac = Fraction(pass3, ambient)
        rows.append({
            "p": p,
            "ambient_two_face_plus_unit_space_states": ambient,
            "missing_third_face_qr0_pass_states": pass3,
            "missing_third_face_qr0_fail_states": ambient - pass3,
            "acceptance_fraction_exact": f"{frac.numerator}/{frac.denominator}",
            "acceptance_rate": pass3 / ambient,
            "missing_third_face_qr0_forced": pass3 == ambient,
        })

    report = {
        "stage": "14-num-alpha11-diag4",
        "classification": "EXHAUSTIVE_FINITE_FIELD_TWO_FACE_TO_THIRD_FACE_QR0_LOCAL_AUDIT",
        "local_universe": "x^2+y^2 and x^2+z^2 are QR_0, while x^2+y^2+z^2 is a nonzero QR (unit space diagonal)",
        "rows": rows,
        "decision": {
            "P3_MISSING_THIRD_FACE_QR0_FORCED": next(r for r in rows if r["p"] == 3)["missing_third_face_qr0_forced"],
            "P7_MISSING_THIRD_FACE_QR0_FORCED": next(r for r in rows if r["p"] == 7)["missing_third_face_qr0_forced"],
            "P11_MISSING_THIRD_FACE_QR0_FORCED": next(r for r in rows if r["p"] == 11)["missing_third_face_qr0_forced"],
            "GLOBAL_THIRD_FACE_INTEGRALITY_CLAIM": False,
            "FINITE_FIELD_EXHAUSTIVE_FACT_ONLY": True,
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
