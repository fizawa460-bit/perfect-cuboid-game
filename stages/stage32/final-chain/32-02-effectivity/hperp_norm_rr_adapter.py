#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from fractions import Fraction

K2 = 16


@dataclass(frozen=True)
class NormRRResult:
    d: int
    N: int
    r: int
    m: int
    C2_numerator: int
    C2_denominator: int
    C2: int | None
    status: str
    reason: str
    effective_divisor_certified: bool
    exact_norm_gate_lhs: int
    exact_norm_gate_rhs: int


def classify_from_norm(d: int, N: int, *, source_affirmed: bool = False) -> NormRRResult:
    if d <= 0 or N < 0:
        return NormRRResult(
            d=d,
            N=N,
            r=0,
            m=0,
            C2_numerator=0,
            C2_denominator=1,
            C2=None,
            status="INVALID_INPUT",
            reason="Require positive degree d and nonnegative N=-y^2.",
            effective_divisor_certified=False,
            exact_norm_gate_lhs=0,
            exact_norm_gate_rhs=0,
        )

    r = math.gcd(d, K2)
    m = K2 // r
    c2 = Fraction(d * d, K2) - Fraction(N, m * m)
    lhs = 16 * N
    rhs = m * m * (d * d - 16 * d + 224)

    if c2.denominator != 1:
        return NormRRResult(
            d=d,
            N=N,
            r=r,
            m=m,
            C2_numerator=c2.numerator,
            C2_denominator=c2.denominator,
            C2=None,
            status="INVALID_INTEGRAL_CLASS_RECONSTRUCTION",
            reason="The supplied scalar N does not reconstruct an integral C^2 under the audited Stage29 y=mC-nH relation.",
            effective_divisor_certified=False,
            exact_norm_gate_lhs=lhs,
            exact_norm_gate_rhs=rhs,
        )

    C2 = int(c2)
    if (C2 - d) % 2:
        return NormRRResult(
            d=d,
            N=N,
            r=r,
            m=m,
            C2_numerator=c2.numerator,
            C2_denominator=1,
            C2=C2,
            status="INVALID_INTEGRAL_CLASS_PARITY",
            reason="Surface Riemann-Roch requires C.(C-K)=C2-d to be even for an integral divisor class.",
            effective_divisor_certified=False,
            exact_norm_gate_lhs=lhs,
            exact_norm_gate_rhs=rhs,
        )

    if not source_affirmed:
        return NormRRResult(
            d=d,
            N=N,
            r=r,
            m=m,
            C2_numerator=c2.numerator,
            C2_denominator=1,
            C2=C2,
            status="RR_INCONCLUSIVE_SOURCE_NOT_AFFIRMED",
            reason="Retained Stage29 finite-Picard and Stage32 surface source locks must be replayed before certification.",
            effective_divisor_certified=False,
            exact_norm_gate_lhs=lhs,
            exact_norm_gate_rhs=rhs,
        )

    if d <= K2:
        return NormRRResult(
            d=d,
            N=N,
            r=r,
            m=m,
            C2_numerator=c2.numerator,
            C2_denominator=1,
            C2=C2,
            status="RR_INCONCLUSIVE",
            reason="d<=16, so the retained nefness argument does not force h2(O(C))=0.",
            effective_divisor_certified=False,
            exact_norm_gate_lhs=lhs,
            exact_norm_gate_rhs=rhs,
        )

    if lhs > rhs:
        return NormRRResult(
            d=d,
            N=N,
            r=r,
            m=m,
            C2_numerator=c2.numerator,
            C2_denominator=1,
            C2=C2,
            status="RR_INCONCLUSIVE",
            reason="Exact Hperp norm is above the RR sufficient threshold; this is not a non-effectivity statement.",
            effective_divisor_certified=False,
            exact_norm_gate_lhs=lhs,
            exact_norm_gate_rhs=rhs,
        )

    return NormRRResult(
        d=d,
        N=N,
        r=r,
        m=m,
        C2_numerator=c2.numerator,
        C2_denominator=1,
        C2=C2,
        status="RR_EFFECTIVE_DIVISOR_CERTIFIED",
        reason="The audited Stage29 norm identity reconstructs C^2 and the exact scalar inequality is equivalent to C^2>=d-14; retained surface data then force h0(O(C))>=1.",
        effective_divisor_certified=True,
        exact_norm_gate_lhs=lhs,
        exact_norm_gate_rhs=rhs,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Stage32 32-02 exact Hperp-norm to RR effectivity adapter")
    ap.add_argument("--d", type=int, required=True, help="canonical degree d=K.C")
    ap.add_argument("--negative-hperp-square", dest="N", type=int, required=True, help="N=-y^2 for y=mC-nH")
    ap.add_argument("--source-affirmed", action="store_true", help="Affirm retained source-lock replay for this invocation")
    args = ap.parse_args()
    print(json.dumps(asdict(classify_from_norm(args.d, args.N, source_affirmed=args.source_affirmed)), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
