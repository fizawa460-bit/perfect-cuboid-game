#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AA" / "receiver-coupled-same-x-twist-intersection-preflight.json"
Z_CERT = ROOT / "stages" / "stage36" / "36-09Z" / "explicit-mw-rankjump-witness-preflight.json"
Z_VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09Z.py"
R_CERT = ROOT / "stages" / "stage36" / "36-09R" / "etau-rankjump-receiver-esigmatau-growth-preflight.json"
S34 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "9184c7ab694415592cc428a675c0ebed27cac510"
Z_HEAD = "718dc86903cf6e1264b78800f2ef6e813abcf6c5"
CERT_BLOB = "be447726a97158849c67ed6d57d6d3c35d6ba20f"
Z_CERT_BLOB = "6a3b05e70fb146eff576df17142547b11679cf65"
Z_VERIFIER_BLOB = "6f12de6f9e5e60dee70fc0c5bcd491105f8ee627"
R_CERT_BLOB = "b55d042ede01032ff8c8b0d872510a53cb857969"
S34_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def sq(q: Fraction) -> bool:
    if q < 0:
        return False
    n, d = q.numerator, q.denominator
    return math.isqrt(n) ** 2 == n and math.isqrt(d) ** 2 == d


def affine_data(p: Fraction):
    nm = p * p - 2 * p - 1
    np = p * p + 2 * p - 1
    s = p * p + 1
    return nm, np, s, nm * nm, np * np


def receiver_values(p: Fraction, x: Fraction, y: Fraction):
    nm, np, s, A, B = affine_data(p)
    assert y * y == x * (x - A) * (x - B)
    S = 4 * s * x / y
    R2a = S * S + 4
    R2b = 4 * (x + A) * (x + B) / ((x - A) * (x - B))
    R2c = 4 * x * (x + A) * (x + B) / (y * y)
    assert R2a == R2b == R2c
    return S, R2a


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(Z_CERT) == Z_CERT_BLOB
    assert blob(Z_VERIFIER) == Z_VERIFIER_BLOB
    assert blob(R_CERT) == R_CERT_BLOB
    assert blob(S34) == S34_BLOB
    assert git("merge-base", "--is-ancestor", BASE, "HEAD") == ""
    assert git("merge-base", "--is-ancestor", Z_HEAD, "HEAD") == ""
    assert git("rev-parse", f"{Z_HEAD}:stages/stage36/36-09Z/explicit-mw-rankjump-witness-preflight.json") == Z_CERT_BLOB
    assert git("rev-parse", f"{Z_HEAD}:stages/stage36/verify_stage36_36_09Z.py") == Z_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AA_RECEIVER_COUPLED_SAME_X_TWIST_INTERSECTION_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["freshness_sync"]["current_base_main_sha"] == BASE
    assert c["freshness_sync"]["sync_merge_commit"] == "deb16e9f06bb572bbf5a90041236b60f500569ef"
    assert c["route_result"]["rankjump_implies_receiver"] is False
    assert c["route_result"]["S34_W03_exact_joint_adapter_ready"] is True
    assert c["route_result"]["S34_W03_intersection_exclusion_executed"] is False

    for pn, pd in ((2, 3), (5, 2), (14, 13), (7, 4)):
        p = Fraction(pn, pd)
        nm, np, s, A, B = affine_data(p)
        assert A + B == 2 * s * s
        assert 4 * s * s - A - B == A + B

    p = Fraction(14, 13)
    x = Fraction(97393, 13**4)
    y = Fraction(9349728, 13**6)
    S, R2 = receiver_values(p, x, y)
    assert S == Fraction(365, 24)
    assert R2 == Fraction(135529, 576)
    assert 135529 == 313 * 433
    assert not sq(R2)

    S0, C0, D0 = 29, 41, 210
    X, Y = Fraction(245), Fraction(30135)
    xh = Y * Y / (4 * X * X)
    yh = Y * (64 * D0 * D0 - X * X) / (8 * X * X)
    assert xh == Fraction(15129, 4)
    assert yh == Fraction(1386825, 8)
    assert yh * yh == xh**3 - 2 * S0 * S0 * xh * xh + C0 * C0 * xh
    p = Fraction(5, 2)
    x = xh / 2**4
    y = yh / 2**6
    S, R2 = receiver_values(p, x, y)
    assert S == Fraction(696, 275)
    assert R2 == Fraction(786916, 75625)
    assert 786916 == 4 * 13 * 37 * 409
    assert not sq(R2)

    for p in (Fraction(2, 3), Fraction(5, 2), Fraction(14, 13)):
        _, _, _, A, B = affine_data(p)
        for x in (Fraction(2), Fraction(7, 3)):
            lhs = (x + A) * (x + B) * (x - A) * (x - B)
            rhs = (x * x - A * A) * (x * x - B * B)
            assert lhs == rhs

    a = c["audit_checkpoint"]
    assert a["natural_batch_checkpoint_reached"] is True
    assert a["hostile_audit_passed"] is False
    assert a["promotion_granted"] is False
    assert c["scope_firewalls"]["whole_p_14_13_receiver_fiber_empty"] is False
    assert c["scope_firewalls"]["whole_p_5_2_receiver_fiber_empty"] is False
    assert c["scope_firewalls"]["receiver_emptiness_proved"] is False

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V61_36_09AA_BATCH_AUDIT_CHECKPOINT"
    assert st["base_main_sha"] == BASE
    aa = st["authority_frontier"]["36-09AA"]
    assert aa["SAME_X_RECEIVER_EQUIVALENCE"] is True
    assert aa["EXPLICIT_Z_POINTS_RECEIVER_INCOMPATIBLE"] is True
    assert aa["RECEIVER_RANKJUMP_INTERSECTION_EMPTY"] is False
    assert st["current"]["hostile_audit_checkpoint_reached"] is True
    assert st["current"]["36_09AB_entry_allowed"] is False
    assert st["promotion_gates"]["36_09AA_hostile_audit_passed"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AA same-x plus/minus twist receiver equivalence verified; both explicit Z MW points fail receiver K; U-AA batch hostile-audit checkpoint reached")


if __name__ == "__main__":
    main()
