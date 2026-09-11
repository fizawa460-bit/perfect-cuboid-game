#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict

K2 = 16
CHI_O = 8


@dataclass(frozen=True)
class RRResult:
    d: int
    C2: int
    status: str
    chi_OC: int | None
    reason: str
    effective_divisor_certified: bool
    integral_class_parity_ok: bool


def classify(d: int, C2: int, *, assumptions_affirmed: bool = True) -> RRResult:
    delta = C2 - d
    if delta % 2:
        return RRResult(
            d=d,
            C2=C2,
            status="INVALID_INTEGRAL_CLASS_PARITY",
            chi_OC=None,
            reason="Surface RR requires C.(C-K)=C2-d to be even for an integral divisor class.",
            effective_divisor_certified=False,
            integral_class_parity_ok=False,
        )

    chi = CHI_O + delta // 2
    if not assumptions_affirmed:
        return RRResult(
            d=d,
            C2=C2,
            status="RR_INCONCLUSIVE_ASSUMPTIONS_NOT_AFFIRMED",
            chi_OC=chi,
            reason="K2=16, chi(O)=8, K nef, Serre duality and RR are conditional inputs of this checkpoint.",
            effective_divisor_certified=False,
            integral_class_parity_ok=True,
        )

    if d <= K2:
        return RRResult(
            d=d,
            C2=C2,
            status="RR_INCONCLUSIVE",
            chi_OC=chi,
            reason="d<=K2, so K.(K-C)=K2-d is not negative and h2-vanishing is not certified by the nefness argument.",
            effective_divisor_certified=False,
            integral_class_parity_ok=True,
        )

    if chi < 1:
        return RRResult(
            d=d,
            C2=C2,
            status="RR_INCONCLUSIVE",
            chi_OC=chi,
            reason="chi(O(C))<1, so RR plus h2=0 alone does not force h0>0.",
            effective_divisor_certified=False,
            integral_class_parity_ok=True,
        )

    return RRResult(
        d=d,
        C2=C2,
        status="RR_EFFECTIVE_DIVISOR_CERTIFIED",
        chi_OC=chi,
        reason="d>K2 gives h2=0 by nefness+Serre duality; chi(O(C))>=1 then forces h0(O(C))>=1.",
        effective_divisor_certified=True,
        integral_class_parity_ok=True,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Conditional Stage32 32-02 RR effectivity sufficient classifier")
    ap.add_argument("--d", type=int, required=True, help="d = K.C")
    ap.add_argument("--c2", type=int, required=True, help="C2 = C.C")
    ap.add_argument(
        "--assumptions-not-affirmed",
        action="store_true",
        help="Fail closed when the surface assumptions are not source-affirmed for the caller.",
    )
    args = ap.parse_args()
    result = classify(args.d, args.c2, assumptions_affirmed=not args.assumptions_not_affirmed)
    print(json.dumps(asdict(result), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
