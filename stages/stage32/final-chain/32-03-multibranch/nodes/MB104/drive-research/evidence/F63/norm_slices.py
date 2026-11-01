#!/usr/bin/env python3
# Explicit checks remain active under python -O.
"""Bounded norm-slice certificates for the two F63 half-degree modular sections."""
from pathlib import Path
import argparse, json
P = 97
ROOT = Path(__file__).resolve().parent

def trim(a):
    while a and (not a[-1]):
        a.pop()
    return a

def add(*ps):
    n = max(map(len, ps), default=0)
    r = [0] * n
    for p in ps:
        for j, x in enumerate(p):
            r[j] = (r[j] + x) % P
    return trim(r)

def scale(a, c):
    return trim([x * c % P for x in a])

def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % P
    return trim(r)

def rem(a, b):
    a = trim(a[:])
    b = trim(b[:])
    while a and len(a) >= len(b):
        q = a[-1] * pow(b[-1], -1, P) % P
        k = len(a) - len(b)
        for j, x in enumerate(b):
            a[k + j] = (a[k + j] - q * x) % P
        trim(a)
    return a

def gcd(a, b):
    while b:
        a, b = (b, rem(a, b))
    return scale(a, pow(a[-1], -1, P)) if a else []

def divmod_poly(a, b):
    a = trim(a[:])
    q = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        factor = a[-1] * pow(b[-1], -1, P) % P
        k = len(a) - len(b)
        q[k] = factor
        for j, x in enumerate(b):
            a[k + j] = (a[k + j] - factor * x) % P
        trim(a)
    return (trim(q), a)

def bezout(a, b):
    r0, r1 = (a, b)
    s0, s1 = ([1], [])
    t0, t1 = ([], [1])
    while r1:
        q, r = divmod_poly(r0, r1)
        r0, r1 = (r1, r)
        s0, s1 = (s1, add(s0, scale(mul(q, s1), -1)))
        t0, t1 = (t1, add(t0, scale(mul(q, t1), -1)))
    factor = pow(r0[-1], -1, P)
    return (scale(r0, factor), scale(s0, factor), scale(t0, factor))

def inputs():
    data = json.loads((ROOT / 'F63-witnesses97.json').read_text())
    return (data['columns'], data['witnesses'])

def section_slice(columns, vector, fixed_leg, t):
    out = [[0] * 15 for _ in range(4)]
    for (z, w), coefficient in zip(columns, vector):
        j, a, b = z
        k = w[0]
        degree, other = (k, j) if fixed_leg == 'z' else (j, k)
        group = a + 2 * b
        out[group][degree] = (out[group][degree] + coefficient * pow(t, other, P)) % P
    return [trim(p) for p in out]

def norm(parts, t):
    A, B, C, D = parts
    q = pow(t, 4, P)
    iv = pow(16, -1, P)
    U2 = [4 * (q + 4) * iv % P, 0, 0, 0, (q + 4) * iv % P]
    V2 = [-4 * (q - 4) * iv % P, 0, 0, 0, (q - 4) * iv % P]
    alpha = add(mul(A, A), mul(U2, mul(B, B)), scale(mul(V2, add(mul(C, C), mul(U2, mul(D, D)))), -1))
    beta = scale(add(mul(A, B), scale(mul(V2, mul(C, D)), -1)), 2)
    return add(mul(alpha, alpha), scale(mul(U2, mul(beta, beta)), -1))

def calculate():
    columns, vectors = inputs()
    results = []
    for fixed_leg in ['z', 'w']:
        for t in range(8):
            ns = [norm(section_slice(columns, x, fixed_leg, t), t) for x in vectors]
            if all((len(p) == 57 for p in ns)) and len(gcd(*ns)) == 1:
                h, s, tb = bezout(*ns)
                if not (h == [1] and add(mul(s, ns[0]), mul(tb, ns[1])) == [1]):
                    raise ValueError('verification condition failed')
                results.append({'fixed_leg': fixed_leg, 'value': t, 'degree': [len(p) - 1 for p in ns], 'leading_coefficients': [p[-1] for p in ns], 'gcd': [1], 'norms': ns, 'bezout': [s, tb]})
                break
        else:
            raise SystemExit('No full-degree coprime slice in bounded range')
    return {'prime': P, 'model': 'U2=(r4+4)(R4+4)/16; V2=(r4-4)(R4-4)/16', 'slices': results}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write-certificate', action='store_true')
    p.add_argument('--certificate', type=Path, default=ROOT / 'F63-norm-slices97.json')
    a = p.parse_args()
    result = calculate()
    if a.write_certificate:
        a.certificate.write_text(json.dumps(result, indent=2) + '\n')
    elif not json.loads(a.certificate.read_text()) == result:
        raise ValueError('norm certificate mismatch')
    print(json.dumps({'status': 'PASS', 'norm_slices': [{k: v for k, v in row.items() if k not in ['norms', 'bezout']} for row in result['slices']]}))
if __name__ == '__main__':
    main()
