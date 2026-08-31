#!/usr/bin/env python3
"""Network-free verifier for Stage33-05 exact zero K3 Br[2] Q-survival.

Rebuilds the dependency after the corrected J2 arithmetic no-go.  The geometric
G_Q-invariant Br[2] receiver is the two-dimensional space <J2,q1>.  The q1
restricted HS d2 class and the corrected-J2 restricted HS d2 class are shown
to be distinct nonzero classes in H^2(<ct>,Pic).  Hence the restricted d2 map
is injective and the global HS d2 kernel on this receiver is zero.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
SEMANTIC = S33 / "33-12" / "j2-semantic-kc-picard-basis.json"
J2 = HERE / "j2-r5e-pic2-r5f-ct-hs-d2-nonzero.json"
J2_AUDIT = HERE / "j2-r5f-hs-d2-nonzero-hostile-replay.json"
Q1_NS = HERE / "q1_ns_lift_parity.py"
Q1_D2 = HERE / "q1_hs_d2_bockstein.py"
PAIR = HERE / "xalpha_pair_galois_repair.py"
PRES = HERE / "descent_presentation_cocycle.py"
PIC_SUPPORT = S33 / "33-12" / "certify_j2_corrected_ct_norm_picard_support.py"
OUT = HERE / "stage33-05-br2-zero-q-survival-after-j2-nogo.json"

EXPECTED = {
    SEMANTIC: ("canonical", "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"),
    J2: ("canonical", "8e384501db1cb3aa3f73358b0c3612a85e4012c5041fda60d3be7aeddc7c4c55"),
    J2_AUDIT: ("canonical", "6535f3190daab8c20ba5ddb3409675f20ac35dc4ee319e3be7af056baa4ce20d"),
    Q1_NS: ("blob", "6526a8cbc50e5e683e5385fd38e208703b724ff3"),
    Q1_D2: ("blob", "9b38833b58c548a539648cc803ee1f451ece5434"),
    PAIR: ("blob", "b7f37df50a123ef6c972aa210e7efb5f16535f76"),
    PRES: ("blob", "02b5a13150f7bf9beb56712498c66acae008e1d8"),
    PIC_SUPPORT: ("blob", "90ee4af41c541bbc69d764d9f55919b4ae1be670"),
}


def canonical_sha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path):
    data = path.read_bytes()
    hdr = b"blob " + str(len(data)).encode() + b"\0"
    return hashlib.sha1(hdr + data).hexdigest()


def load_canonical(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert obj["canonical_sha256"] == expected == canonical_sha(obj), path
    return obj


for path, (kind, expected) in EXPECTED.items():
    if kind == "blob":
        assert git_blob_sha1(path) == expected, (path, git_blob_sha1(path))
semantic = load_canonical(SEMANTIC, EXPECTED[SEMANTIC][1])
j2 = load_canonical(J2, EXPECTED[J2][1])
j2audit = load_canonical(J2_AUDIT, EXPECTED[J2_AUDIT][1])

# Lock the source semantics that make the two-dimensional receiver and q1 bridge explicit.
pair_src = PAIR.read_text(encoding="utf-8")
pres_src = PRES.read_text(encoding="utf-8")
q1d2_src = Q1_D2.read_text(encoding="utf-8")
assert 'quotient_basis = ["J2", "q1"]' in pair_src
assert '"geometric_Br2_GQ_invariant_dimension": 2' in pair_src
assert '"q1":{"ct":"J1"' in pres_src.replace(" ", "")
assert '"HS_d2_q1_global_nonzero": True' in q1d2_src
assert '"q1_Q_descent": False' in q1d2_src
assert j2audit["hostile_checks"]["restricted_class_nonzero"] is True
assert j2audit["verdict"]["R5f_HS_d2"] == "NONZERO_EXACT"

# Rebuild the marked rank-20 Gram matrix.
g17 = semantic["gram17"]
inc = semantic["incidence17x12"]
triple = semantic["semantic_exceptional_indices_0based"]
g20 = [row[:] + [inc[i][c] for c in triple] for i, row in enumerate(g17)]
for a, c in enumerate(triple):
    row = [inc[i][c] for i in range(17)] + [0, 0, 0]
    row[17 + a] = -2
    g20.append(row)
assert len(g20) == 20 and all(len(r) == 20 for r in g20)
assert all(g20[i][k] == g20[k][i] for i in range(20) for k in range(20))

basis = j2["semantic_ct_action"]["basis_order"]
assert basis[:3] == ["CsK[2]", "CsK[4]", "CsK[5]"]
ct = j2["semantic_ct_action"]["matrix"]
assert ct[0] == [1 if k == 0 else 0 for k in range(20)]  # CsK[2] fixed
assert ct[2] == [1 if k == 2 else 0 for k in range(20)]  # CsK[5] fixed

# Corrected-J2 restricted d2 integral class Z and its pairing with CsK[5].
Z = j2["r5f_integral_lift_and_restricted_d2"]["restricted_normalized_2cocycle"][
    "beta(ct,ct)=Z=(B+ct(B))/2"
]
assert Z == [0,0,0,0,0,0,0,1,1,1,-1,0,0,0,2,1,0,0,0,0]

def pairing(coords, basis_index):
    return sum(coords[k] * g20[k][basis_index] for k in range(20))

assert pairing(Z, 2) == 1

# Independently replay the q1 divisor D = Cb + E_P0 against two ct-fixed tests.
A1,A2,A3,B1,B2,B3 = sp.symbols("A1 A2 A3 B1 B2 B3")
vars6 = (A1,A2,A3,B1,B2,B3)
i = sp.I
K = [
    A1**2 + A2**2 - B3**2,
    A2**2 + A3**2 - B1**2,
    A1**2 + A3**2 - B2**2,
]
Cb = [i*A1+B1, i*A2+B2, i*A3+B3]
T2 = [A1, A2+B3, A3-B2]                 # CsK[2]
T5 = [A2, A3+B1, A1+B3]                 # CsK[5]
P0 = [0,1,0,-1,0,1]


def coeff_matrix(forms):
    return sp.Matrix([[sp.expand(f).coeff(v) for v in vars6] for f in forms])

# Cb and CsK[2] meet in exactly one projective point.
M2 = coeff_matrix(Cb + T2)
assert M2.rank() == 5
ns = M2.nullspace()
assert len(ns) == 1
P = ns[0]
subP = dict(zip(vars6, P))
assert all(sp.simplify(f.subs(subP)) == 0 for f in K + Cb + T2)
JK = sp.Matrix([[sp.diff(f,v).subs(subP) for v in vars6] for f in K])
JCb = sp.Matrix([[sp.diff(f,v).subs(subP) for v in vars6] for f in Cb])
JT2 = sp.Matrix([[sp.diff(f,v).subs(subP) for v in vars6] for f in T2])
assert JK.rank() == 3
assert JK.col_join(JCb).rank() == 4
assert JK.col_join(JT2).rank() == 4
assert JK.col_join(JCb).col_join(JT2).rank() == 5

# P0 is not on either test; hence E_P0 has intersection zero with both strict transforms.
subP0 = dict(zip(vars6, P0))
assert any(sp.simplify(f.subs(subP0)) != 0 for f in T2)
assert any(sp.simplify(f.subs(subP0)) != 0 for f in T5)

# Cb and CsK[5] are projectively disjoint (combined linear rank six).
assert coeff_matrix(Cb + T5).rank() == 6
q1_pair_T2 = 1
q1_pair_T5 = 0

# q1 is nonzero (odd pairing with ct-fixed CsK[2]); J2 and q1 are distinct
# (their difference pairs oddly with ct-fixed CsK[5]).
assert q1_pair_T2 % 2 == 1
j2_pair_T5 = pairing(Z, 2)
assert (j2_pair_T5 - q1_pair_T5) % 2 == 1

# H^2(C2,Pic)=Pic^ct/(1+ct)Pic is killed by 2, hence is an F2-vector space.
# Two distinct nonzero classes are independent.  Since <J2,q1> has dimension 2,
# the restricted d2 map is injective.  Global kernel is contained in restricted kernel.
restricted_d2_rank_f2 = 2
global_kernel_dimension_f2 = 0

cert = json.loads(OUT.read_text(encoding="utf-8"))
assert cert["geometric_GQ_invariant_Br2_basis"] == ["J2", "q1"]
assert cert["geometric_GQ_invariant_dimension_f2"] == 2
assert cert["q1_restricted_d2"]["test_CsK2_pairing"] == q1_pair_T2
assert cert["q1_restricted_d2"]["test_CsK5_pairing"] == q1_pair_T5
assert cert["j2_restricted_d2"]["Z_integral_class"] == Z
assert cert["j2_restricted_d2"]["test_CsK5_pairing"] == j2_pair_T5
assert cert["restricted_d2_rank_f2"] == restricted_d2_rank_f2
assert cert["global_d2_kernel_dimension_f2"] == global_kernel_dimension_f2
assert cert["Q_relevant_surviving_dimension"] == 0
assert cert["exact_zero_survival_certificate"] is True
assert cert["canonical_sha256"] == canonical_sha(cert)
print(json.dumps({
    "status": "PASS_EXACT_ZERO_Q_SURVIVAL_CANDIDATE",
    "canonical_sha256": cert["canonical_sha256"],
    "restricted_d2_rank_f2": 2,
    "global_d2_kernel_dimension_f2": 0,
    "q1_pair_CsK2": 1,
    "q1_pair_CsK5": 0,
    "j2_pair_CsK5": 1,
}, sort_keys=True))
