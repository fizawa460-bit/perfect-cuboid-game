#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09L" / "physical-base-full2-descent-preflight.json"
K_CERT = ROOT / "stages" / "stage36" / "36-09K" / "genus-one-quartic-elliptic-adapter.json"
BASE = "f91c045796cba859ec1dd172cf7871fcac5f6d8a"
V35_BLOB = "eba95aaf3cfc27853793474e479792626cc9840b"
K_CERT_BLOB = "1a838c473343eb0eac0a0a871c95fdf207475d53"
CERT_BLOB = "56fd432a3ae6046bc4643b56bf562660af49fe89"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def check_fiber(q: Fraction) -> None:
    r = q + 1/q
    h = q - 1/q
    s = r*r
    assert r*r - h*h == 4
    assert h != 0 and r != 0 and h not in (2, -2)

    e0 = s*s
    ep = 4*s*h
    em = -4*s*h
    a = r*(h-2)
    b = r*(h+2)
    assert e0-ep == a*a
    assert e0-em == b*b
    assert ep-em == 8*s*h

    A = a*a+b*b
    B = a*a*b*b
    assert A == 2*s*s
    assert B == s*s*(h*h-4)*(h*h-4)

    x = a*b
    y = a*b*(a+b)
    assert y*y == x*(x+a*a)*(x+b*b)
    m = a+b
    x2 = m*m-A-2*x
    y2 = -y + m*(x-x2)
    assert x2 == 0 and y2 == 0
    assert x != 0 and y != 0
    xi = e0+x
    assert xi == 2*s*h*h

    k = b/a
    U = x/(a*a)
    V = y/(a*a*a)
    assert U == k and V == k*(k+1)
    assert V*V == U*(U+1)*(U+k*k)
    rho = r*(k-1)/2
    assert rho*rho == 2*(k*k+1)

    Ap = -2*A
    Bp = A*A-4*B
    assert Ap == -4*s*s
    assert Bp == 64*s*s*h*h
    R1 = 4*s*h*h
    R2 = 16*s
    assert R1+R2 == 4*s*s
    assert R1*R2 == 64*s*s*h*h


def main() -> None:
    c = json.loads(CERT.read_text())
    s = json.loads(STATE.read_text())
    assert c["schema"] == "STAGE36_36_09L_PHYSICAL_BASE_FULL2_DESCENT_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V35_BLOB
    assert blob(K_CERT) == K_CERT_BLOB

    for q in [Fraction(3), Fraction(5,2), Fraction(7,3), Fraction(-3,2)]:
        check_fiber(q)

    for p in [3,5,7,11,13,17,19,23]:
        h = Fraction(p*p-1, p)
        assert (p*p-1) % p == p-1
        assert h.denominator == p
        assert h != 0 and h*h != 4

    rd = c["root_difference_collapse"]
    assert rd["squareclasses"] == {
        "[e0-eplus]": "1",
        "[e0-eminus]": "1",
        "[eplus-eminus]": "[2*h]",
    }
    o4 = c["universal_rational_order4_point"]
    assert o4["conclusion"] == "P4 has exact order 4 on every retained physical fiber"
    assert "Z/4 x Z/2" in o4["torsion_credit"]
    iso = c["two_isogeny_quotient"]
    assert "X1*(X1-4*s*h^2)*(X1-16*s)" in iso["quotient_model"]
    obs = c["fixed_S_uniform_descent_obstruction"]
    assert obs["route_effect"] == "BLOCK_FIXED_S_UNIFORM_FULL2_SELMER_ENUMERATION_FROM_CURRENT_DATA"

    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V36_36_09L_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    L = s["authority_frontier"]["36-09L"]
    assert L["certificate_blob_sha"] == CERT_BLOB
    assert L["UNIVERSAL_RATIONAL_ORDER4_POINT"] is True
    assert L["FIXED_S_UNIFORM_FULL2_DESCENT"] == "BLOCKED"
    assert L["B3_TORSION_ENHANCED_2_ISOGENY_FAMILY"] == "LIVE"
    assert s["current"]["36_09M_entry_allowed"] is False
    assert s["promotion_gates"]["full_2_Selmer_group_computed"] is False
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False
    print("36-09L exact full-2 descent preflight verified; universal order-4 found; fixed-S uniform descent blocked; 36-09M locked")


if __name__ == "__main__":
    main()
