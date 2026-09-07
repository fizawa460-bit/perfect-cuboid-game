#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648d-deraux-affine-sixpoint-orbit-absolute-line-obstruction.json"
EXPECTED_CERT = "598f3557d84423702be97a6fc942cf3254e68c57b3ccb1950f4d29c3fb3a69f0"


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


def from_rows(rows):
    return tuple(sum((int(x) & 1) << j for j, x in enumerate(row)) for row in rows)


def rows_list(A):
    return [[(A[i] >> j) & 1 for j in range(4)] for i in range(4)]


ID_AFF = (I4, 0)


def aff_apply(a, x: int) -> int:
    M, t = a
    return mat_vec(M, x) ^ t


def aff_mul(a, b):
    M, t = a
    N, u = b
    return (mat_mul(M, N), mat_vec(M, u) ^ t)


def aff_inv(a):
    M, t = a
    Mi = mat_inv(M)
    assert Mi is not None
    return (Mi, mat_vec(Mi, t))


def close_affine_group(gens):
    group = {ID_AFF}
    stack = [ID_AFF]
    while stack:
        a = stack.pop()
        for g in gens:
            b = aff_mul(g, a)
            if b not in group:
                group.add(b)
                stack.append(b)
    return group


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
post1648c = locked(locks["post1648c_full_j2_obstruction"])
rosati = locked(locks["principal_rosati"])

assert post1648b["curve_pair_action"]["phi2_x_map"] == "-(x+i)/(1+i*x)"
assert post1648b["curve_pair_action"]["phi6_x_map"] == "i*(x-1)/(x+1)"
assert post1648c["source_J2_model"]["coordinate_basis_pair_subsets"] == [
    ["+1", "-1"], ["+1", "+i"], ["+1", "-i"], ["+1", "0"]
]

branch_order = ["+1", "-1", "+i", "-i", "0", "infinity"]
idx = {name: i for i, name in enumerate(branch_order)}
points_complex = {
    "+1": ga(1), "-1": ga(-1), "+i": ga(0, 1), "-i": ga(0, -1),
    "0": ga(0), "infinity": INF,
}
reverse = {v: k for k, v in points_complex.items()}
phi2_coeff = (ga(-1), ga(0, -1), ga(0, 1), ga(1))
phi6_coeff = (ga(0, 1), ga(0, -1), ga(1), ga(1))
phi2_point = {name: reverse[mobius(x, *phi2_coeff)] for name, x in points_complex.items()}
phi6_point = {name: reverse[mobius(x, *phi6_coeff)] for name, x in points_complex.items()}

ALL = (1 << 6) - 1


def canon(mask: int) -> int:
    assert mask.bit_count() % 2 == 0
    return min(mask, mask ^ ALL)


basis_classes = [
    (1 << idx["+1"]) | (1 << idx["-1"]),
    (1 << idx["+1"]) | (1 << idx["+i"]),
    (1 << idx["+1"]) | (1 << idx["-i"]),
    (1 << idx["+1"]) | (1 << idx["0"]),
]
coord_to_class = {}
for v in range(16):
    m = 0
    for i, b in enumerate(basis_classes):
        if (v >> i) & 1:
            m ^= b
    coord_to_class[v] = canon(m)
class_to_coord = {c: v for v, c in coord_to_class.items()}
assert len(class_to_coord) == 16


def pair_coord(a: str, b: str) -> int:
    return class_to_coord[canon((1 << idx[a]) | (1 << idx[b]))]


source_points = {"infinity": 0}
for name in branch_order[:-1]:
    source_points[name] = pair_coord(name, "infinity")

expected_source_points = {
    name: sum((bit & 1) << i for i, bit in enumerate(bits))
    for name, bits in cert["source_affine_J2_model"]["weierstrass_point_coordinates_f2"].items()
}
assert source_points == expected_source_points


def perm_indices(action):
    return [idx[action[name]] for name in branch_order]


def permute_mask(mask: int, p) -> int:
    out = 0
    for i in range(6):
        if (mask >> i) & 1:
            out |= 1 << p[i]
    return out


def source_linear_matrix(action):
    p = perm_indices(action)
    cols = [class_to_coord[canon(permute_mask(b, p))] for b in basis_classes]
    return tuple(sum(((cols[j] >> i) & 1) << j for j in range(4)) for i in range(4))


S2 = source_linear_matrix(phi2_point)
S6 = source_linear_matrix(phi6_point)
t2 = source_points[phi2_point["infinity"]]
t6 = source_points[phi6_point["infinity"]]
source_gens = [(S2, t2), (S6, t6)]
for action, aff in ((phi2_point, source_gens[0]), (phi6_point, source_gens[1])):
    for name, x in source_points.items():
        assert aff_apply(aff, x) == source_points[action[name]]

src_model = cert["source_affine_J2_model"]
assert rows_list(S2) == src_model["phi2_affine"]["linear"]
assert [(t2 >> i) & 1 for i in range(4)] == src_model["phi2_affine"]["translation"]
assert rows_list(S6) == src_model["phi6_affine"]["linear"]
assert [(t6 >> i) & 1 for i in range(4)] == src_model["phi6_affine"]["translation"]
source_group = close_affine_group(source_gens)
assert len(source_group) == 24 == src_model["generated_affine_group_order_mod2"]

E_source = tuple(
    sum((((basis_classes[i] & basis_classes[j]).bit_count() & 1) << j) for j in range(4))
    for i in range(4)
)
assert rows_list(E_source) == src_model["weil_form_matrix_f2"]
assert rows_list(E_source) == post1648c["source_J2_model"]["weil_form_matrix_f2"]

z1 = pair_coord("+1", "-1")
z2 = pair_coord("+i", "-i")
z3 = pair_coord("0", "infinity")
assert [[(z >> i) & 1 for i in range(4)] for z in (z1, z2, z3)] == [
    src_model["W_nonzero_coordinates_f2"]["Z1_delta_pm1"],
    src_model["W_nonzero_coordinates_f2"]["Z2_delta_pmi"],
    src_model["W_nonzero_coordinates_f2"]["Z3_delta_0inf"],
]

deraux_linear = {
    "R1": [["1", "0"], ["1-r", "-1"]],
    "R2": [["-1+r", "2"], ["1+r", "1-r"]],
    "R3": [["1", "-1-r"], ["0", "-1"]],
}
deraux_translation_bits = {"R1": 0, "R2": 0, "R3": 1 | 4}

parse = {
    "0": (0, 0), "1": (1, 0), "-1": (-1, 0), "2": (2, 0), "-2": (-2, 0),
    "r": (0, 1), "-r": (0, -1), "1+r": (1, 1), "1-r": (1, -1),
    "-1+r": (-1, 1), "-1-r": (-1, -1),
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


target_gens = [(O_to_f2(deraux_linear[name]), deraux_translation_bits[name]) for name in ("R1", "R2", "R3")]
target_model = cert["target_deraux_affine_J2_model"]
for name, (M, t) in zip(("R1", "R2", "R3"), target_gens):
    assert rows_list(M) == target_model["deraux_generators_mod2"][name]["linear"]
    assert [(t >> i) & 1 for i in range(4)] == target_model["deraux_generators_mod2"][name]["translation"]

E_target = from_rows([[x & 1 for x in row] for row in rosati["principal_polarization"]["riemann_form_matrix"]])
assert rows_list(E_target) == target_model["riemann_form_matrix_f2"]
for M, _ in target_gens:
    assert mat_mul(mat_mul(mat_transpose(M), E_target), M) == E_target

target_group = close_affine_group(target_gens)
assert len(target_group) == 24 == target_model["generated_affine_group_order_mod2"]

p0 = 1 | 2 | 8
assert [(p0 >> i) & 1 for i in range(4)] == target_model["isotropy8_representative_numerator_f2"]
target_six = {aff_apply(g, p0) for g in target_group}
assert len(target_six) == 6
assert sorted([[(v >> i) & 1 for i in range(4)] for v in target_six]) == target_model["sixpoint_orbit_f2"]

source_six = set(source_points.values())
assert len(source_six) == 6

symplectic_linear = []
sixpoint_affine = []
full_conjugacies = []
target_group_set = set(target_group)

for rows in itertools.product(range(16), repeat=4):
    P = tuple(rows)
    Pinv = mat_inv(P)
    if Pinv is None:
        continue
    if mat_mul(mat_mul(mat_transpose(P), E_target), P) != E_source:
        continue
    symplectic_linear.append(P)
    good_translations = []
    for t in range(16):
        image_set = {mat_vec(P, x) ^ t for x in source_six}
        if image_set == target_six:
            good_translations.append(t)
            sixpoint_affine.append((P, t))
    for t in good_translations:
        h = (P, t)
        hi = aff_inv(h)
        if all(aff_mul(aff_mul(h, sgen), hi) in target_group_set for sgen in source_gens):
            full_conjugacies.append(h)

audit = cert["finite_affine_conjugacy_audit"]
assert len(symplectic_linear) == 720 == audit["symplectic_linear_map_count_between_locked_weil_forms"]
assert len(sixpoint_affine) == 720 == audit["symplectic_affine_maps_sending_source_sixpoint_set_to_deraux_sixpoint_orbit"]
assert len(full_conjugacies) == 48 == audit["full_affine_group_conjugacy_count"]

line_vector_to_name = {4: "L1", 8: "L2", 12: "L3"}
line_bijections = []
plane_images = set()
for P, _ in full_conjugacies:
    image = frozenset(mat_vec(P, z) for z in (z1, z2, z3))
    plane_images.add(image)
    line_bijections.append(tuple(line_vector_to_name[mat_vec(P, z)] for z in (z1, z2, z3)))

assert plane_images == {frozenset({4, 8, 12})}
counts = {}
for m in line_bijections:
    counts[m] = counts.get(m, 0) + 1
assert len(counts) == 6
assert set(counts.values()) == {8}
expected_maps = {
    (x["Z1"], x["Z2"], x["Z3"])
    for x in audit["induced_W_line_bijections"]
}
assert set(counts) == expected_maps
assert audit["each_W_line_bijection_multiplicity"] == 8
assert audit["delta_0inf_possible_lines"] == ["L1", "L2", "L3"]
assert audit["delta_0inf_possible_residues_decimal"] == [73, 97, 235]
assert audit["deraux_sixpoint_orbit_plus_full_affine_action_determines_absolute_line"] is False

assert cert["decision"]["survivors_current_credit"] == [73, 97, 235]
assert cert["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert cert["decision"]["Q602_excluded"] is False
assert cert["decision"]["O210_excluded"] is False
assert cert["firewalls"]["one_of_48_affine_conjugacies_selected_without_source"] is False
assert cert["firewalls"]["deraux_order8_orbit_promoted_to_marked_weierstrass_labelling"] is False

print("POST1648D_DERAUX_AFFINE_SIXPOINT_ORBIT_ABSOLUTE_LINE_OBSTRUCTION_COMPLETE")
print(f"certificate_canonical={EXPECTED_CERT}")
print("source_affine_group_order=24 target_affine_group_order=24 target_sixpoint_orbit=6")
print("symplectic_linear=720 sixpoint_affine=720 full_affine_conjugacies=48")
print("W_line_bijections=6 each_multiplicity=8 delta_0inf_possible=L1,L2,L3")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
