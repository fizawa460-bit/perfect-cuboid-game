#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data")
OUT = ROOT / "13-12ag/proof_explicitness_audit_report.json"
GEOM = ROOT / "13-3/geometric_chamber_report.json"
INDIV = ROOT / "13-7/individual_category_asymptotic_report.json"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def inert_unit_row(p: int) -> dict:
    assert p % 4 == 3

    circle_points = sum(1 + chi(1 - x * x, p) for x in range(p))
    hyperbola_points = sum(1 + chi(1 + z * z, p) for z in range(p))
    jacobi = sum(chi(u, p) * chi(1 - u, p) for u in range(p))

    s0 = s1 = s2 = s3 = 0
    total = zero_states = accepted = 0

    for x in range(p):
        wy = 1 + chi(1 - x * x, p)
        for z in range(p):
            wd = 1 + chi(1 + z * z, p)
            weight = wy * wd
            q = (x * x + z * z) % p
            cq = chi(q, p)

            s0 += cq
            s1 += chi(1 - x * x, p) * cq
            s2 += chi(1 + z * z, p) * cq
            s3 += chi(1 - x * x, p) * chi(1 + z * z, p) * cq

            total += weight
            if q == 0:
                zero_states += weight
            if cq >= 0:
                accepted += weight

    weighted_character_sum = s0 + s1 + s2 + s3

    # Independent u,t expansion of S3=A+B-C-D.
    A = B = C = D = 0
    for u in range(p):
        for t in range(p):
            K = ((1 - u) * (1 - t) * (u - t)) % p
            cK = chi(K, p)
            A += cK
            B += chi(u, p) * cK
            C += chi(t, p) * cK
            D += chi(u * t, p) * cK

    expected = {
        "circle_points": p + 1,
        "hyperbola_points": p - 1,
        "jacobi_chi_chi": 1,
        "S0": 0,
        "S1": p - 1,
        "S2": p + 1,
        "S3": -2,
        "A": 0,
        "B": -1,
        "C": 1,
        "D": 0,
        "weighted_character_sum": 2 * (p - 1),
        "total_unit_states": p * p - 1,
        "zero_states": 4,
        "accepted_unit_states": (p + 1) * (p + 1) // 2,
    }

    actual = {
        "circle_points": circle_points,
        "hyperbola_points": hyperbola_points,
        "jacobi_chi_chi": jacobi,
        "S0": s0,
        "S1": s1,
        "S2": s2,
        "S3": s3,
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "weighted_character_sum": weighted_character_sum,
        "total_unit_states": total,
        "zero_states": zero_states,
        "accepted_unit_states": accepted,
    }

    return {
        "p": p,
        "actual": actual,
        "expected": expected,
        "pass": actual == expected,
        "alpha_p": accepted / total,
        "alpha_formula": (p + 1) / (2 * (p - 1)),
    }


def bridge_report() -> dict:
    geom = json.loads(GEOM.read_text())
    indiv = json.loads(INDIV.read_text())
    names = ("ab", "ac", "bc")

    I = [float(geom["numerical_chamber_integrals"][f"I_{q}"]) for q in names]
    J = [float(indiv["stage13_3b_bridge"]["J_from_stage13_3b"][q]) for q in names]
    target = [2.0 * x / math.pi for x in I]
    errors = [abs(J[i] - target[i]) for i in range(3)]

    return {
        "identity": "w_q d_omega = dtheta dalpha; psi=pi/2-theta; J_q=(2/pi)I_q",
        "I": dict(zip(names, I)),
        "J": dict(zip(names, J)),
        "two_I_over_pi": dict(zip(names, target)),
        "max_abs_numeric_validator_error": max(errors),
        "numeric_validator_pass": max(errors) < 3e-12,
        "symbolic_status": "PROVED_IN_13_12AG_RESULT_MD",
    }


def build_report() -> dict:
    rows = [
        inert_unit_row(p)
        for p in range(3, 100)
        if is_prime(p) and p % 4 == 3
    ]
    failures = [row["p"] for row in rows if not row["pass"]]
    bridge = bridge_report()

    return {
        "metadata": {
            "stage": "13-12ag",
            "scope": "post-R03 proof-explicitness audit; finite computations validate but do not replace the symbolic proofs in result.md",
        },
        "coarea_bridge": bridge,
        "inert_character_sum": {
            "symbolic_chain": [
                "T=(p+1)(p-1)=p^2-1",
                "S=S0+S1+S2+S3",
                "S0=0",
                "S1=p-1",
                "S2=p+1",
                "S3=A+B-C-D=-2 with (A,B,C,D)=(0,-1,1,0)",
                "S=2(p-1)",
                "N0=4",
                "Nacc=(T+S+N0)/2=(p+1)^2/2",
                "alpha_p=(p+1)/(2(p-1))",
            ],
            "checked_inert_primes_below_100": len(rows),
            "failures": failures,
            "rows": rows,
            "symbolic_status": "PROVED_IN_13_12AG_RESULT_MD",
        },
        "selberg_delange_crosswalk": {
            "zero_scale": "A0=zeta^1 * G_h with G_h holomorphic near 1",
            "zero_base": "B0=zeta^2 * G_b with G_b holomorphic near 1",
            "residual_euler_products": "local quotient 1+O(p^(-2 sigma)); absolute convergence for sigma>1/2",
            "mixed_correction": "weighted Wiener plus all fixed logarithmic moments",
            "nonzero_scale": "A_l=L(s,xi_8l)E_l; no zeta pole",
            "retained_range": "1<=ell<=(log B)^4",
            "external_boundary": "finite-order Selberg-Delange/Tauberian plus standard Dirichlet/Gaussian-Hecke zero-free and vertical-growth input",
            "status": "HYPOTHESES_MAPPED_EXPLICITLY_IN_13_12AG_RESULT_MD",
        },
        "status": {
            "STAGE13_12AG": "COMPLETE_PROOF_EXPLICITNESS_SUPPLEMENT",
            "COAREA_IQ_TO_INTERVAL_LENGTH": "PROVED_EXPLICITLY",
            "ANALYTIC_JQ_EQ_2IQ_OVER_PI": "PROVED_WITH_FULL_JACOBIAN_CHAIN",
            "INERT_UNIT_CHARACTER_SUM": "PROVED_SYMBOLICALLY",
            "SELBERG_DELANGE_HYPOTHESIS_CROSSWALK": "RECORDED",
            "R03_ARTIFACT_MUTATED": False,
            "STAGE13_THEOREM_CONSTANTS_CHANGED": False,
            "STAGE13_COUNTING_CONVENTION_CHANGED": False,
        },
        "pass": not failures and bridge["numeric_validator_pass"],
    }


def main() -> None:
    report = build_report()
    if not report["pass"]:
        raise SystemExit("Stage13-12ag audit failed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
