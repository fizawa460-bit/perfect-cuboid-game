#!/usr/bin/env python3
"""Exact F2 enumeration for Stage29-02hb.

No external dependencies. Enumerates Campedelli labelings of the audited
seven-line arrangement, quotients by GL(3,F2), and computes both:
  * geometric/Q(i)-visible S4 orbits of quotient kernels;
  * the certified Q-defined S3 coordinate-permutation orbits inherited from
    the audited full sign cover.

The latter is deliberately kept separate: the S4 orbit count must not be used
as a Q-arithmetic orbit count.
"""

from itertools import permutations

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
ONES = (1, 1, 1, 1, 1, 1, 1)


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


def in_span(v, basis):
    return len(rref(basis, len(v))[1]) == len(rref(tuple(basis) + (v,), len(v))[1])


def rank_vectors(vs):
    return len(rref(vs, len(vs[0]))[1])


def admissible_labelings():
    out = []
    for perm in permutations(VECTORS):
        lab = dict(zip(NAMES, perm))
        if all(vxor(lab[a], lab[b], lab[c]) != (0, 0, 0)
               for a, b, c in TRIPLES):
            # For three distinct nonzero F2^3 vectors, nonzero total sum is
            # equivalent to linear independence. Keep that load-bearing local
            # freeness condition explicit.
            assert all(rank_vectors((lab[a], lab[b], lab[c])) == 3
                       for a, b, c in TRIPLES)
            out.append(lab)
    return out


def kernel_of_labeling(lab):
    matrix = [[lab[n][r] for n in NAMES] for r in range(3)]
    kernel_upstairs = nullspace(matrix, 7)
    # Upstairs the kernel has rank four and contains the all-ones projective
    # sign; modulo it the actual subgroup H <= Gamma has rank three.
    assert len(kernel_upstairs) == 4
    assert in_span(ONES, kernel_upstairs)
    return kernel_upstairs


def arrangement_automorphisms():
    autos = []
    for p in permutations(range(7)):
        mapped = {frozenset(p[i] for i in t) for t in TRIPLE_SETS}
        if mapped == TRIPLE_SETS:
            autos.append(p)
    return autos


def q_liftable_coordinate_permutations():
    """The audited Q-liftable base subgroup from 29-02ha: S3 on indices."""
    out = []
    for target in permutations((1, 2, 3)):
        m = {1: target[0], 2: target[1], 3: target[2]}
        image = {}
        for i in (1, 2, 3):
            image[f"A{i}"] = f"A{m[i]}"
            image[f"B{i}"] = f"B{m[i]}"
        image["C"] = "C"
        out.append(tuple(IDX[image[n]] for n in NAMES))
    assert len(set(out)) == 6
    return out


def permute_kernel(kernel, perm):
    rows = []
    for row in kernel:
        y = [0] * 7
        for i, value in enumerate(row):
            y[perm[i]] = value
        rows.append(tuple(y))
    return rref(rows, 7)[0]


def kernel_orbits(keys, group):
    index = {k: i for i, k in enumerate(keys)}
    seen = set()
    orbits = []
    for i, k in enumerate(keys):
        if i in seen:
            continue
        orbit = {index[permute_kernel(k, p)] for p in group}
        seen |= orbit
        orbits.append(sorted(orbit))
    return orbits


def main():
    labs = admissible_labelings()
    assert len(labs) == 1680

    kernels = {}
    for lab in labs:
        kernels.setdefault(kernel_of_labeling(lab), lab)
    assert len(kernels) == 10

    geometric_group = arrangement_automorphisms()
    assert len(geometric_group) == 24
    q_group = q_liftable_coordinate_permutations()

    keys = list(kernels)
    geometric_orbits = kernel_orbits(keys, geometric_group)
    q_orbits = kernel_orbits(keys, q_group)

    geometric_sizes = sorted(len(o) for o in geometric_orbits)
    q_sizes = sorted(len(o) for o in q_orbits)
    assert geometric_sizes == [2, 8]
    assert q_sizes == [2, 2, 6]

    # The geometric size-8 orbit splits over the certified Q symmetry into
    # one size-6 and one size-2 orbit; the geometric size-2 orbit remains size 2.
    g8 = next(set(o) for o in geometric_orbits if len(o) == 8)
    g2 = next(set(o) for o in geometric_orbits if len(o) == 2)
    assert sorted(len(o) for o in q_orbits if set(o) <= g8) == [2, 6]
    assert sorted(len(o) for o in q_orbits if set(o) <= g2) == [2]

    print("raw_admissible_labelings=1680")
    print("GL3_F2_order=168")
    print("distinct_rank3_kernels=10")
    print("geometric_arrangement_aut_order=24")
    print("geometric_Qi_kernel_orbit_sizes=8,2")
    print("certified_Q_liftable_base_aut_order=6")
    print("certified_Q_kernel_orbit_sizes=6,2,2")
    print("exact_Q_isomorphism_class_count_not_claimed=true")

    for j, orbit in enumerate(geometric_orbits, 1):
        k = keys[orbit[0]]
        lab = kernels[k]
        print(f"geometric_orbit_{j}_size={len(orbit)}")
        print(" representative_labels=" + ",".join(
            f"{n}:{''.join(map(str, lab[n]))}" for n in NAMES))
        print(" representative_kernel_upstairs_basis=")
        for row in k:
            print("  " + "".join(map(str, row)))


if __name__ == "__main__":
    main()
