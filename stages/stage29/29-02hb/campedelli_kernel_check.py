#!/usr/bin/env python3
"""Exact F2 enumeration for Stage29-02hb.

No external dependencies. Enumerates Campedelli labelings of the audited
seven-line arrangement, quotients by GL(3,F2), and computes the action of the
arrangement incidence automorphism group on quotient kernels.
"""

from itertools import permutations, combinations

NAMES = ["A1", "A2", "A3", "B3", "B2", "B1", "C"]
IDX = {n: i for i, n in enumerate(NAMES)}
TRIPLES = [
    ("A1", "A2", "B3"),
    ("A1", "A3", "B2"),
    ("A1", "B1", "C"),
    ("A2", "A3", "B1"),
    ("A2", "B2", "C"),
    ("A3", "B3", "C"),
]
TRIPLE_SETS = {frozenset(IDX[n] for n in t) for t in TRIPLES}
VECTORS = [
    (a, b, c)
    for a in (0, 1)
    for b in (0, 1)
    for c in (0, 1)
    if (a, b, c) != (0, 0, 0)
]


def vxor(*vs):
    return tuple(sum(x) & 1 for x in zip(*vs))


def rref(rows, ncols):
    rows = [list(r) for r in rows if any(r)]
    rr = 0
    pivots = []
    for col in range(ncols):
        pivot = next((i for i in range(rr, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rr], rows[pivot] = rows[pivot], rows[rr]
        for i in range(len(rows)):
            if i != rr and rows[i][col]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[rr])]
        pivots.append(col)
        rr += 1
        if rr == len(rows):
            break
    return tuple(tuple(r) for r in rows), tuple(pivots)


def nullspace(mat, ncols):
    rr, pivots = rref(mat, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        x = [0] * ncols
        x[f] = 1
        for row, p in reversed(list(enumerate(pivots))):
            s = 0
            for c in free:
                s ^= rr[row][c] & x[c]
            x[p] = s
        basis.append(tuple(x))
    return rref(basis, ncols)[0]


def admissible_labelings():
    out = []
    for perm in permutations(VECTORS):
        lab = dict(zip(NAMES, perm))
        if all(vxor(lab[a], lab[b], lab[c]) != (0, 0, 0)
               for a, b, c in TRIPLES):
            out.append(lab)
    return out


def kernel_of_labeling(lab):
    matrix = [[lab[n][r] for n in NAMES] for r in range(3)]
    return nullspace(matrix, 7)


def arrangement_automorphisms():
    autos = []
    for p in permutations(range(7)):
        mapped = {frozenset(p[i] for i in t) for t in TRIPLE_SETS}
        if mapped == TRIPLE_SETS:
            autos.append(p)
    return autos


def permute_kernel(kernel, perm):
    rows = []
    for row in kernel:
        y = [0] * 7
        for i, value in enumerate(row):
            y[perm[i]] = value
        rows.append(tuple(y))
    return rref(rows, 7)[0]


def main():
    labs = admissible_labelings()
    assert len(labs) == 1680

    kernels = {}
    for lab in labs:
        kernels.setdefault(kernel_of_labeling(lab), lab)
    assert len(kernels) == 10

    autos = arrangement_automorphisms()
    assert len(autos) == 24

    keys = list(kernels)
    index = {k: i for i, k in enumerate(keys)}
    seen = set()
    orbits = []
    for i, k in enumerate(keys):
        if i in seen:
            continue
        orbit = {index[permute_kernel(k, p)] for p in autos}
        seen |= orbit
        orbits.append(sorted(orbit))

    orbit_sizes = sorted(len(o) for o in orbits)
    assert orbit_sizes == [2, 8]

    print("raw_admissible_labelings=1680")
    print("GL3_F2_order=168")
    print("distinct_rank3_kernels=10")
    print("arrangement_aut_order=24")
    print("kernel_orbit_sizes=8,2")

    for j, orbit in enumerate(orbits, 1):
        k = keys[orbit[0]]
        lab = kernels[k]
        print(f"orbit_{j}_size={len(orbit)}")
        print(" representative_labels=" + ",".join(
            f"{n}:{''.join(map(str, lab[n]))}" for n in NAMES))
        print(" representative_kernel_upstairs_basis=")
        for row in k:
            print("  " + "".join(map(str, row)))


if __name__ == "__main__":
    main()
