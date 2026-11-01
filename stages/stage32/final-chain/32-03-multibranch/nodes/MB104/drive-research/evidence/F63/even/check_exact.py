#!/usr/bin/env python3
# Explicit checks remain active under python -O.
"""Check the discovered rank upper bound over Q(i), without CRT.

CRT output is accepted only after all 4*344 Gaussian-rational identities
are checked exactly. A second formula checks all finite-field entries.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import json
import argparse
ROOT = Path(__file__).resolve().parent
SCALE = 2 ** 32

def binom(a, k):
    out = Q(1)
    for j in range(k):
        out = out * (a - j) / (j + 1)
    return out

def one_leg(leg, kind, k):
    j, a, b = leg
    parity, half = (b, a) if kind == 'v' else (a, b)
    if k < parity or (k - parity) % 2:
        return Q(0)
    h = (k - parity) // 2
    value = sum((binom(Q(j, 4), s) * binom(Q(half, 2), h - s) / 2 ** (h - s) for s in range(h + 1)), Q(0))
    return value if kind == 'v' else value * (-1) ** h

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--from-discovery', action='store_true', help='Explicitly build the relation certificate from CRT candidates.')
    parser.add_argument('--relations', type=Path, default=ROOT / 'F63-EVEN-exact-relations.json')
    args = parser.parse_args()
    data = json.loads((ROOT / 'matrix97.json').read_text())
    cols = data['columns']
    labels = data['jet_rows_per_node']
    nodes = data['nodes']
    raw = (ROOT / 'A97.bin').read_bytes()
    if args.from_discovery:
        candidates = list(ROOT.glob('relations_candidate_*.json'))
        source = max(candidates, key=lambda p: int(p.stem.rsplit('_', 1)[-1]))
        reconstructed = json.loads(source.read_text())
        rr = [Q(x) for x in reconstructed['coefficients']]
        pivots = reconstructed['pivots']
        relations = []
        for row in range(4):
            coefficients = [(rr[(row * 224 + j) * 2], rr[(row * 224 + j) * 2 + 1]) for j in range(224)]
            denominator = lcm(*(x.denominator for pair in coefficients for x in pair))
            relations.append([(int(a * denominator), int(b * denominator)) for a, b in coefficients])
        observed = None
    else:
        observed = json.loads(args.relations.read_text())
        pivots = observed['pivots']
        relations = []
        if not (len(observed['relations']) == 4 and len(set(pivots)) == 4):
            raise ValueError('verification condition failed')
        for sparse in observed['relations']:
            row = [(0, 0)] * 224
            seen = set()
            for j, re, im in sparse:
                if not (isinstance(j, int) and 0 <= j < 224 and (j not in seen)):
                    raise ValueError('verification condition failed')
                seen.add(j)
                row[j] = (int(re), int(im))
            relations.append(row)
    for row, integers in enumerate(relations):
        denominator = integers[pivots[row]][0]
        if not (denominator and integers[pivots[row]][1] == 0):
            raise ValueError('verification condition failed')
        for k, pivot in enumerate(pivots):
            if not integers[pivot] == ((denominator, 0) if k == row else (0, 0)):
                raise ValueError('verification condition failed')
    legs = {tuple(z) for z, w in cols} | {tuple(w) for z, w in cols}
    cache = {(leg, kind, k): one_leg(leg, kind, k) for leg in legs for kind in ('u', 'v') for k in range(8)}
    P, b, ii = (97, 14, 22)
    e = ii * b % P
    c = (1 + ii) % P
    accum = [[[0, 0] for _ in cols] for _ in range(4)]
    count = 0
    for column, (z, w) in enumerate(cols):
        z, w = (tuple(z), tuple(w))
        jz, a, bb = z
        jw = w[0]
        power = (jz + jw) // 2
        for node_index, (kind, rz, oz, rw, ow) in enumerate(nodes):
            if kind == 'v':
                phase = {b: 0, -b % P: 2, e: 1, -e % P: 3}[rz] * jz
                constant = 2 ** (power + a) * (1 if oz == b else (-1) ** a)
            else:
                phase = power + {c: 0, -c % P: 2, ii * c % P: 1, -ii * c % P: 3}[rw] * jw
                constant = 2 ** (power + bb) * (-1) ** bb * (1 if ow == e else (-1) ** bb)
            phase %= 4
            for local, (x, y) in enumerate(labels):
                value = cache[z, kind, x] * cache[w, kind, y] * constant * SCALE
                if not value.denominator == 1:
                    raise ValueError('verification condition failed')
                value = int(value)
                row = node_index * 16 + local
                if not value % P * pow(SCALE, -1, P) * pow(ii, phase, P) % P == raw[row * 344 + column]:
                    raise ValueError('verification condition failed')
                count += 1
                if not value:
                    continue
                for q, relation in enumerate(relations):
                    re, im = relation[row]
                    if not (re or im):
                        continue
                    re, im = ((re, im), (-im, re), (-re, -im), (im, -re))[phase]
                    accum[q][column][0] += re * value
                    accum[q][column][1] += im * value
    if not all((pair == [0, 0] for row in accum for pair in row)):
        raise ValueError('verification condition failed')
    out = {'schema': 'F63-EVEN-EXACT-LEFT-RELATIONS-v1', 'field': 'Q(i)', 'matrix_shape': [224, 344], 'independent_relations': 4, 'pivots': pivots, 'coefficient_basis': ['1', 'i'], 'relations': [[[j, str(a), str(b)] for j, (a, b) in enumerate(row) if a or b] for row in relations], 'checked_gaussian_identities': 4 * 344, 'checked_reduction_entries': count, 'exact_identity_result': 'PASS', 'rank_upper_bound': 220}
    if args.from_discovery:
        args.relations.write_text(json.dumps(out, indent=2) + '\n')
    elif not observed == out:
        raise ValueError('relation certificate metadata/content mismatch')
    print(json.dumps({k: out[k] for k in ('field', 'independent_relations', 'checked_gaussian_identities', 'checked_reduction_entries', 'exact_identity_result', 'rank_upper_bound')}))
if __name__ == '__main__':
    main()
