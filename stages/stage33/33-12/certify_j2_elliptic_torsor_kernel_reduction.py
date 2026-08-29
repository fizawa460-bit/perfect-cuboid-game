#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-elliptic-torsor-kernel-reduction.json"
t, s = sp.symbols("t s")

F = sp.expand(t**2*(1-s**2)**2 + s**2*(1-t**2)**2)
A = sp.cancel((t**4 - 4*t**2 + 1)/t**2)
H = t**4 - 4*t**2 + 1
q = t**4 - 6*t**2 + 1

assert sp.expand(F - t**2*(s**4 + A*s**2 + 1)) == 0
assert sp.factor(A**2 - 4 - ((t**2-1)**2*q)/t**4) == 0

# Standard Jacobian of y^2=s^4+A*s^2+1:
# V^2=U(U^2-2*A*U+A^2-4).  Scale U=X/t^2, V=Y/t^3.
X, Y = sp.symbols("X Y")
scaled_rhs = sp.expand(X*(X**2 - 2*H*X + (t**2-1)**2*q))
assert scaled_rhs.subs(X, 0) == 0

cert = json.loads(CERT.read_text(encoding="utf-8"))
sha = cert.pop("canonical_sha256")
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
assert hashlib.sha256(canonical).hexdigest() == sha
assert sha == "9e3520da8c6945a4e90f3e6e87711100df666c58a50caf2787a268e0ca9d0bde"
assert cert["jacobian_section_materialized"] is True
assert cert["named_j2_order"] == 2
assert cert["torsor_kernel_reduction"]["candidate_count_before"] == 3
assert cert["torsor_kernel_reduction"]["candidate_count_after"] == 3
assert cert["torsor_kernel_reduction"]["torsor_equation_materialized"] is False
assert cert["torsor_kernel_reduction"]["torsor_picard_lattice_materialized"] is False
assert cert["stage33_12_closed_exact"] is False
assert cert["stage33_13_released"] is False
print("PASS j2 elliptic torsor kernel reduction")
