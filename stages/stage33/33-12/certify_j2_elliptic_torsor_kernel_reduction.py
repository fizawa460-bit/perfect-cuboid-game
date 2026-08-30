#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-elliptic-torsor-kernel-reduction.json"


def add(a, b):
    out = dict(a)
    for mon, coeff in b.items():
        out[mon] = out.get(mon, 0) + coeff
        if out[mon] == 0:
            del out[mon]
    return out


def neg(a):
    return {mon: -coeff for mon, coeff in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = {}
    for (ta, sa), ca in a.items():
        for (tb, sb), cb in b.items():
            mon = (ta + tb, sa + sb)
            out[mon] = out.get(mon, 0) + ca * cb
            if out[mon] == 0:
                del out[mon]
    return out


def scale(a, n):
    return {mon: n * coeff for mon, coeff in a.items() if n * coeff}


def power(a, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = mul(out, a)
    return out


one = {(0, 0): 1}
t = {(1, 0): 1}
s = {(0, 1): 1}
t2 = power(t, 2)
s2 = power(s, 2)
H = add(add(power(t, 4), scale(t2, -4)), one)
q = add(add(power(t, 4), scale(t2, -6)), one)

# Exact polynomial verification of
# t^2(1-s^2)^2+s^2(1-t^2)^2=t^2*s^4+H*s^2+t^2.
F = add(mul(t2, power(sub(one, s2), 2)), mul(s2, power(sub(one, t2), 2)))
scaled_quartic = add(add(mul(t2, power(s, 4)), mul(H, s2)), t2)
assert sub(F, scaled_quartic) == {}

# Clear denominators in A=H/t^2 and verify
# A^2-4=((t^2-1)^2*q)/t^4 exactly.
assert sub(sub(power(H, 2), scale(power(t, 4), 4)), mul(power(sub(t2, one), 2), q)) == {}

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
