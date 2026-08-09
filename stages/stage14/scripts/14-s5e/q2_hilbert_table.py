#!/usr/bin/env python3
from itertools import product

UNITS = (1, 3, 5, 7)
CLASSES = tuple((a, u) for a in (0, 1) for u in UNITS)


def eps(u: int) -> int:
    return ((u - 1) // 2) & 1


def omega(u: int) -> int:
    return ((u * u - 1) // 8) & 1


def mul_class(x, y):
    a, u = x
    b, v = y
    return ((a + b) & 1, (u * v) % 8)


def hilbert_bit(x, y):
    a, u = x
    b, v = y
    return (eps(u) * eps(v) + a * omega(v) + b * omega(u)) & 1


def hilbert_symbol(x, y):
    return -1 if hilbert_bit(x, y) else 1


def inv_class(x):
    # Every element of Q2*/Q2*^2 has order two.
    return x


def main():
    assert len(CLASSES) == 8
    one = (0, 1)

    # Symmetric bilinear pairing checks.
    for x, y, z in product(CLASSES, repeat=3):
        assert hilbert_bit(x, y) == hilbert_bit(y, x)
        assert hilbert_bit(mul_class(x, y), z) == (hilbert_bit(x, z) ^ hilbert_bit(y, z))
        assert hilbert_bit(x, mul_class(y, z)) == (hilbert_bit(x, y) ^ hilbert_bit(x, z))

    # Product-square triples: d3 is forced by d1,d2.
    states = []
    for d1, d2 in product(CLASSES, repeat=2):
        d3 = mul_class(d1, d2)
        assert mul_class(mul_class(d1, d2), d3) == one
        states.append((d1, d2, d3))
    assert len(states) == 64
    assert len(set(states)) == 64

    minus_one = (0, 7)
    two = (1, 1)
    rows = []
    for idx, (d1, d2, d3) in enumerate(states):
        rows.append({
            "id": idx,
            "d1": d1,
            "d2": d2,
            "d3": d3,
            "h12": hilbert_symbol(d1, d2),
            "h13": hilbert_symbol(d1, d3),
            "h23": hilbert_symbol(d2, d3),
            "hm1_1": hilbert_symbol(minus_one, d1),
            "hm1_2": hilbert_symbol(minus_one, d2),
            "hm1_3": hilbert_symbol(minus_one, d3),
            "h2_1": hilbert_symbol(two, d1),
            "h2_2": hilbert_symbol(two, d2),
            "h2_3": hilbert_symbol(two, d3),
        })

    # Exact state/table invariants used by CI.
    assert len(rows) == 64
    print("STAGE14_S5E=COMPLETE_Q2_HILBERT_PAIRING_AND_64_STATE_ENCODING")
    print("Q2_SQUARECLASS_GROUP_SIZE=8")
    print("Q2_PRODUCT_SQUARE_DESCENT_STATE_COUNT=64")
    print("Q2_HILBERT_SYMBOL_FORMULA_LOCKED=true")
    print("Q2_PAIRING_TABLE_EXACT=true")
    print("P2_COVERING_SPECIFIC_64_STATE_SOLUBILITY_CLASSIFIED=false")
    print("NEXT=Stage14-s5f")


if __name__ == "__main__":
    main()
