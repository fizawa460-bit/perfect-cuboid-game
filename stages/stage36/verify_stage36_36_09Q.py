#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09Q" / "etau-torsion-growth-stage14-second-basechange-preflight.json"
LOCK = ROOT / "stages" / "stage36" / "36-09Q" / "stage14-pythagorean-basechange-source-lock.md"
P_CERT = ROOT / "stages" / "stage36" / "36-09P" / "etau-generic-mw-zero-exceptional-growth-preflight.json"
STAGE14 = ROOT / "stages" / "stage14" / "archive" / "stage14-4af-specialization-triple.md"
STAGE14_DATA = ROOT / "stages" / "stage14" / "data" / "14-4" / "specialization_triple_audit.json"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "c17f1a681c220292f93880a726f1f571174f53b9"
V45_BLOB = "313f70b43cd7ab7eaeb2a240027f9f9137492222"
CERT_BLOB = "36b24b1a42231ccfec9364df6a8d52af13ceb6de"
LOCK_BLOB = "cb231b7d1351a9787c3da2e187c4bd0e67adf7c9"
P_CERT_BLOB = "a611b698fccfbd29a971ccede5c77b6832101c77"
STAGE14_BLOB = "f14d6840d10aaa36df63b2d4a70a07d509b596ce"
STAGE14_DATA_BLOB = "d0d9d8ececd2432bedc94511e94ed3da11ec2d91"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def is_square_int(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def is_square_fraction(q: Fraction) -> bool:
    return q >= 0 and is_square_int(q.numerator) and is_square_int(q.denominator)


def base_identities() -> None:
    # All identities have degree <= 8; ten distinct retained integer samples
    # prove the corresponding numerator polynomial identities coefficientwise.
    samples = [-6,-5,-4,-3,-2,2,3,4,5,6]
    for p in samples:
        D = p * (p*p - 1)
        C = p**4 - 6*p*p + 1
        H = (p*p + 1)**2
        Nm = p*p - 2*p - 1
        Np = p*p + 2*p - 1
        assert C == Nm * Np
        assert H + 4*D == Np*Np
        assert H - 4*D == Nm*Nm
        assert H*H - C*C == (4*D)**2
        assert Np*Np - Nm*Nm == 8*D
        assert Np*Np + Nm*Nm == 2*(p*p+1)**2

        t = Fraction(C, 4*D)
        h = Fraction(H, 4*D)
        u = Fraction(Nm, Np)
        assert h*h == 1 + t*t
        assert t == Fraction(2)*u/(1-u*u)
        assert h == (1+u*u)/(1-u*u)
        assert 2*(1+u*u) == Fraction(4*(p*p+1)**2, Np*Np)


def isomorphism_check() -> None:
    # Direct denominator-cleared identity for the S3 Legendre transform.
    # With a^2+b^2=1 and U=X/(X-1):
    # b^2*X + a^2*(X-1) = X-a^2,
    # which is exactly the missing factor in the target Stage14 cubic.
    for a2 in [Fraction(1,4), Fraction(9,25), Fraction(25,169)]:
        b2 = 1-a2
        for X in [Fraction(2), Fraction(3,2), Fraction(-1), Fraction(7,3)]:
            if X == 1:
                continue
            assert b2*X + a2*(X-1) == X-a2
            U = X/(X-1)
            t2 = a2/b2
            old_rhs = X*(X-1)*(X-a2)
            transformed_lhs = old_rhs/(b2*(X-1)**4)
            target_rhs = U*(U-1)*(U+t2)
            assert transformed_lhs == target_rhs
            # Open round-trip.
            assert U/(U-1) == X


def denominator_safety() -> None:
    # Nplus/Nminus have discriminant 8 and therefore no rational roots;
    # C viewed as z^2-6z+1 in z=p^2 has discriminant 32.
    assert not is_square_int(8)
    assert not is_square_int(32)


def converse_basechange_check() -> None:
    # Discriminant of (u-1)p^2+2(u+1)p+(1-u) is 8(u^2+1).
    for u in [Fraction(1,4), Fraction(2,3), Fraction(-3,5), Fraction(5,7)]:
        A=u-1; B=2*(u+1); C0=1-u
        disc=B*B-4*A*C0
        assert disc == 8*(u*u+1)

    # Forward p -> u always lands on the exact second-conic square locus.
    for p in [Fraction(2),Fraction(3,2),Fraction(-2),Fraction(5,3),Fraction(-4,3)]:
        if p in (0,1,-1):
            continue
        Np=p*p+2*p-1
        Nm=p*p-2*p-1
        u=Nm/Np
        rhs=2*(1+u*u)
        witness=2*(p*p+1)/Np
        assert rhs == witness*witness


def source_authority_check() -> None:
    text = STAGE14.read_text()
    assert "E_t:" in text and "Y^2=X(X-1)(X+t^2)" in text
    assert "rank}E(\\overline{\\mathbf Q}(u))" in text
    assert "E_t(\\mathbf Q)_{tors}" in text
    assert "Z/2\\mathbf Z\\times\\mathbf Z/4\\mathbf Z" in text
    assert "rank-jump frequency" in text
    lock = LOCK.read_text()
    assert STAGE14_BLOB in lock
    assert "No Stage35-EX provisional claim is imported as authority" in lock


def bounded_diagnostic_check(c: dict) -> None:
    data=json.loads(STAGE14_DATA.read_text())
    seen=[]
    for row in data["finite_audit"]["samples"]:
        S,X,H=row["F1"]
        u=Fraction(X,H+S)
        if u not in seen:
            seen.append(u)
        assert not is_square_fraction(2*(1+u*u))
    expected={Fraction(1,4),Fraction(4,5),Fraction(3,11),Fraction(5,11),Fraction(3,13)}
    assert set(seen)==expected
    assert c["bounded_diagnostic"]["credit"] == "NONE"


def main() -> None:
    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09Q_E_TAU_TORSION_GROWTH_STAGE14_SECOND_BASECHANGE_PREFLIGHT_V1"
    assert c["status"] == "EXACT_TORSION_GROWTH_EXCLUDED_AND_RANKJUMP_SECOND_BASECHANGE_REDUCTION_PENDING_HOSTILE_AUDIT"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert blob(LOCK) == LOCK_BLOB
    assert blob(P_CERT) == P_CERT_BLOB
    assert blob(STAGE14) == STAGE14_BLOB
    assert blob(STAGE14_DATA) == STAGE14_DATA_BLOB
    assert blob(W03) == W03_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V45_BLOB

    base_identities()
    isomorphism_check()
    denominator_safety()
    converse_basechange_check()
    source_authority_check()
    bounded_diagnostic_check(c)

    iso=c["exact_isomorphism_to_stage14_signed_family"]
    assert iso["birational_isomorphism_over_Qp"] is True
    ba=c["stage14_pythagorean_base_adapter"]
    assert ba["description"] == "SECOND_PYTHAGOREAN_CONIC_BASE_CHANGE"
    tg=c["torsion_growth_exclusion"]
    assert tg["stage14_fiberwise_theorem_applies"] is True
    assert tg["specialized_torsion_for_every_retained_p"] == "Z/4 x Z/2"
    assert tg["torsion_growth_possible"] is False
    assert tg["torsion_growth_excluded"] is True
    rr=c["remaining_rankjump_reduction"]
    assert rr["only_remaining_MW_growth_species"] == "positive rank jump"
    assert rr["stage14_uniform_rankjump_exclusion_available"] is False
    assert rr["rankjump_excluded"] is False
    assert rr["joint_rankjump_receiver_intersection_executed"] is False
    assert rr["receiver_closed"] is False
    fw=c["scope_firewalls"]
    assert fw["E_tau_torsion_growth_excluded"] is True
    assert fw["E_tau_positive_rank_jumps_excluded"] is False
    assert fw["second_basechange_rankjump_locus_empty"] is False
    assert fw["S34_W03_receiver_intersection_empty"] is False
    assert fw["receiver_emptiness_proved"] is False
    assert fw["R29_CAMP2_closed"] is False
    assert fw["Q11_CAMPEDELLI_closed"] is False
    assert fw["endpoint_closed"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False

    print("36-09Q exact: E_tau torsion growth excluded on every retained p; only positive-rank growth remains on the second-Pythagorean conic base change")


if __name__ == "__main__":
    main()
