#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648c-full-j2-group-conjugacy-absolute-line-obstruction.json"
EXPECTED_CERT = "3bfabbc8cacaa0f189a0e0fa65924220dbe4d070d243e188051d2195f8077dcb"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def csha_without(obj: dict, field: str) -> str:
    body = dict(obj)
    body.pop(field, None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def locked(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), lock["path"]
    assert git_blob_sha(path) == lock["blob_sha1"], lock["path"]
    obj = json.loads(path.read_text(encoding="utf-8"))
    expected = lock["canonical_sha256"]
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in obj else "canonical_sha256"
    assert obj[field] == expected
    assert csha_without(obj, field) == expected
    return obj


# 4x4 F2 matrices are tuples of four 4-bit row masks.
I4 = (1, 2, 4, 8)


def mat_vec(A, v: int) -> int:
    out = 0
    for i, row in enumerate(A):
        if (row & v).bit_count() & 1:
            out |= 1 << i
    return out


def mat_mul(A, B):
    rows = []
    for i in range(4):
        row = 0
        for j in range(4):
            bit = 0
            for k in range(4):
                bit ^= ((A[i] >> k) & 1) & ((B[k] >> j) & 1)
            row |= bit << j
        rows.append(row)
    return tuple(rows)


def mat_transpose(A):
    return tuple(sum(((A[j] >> i) & 1) << j for j in range(4)) for i in range(4))


def mat_inv(A):
    rows = [A[i] | ((1 << i) << 4) for i in range(4)]
    for col in range(4):
        pivot = next((i for i in range(col, 4) if (rows[i] >> col) & 1), None)
        if pivot is None:
            return None
        rows[col], rows[pivot] = rows[pivot], rows[col]
        for i in range(4):
            if i != col and ((rows[i] >> col) & 1):
                rows[i] ^= rows[col]
    return tuple((rows[i] >> 4) & 15 for i in range(4))


def close_group(gens):
    group = {I4}
    stack = [I4]
    while stack:
        a = stack.pop()
        for g in gens:
            b = mat_mul(a, g)
            if b not in group:
                group.add(b)
                stack.append(b)
    return group


def from_rows(rows):
    return tuple(sum((int(x) & 1) << j for j, x in enumerate(row)) for row in rows)


def rows_list(A):
    return [[(A[i] >> j) & 1 for j in range(4)] for i in range(4)]


# Exact Gaussian-rational Möbius action for the source branch points.
G = tuple[Fraction, Fraction]
INF = None


def ga(a=0, b=0):
    return (Fraction(a), Fraction(b))


def gadd(x: G, y: G) -> G:
    return (x[0] + y[0], x[1] + y[1])


def gmul(x: G, y: G) -> G:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def ginv(x: G) -> G:
    n = x[0] * x[0] + x[1] * x[1]
    assert n != 0
    return (x[0] / n, -x[1] / n)


def gdiv(x: G, y: G) -> G:
    return gmul(x, ginv(y))


def mobius(x, a: G, b: G, c: G, d: G):
    if x is INF:
        return INF if c == ga(0) else gdiv(a, c)
    num = gadd(gmul(a, x), b)
    den = gadd(gmul(c, x), d)
    return INF if den == ga(0) else gdiv(num, den)


cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT
assert csha_without(cert, "canonical_sha256_without_this_field") == EXPECTED_CERT
locks = cert["source_locks"]
post1648b = locked(locks["post1648b_generator_pair_preflight"])
abstract_w = locked(locks["abstract_w_weierstrass"])
gauge = locked(locks["marked_w_gauge_orbit"])
rosati = locked(locks["principal_rosati"])

assert post1648b["curve_pair_action"]["phi2_x_map"] == "-(x+i)/(1+i*x)"
assert post1648b["curve_pair_action"]["phi6_x_map"] == "i*(x-1)/(x+1)"
assert abstract_w["weierstrass_model"]["id_to_x"] == {
    "1": "+1", "6": "-1", "3": "+i", "5": "-i", "2": "0", "4": "infinity"
}

branch_order = ["+1", "-1", "+i", "-i", "0", "infinity"]
points = {
    "+1": ga(1), "-1": ga(-1), "+i": ga(0, 1), "-i": ga(0, -1),
    "0": ga(0), "infinity": INF,
}
reverse = {v: k for k, v in points.items()}
phi2_coeff = (ga(-1), ga(0, -1), ga(0, 1), ga(1))
phi6_coeff = (ga(0, 1), ga(0, -1), ga(1), ga(1))
phi2 = {name: reverse[mobius(x, *phi2_coeff)] for name, x in points.items()}
phi6 = {name: reverse[mobius(x, *phi6_coeff)] for name, x in points.items()}

# Even subsets modulo complements.
ALL = (1 << 6) - 1


def canon(mask: int) -> int:
    assert mask.bit_count() % 2 == 0
    return min(mask, mask ^ ALL)


def perm_indices(action):
    idx = {name: i for i, name in enumerate(branch_order)}
    return [idx[action[name]] for name in branch_order]


def permute_mask(mask: int, p) -> int:
    out = 0
    for i in range(6):
        if (mask >> i) & 1:
            out |= 1 << p[i]
    return out

basis_classes = [3, 5, 9, 17]
coord_to_class = {}
for v in range(16):
    m = 0
    for i, b in enumerate(basis_classes):
        if (v >> i) & 1:
            m ^= b
    coord_to_class[v] = canon(m)
class_to_coord = {c: v for v, c in coord_to_class.items()}
assert len(class_to_coord) == 16


def source_matrix(action):
    p = perm_indices(action)
    cols = [class_to_coord[canon(permute_mask(b, p))] for b in basis_classes]
    return tuple(sum(((cols[j] >> i) & 1) << j for j in range(4)) for i in range(4))

S2 = source_matrix(phi2)
S6 = source_matrix(phi6)
source_group = close_group([S2, S6])
assert len(source_group) == 24

# Weil pairing = parity of intersection in the even-subset model.
E_source = tuple(
    sum((((basis_classes[i] & basis_classes[j]).bit_count() & 1) << j) for j in range(4))
    for i in range(4)
)

z1 = class_to_coord[canon((1 << 0) | (1 << 1))]
z2 = class_to_coord[canon((1 << 2) | (1 << 3))]
z3 = class_to_coord[canon((1 << 4) | (1 << 5))]
assert [z1, z2, z3] == [1, 6, 7]

# Reconstruct target G12 mod 2 from the locked Z[r] matrices.
parse = {
    "0": (0, 0), "1": (1, 0), "-1": (-1, 0), "2": (2, 0), "-2": (-2, 0),
    "r": (0, 1), "-r": (0, -1), "1+r": (1, 1), "1-r": (1, -1), "-1+r": (-1, 1),
}


def O_to_f2(A):
    cols = []
    for j in range(4):
        const = [0, 0]
        rad = [0, 0]
        if j < 2:
            const[j] = 1
        else:
            rad[j - 2] = 1
        yc = [0, 0]
        yr = [0, 0]
        for i in range(2):
            for k in range(2):
                a, b = parse[A[i][k]]
                a &= 1
                b &= 1
                yc[i] ^= a * const[k]
                yr[i] ^= b * const[k] ^ a * rad[k]
        cols.append(yc[0] | (yc[1] << 1) | (yr[0] << 2) | (yr[1] << 3))
    return tuple(sum(((cols[j] >> i) & 1) << j for j in range(4)) for i in range(4))

b1 = O_to_f2(rosati["g12_invariance_replay"]["b1"])
b2 = O_to_f2(rosati["g12_invariance_replay"]["b2"])
b3 = O_to_f2(gauge["principal_automorphisms"]["b3"])
b4 = O_to_f2(gauge["principal_automorphisms"]["b4"])
target_group = close_group([b1, b2, b3, b4])
assert len(target_group) == 24

E_target = from_rows([[x & 1 for x in row] for row in rosati["principal_polarization"]["riemann_form_matrix"]])
assert rows_list(E_source) == cert["source_J2_model"]["weil_form_matrix_f2"]
assert rows_list(E_target) == cert["target_J2_model"]["riemann_form_matrix_f2"]
assert rows_list(S2) == cert["source_J2_model"]["phi2_matrix_f2"]
assert rows_list(S6) == cert["source_J2_model"]["phi6_matrix_f2"]
for name, m in {"b1": b1, "b2": b2, "b3": b3, "b4": b4}.items():
    assert rows_list(m) == cert["target_J2_model"]["principal_generators_mod2"][name]

# Exhaust all GL4(F2) and retain full-group conjugacies.
group_conjugacies = []
symplectic_conjugacies = []
for rows in itertools.product(range(16), repeat=4):
    P = tuple(rows)
    Pinv = mat_inv(P)
    if Pinv is None:
        continue
    c2 = mat_mul(mat_mul(P, S2), Pinv)
    c6 = mat_mul(mat_mul(P, S6), Pinv)
    if c2 not in target_group or c6 not in target_group:
        continue
    group_conjugacies.append(P)
    if mat_mul(mat_mul(mat_transpose(P), E_target), P) == E_source:
        symplectic_conjugacies.append(P)

assert len(group_conjugacies) == 48
assert len(symplectic_conjugacies) == 48

line_vector_to_name = {4: "L1", 8: "L2", 12: "L3"}
plane_images = set()
line_bijections = set()
z3_images = set()
for P in symplectic_conjugacies:
    image = frozenset(mat_vec(P, z) for z in (z1, z2, z3))
    plane_images.add(image)
    mapped = tuple(line_vector_to_name[mat_vec(P, z)] for z in (z1, z2, z3))
    line_bijections.add(mapped)
    z3_images.add(line_vector_to_name[mat_vec(P, z3)])

assert plane_images == {frozenset({4, 8, 12})}
assert len(line_bijections) == 6
assert z3_images == {"L1", "L2", "L3"}
expected_bijections = {
    (x["Z1"], x["Z2"], x["Z3"])
    for x in cert["finite_conjugacy_audit"]["induced_W_line_bijections"]
}
assert line_bijections == expected_bijections

audit = cert["finite_conjugacy_audit"]
assert audit["ambient_GL4_F2_order"] == 20160
assert audit["symplectic_group_conjugacy_count"] == 48
assert audit["source_W_image_plane_count"] == 1
assert audit["induced_W_line_bijection_count"] == 6
assert audit["delta_0inf_possible_lines"] == ["L1", "L2", "L3"]
assert audit["delta_0inf_possible_residues_decimal"] == [73, 97, 235]
assert audit["full_group_action_alone_determines_absolute_line"] is False

assert cert["decision"]["survivors_current_credit"] == [73, 97, 235]
assert cert["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert cert["decision"]["Q602_excluded"] is False
assert cert["decision"]["O210_excluded"] is False
assert cert["firewalls"]["one_of_48_conjugacies_selected_without_source"] is False
assert cert["firewalls"]["conditional_residue235_from_post1648b_promoted"] is False

print("POST1648C_FULL_J2_GROUP_CONJUGACY_ABSOLUTE_LINE_OBSTRUCTION_COMPLETE")
print(f"certificate_canonical={EXPECTED_CERT}")
print("source_group_order=24 target_group_order=24 GL4_order=20160")
print("symplectic_group_conjugacies=48 unique_W_image_plane=span(r*e1,r*e2)")
print("W_line_bijections=6 delta_0inf_possible=L1,L2,L3")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
