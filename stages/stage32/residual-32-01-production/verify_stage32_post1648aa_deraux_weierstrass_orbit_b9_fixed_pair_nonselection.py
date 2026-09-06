#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648aa-deraux-weierstrass-orbit-b9-fixed-pair-nonselection.json"
NOTE = HERE / "post1648aa-deraux-weierstrass-orbit-b9-fixed-pair-nonselection-source-note.md"
ZCERT = HERE / "post1648z-kkk-full-bolza-homology-marking-nonselection.json"
ROSATI = HERE / "post1490-o210-q4-bolza-principal-rosati-lock.json"

EXPECTED_CERT_CANONICAL = "a0ca0342db4902e737f28aa5f0de447cca2a2fce71f8cf0cdd2775d51804f7c7"
EXPECTED_NOTE_BLOB = "7cec0431ce48200b68557b9d88da2b73ed5ddbac"
EXPECTED_Z_BLOB = "da3d30630698fc77098b3316c4ea4f19bc8258ef"
EXPECTED_Z_CANONICAL = "b8db79100ebc404a497e64e973fce7f631f6475b3fc220c32874f07095a6576e"
EXPECTED_ROSATI_BLOB = "e28c4533883440ea0963d4d4e8859aa95409cf10"
EXPECTED_ROSATI_CANONICAL = "8d828cdf6d1f5cb1d790c46292535dc252e503356e1047ce972c41e61f524529"


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


# Q(r), r^2=-2. Elements are pairs (a,b)=a+b*r.
def R(a=0, b=0):
    return (Fraction(a), Fraction(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def mm(A, B):
    return [[add(mul(A[i][0], B[0][j]), mul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def mv(A, v):
    return [add(mul(A[i][0], v[0]), mul(A[i][1], v[1])) for i in range(2)]


def red(x):
    return (x[0] % 1, x[1] % 1)


def compose(f, g):
    # f after g
    A, t = f
    B, u = g
    AB = mm(A, B)
    Au = mv(A, u)
    return AB, [red(add(Au[i], t[i])) for i in range(2)]


def key(f):
    A, t = f
    return (
        tuple(tuple(tuple(e) for e in row) for row in A),
        tuple(red(x) for x in t),
    )


ZERO = R()
ONE = R(1)
I2 = [[ONE, ZERO], [ZERO, ONE]]
ID = (I2, [ZERO, ZERO])

# Deraux arXiv:1611.05112v2, Definition 4.1, lower-right 2x2 block + lower-left translation.
R1 = (
    [[R(1), R(0)], [R(1, -1), R(-1)]],
    [R(0), R(0)],
)
R2 = (
    [[R(-1, 1), R(2)], [R(1, 1), R(1, -1)]],
    [R(0), R(0)],
)
R3 = (
    [[R(1), R(-1, -1)], [R(0), R(-1)]],
    [R(Fraction(1, 2), Fraction(1, 2)), R(1)],
)
GENS = (R1, R2, R3)


def close_affine_group():
    seen = {key(ID): ID}
    queue = [ID]
    while queue:
        f = queue.pop(0)
        for g in GENS:
            h = compose(f, g)
            k = key(h)
            if k not in seen:
                seen[k] = h
                queue.append(h)
    return list(seen.values())


def order(f):
    x = ID
    for n in range(1, 49):
        x = compose(x, f)
        if key(x) == key(ID):
            return n
    raise AssertionError("order > 48")


def ring_mul_mod2(x, y):
    a, b = x
    c, d = y
    # r^2=-2=0 mod 2
    return ((a * c) % 2, (a * d + b * c) % 2)


def act_bits(f, v):
    A, t = f
    z = [(v[0], v[2]), (v[1], v[3])]
    out = []
    for i in range(2):
        s = (0, 0)
        for j in range(2):
            a = (int(A[i][j][0]) % 2, int(A[i][j][1]) % 2)
            p = ring_mul_mod2(a, z[j])
            s = ((s[0] + p[0]) % 2, (s[1] + p[1]) % 2)
        ta = int(2 * t[i][0]) % 2
        tb = int(2 * t[i][1]) % 2
        out.append(((s[0] + ta) % 2, (s[1] + tb) % 2))
    return (out[0][0], out[1][0], out[0][1], out[1][1])


def xor(u, v):
    return tuple(a ^ b for a, b in zip(u, v))


def cycle_type(f, orbit):
    unseen = set(orbit)
    lengths = []
    while unseen:
        start = next(iter(unseen))
        cur = start
        n = 0
        while cur in unseen:
            unseen.remove(cur)
            n += 1
            cur = act_bits(f, cur)
        lengths.append(n)
    return sorted(lengths)


def trace(A):
    return add(A[0][0], A[1][1])


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT_CANONICAL
    assert git_blob_sha(NOTE) == EXPECTED_NOTE_BLOB

    zcert = json.loads(ZCERT.read_text(encoding="utf-8"))
    assert git_blob_sha(ZCERT) == EXPECTED_Z_BLOB
    assert canonical_sha(zcert) == EXPECTED_Z_CANONICAL
    rosati = json.loads(ROSATI.read_text(encoding="utf-8"))
    assert git_blob_sha(ROSATI) == EXPECTED_ROSATI_BLOB
    assert canonical_sha(rosati) == EXPECTED_ROSATI_CANONICAL
    assert rosati["principal_polarization"]["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]

    group = close_affine_group()
    assert len(group) == 48

    # Table-2 order-8-orbit representative q=(1/2,(1+r)/2).
    q = (1, 1, 0, 1)
    orbit = {q}
    changed = True
    while changed:
        changed = False
        for v in list(orbit):
            for g in GENS:
                w = act_bits(g, v)
                if w not in orbit:
                    orbit.add(w)
                    changed = True
    expected_orbit = {
        (0, 0, 1, 0), (0, 0, 1, 1), (1, 0, 0, 0),
        (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 1),
    }
    assert orbit == expected_orbit

    diffs = {xor(u, v) for u, v in itertools.combinations(sorted(orbit), 2)}
    all_nonzero = set(itertools.product((0, 1), repeat=4)) - {(0, 0, 0, 0)}
    assert diffs == all_nonzero

    # Image on A[2] has order 24 because central -I is invisible mod 2.
    perms = {
        tuple(act_bits(f, v) for v in itertools.product((0, 1), repeat=4))
        for f in group
    }
    assert len(perms) == 24

    candidates = []
    for f in group:
        if order(f) != 8:
            continue
        if cycle_type(f, orbit) != [1, 1, 4]:
            continue
        fixed = sorted(v for v in orbit if act_bits(f, v) == v)
        assert len(fixed) == 2
        d = xor(fixed[0], fixed[1])
        candidates.append((f, d))
    assert len(candidates) == 12

    lines = {
        (0, 0, 1, 0): "L1",
        (0, 0, 0, 1): "L2",
        (0, 0, 1, 1): "L3",
    }
    by_trace = {"+r": Counter(), "-r": Counter()}
    for f, d in candidates:
        tr = trace(f[0])
        if tr == R(0, 1):
            s = "+r"
        elif tr == R(0, -1):
            s = "-r"
        else:
            raise AssertionError(f"unexpected order-8 trace {tr}")
        assert d in lines
        by_trace[s][lines[d]] += 1

    assert by_trace["+r"] == Counter({"L1": 2, "L2": 2, "L3": 2})
    assert by_trace["-r"] == Counter({"L1": 2, "L2": 2, "L3": 2})

    replay = cert["deraux_affine_A2_replay"]
    assert replay["full_affine_group_order"] == 48
    assert replay["A2_affine_image_order"] == 24
    assert replay["orbit_size"] == 6
    assert replay["unordered_pair_difference_count"] == 15
    assert replay["pair_differences_equal_all_nonzero_A2_vectors"] is True

    test = cert["B9_fixed_pair_test"]
    assert test["actual_order8_affine_elements_with_cycle_type_114"] == 12
    assert test["linear_trace_class_counts"] == {"+r": 6, "-r": 6}
    assert test["fixed_pair_difference_counts_by_trace"] == {
        "+r": {"L1": 2, "L2": 2, "L3": 2},
        "-r": {"L1": 2, "L2": 2, "L3": 2},
    }
    assert test["fixed_pair_difference_counts_total"] == {"L1": 4, "L2": 4, "L3": 4}
    assert test["absolute_W_line_selected"] is False

    decision = cert["decision"]
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert cert["semantic_boundary"]["two_sided_set_level_anchor_obtained"] is True
    assert cert["semantic_boundary"]["pointwise_source_to_target_weierstrass_binding_obtained"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_current_credit"] is False

    print("POST1648AA_DERAUX_WEIERSTRASS_ORBIT_B9_FIXED_PAIR_NONSELECTION_COMPLETE")
    print("deraux_affine_group=48 A2_image=24 six_point_orbit=6 pair_differences=15")
    print("order8_cycle_114_candidates=12 trace_classes=+r:6,-r:6")
    print("fixed_pair_lines_each_trace=L1:2,L2:2,L3:2")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
