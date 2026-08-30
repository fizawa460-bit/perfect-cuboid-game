#!/usr/bin/env python3
"""Network-free verifier for the corrected Stage33-05 R4 translation-descent J2 torsor."""

from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sympy as sp

CERT = Path(__file__).with_name("j2-r4-correct-translation-torsor.json")

def canonical_sha(d):
    d = dict(d)
    d.pop("canonical_sha256", None)
    raw = json.dumps(d, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def quartic_j(A, C, E):
    # Binary quartic A*u^4 + C*u^2*v^2 + E*v^4 (B=D=0).
    I = sp.expand(12*A*E + C**2)
    J = sp.expand(72*A*C*E - 2*C**3)
    return sp.factor(1728 * 4*I**3 / (4*I**3 - J**2))

def cubic_j(A, B):
    # y^2=x*(x^2+A*x+B)
    c4 = 16*(A**2 - 3*B)
    delta = 16*B**2*(A**2 - 4*B)
    return sp.factor(c4**3 / delta)

def main():
    c = json.loads(CERT.read_text())
    t = sp.symbols("t")
    x, y, w = sp.symbols("x y w")
    sq2 = sp.sqrt(2)

    q = t**4 - 6*t**2 + 1
    a = (t**2 + 1)**2
    b = (2*t*(t**2 - 1))**2
    d = (t + 1 + sq2)/(t - 1 + sq2)

    assert sp.factor(a**2 - 4*b - q**2) == 0

    # R3 f2 has the two exact odd branch valuations recorded in the certificate.
    r2 = -(1 + sq2)
    r4 = 1 - sq2
    num, den = sp.fraction(sp.cancel(d))
    assert sp.simplify(num.subs(t, r2)) == 0
    assert sp.simplify(den.subs(t, r4)) == 0
    assert sp.simplify(sp.diff(num, t).subs(t, r2)) != 0
    assert sp.simplify(sp.diff(den, t).subs(t, r4)) != 0
    assert sp.simplify(q.subs(t, r2)) == 0
    assert sp.simplify(q.subs(t, r4)) == 0

    # Translation by T=(0,0) on E: y^2=x*(x^2+a*x+b).
    xT = b/x
    yT = -b*y/x**2
    Eeq = y**2 - x*(x**2 + a*x + b)
    translated = sp.factor(yT**2 - xT*(xT**2 + a*xT + b))
    assert sp.factor(translated - b**2/x**4 * Eeq) == 0

    # Semilinear action sends (w,x,y)->(-w,b/x,-b*y/x^2).
    u0 = x + b/x
    n = w*y/x
    v = w*(x - b/x)
    subs = {w: -w, x: b/x, y: -b*y/x**2}
    assert sp.factor(u0.subs(subs, simultaneous=True) - u0) == 0
    assert sp.factor(n.subs(subs, simultaneous=True) - n) == 0
    assert sp.factor(v.subs(subs, simultaneous=True) - v) == 0

    # Eliminate u0 from n^2=d*(u0+a), v^2=d*(u0^2-4b).
    u = sp.Symbol("u0")
    n2 = d*(u + a)
    eliminated = sp.expand(n2**2 - 2*a*d*n2 + d**2*q**2 - d**2*(u**2 - 4*b))
    assert sp.factor(eliminated) == 0

    # Attempt-1 quartic has the dual 2-isogenous Jacobian, not E.
    jE = cubic_j(a, b)
    jEprime = cubic_j(-2*a, q**2)
    jold = quartic_j(d, a, b/d)
    assert sp.factor(jold - jEprime) == 0
    assert sp.factor(jEprime - jE) != 0

    # Correct translation-descent quartic, after division by d.
    jcorrect = quartic_j(1/d, -2*a, d*q**2)
    assert sp.factor(jcorrect - jE) == 0

    assert c["attempt"] == 2
    assert c["status"] == "PASS_EXACT_R4_ATTEMPT2_CORRECT_E_TORSOR_MODEL_LATTICE_PENDING"
    assert c["attempt1_diagnosis"]["old_ns_glue_target_revoked"] is True
    assert c["attempt1_diagnosis"]["binary_quartic_j_invariant_matches_E"] is False
    assert c["attempt1_diagnosis"]["binary_quartic_j_invariant_matches_Eprime"] is True
    assert c["lattice_reduction"]["candidate_minimum_norms"] == [4,8,12]
    assert c["lattice_reduction"]["minimum_norm_selected"] is False
    assert c["firewalls"]["stage33_05_reclosed"] is False
    assert c["firewalls"]["stage33_12_closed_exact"] is False
    assert c["firewalls"]["stage33_13_released"] is False
    assert c["canonical_sha256"] == canonical_sha(c)

    print(json.dumps({
        "status": "PASS_EXACT",
        "canonical_sha256": c["canonical_sha256"],
        "attempt": 2,
        "correct_jacobian": "E",
        "attempt1_jacobian": "Eprime_Tr",
        "candidate_minimum_norms": [4,8,12]
    }, sort_keys=True))

if __name__ == "__main__":
    main()
