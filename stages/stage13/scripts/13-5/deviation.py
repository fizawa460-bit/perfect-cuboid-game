#!/usr/bin/env python3
"""Stage13-5: define deviation from the reference proportion (1/2,1/4,1/4).

Primary population: canonical primitive exactly-one counts N_ab,N_ac,N_bc.
Control population: raw incidences A_ab,A_ac,A_bc.

For any positive count vector X=(X_ab,X_ac,X_bc), let P=X/sum X and
P0=(1/2,1/4,1/4).  Define Delta=P-P0 and the two independent coordinates

    alpha = P_ab - 1/2,
    beta  = (P_ac - P_bc)/2.

Then exactly

    Delta = alpha*(1,-1/2,-1/2) + beta*(0,1,-1).

Thus alpha measures the leading-vs-pair deviation and beta measures the split
between the two near-1 components.  This is a definition/finite diagnostic only;
no convergence or asymptotic claim is made.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage13/data/13-3/raw_incidence_report.json"
OUTPUT = ROOT / "stages/stage13/data/13-5/deviation_report.json"

REF = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 4))


def stats(counts: dict[str, int]) -> dict:
    xs = (int(counts["ab"]), int(counts["ac"]), int(counts["bc"]))
    total = sum(xs)
    p = tuple(Fraction(x, total) for x in xs)
    delta = tuple(p[i] - REF[i] for i in range(3))
    alpha = delta[0]
    beta = (p[1] - p[2]) / 2

    # Exact reconstruction check.
    recon = (
        alpha,
        -alpha / 2 + beta,
        -alpha / 2 - beta,
    )
    if recon != delta or sum(delta) != 0:
        raise ArithmeticError(("deviation reconstruction", xs, delta, recon))

    l1 = sum(abs(x) for x in delta)
    linf = max(abs(x) for x in delta)
    l2 = math.sqrt(sum(float(x * x) for x in delta))

    return {
        "counts": {"ab": xs[0], "ac": xs[1], "bc": xs[2], "total": total},
        "proportion": {"ab": float(p[0]), "ac": float(p[1]), "bc": float(p[2])},
        "delta": {"ab": float(delta[0]), "ac": float(delta[1]), "bc": float(delta[2])},
        "mode": {"alpha_leading": float(alpha), "beta_split": float(beta)},
        "norm": {"L1": float(l1), "Linf": float(linf), "L2": l2},
    }


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = []
    for row in source["rows"]:
        rows.append(
            {
                "B": int(row["B"]),
                "raw": stats(row["raw_incidence"]),
                "exact_one": stats(row["exact_one"]),
            }
        )

    top = rows[-1]["exact_one"]
    alpha = Fraction(131, 168030)
    beta = Fraction(619, 84015)

    report = {
        "metadata": {
            "stage": "13-5",
            "title": "Deviation coordinates from the reference proportion (1/2,1/4,1/4)",
            "primary_population": "exact-one canonical primitive count N",
            "control_population": "raw face incidence A",
            "scope": "definition plus finite diagnostics; no convergence or asymptotic claim",
        },
        "definition": {
            "reference": "P0=(1/2,1/4,1/4)",
            "primary": "P(B)=(N_ab,N_ac,N_bc)/N1; Delta(B)=P(B)-P0",
            "coordinates": {
                "alpha": "P_ab-1/2 = (N_ab-N_ac-N_bc)/(2N1)",
                "beta": "(P_ac-P_bc)/2 = (N_ac-N_bc)/(2N1)",
                "reconstruction": "Delta = alpha*(1,-1/2,-1/2) + beta*(0,1,-1)",
                "exact_reference_condition": "Delta=0 iff alpha=beta=0 iff proportions are exactly (1/2,1/4,1/4)",
            },
            "interpretation": {
                "alpha": "leading-vs-pair mode: whether ab carries exactly one half of the total",
                "beta": "two-near-1 split mode: the ac/bc imbalance after total normalization",
                "basis_orthogonal_Euclidean": True,
            },
        },
        "rows": rows,
        "largest_bound": {
            "B": 100000,
            "exact_one_counts": top["counts"],
            "alpha_exact": "131/168030",
            "beta_exact": "619/84015",
            "alpha": float(alpha),
            "beta": float(beta),
            "abs_beta_over_abs_alpha": float(abs(beta / alpha)),
            "delta": top["delta"],
            "L1": top["norm"]["L1"],
            "Linf": top["norm"]["Linf"],
            "interpretation": "At B=100000 the normalized deviation is much more strongly expressed in the ac-vs-bc split coordinate beta than in the leading-half coordinate alpha. This is a finite statement only.",
        },
        "conclusion": {
            "deviation_vector_defined": True,
            "two_independent_coordinates_defined": True,
            "largest_bound_leading_coordinate_small": True,
            "largest_bound_split_coordinate_dominates_in_absolute_coordinate_size": True,
            "convergence_claim": False,
            "next": "Stage13-6: classify alpha, beta and Delta by overlap, geometry, parity, representation density, primitive support, and boundary layers.",
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["largest_bound"], indent=2))


if __name__ == "__main__":
    main()
