#!/usr/bin/env python3
from fractions import Fraction

FIBERS = [
    ("20/21", 1, [("-45/49", "10/343")]),
    ("80/39", 1, [("-160/39", "1760/1521")]),
    ("24/7", 1, [("-75/7", "510/49")]),
    ("84/13", 1, [("17787/169", "216678/169")]),
    ("48/55", 1, [("-24/25", "24/275")]),
    ("20/99", 1, [("-20/27", "980/2673")]),
    ("60/11", 2, [("-180/11", "7020/121"), ("-300/11", "5100/121")]),
]


def q(s: str) -> Fraction:
    return Fraction(s)


def on_curve(qq: Fraction, x: Fraction, y: Fraction) -> bool:
    return y * y == x * (x + 1) * (x + qq * qq)


seen = set()
for label, expected_rank, pts in FIBERS:
    assert label not in seen
    seen.add(label)
    qq = q(label)
    assert qq not in (0, 1, -1)
    assert expected_rank == len(pts)
    for xs, ys in pts:
        x, y = q(xs), q(ys)
        assert on_curve(qq, x, y), (label, xs, ys)

assert len(FIBERS) == 7
assert sum(rank for _, rank, _ in FIBERS) == 8
print("STAGE34_01_MW_INPUT_VERIFIER_PASS")
print("fibers=7 source_free_points=8")
