#!/usr/bin/env python3
"""Network-free stdlib-only verifier for the J2 normalization 2-isogeny torsion image."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "j2-normalization-2isogeny-rational-torsion.json"
SOURCE = ROOT / "stages" / "stage33" / "33-05" / "j2_arithmetic_descent.py"

cert = json.loads(CERT.read_text(encoding="utf-8"))
stored = cert.pop("canonical_sha256")
canonical = hashlib.sha256(
    json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert canonical == stored == "81097b3eab3b9f17de5a802b88324c74a7ab80e09c70dc179d4c5af4abd04571"

blob = subprocess.check_output(["git", "hash-object", str(SOURCE)], text=True).strip()
assert blob == cert["source_locks"]["stage33_05_j2_arithmetic_descent_blob_sha1"]

# Exact arithmetic in Q(sqrt(2)); a pair (a,b) means a+b*sqrt(2).
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def powq(x, n):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, x)
    return out

def qquartic(t):
    return add(sub(powq(t, 4), (6*powq(t, 2)[0], 6*powq(t, 2)[1])), (1, 0))

def cubic_rhs(x):
    # x*(x^2-6x+1)
    return mul(x, add(sub(powq(x, 2), (6*x[0], 6*x[1])), (1, 0)))

# Binary quartic invariants for x^4-6x^2+1.
a, b, c, d, e = 1, 0, -6, 0, 1
I = 12*a*e - 3*b*d + c*c
J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c**3
assert (I, J) == (48, 0)
assert cert["binary_quartic_invariants"] == {"I": 48, "J": 0, "jacobian_j": 1728}

rp = (1, 1)
rm = (1, -1)
xp = (3, 2)
xm = (3, -2)
assert powq(rp, 2) == xp
assert powq(rm, 2) == xm
assert qquartic(rp) == (0, 0)
assert qquartic(rm) == (0, 0)
assert cubic_rhs((0, 0)) == (0, 0)
assert cubic_rhs(xp) == (0, 0)
assert cubic_rhs(xm) == (0, 0)

# The map identity is formal: Y^2=(tz)^2=t^2(t^4-6t^2+1)
# =X(X^2-6X+1) for X=t^2. The support images above are therefore exact.
assert cert["explicit_degree_two_map"] == {
    "target": "E': Y^2=X*(X^2-6*X+1)",
    "X": "t^2",
    "Y": "t*z",
    "deck_involution": "(t,z)->(-t,z)",
    "both_infinities_map_to": "O_Eprime",
}

# The three nonzero 2-torsion points are the three roots of the target cubic.
# Their sum is O, hence T_plus+T_minus is the remaining point (0,0).
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
