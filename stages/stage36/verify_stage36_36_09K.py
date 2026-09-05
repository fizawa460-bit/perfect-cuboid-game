#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09K" / "genus-one-quartic-elliptic-adapter.json"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
J_CERT = ROOT / "stages" / "stage36" / "36-09J" / "reciprocal-involution-two-linear-cover-preflight.json"
S31 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S31-W01.md"

CERT_BLOB = "1a838c473343eb0eac0a0a871c95fdf207475d53"
J_CERT_BLOB = "72e9ca86f726f2ff286c983138d9381acdd97e62"
S31_BLOB = "122a6c1c5c871c1c7b797017e854de8ec55e7c50"
V33_BLOB = "b4aa2e3e163ee65931f272075887bc010f7b9429"
BASE = "0bc325f9b9db817193bc271121d19cb04970c5b9"

Mon = Tuple[int, int, int, int]  # Z, u/v, P, local-w

class Poly:
    def __init__(self, d: Dict[Mon, int] | None = None):
        self.d = {m: c for m, c in (d or {}).items() if c}
    @staticmethod
    def c(n: int) -> "Poly":
        return Poly({(0,0,0,0): n})
    @staticmethod
    def v(i: int) -> "Poly":
        m=[0,0,0,0]; m[i]=1
        return Poly({tuple(m): 1})
    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly.c(other)
        d=dict(self.d)
        for m,c in other.d.items(): d[m]=d.get(m,0)+c
        return Poly(d)
    __radd__=__add__
    def __neg__(self): return Poly({m:-c for m,c in self.d.items()})
    def __sub__(self, other): return self + (-other if isinstance(other,Poly) else -Poly.c(other))
    def __rsub__(self, other): return (other if isinstance(other,Poly) else Poly.c(other)) - self
    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly.c(other)
        d: Dict[Mon,int]={}
        for m,c in self.d.items():
            for n,e in other.d.items():
                k=tuple(a+b for a,b in zip(m,n))
                d[k]=d.get(k,0)+c*e
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self, n:int):
        assert n>=0
        r=Poly.c(1); b=self
        while n:
            if n&1: r=r*b
            b=b*b; n//=2
        return r
    def __eq__(self, other):
        other = other if isinstance(other, Poly) else Poly.c(other)
        return self.d == other.d
    def __repr__(self): return repr(self.d)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))

def exact_algebra() -> None:
    z=Poly.v(0); u=Poly.v(1); p=Poly.v(2); w=Poly.v(3)
    one=Poly.c(1); s=z+2; d=z-2

    # Mobius x=(1+u)/(1-u), with denominators cleared exactly.
    Aclr=(one+u)**2 + z*(one+u)*(one-u) + (one-u)**2
    Bclr=d*((one+u)**2+(one-u)**2) + 2*(z+6)*(one-u**2)
    assert Aclr == s + (2-z)*u**2
    assert Bclr == 4*(s-4*u**2)
    Cu=s**2 - s**2*u**2 + 4*d*u**4
    assert Aclr*Bclr == 4*Cu
    assert (s-4*u**2)*(s+(2-z)*u**2) == Cu

    # Quartic -> cubic. Set y=p*u^2-s and D=p^2-4d.
    D=p**2-4*d
    ysub=p*u**2-s
    R=D*u**2-(2*s*p-s**2)
    assert ysub**2-Cu == u**2*R

    # xi=2sp, eta=2s*u*D. E residual is exactly 4*s^2*D*R.
    xi=2*s*p
    eta=2*s*u*D
    Erhs=(xi-s**2)*(xi**2-16*s**2*d)
    assert eta**2-Erhs == 4*s**2*D*R

    # Inverse denominator collision at p=s/2 is equivalent to Z=6.
    assert s**2-16*d == (z-6)**2

    # Cubic polynomial discriminant for X^3+a X^2+b X+c.
    aa=-s**2
    bb=-16*s**2*d
    cc=16*s**4*d
    disc=aa**2*bb**2 - 4*bb**3 - 4*aa**3*cc - 27*cc**2 + 18*aa*bb*cc
    expected=64*s**6*d*(z-6)**4
    assert disc == expected

    # u=infinity local chart v=1/u, local w=y/u^2.
    # On w^2=4d-s^2 v^2+s^2 v^4 and p=w+s v^2,
    # D=p^2-4d equals v^2*(2sw-s^2+2s^2v^2), hence Q=D/v -> 0.
    v=u
    Ploc=w+s*v**2
    Dloc=Ploc**2-4*d
    local_curve=w**2-(4*d-s**2*v**2+s**2*v**4)
    assert Dloc - v**2*(2*s*w-s**2+2*s**2*v**2) == local_curve

    # u=0 local identity. At y->-s, (y+s)/u^2 -> s/2.
    # Encoding with w as y: (w+s)(w-s)=u^2(-s^2+4du^2).
    assert (w+s)*(w-s) - u**2*(-s**2+4*d*u**2) == w**2-Cu

    # Distinct rational 2-torsion on physical h^2=d:
    # product of differences from s^2 to +/-4sh is s^2*(Z-6)^2.
    assert s**2*(s**2-16*d) == s**2*(z-6)**2


def main() -> None:
    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09K_GENUS_ONE_QUARTIC_ELLIPTIC_ADAPTER_V1"
    assert c["status"] == "EXACT_S31_W01_BIRATIONAL_ADAPTER_PENDING_HOSTILE_AUDIT"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert blob(J_CERT) == J_CERT_BLOB
    assert blob(S31) == S31_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V33_BLOB

    exact_algebra()

    e=c["elliptic_model_EZ"]
    assert e["weierstrass_equation"] == "eta^2=(xi-s^2)*(xi^2-16*s^2*(Z-2))"
    assert e["cubic_polynomial_discriminant"] == "64*s^6*(Z-2)*(Z-6)^4"
    assert e["smooth_on_physical_domain"] is True

    inv=c["inverse_map_EZ_to_Cu_open"]
    assert "Z=6 is excluded" in inv["denominator_fail_close"]
    ex=c["complete_projective_exceptional_locus"]
    assert len(ex["Cu_points"]) == 4
    assert ex["all_inverse_denominator_zero_points_accounted_for"] is True
    assert ex["all_forward_u_zero_or_infinity_points_accounted_for"] is True

    t=c["physical_full_rational_2_torsion"]
    assert t["all_defined_over_Q_on_physical_domain"] is True
    assert "(Z/2)^2" in t["conclusion"]

    a=c["S31_W01_applicability"]
    assert a["type_match"] is True
    assert a["triggered_at_adapter_credit"] is True
    assert len(a["requirements_discharged"]) == 8
    assert a["integral_or_S_integral_transfer_credit"] is False
    assert a["rational_point_completeness_credit"] is False
    assert a["receiver_closure_credit"] is False

    s=json.loads(STATE.read_text())
    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V34_36_09K_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    assert s["base_main_sha"] == BASE
    k=s["authority_frontier"]["36-09K"]
    assert k["certificate_blob_sha"] == CERT_BLOB
    assert k["S31_W01_ADAPTER_CERTIFICATE_COMPLETE"] is True
    assert k["S31_W01_PROMOTED_TRIGGER"] is False
    assert k["PHYSICAL_FULL_RATIONAL_2_TORSION"] is True
    assert s["cycle_ledger"]["counts"] == {"live":1,"untested":3,"blocked":6,"dominated":2}
    assert s["current"]["unit"] == "36-09K"
    assert s["current"]["36_09L_entry_allowed"] is False
    assert s["promotion_gates"]["genus_one_quartic_adapter_certificate_complete"] is True
    assert s["promotion_gates"]["genus_one_quartic_adapter_triggered"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False
    assert s["claims"]["new_theorem_credit"] is False
    assert s["claims"]["receiver_emptiness_proved"] is False
    assert s["claims"]["endpoint_closed"] is False
    assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False
    print("36-09K exact quartic<->elliptic adapter PASS; exceptional locus complete; full physical rational 2-torsion; S31-W01 promotion held for hostile audit")

if __name__ == "__main__":
    main()
