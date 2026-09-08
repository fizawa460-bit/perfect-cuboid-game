#!/usr/bin/env python3
import hashlib
import itertools
import json
import subprocess
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ARTIFACT = HERE / "ex4-08-frozen-package-ambiguity-certificate-scratch.json"

ZERO = (0, 0)
ONE = (1, 0)
MONE = (-1, 0)
R = (0, 1)

def radd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def rneg(x):
    return (-x[0], -x[1])

def rmul(x, y):
    return (x[0] * y[0] - 2 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])

def mmul(A, B):
    return tuple(
        tuple(radd(rmul(A[i][0], B[0][j]), rmul(A[i][1], B[1][j]))
              for j in range(2))
        for i in range(2)
    )

I = ((ONE, ZERO), (ZERO, ONE))
S = ((ONE, radd(ONE, R)), (ZERO, MONE))
T = ((ONE, ONE), (MONE, ZERO))

def det(A):
    return radd(rmul(A[0][0], A[1][1]), rneg(rmul(A[0][1], A[1][0])))

def minv(A):
    d = det(A)
    if d == ONE:
        dinv = ONE
    elif d == MONE:
        dinv = MONE
    else:
        raise AssertionError(f"nonunit determinant {d}")
    adj = ((A[1][1], rneg(A[0][1])),
           (rneg(A[1][0]), A[0][0]))
    return tuple(tuple(rmul(dinv, adj[i][j]) for j in range(2)) for i in range(2))

TINV = minv(T)

def generate_group():
    gens = (S, T, minv(S), TINV)
    seen = {I}
    q = deque([I])
    while q:
        g = q.popleft()
        for a in gens:
            h = mmul(g, a)
            if h not in seen:
                seen.add(h)
                q.append(h)
    return seen

def mod2_mat4(A):
    ar = [[A[i][j][0] & 1 for j in range(2)] for i in range(2)]
    br = [[A[i][j][1] & 1 for j in range(2)] for i in range(2)]
    M = [[0] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            M[i][j] = ar[i][j]
            M[i + 2][j] = br[i][j]
            M[i + 2][j + 2] = ar[i][j]
    return tuple(tuple(row) for row in M)

L1 = (0, 0, 1, 0)
L2 = (0, 0, 0, 1)
L3 = (0, 0, 1, 1)
LINES = (L1, L2, L3)

def act4(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) & 1 for i in range(4))

def line_perm(A):
    M = mod2_mat4(A)
    imgs = tuple(act4(M, v) for v in LINES)
    assert set(imgs) == set(LINES)
    return tuple(LINES.index(x) for x in imgs)

def conj(h, a):
    return mmul(mmul(h, a), minv(h))

def order(A):
    x = I
    for n in range(1, 97):
        x = mmul(x, A)
        if x == I:
            return n
    raise AssertionError("order bound exceeded")

def canonical_sha256(data):
    d = dict(data)
    expected = d.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    assert got == expected, (got, expected)
    return got

def git_blob_sha(path):
    out = subprocess.check_output(
        ["git", "-C", str(ROOT), "hash-object", str(path)],
        text=True
    ).strip()
    return out

def check_source_locks(data):
    package = data["frozen_package"]
    for item in package["audited_core"] + package["candidate_and_scratch_strengthening"]:
        path = ROOT / item["path"]
        assert path.exists(), item["path"]
        if "blob_sha1" in item:
            assert git_blob_sha(path) == item["blob_sha1"], item["path"]
        if path.suffix == ".json" and "canonical_sha256" in item:
            obj = json.loads(path.read_text())
            embedded = obj.get("canonical_sha256_without_this_field")
            if embedded is not None:
                assert embedded == item["canonical_sha256"], item["path"]

def equivariant_bijections(target_phi2, target_phi6):
    source_phi2 = (0, 2, 1)  # Z1 fixed; Z2<->Z3
    source_phi6 = (2, 0, 1)  # Z1->Z3->Z2->Z1
    out = []
    for f in itertools.permutations(range(3)):
        if all(
            f[source_phi2[i]] == target_phi2[f[i]]
            and f[source_phi6[i]] == target_phi6[f[i]]
            for i in range(3)
        ):
            out.append(f)
    return out

def main():
    data = json.loads(ARTIFACT.read_text())
    canonical_sha256(data)
    check_source_locks(data)

    G = generate_group()
    assert len(G) == 48

    center = [g for g in G if all(mmul(g, h) == mmul(h, g) for h in G)]
    assert len(center) == 2
    assert set(center) == {
        I,
        ((MONE, ZERO), (ZERO, MONE)),
    }

    perms = Counter(line_perm(g) for g in G)
    assert len(perms) == 6
    assert set(perms.values()) == {8}

    kernel = [g for g in G if line_perm(g) == (0, 1, 2)]
    assert len(kernel) == 8
    assert Counter(order(g) for g in kernel) == Counter({4: 6, 2: 1, 1: 1})

    line_stabilizers = [
        sum(1 for g in G if line_perm(g)[i] == i)
        for i in range(3)
    ]
    assert line_stabilizers == [16, 16, 16]

    pair_classes = {}
    for h in G:
        pair = (conj(h, S), conj(h, TINV))
        pair_classes.setdefault(pair, []).append(h)
    assert len(pair_classes) == 24
    assert set(len(v) for v in pair_classes.values()) == {2}

    bijection_counts = Counter()
    delta_counts = Counter()
    for pair in pair_classes:
        target_phi2 = line_perm(pair[0])
        target_phi6 = line_perm(pair[1])
        eq = equivariant_bijections(target_phi2, target_phi6)
        assert len(eq) == 1
        f = eq[0]
        bijection_counts[f] += 1
        delta_counts[f[2]] += 1  # source Z3

        product = mmul(pair[0], pair[1])
        p = line_perm(product)
        fixed = [i for i in range(3) if p[i] == i]
        assert fixed == [f[2]]

    assert len(bijection_counts) == 6
    assert set(bijection_counts.values()) == {4}
    assert delta_counts == Counter({0: 8, 1: 8, 2: 8})

    enum = data["strongest_admissible_identification_enumeration"]
    assert enum["G_order"] == 48
    assert enum["projective_ambiguity_group_order"] == 24
    assert enum["ordered_pair_inner_conjugacy_orbit_size"] == 24
    assert enum["delta0inf_projective_identification_counts"] == {
        "L1": 8, "L2": 8, "L3": 8
    }

    amb = data["residual_ambiguity_group_action"]
    assert amb["G_action_on_W_lines_image"] == "S3"
    assert amb["G_action_on_W_lines_image_order"] == 6
    assert amb["kernel_in_G_order"] == 8
    assert amb["kernel_in_G_structure"] == "Q8"
    assert amb["kernel_in_projective_group_order"] == 4
    assert amb["kernel_in_projective_group_structure"] == "V4"
    assert amb["line_stabilizer_in_G_order"] == 16
    assert amb["line_stabilizer_in_projective_group_order"] == 8

    obstruction = data["bounded_obstruction"]
    assert obstruction["strong_package_possible_lines"] == ["L1", "L2", "L3"]
    assert obstruction["strong_package_possible_residues"] == [73, 97, 235]
    assert obstruction["result"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE_CANDIDATE"

    decision = data["decision"]
    assert decision["bounded_terminal_outcome_candidate"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
    assert decision["absolute_W_line_identified"] is False
    assert decision["absolute_Q602_residue_identified"] is False
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert decision["stage32_main_credit"] is False

    print(json.dumps({
        "artifact": ARTIFACT.name,
        "canonical_sha256": data["canonical_sha256_without_this_field"],
        "G_order": len(G),
        "projective_pair_classes": len(pair_classes),
        "W_action_image_order": len(perms),
        "W_kernel_order": len(kernel),
        "line_stabilizer_order": line_stabilizers[0],
        "distinct_source_to_W_bijections": len(bijection_counts),
        "bijection_multiplicity": sorted(set(bijection_counts.values())),
        "delta0inf_line_counts": {
            "L1": delta_counts[0],
            "L2": delta_counts[1],
            "L3": delta_counts[2],
        },
        "result": obstruction["result"],
    }, indent=2))

if __name__ == "__main__":
    main()
