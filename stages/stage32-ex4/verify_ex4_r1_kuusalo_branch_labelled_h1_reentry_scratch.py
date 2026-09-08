#!/usr/bin/env python3
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "stages/stage32-ex4/ex4-r1-kuusalo-branch-labelled-h1-reentry-scratch.json"

def load(path):
    return json.loads(path.read_text())

def canonical_sha_without_field(obj):
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % 2
             for j in range(len(B[0]))] for i in range(len(A))]

def mv(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) % 2 for i in range(len(A))]

def tr(A):
    return [list(x) for x in zip(*A)]

def rank4(A):
    M = [row[:] for row in A]
    r = 0
    for c in range(4):
        p = next((i for i in range(r, 4) if M[i][c] % 2), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(4):
            if i != r and M[i][c] % 2:
                M[i] = [(a ^ b) for a, b in zip(M[i], M[r])]
        r += 1
    return r

def from_bits(bits):
    vals = [(bits >> k) & 1 for k in range(16)]
    return [vals[4*i:4*i+4] for i in range(4)]

def fixed_nonzero(A):
    out = []
    for v in itertools.product((0, 1), repeat=4):
        if v == (0, 0, 0, 0):
            continue
        vv = list(v)
        if mv(A, vv) == vv:
            out.append(vv)
    return out

a = load(ART)
assert a["schema"] == "STAGE32EX4_R1_KUUSALO_BRANCH_LABELLED_H1_REENTRY_SCRATCH_V1"
assert a["status"] == "SCRATCH_REPLAYABLE_SOURCE_H1_REENTRY_TARGET_LITERAL_BINDING_MISSING"
assert canonical_sha_without_field(a) == a["canonical_sha256_without_this_field"]
assert a["canonical_sha256_without_this_field"] == "cc2ac8033071a594d8ba75b5ac0cc1bbc66039fe608af9452360fb038489f1cf"

for lock in a["source_locks"].values():
    p = ROOT / lock["path"]
    assert p.exists(), lock["path"]
    assert git_blob_sha1(p) == lock["blob_sha1"], lock["path"]
    if "canonical_sha256" in lock:
        src = load(p)
        assert src["canonical_sha256_without_this_field"] == lock["canonical_sha256"]

src = a["source_side_exact_reconstruction"]
M = src["f1_mod2_matrix"]
J = src["intersection_form_mod2"]
assert fixed_nonzero(M) == [[1, 1, 1, 1]]
assert src["deduced_delta0inf_coordinate_mod2"] == [1, 1, 1, 1]
assert mm(mm(tr(M), J), M) == J

tgt = a["retained_literal_order8_preflight"]
A = tgt["A_mod2_F2_4_matrix"]
E = tgt["weil_pairing_mod2"]
assert fixed_nonzero(A) == [[0, 0, 0, 1]]
assert tgt["fixed_line"] == "L2"
assert tgt["line_to_residue"] == {"L1": 73, "L2": 97, "L3": 235}

count = 0
images = set()
for bits in range(1 << 16):
    Q = from_bits(bits)
    if rank4(Q) != 4:
        continue
    if mm(mm(tr(Q), E), Q) != J:
        continue
    if mm(A, Q) != mm(Q, M):
        continue
    count += 1
    images.add(tuple(mv(Q, [1, 1, 1, 1])))

assert count == 8
assert images == {(0, 0, 0, 1)}
test = a["finite_literal_intertwiner_test"]
assert test["all_4x4_F2_matrices_tested"] == 65536
assert test["invertible_symplectic_intertwiner_count"] == count
assert test["delta0inf_image_set"] == [[0, 0, 0, 1]]
assert test["conditional_line"] == "L2"
assert test["conditional_residue"] == 97
assert test["conditional_only"] is True

d = a["decision"]
assert d["reentry_condition_met"] is True
assert d["source_side_branch_labelled_H1_marking_obtained"] is True
assert d["direct_source_delta0inf_coordinate_obtained"] is True
assert d["absolute_delta0inf_retained_W_line_identified"] is False
assert d["absolute_Q602_residue_identified"] is False
assert d["Q602_excluded"] is False
assert d["O210_excluded"] is False
assert d["stage32_main_credit"] is False

f = a["firewalls"]
for key in [
    "prior_audited_terminal_revoked",
    "literal_target_word_promoted_without_source_binding",
    "conditional_residue97_promoted",
    "post1648j_promoted_to_audited",
    "Q602_excluded",
    "O210_excluded",
    "stage32_main_credit",
    "perfect_cuboid_claim",
]:
    assert f[key] is False, key

print("Stage32EX4 R1 Kuusalo branch-labelled H1 reentry scratch: PASS")
print("source_delta0inf=[1,1,1,1]")
print("literal_A_intertwiners=8 all_map_to_L2 conditional_residue=97")
print("absolute_retained_line=false stage32_main_credit=false")
