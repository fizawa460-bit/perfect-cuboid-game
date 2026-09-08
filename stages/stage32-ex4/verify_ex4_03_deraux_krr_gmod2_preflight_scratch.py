#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "ex4-03-deraux-krr-gmod2-preflight-scratch.json"
EXPECTED = "97e73b2c9a1ea30569ab82916b99a88b0924ada4acd8b9205df2b590914e36b1"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def load_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    assert canonical(doc) == lock["canonical_sha256"], path
    return doc


def vxor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def matvec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(4)) & 1 for i in range(4))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) & 1 for j in range(4)) for i in range(4))


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(4)) for i in range(4))


I4 = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
Z4 = (0, 0, 0, 0)


def inv4(A):
    rows = [list(A[i]) + list(I4[i]) for i in range(4)]
    for c in range(4):
        pivot = next((r for r in range(c, 4) if rows[r][c]), None)
        if pivot is None:
            return None
        if pivot != c:
            rows[c], rows[pivot] = rows[pivot], rows[c]
        for r in range(4):
            if r != c and rows[r][c]:
                rows[r] = [x ^ y for x, y in zip(rows[r], rows[c])]
    return tuple(tuple(row[4:]) for row in rows)


def aff_comp(g, h):
    A, a = g
    B, b = h
    return matmul(A, B), vxor(matvec(A, b), a)


def aff_inv(g):
    A, a = g
    Ai = inv4(A)
    assert Ai is not None
    return Ai, matvec(Ai, a)


def aff_key(g):
    A, a = g
    return tuple(x for row in A for x in row) + a


def aff_act(g, v):
    A, a = g
    return vxor(matvec(A, v), a)


def generate_group(gens):
    ident = (I4, Z4)
    out = {aff_key(ident): ident}
    stack = [ident]
    while stack:
        g = stack.pop()
        for h in gens:
            x = aff_comp(g, h)
            k = aff_key(x)
            if k not in out:
                out[k] = x
                stack.append(x)
    return out


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

ex4_02 = load_lock(cert["repo_source_locks"]["ex4_02_inventory"])
rosati = load_lock(cert["repo_source_locks"]["principal_rosati"])
cecotti = load_lock(cert["repo_source_locks"]["cecotti_generator_pair_preflight"])

assert ex4_02["decision"]["result"] == "EX4_02_CURRENT_FROZEN_SOURCE_INVENTORY_DOES_NOT_YET_SUPPLY_EXACT_PRODUCT_BINDING"
assert rosati["quadratic_order"]["relation"] == "r^2=-2"
assert rosati["principal_polarization"]["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]
assert cecotti["curve_pair_action"]["phi2_x_map"] == "-(x+i)/(1+i*x)"
assert cecotti["curve_pair_action"]["phi6_x_map"] == "i*(x-1)/(x+1)"
assert cecotti["actual_obstruction"]["absolute_delta0inf_retained_W_line_identified"] is False

src = cert["source_weierstrass_A2_model"]
labels = ["infinity", "0", "1", "-1", "i", "-i"]
points = {k: tuple(v) for k, v in src["point_vectors"].items()}
assert list(src["branch_labels"]) == labels
assert points["infinity"] == Z4
assert points["-i"] == (1, 1, 1, 1)

phi2 = src["phi2_branch_permutation"]
phi6 = src["phi6_branch_permutation"]


def affine_from_label_perm(perm):
    t = points[perm["infinity"]]
    basis_labels = ["0", "1", "-1", "i"]
    cols = [vxor(points[perm[x]], t) for x in basis_labels]
    A = tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
    assert inv4(A) is not None
    for lab in labels:
        assert aff_act((A, t), points[lab]) == points[perm[lab]]
    return A, t


P2 = affine_from_label_perm(phi2)
P6 = affine_from_label_perm(phi6)
H = generate_group([P2, P6])
assert len(H) == 24
assert src["affine_group_image_order_on_A2"] == 24

tgt = cert["deraux_A2_model"]
DG = tgt["mod2_affine_generators_in_literal_coordinate_order"]


def unpack(name):
    return tuple(tuple(row) for row in DG[name]["M"]), tuple(DG[name]["t"])


R1, R2, R3 = unpack("R1"), unpack("R2"), unpack("R3")
G = generate_group([R1, R2, R3])
assert len(G) == 24
assert tgt["affine_group_image_order_on_A2"] == 24

rep = tuple(tgt["table2_order8_representative_A2_vector"])
orbit = sorted({aff_act(g, rep) for g in G.values()})
assert orbit == [tuple(x) for x in tgt["six_point_orbit"]]
assert len(orbit) == 6

source_order = [points[x] for x in labels]


def affine_from_six_images(images):
    t = images[0]
    cols = [vxor(images[j], t) for j in range(1, 5)]
    A = tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
    if inv4(A) is None:
        return None
    if aff_act((A, t), source_order[5]) != images[5]:
        return None
    return A, t


Hvals = list(H.values())
Gkeys = set(G)
conjugators = []
affine_extensions = 0
for images in itertools.permutations(orbit):
    a = affine_from_six_images(images)
    if a is None:
        continue
    affine_extensions += 1
    ai = aff_inv(a)
    image_keys = {aff_key(aff_comp(aff_comp(a, h), ai)) for h in Hvals}
    if image_keys == Gkeys:
        conjugators.append(a)

enum = cert["finite_conjugator_enumeration"]
assert enum["six_point_bijections_tested"] == 720
assert affine_extensions == enum["bijections_extending_to_affine_F2_4_maps"] == 720
assert len(conjugators) == enum["affine_maps_conjugating_source_order24_group_to_deraux_order24_group"] == 48

Es = tuple(tuple(row) for row in src["weil_pairing_matrix_in_source_basis"])
Et = tuple(tuple(row) for row in tgt["weil_pairing_matrix_from_principal_rosati_mod2"])
symplectic = sum(matmul(matmul(transpose(A), Et), A) == Es for A, _ in conjugators)
assert symplectic == enum["conjugators_also_matching_source_and_target_weil_pairings"] == 48

conj_by_key = {aff_key(a): a for a in conjugators}
unseen = set(conj_by_key)
inner_orbits = []
while unseen:
    k0 = next(iter(unseen))
    a0 = conj_by_key[k0]
    orb = {aff_key(aff_comp(g, a0)) for g in G.values()} & set(conj_by_key)
    inner_orbits.append(orb)
    unseen -= orb
assert sorted(len(x) for x in inner_orbits) == [24, 24]
assert sorted(enum["target_inner_gauge_orbits"]) == [24, 24]

delta = points["0"]
W = {name: tuple(v) for name, v in tgt["retained_W_under_literal_coordinate_preflight"]["lines"].items()}
Wrev = {v: k for k, v in W.items()}
counts = Counter()
for A, _ in conjugators:
    image = matvec(A, delta)
    assert image in Wrev
    counts[Wrev[image]] += 1
assert dict(counts) == enum["delta0inf_W_line_counts_all_48_under_literal_target_coordinates"] == {"L1": 16, "L2": 16, "L3": 16}
assert enum["all_48_delta0inf_linear_images_are_nonzero_W_lines"] is True

per_inner = []
for orb in inner_orbits:
    c = Counter()
    for k in orb:
        A, _ = conj_by_key[k]
        c[Wrev[matvec(A, delta)]] += 1
    per_inner.append(dict(c))
assert all(c == {"L1": 8, "L2": 8, "L3": 8} for c in per_inner)

prod = aff_comp(P2, P6)
target_products = Counter()
fixed_line_classes = Counter()
for a in conjugators:
    p = aff_comp(aff_comp(a, prod), aff_inv(a))
    target_products[aff_key(p)] += 1
for k in target_products:
    Aflat = k[:16]
    A = tuple(tuple(Aflat[4*i:4*i+4]) for i in range(4))
    fixed = [name for name, w in W.items() if matvec(A, w) == w]
    assert len(fixed) == 1
    fixed_line_classes[fixed[0]] += 1
assert len(target_products) == enum["source_product_phi2_phi6"]["distinct_target_affine_product_classes_among_48_conjugators"] == 6
assert set(target_products.values()) == {8}
assert dict(fixed_line_classes) == {"L1": 2, "L2": 2, "L3": 2}

residue = tgt["retained_W_under_literal_coordinate_preflight"]["line_to_Q602_residue"]
res_counts = {str(residue[line]): counts[line] for line in ["L1", "L2", "L3"]}
assert res_counts == enum["conditional_Q602_residue_counts_under_literal_target_coordinates"]

assert cert["coordinate_firewall"]["deraux_Zr2_literal_basis_equals_retained_Zr2_marked_basis_source_bound"] is False
assert cert["decision"]["result"] == "EX4_03_DERAUX_KRR_MOD2_CONJUGATOR_PREFLIGHT_NONPRUNING"
assert cert["decision"]["absolute_W_line_identified"] is False
assert cert["decision"]["absolute_Q602_residue_identified"] is False
assert cert["decision"]["retained_claim_dag_sync_performed"] is False
assert not any(cert["firewalls"].values())

print("PASS_STAGE32EX4_EX4_03_DERAUX_KRR_GMOD2_PREFLIGHT")
print(f"certificate_canonical={EXPECTED}")
print("source_A2_group=24 deraux_A2_group=24 six_point_orbit=6")
print("affine_conjugators=48 target_inner_orbits=24,24")
print("delta0inf_lines=L1:16,L2:16,L3:16 each_inner_orbit=8,8,8")
print("absolute_W_line=false absolute_Q602_residue=false claim_sync=false")
