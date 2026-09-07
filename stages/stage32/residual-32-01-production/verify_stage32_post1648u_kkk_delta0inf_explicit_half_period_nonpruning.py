#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648u-kkk-delta0inf-explicit-half-period-nonpruning.json"
EXPECTED = "eb0d69e1f219e6204399aeed2a0498bbefd13d2e6dc9a02f0927bb7eec73f281"

def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    assert claimed == got
    return got

def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mt(A):
    return [list(row) for row in zip(*A)]

def det4(M):
    out = 0
    for p in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
        term = 1
        for i in range(4):
            term *= M[i][p[i]]
        out += (-1 if inv % 2 else 1) * term
    return out

def pair_mul(x, y):
    return (x[0] * y[0] - 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def pair_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def real_matrix(entries):
    alpha, beta, gamma, delta = entries
    aa, ab = alpha
    ba, bb = beta
    ca, cb = gamma
    da, db = delta
    return [
        [aa, ba, -2 * ab, -2 * bb],
        [ca, da, -2 * cb, -2 * db],
        [ab, bb, aa, ba],
        [cb, db, ca, da],
    ]

def mod2_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) & 1 for i in range(4))

cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

nlock = cert["source_locks"]["post1648N"]
npath = ROOT / nlock["path"]
assert npath.is_file()
assert blob_sha1(npath) == nlock["git_blob_sha1"]
ncert = json.loads(npath.read_text())
assert canonical(ncert) == nlock["canonical_sha256"]
assert ncert["exact_enumeration"]["principal_polarization_maps_found"] == 48

T_cycle = [
    [0, -1, 1, -1],
    [0, 1, 0, 1],
    [-1, 1, -1, 1],
    [-1, -1, 0, 0],
]
mu = mt(T_cycle)
fixed = []
for v in itertools.product((0, 1), repeat=4):
    if mod2_vec(mu, v) == v:
        fixed.append(v)
assert fixed == [(0, 0, 0, 0), (0, 0, 1, 1)]
delta = (0, 0, 1, 1)

derived = cert["kkk_mod2_derivation"]
assert derived["unique_nonzero_fixed_vector"] == list(delta)
assert derived["delta_0inf_half_period_vector_mod2"] == list(delta)
assert derived["fixed_subspace_mod2_vectors"] == [list(v) for v in fixed]

ros_lock = ncert["repo_source_lock"]
ros_path = ROOT / ros_lock["path"]
assert ros_path.is_file()
assert blob_sha1(ros_path) == ros_lock["git_blob_sha1"]
ros = json.loads(ros_path.read_text())
assert canonical(ros) == ros_lock["canonical_sha256"]

E = ros["principal_polarization"]["riemann_form_matrix"]
source_form = [
    [0, 0, -1, 0],
    [0, 0, 0, -1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
]
C2 = [
    [-1, 1, 2, 0],
    [1, -1, 0, 2],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
]
els = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
valid = []
for alpha, beta, gamma, delta_entry in itertools.product(els, repeat=4):
    determinant = pair_sub(pair_mul(alpha, delta_entry), pair_mul(beta, gamma))
    if determinant not in ((2, 0), (-2, 0)):
        continue
    R = real_matrix((alpha, beta, gamma, delta_entry))
    M2 = mm(R, C2)
    if any(x % 2 for row in M2 for x in row):
        continue
    M = [[x // 2 for x in row] for row in M2]
    if abs(det4(M)) != 1:
        continue
    if mm(mm(mt(M), E), M) != source_form:
        continue
    valid.append(M)
assert len(valid) == 48

L1 = (0, 0, 1, 0)
L2 = (0, 0, 0, 1)
L3 = (0, 0, 1, 1)
counts = {"L1": 0, "L2": 0, "L3": 0}
lookup = {L1: "L1", L2: "L2", L3: "L3"}
for M in valid:
    image = mod2_vec(M, delta)
    assert image in lookup
    counts[lookup[image]] += 1
assert counts == {"L1": 16, "L2": 16, "L3": 16}

test = cert["exact_torsor_test"]
assert test["polarized_period_lattice_isomorphisms_replayed"] == 48
assert test["all_images_land_in_retained_W_nonzero_lines"] is True
assert test["multiplicity_by_target_line"] == counts
assert test["distinct_target_lines"] == 3

dec = cert["decision"]
assert dec["explicit_branch_point_half_period_marking_obtained"] is True
assert dec["explicit_delta0inf_source_vector_obtained"] is True
assert dec["explicit_delta0inf_half_period_breaks_48_ppav_torsor"] is False
assert dec["absolute_delta0inf_retained_W_line_identified"] is False
assert dec["survivors_current_credit"] == [73, 97, 235]
assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
assert not any(cert["firewalls"].values())

print("POST1648U_KKK_DELTA0INF_EXPLICIT_HALF_PERIOD_NONPRUNING_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("kkk_delta0inf_mod2=(0,0,1,1)")
print("polarized_ppav_isomorphisms=48 delta0inf_target_counts=L1:16,L2:16,L3:16")
print("absolute_delta0inf_retained_W_line_identified=false")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
