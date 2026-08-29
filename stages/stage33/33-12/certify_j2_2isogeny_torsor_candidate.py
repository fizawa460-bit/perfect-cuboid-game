#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
p = ROOT / 'j2-2isogeny-torsor-candidate.json'
cert = json.loads(p.read_text(encoding='utf-8'))


def add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
        if out[e] == 0:
            del out[e]
    return out


def neg(a):
    return {e: -c for e, c in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = ea + eb
            out[e] = out.get(e, 0) + ca * cb
            if out[e] == 0:
                del out[e]
    return out


def scale(a, n):
    return {e: n * c for e, c in a.items() if n * c}


def power(a, n):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, a)
    return out


one = {0: 1}
t = {1: 1}
t2 = power(t, 2)
H = add(add(power(t, 4), scale(t2, -4)), one)
q = add(add(power(t, 4), scale(t2, -6)), one)
Dp = add(add(t2, scale(t, -2)), {0: -1})
Dm = add(add(t2, scale(t, 2)), {0: -1})
D = mul(power(sub(t2, one), 2), q)

assert sub(q, mul(Dp, Dm)) == {}
assert sub(sub(power(H, 2), D), scale(power(t, 4), 4)) == {}

# E:y^2=x(x^2+a*x+b), with a=-2H,b=D.  Its quotient by (0,0) is
# Ehat:y^2=x(x^2-2a*x+(a^2-4b)).
a = scale(H, -2)
b = D
assert sub(scale(a, -2), scale(H, 4)) == {}
assert sub(sub(power(a, 2), scale(b, 4)), scale(power(t, 4), 16)) == {}

# D/Dplus=(t^2-1)^2*Dminus, checked without division.
assert sub(D, mul(Dp, mul(power(sub(t2, one), 2), Dm))) == {}
assert cert['candidate_torsor_equation'] == "N^2=Dplus*U^4-2*H*U^2*V^2+(t^2-1)^2*Dminus*V^4"
assert cert['named_j2_identification_certified'] is False
assert cert['candidate_count_after'] == 3
assert cert['route_status'] == 'BLOCKED_NEW_PATTERN_ISOLATED'
claimed = cert.pop('canonical_sha256')
canonical = json.dumps(cert, sort_keys=True, separators=(',', ':')).encode()
actual = hashlib.sha256(canonical).hexdigest()
assert actual == claimed, (actual, claimed)
print('PASS', claimed)
