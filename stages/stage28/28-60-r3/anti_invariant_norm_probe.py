#!/usr/bin/env python3
"""Stage28-60-r3 exact anti-invariant lattice probe.

Reuses the audited Stage14-4ak Shimada identification to reconstruct the
physical deck anti-invariant lattice K and verifies the quadratic-form
congruence needed for the low-degree rational-curve spectrum.

This script does not execute arbitrary Maple code: it parses only literal list
assignments from Shimada's S0S3.txt / Borcherds.txt, exactly as the audited
Stage14 scripts do.
"""
from __future__ import annotations

import argparse
import ast
import json
import shutil
import subprocess
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


def gps(M):
    return '[' + ';'.join(','.join(str(x) for x in row) for row in M) + ']'


def split_image_d2_values(m: int) -> list[int]:
    """Possible D^2 for a split rational curve of M-degree m.

    On Y, L=-K_Y has L^2=4. For a rational normalization of D,
        D^2 = m + 2 p_a(D) - 2,
    and Hodge gives 4 D^2 <= m^2.
    """
    vals = []
    p = 0
    while True:
        d2 = m + 2 * p - 2
        if 4 * d2 > m * m:
            break
        vals.append(d2)
        p += 1
    return vals


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
    Ts = parse_list(bor, 'Tsigma')
    inv = parse_list(bor, 'iotasigmaz')

    refine = json.loads(args.refine.read_text())
    equiv = json.loads(args.equiv.read_text())
    assert equiv['equivalent'] is True
    passed = [x for x in refine['candidates'] if x['pass']]
    if len(passed) != 2:
        raise RuntimeError(f'expected two equivalent physical labelings, got {len(passed)}')
    # Stage14-4ak proves the two survivors are AutX0f-equivalent.  One
    # representative therefore gives the intrinsic anti-invariant lattice.
    p = passed[0]
    deck_index = p['deck_candidates'][0]['index']
    deck = mm(inv, Ts[deck_index])

    A = [row[:] for row in deck]
    for i in range(N):
        A[i][i] += 1

    gp = f'''A={gps(A)}; G={gps(G)}; K=matkerint(A~); Q=-K~*G*K;\nprint("RANK=",matsize(K)[2]);\nprint("DETQ=",matdet(Q));\nfor(i=1,matsize(Q)[1],print("QROW=",Vec(Q[i,])));\nR=qfminim(Q,24); V=R[3];\nfor(n=4,24,4, c=0; for(j=1,matsize(V)[2],if(qfeval(Q,V[,j])==n,c++)); print("THETA=",n,",",2*c));\n'''
    lines = subprocess.run(
        ['gp', '-fq'], input=gp, text=True, capture_output=True, check=True
    ).stdout.splitlines()

    rank = int(next(x.split('=', 1)[1] for x in lines if x.startswith('RANK=')))
    detq = int(next(x.split('=', 1)[1] for x in lines if x.startswith('DETQ=')))
    qrows = [ast.literal_eval(x.split('=', 1)[1]) for x in lines if x.startswith('QROW=')]
    theta = {}
    for x in lines:
        if x.startswith('THETA='):
            n, c = x.split('=', 1)[1].split(',')
            theta[int(n)] = int(c)

    assert rank == 6
    assert len(qrows) == rank and all(len(r) == rank for r in qrows)
    assert detq == 256

    diagonal_divisible_by_4 = all(qrows[i][i] % 4 == 0 for i in range(rank))
    off_diagonal_even = all(
        qrows[i][j] % 2 == 0 for i in range(rank) for j in range(rank) if i != j
    )
    every_norm_divisible_by_4 = diagonal_divisible_by_4 and off_diagonal_even
    assert every_norm_divisible_by_4

    degree_cases = {}
    for m in (5, 6):
        d2s = split_image_d2_values(m)
        anti_norms = [2 * d2 + 8 for d2 in d2s]
        degree_cases[str(m)] = {
            'possible_split_image_D2': d2s,
            'required_anti_invariant_positive_norms': anti_norms,
            'all_required_norms_divisible_by_4': all(n % 4 == 0 for n in anti_norms),
            'excluded_by_norm_mod_4': all(n % 4 != 0 for n in anti_norms),
        }

    # Degree five is odd, so away from the branch it cannot be a connected
    # two-to-one pullback.  The physical branch has no positive-real locus by
    # the audited Stage28-50-r2 firewall, hence the split cases are exhaustive.
    assert degree_cases['5']['excluded_by_norm_mod_4']
    assert degree_cases['6']['all_required_norms_divisible_by_4']

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
        'theta_vector_counts_through_24': theta,
        'degree_cases': degree_cases,
        'm5_split_norm_obstruction': 'PASS',
        'm5_physical_rational_curve_excluded_subject_to_stage28_branch_firewall': True,
        'm6_requires_finer_coset_effectivity_descent_analysis': True,
    }
    args.out.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
