#!/usr/bin/env python3
"""Build the bounded m=1 Route-F jet experiment over F_97.

This script builds a finite matrix only. Characteristic-zero conclusions
require the rank upper bound and the unit-minor lifting argument in the note.
"""
import json
from pathlib import Path
from array import array

ROOT = Path(__file__).resolve().parent
P, SQRT2, II = 97, 14, 22
N, ORDER = 14, 16


def binomial(a, k):
    value = 1
    for j in range(k):
        value = value*(a-j)*pow(j+1, -1, P) % P
    return value


def series(j, a, b, kind, r0, other0):
    # The local parameter is v in kind v, and u in kind u.
    parity, half_power = (b, a) if kind == 'v' else (a, b)
    sign = 1 if kind == 'v' else -1
    alpha, beta = j*pow(4, -1, P) % P, half_power*pow(2, -1, P) % P
    out = [0]*(ORDER+1)
    constant = pow(r0, j, P)*pow(other0, half_power, P) % P
    for h in range((ORDER-parity)//2+1):
        coeff = sum(binomial(alpha, k)*binomial(beta, h-k)*pow(2, -(h-k), P)
                    for k in range(h+1)) % P
        out[parity+2*h] = constant*coeff*pow(sign, h, P) % P
    return out


def main():
    assert SQRT2*SQRT2 % P == 2 and II*II % P == P-1
    b, e, c = SQRT2, II*SQRT2 % P, (1+II) % P
    legs = [(j, a, bb) for a in (0, 1) for bb in (0, 1)
            for j in range(2*N-2*a-2*bb+1)]
    columns = [(z, w) for z in legs for w in legs
               if z[1:] == w[1:] and (z[0]-w[0]) % 2 == 0]
    assert len(columns) == 1464
    # z=(r,u,v), w=(r,u,v). Missing points are P27 and P35.
    v_nodes = [('v', rz, uz, b, b)
               for rz in (b, -b % P, e, -e % P) for uz in (b, -b % P)
               if (rz, uz) != (e, b)]
    u_nodes = [('u', c, e, rw, vw)
               for rw in (c, -c % P, II*c % P, -II*c % P)
               for vw in (e, -e % P) if (rw, vw) != (c, -e % P)]
    nodes = v_nodes+u_nodes
    assert len(nodes) == 14
    jet_rows = [(i, j) for i in range(ORDER) for j in range(ORDER-i) if (i+j) % 2 == 0]
    assert len(jet_rows) == 64
    def pack(values):
        return bytes(values) if P < 256 else array('H', values).tobytes()
    matrix, leading = [], []
    for kind, rz, oz, rw, ow in nodes:
        zs = {leg: series(*leg, kind, rz, oz) for leg in legs}
        ws = {leg: series(*leg, kind, rw, ow) for leg in legs}
        for i, j in jet_rows:
            matrix.append(pack(zs[z][i]*ws[w][j] % P for z, w in columns))
        for i in range(ORDER+1):
            leading.append(pack(zs[z][i]*ws[w][ORDER-i] % P for z, w in columns))
    # Evaluation at the two omitted nodes. Both functionals use omega^14 frames.
    def evaluation(zpoint, wpoint):
        def mon(leg, point):
            j, a, bb = leg
            r, u, v = point
            return pow(r, j, P)*pow(u, a, P)*pow(v, bb, P) % P
        return pack(mon(z, zpoint)*mon(w, wpoint) % P for z, w in columns)
    ev27 = evaluation((e, b, 0), (b, b, 0))
    ev35 = evaluation((c, 0, e), (c, 0, -e % P))
    (ROOT/'A97.bin').write_bytes(b''.join(matrix))
    (ROOT/'leading97.bin').write_bytes(b''.join(leading))
    (ROOT/'evaluations97.bin').write_bytes(ev27+ev35)
    data = {'field': P, 'sqrt2': SQRT2, 'i': II, 'm': 1, 'n': N,
            'cover_order': ORDER, 'rows': len(matrix), 'cols': len(columns),
            'columns': columns, 'nodes': nodes, 'jet_rows_per_node': jet_rows,
            'row_order': 'node, then (a-exponent,b-exponent)',
            'leading_order': 'node, then a-exponent 0..16'}
    (ROOT/'matrix97.json').write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({k: data[k] for k in ('field','rows','cols','cover_order')}))


if __name__ == '__main__':
    main()
