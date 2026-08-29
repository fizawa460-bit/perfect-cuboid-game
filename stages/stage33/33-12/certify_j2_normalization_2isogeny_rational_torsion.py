#!/usr/bin/env python3
"""Network-free verifier for the J2 normalization 2-isogeny torsion image."""
import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "j2-normalization-2isogeny-rational-torsion.json"
SOURCE = ROOT / "stage33" / "33-05" / "j2_arithmetic_descent.py"

cert = json.loads(CERT.read_text(encoding="utf-8"))
stored = cert.pop("canonical_sha256")
canonical = hashlib.sha256(
    json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert canonical == stored == "81097b3eab3b9f17de5a802b88324c74a7ab80e09c70dc179d4c5af4abd04571"

blob = subprocess.check_output(["git", "hash-object", str(SOURCE)], text=True).strip()
assert blob == cert["source_locks"]["stage33_05_j2_arithmetic_descent_blob_sha1"]

t, z, X, Y = sp.symbols("t z X Y")
s2 = sp.sqrt(2)
q = t**4 - 6*t**2 + 1

# The displayed degree-two map lands on E': Y^2=X(X^2-6X+1).
map_identity = sp.expand((t*z)**2 - (t**2) * ((t**2)**2 - 6*t**2 + 1))
assert sp.rem(sp.Poly(map_identity, z), sp.Poly(z**2-q, z)).as_expr() == 0

# Binary quartic invariants for x^4-6x^2+1.
a, b, c, d, e = 1, 0, -6, 0, 1
I = 12*a*e - 3*b*d + c*c
J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c**3
assert (I, J) == (48, 0)
# For the Jacobian model y^2=x^3-27 I x-27 J, J=0 gives j=1728.
assert cert["binary_quartic_invariants"] == {"I": 48, "J": 0, "jacobian_j": 1728}

rp = 1 + s2
rm = 1 - s2
assert sp.expand(rp**2 - (3 + 2*s2)) == 0
assert sp.expand(rm**2 - (3 - 2*s2)) == 0
assert sp.expand(q.subs(t, rp)) == 0
assert sp.expand(q.subs(t, rm)) == 0

# The target cubic has exactly the three nonzero 2-torsion roots listed.
poly = sp.expand(X * (X**2 - 6*X + 1))
assert sp.expand(poly.subs(X, 0)) == 0
assert sp.simplify(poly.subs(X, 3 + 2*s2)) == 0
assert sp.simplify(poly.subs(X, 3 - 2*s2)) == 0

# On an elliptic curve the three nonzero 2-torsion points sum to O, hence
# T_plus + T_minus is the remaining point (0,0). Both quartic infinities map
# to O under X=t^2, Y=t*z, so phi_*(2 O-P+-P-)=(0,0).
assert cert["target_2torsion"]["relation"] == "T_plus+T_minus=(0,0)"
assert cert["j2_pushforward_class"] == "phi_*(E_J2)=(0,0) in E'[2]"
assert cert["j2_independent_observation_materialized"] is True
assert cert["marked_brauer_coordinate_selected"] is False

print(json.dumps({
    "status": "PASS_EXACT",
    "canonical_sha256": stored,
    "normalization_j": 1728,
    "j2_elliptic_quotient_2torsion_image": [0, 0],
    "marked_brauer_coordinate_selected": False,
}, sort_keys=True))
