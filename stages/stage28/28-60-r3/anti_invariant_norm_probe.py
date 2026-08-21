#!/usr/bin/env python3
"""Stage28-60-r3 exact anti-invariant lattice probe.

Reuses the audited Stage14-4ak Shimada identification to reconstruct the
physical deck anti-invariant lattice.  The load-bearing output is a congruence:
every integral anti-invariant norm is divisible by four.  Combined with the
geometric identity -x^2 = 2*(M.C) (mod 4) for a split curve, this excludes
all odd physical M-degrees without any smoothness assumption.

The script also records the M-degree histogram of Shimada's distinguished 40
(-2)-curves.  That histogram is diagnostic only; L40 is not the complete root
spectrum.
"""
from __future__ import annotations

import argparse
import ast
import json
import shutil
import subprocess
from collections import Counter
from pathlib import Path

N = 20
ALLOWED = (
    ast.Expression,
    ast.List,
    ast.Tuple,
    ast.Constant,
    ast.UnaryOp,
    ast.USub,
    ast.UAdd,
    ast.Load,
)


def parse_list(path: Path, name: str):
    text = path.read_text()
    k = text.find(name + ':=')
    if k < 0:
        raise KeyError(name)
    i = text.find('[', k)
    depth = 0
    quote = None
    esc = False
    for j in range(i, len(text)):
        c = text[j]
        if quote:
            if esc:
                esc = False
            elif c == '\\':
                esc = True
            elif c == quote:
                quote = None
            continue
        if c in "'\"":
            quote = c
        elif c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                tree = ast.parse(text[i : j + 1], mode='eval')
                if any(not isinstance(x, ALLOWED) for x in ast.walk(tree)):
                    raise ValueError(name)
                return ast.literal_eval(tree)
    raise ValueError(f'unterminated {name}')


def mm(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)]
        for i in range(N)
    ]


def dot(v, w, G):
    return sum(v[i] * G[i][j] * w[j] for i in range(N) for j in range(N))


def gps(M):
    return '[' + ';'.join(','.join(str(x) for x in row) for row in M) + ']'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('root', type=Path)
    ap.add_argument('refine', type=Path)
    ap.add_argument('equiv', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()

    if not shutil.which('gp'):
        raise RuntimeError('PARI/GP gp not found')

    s0 = next(args.root.rglob('S0S3.txt'))
    bor = next(args.root.rglob('Borcherds.txt'))
    G = parse_list(s0, 'GramS0')
    L40 = parse_list(s0, 'L40vs')
    Ts = parse_list(bor, 'Tsigma')
    inv = parse_list(bor, 'iotasigmaz')

    refine = json.loads(args.refine.read_text())
    equiv = json.loads(args.equiv.read_text())
    assert equiv['equivalent'] is True
    passed = [x for x in refine['candidates'] if x['pass']]
    if len(passed) != 2:
        raise RuntimeError(f'expected two equivalent physical labelings, got {len(passed)}')

    # Stage14-4ak proves the two survivors are AutX0f-equivalent.  Verify that
    # the distinguished-root M-degree multiset agrees before choosing one.
    l40_degree_lists = []
    for pp in passed:
        degs = [dot(pp['M'], c, G) for c in L40]
        assert min(degs) >= 0
        l40_degree_lists.append(degs)
    assert sorted(l40_degree_lists[0]) == sorted(l40_degree_lists[1])

    p = passed[0]
    M = p['M']
    deck_index = p['deck_candidates'][0]['index']
    deck = mm(inv, Ts[deck_index])

    # Saturated anti-invariant lattice ker(delta+1) in the full NS lattice.
    A = [row[:] for row in deck]
    for i in range(N):
        A[i][i] += 1

    gp = f'''A={gps(A)}; G={gps(G)}; K=matkerint(A~); Q=-K~*G*K;\nprint("RANK=",matsize(K)[2]);\nprint("DETQ=",matdet(Q));\nfor(i=1,matsize(Q)[1],print("QROW=",Vec(Q[i,])));\n'''
    lines = subprocess.run(
        ['gp', '-fq'], input=gp, text=True, capture_output=True, check=True
    ).stdout.splitlines()

    rank = int(next(x.split('=', 1)[1] for x in lines if x.startswith('RANK=')))
    detq = int(next(x.split('=', 1)[1] for x in lines if x.startswith('DETQ=')))
    qrows = [ast.literal_eval(x.split('=', 1)[1]) for x in lines if x.startswith('QROW=')]

    assert rank == 6
    assert len(qrows) == rank and all(len(r) == rank for r in qrows)
    assert detq == 256

    diagonal_divisible_by_4 = all(qrows[i][i] % 4 == 0 for i in range(rank))
    off_diagonal_even = all(
        qrows[i][j] % 2 == 0 for i in range(rank) for j in range(rank) if i != j
    )
    every_norm_divisible_by_4 = diagonal_divisible_by_4 and off_diagonal_even
    assert every_norm_divisible_by_4

    # For a split curve x=C-delta(C):
    #   x^2 = 4 C^2 - 2 D^2,
    # K3 evenness kills the first term mod 4, while base adjunction gives
    # D^2 == L.D == M.C (mod 2).  Hence -x^2 == 2(M.C) (mod 4).
    # Therefore every odd M-degree is incompatible with the lattice norm law.
    odd_degree_obstruction_mod4 = {
        str(m): (2 * m) % 4 for m in (1, 3, 5, 7, 9)
    }
    assert all(v == 2 for v in odd_degree_obstruction_mod4.values())

    l40_degs = l40_degree_lists[0]
    histogram = {str(k): v for k, v in sorted(Counter(l40_degs).items())}
    l40_degree6_indices = [i + 1 for i, d in enumerate(l40_degs) if d == 6]

    out = {
        'status': 'PASS',
        'physical_labelings_before_equivalence': len(passed),
        'physical_labelings_equivalent_under_AutX0f': True,
        'anti_invariant_rank': rank,
        'anti_invariant_positive_form_determinant': detq,
        'positive_gram_matrix': qrows,
        'diagonal_divisible_by_4': diagonal_divisible_by_4,
        'off_diagonal_even': off_diagonal_even,
        'every_anti_invariant_norm_divisible_by_4': every_norm_divisible_by_4,
        'split_curve_congruence': '-x^2 congruent 2*(M.C) mod 4',
        'odd_degree_required_residue_mod4': 2,
        'all_odd_physical_M_degrees_excluded_subject_to_branch_firewall': True,
        'M_degree_5_excluded_subject_to_branch_firewall': True,
        'M_degree_6_excluded_by_mod4': False,
        'distinguished_L40_diagnostic': {
            'complete_root_spectrum': False,
            'M_degree_histogram': histogram,
            'M_degree_6_indices_1based': l40_degree6_indices,
            'M_degree_6_count': len(l40_degree6_indices),
        },
        'M6_requires_complete_gluing_effectivity_descent_analysis': True,
    }
    args.out.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
