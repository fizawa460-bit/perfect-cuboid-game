#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

RANK = 63
BASE_CONSTRAINTS = 140
DEGREE = 16


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_base(path: pathlib.Path):
    lines = path.read_text().splitlines()
    assert lines[0] == "S32_D16_CONSTRAINED_HPERP_V1"
    header = lines[:4]
    n, m = map(int, lines[4].split())
    assert (n, m) == (RANK, BASE_CONSTRAINTS)
    at = 5
    q = [list(map(int, lines[at+i].split())) for i in range(RANK)]
    at += RANK
    p0, caps, lin = [], [], []
    for _ in range(BASE_CONSTRAINTS):
        row = list(map(int, lines[at].split())); at += 1
        assert len(row) == 2 + RANK
        p0.append(row[0]); caps.append(row[1]); lin.append(row[2:])
    assert at == len(lines)
    return header, q, p0, caps, lin


def exact_parent_inventory() -> set[tuple[int,int]]:
    # Generic bounded-multiplicity Stage32 aggregate equations at d=16.
    # A-type: 32 exceptional coordinates, B/C: 8 each, each cap 4.
    # q-head: 4 normal coordinates, each cap 8.
    parents: set[tuple[int,int]] = set()
    for x in range(32*4 + 1):
        for y in range(8*4 + 1):
            for z in range(8*4 + 1):
                e = x+y+z
                if 19*DEGREE - 5*e < 0:
                    continue
                for t in range(4*8 + 1):
                    if 8*y + 16*z + 16*t != 8*DEGREE:
                        continue
                    anum = -24*x + 32*y + 96*z + 120*t
                    if anum % 8:
                        continue
                    a = anum//8
                    if a < 0:
                        continue
                    if -40*x + 112*y + 264*z + 304*t != 8*(19*DEGREE - 5*e):
                        continue
                    parents.add((e,a))
    assert len(parents) == 282
    return parents


def cut_accepts(e: int, a: int) -> bool:
    c1 = a + 3*e - 7*DEGREE
    c2 = 2*a + 7*e - 15*DEGREE
    return 0 <= c1 <= DEGREE//2 and 0 <= c2 <= 40


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', type=pathlib.Path, required=True)
    ap.add_argument('--output', type=pathlib.Path, required=True)
    args=ap.parse_args()
    header,q,p0,caps,lin=load_base(args.input)

    parents=exact_parent_inventory()
    formal={(e,a) for e in range(19*DEGREE//5 + 1) for a in range(19*DEGREE + 1)}
    cutset={pair for pair in formal if cut_accepts(*pair)}
    # Two aggregate inequalities are exactly the 282-parent projection.
    assert cutset == parents

    A0=sum(p0[:46]); E0=sum(p0[92:140])
    Alin=[sum(lin[r][j] for r in range(46)) for j in range(RANK)]
    Elin=[sum(lin[r][j] for r in range(92,140)) for j in range(RANK)]

    # cut1 = A + 3E - 7d = z+t, hence 0..d/2.
    cut1_p0=A0+3*E0-7*DEGREE
    cut1_lin=[Alin[j]+3*Elin[j] for j in range(RANK)]
    # cut2 = 2A + 7E - 15d; exact d16 parent projection gives 0..40.
    cut2_p0=2*A0+7*E0-15*DEGREE
    cut2_lin=[2*Alin[j]+7*Elin[j] for j in range(RANK)]
    assert 0 <= cut1_p0 <= DEGREE//2
    assert 0 <= cut2_p0 <= 40
    assert any(cut1_lin) or any(cut2_lin)

    p0v=p0+[cut1_p0,cut2_p0]
    capv=caps+[DEGREE//2,40]
    linv=lin+[cut1_lin,cut2_lin]
    payload={
        'base_core_sha':header[1], 'base_source_blob':header[2], 'base_prepared_sha':header[3],
        'q':q, 'p0':p0v, 'caps':capv, 'lin':linv,
        'parent_count':len(parents),
        'cuts':['0<=A+3E-7d<=d/2','0<=2A+7E-15d<=40'],
    }
    sha=csha(payload)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('w') as f:
        f.write('S32_D16_CONSTRAINED_HPERP_PARENT_CUTS_V1\n')
        f.write(header[1]+'\n'); f.write(header[2]+'\n'); f.write(sha+'\n')
        f.write(f'{RANK} {BASE_CONSTRAINTS+2}\n')
        for row in q: f.write(' '.join(map(str,row))+'\n')
        for r in range(BASE_CONSTRAINTS+2):
            f.write(f'{p0v[r]} {capv[r]} '+' '.join(map(str,linv[r]))+'\n')
    print(json.dumps({
        'schema':'STAGE32_SCOUT_D16_PARENT_POLYTOPE_PREP_V1',
        'parent_count':len(parents),
        'formal_parent_count':len(formal),
        'cut1_at_H':cut1_p0,'cut2_at_H':cut2_p0,
        'cut1_lin_nonzero':sum(v!=0 for v in cut1_lin),
        'cut2_lin_nonzero':sum(v!=0 for v in cut2_lin),
        'prepared_input_sha256':sha,
    },sort_keys=True))

if __name__=='__main__':
    main()
