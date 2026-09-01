#!/usr/bin/env python3
"""Materialize corrected J2 proper-Br2 by the Picard adjoint map.

For the degree-2 quotient S -> Kc, the full semantic PicK pullback matrix P
fixes the adjoint pushforward on dual lattices.  In Picard covector coordinates,
a full-surface discriminant covector z_S is sent to z_K = z_S P^T.  Via the
K3 discriminant anti-isometries this gives the induced T(S)/2T(S) ->
T(Kc)/2T(Kc) map.  The corrected J2 functional beta1=[1,0] is then simply the
first source coordinate of each of the 14 target T/2T basis vectors.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import itertools
import json
import re
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
LEGACY = S33 / "33-07"
SEMANTIC = HERE / "j2-semantic-kc-picard-basis.json"
KC2 = HERE / "j2-semantic-kc-discriminant-2torsion-target.json"
U1 = HERE / "j2-semantic-u1-full-surface-smith-source.json"
U2 = HERE / "j2-semantic-u2-full-surface-at2.json"
PROPER = LEGACY / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
OLD_BASE = LEGACY / "picard_base_rows_retained.py"
OUT = HERE / "j2-picard-adjoint-proper-br2.json"

SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
LOCKS = {
    SEMANTIC: "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0",
    KC2: "0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df",
    U1: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    U2: "60b6d058459f7745f6fa3f9b6d3b44f1610e12ff46c42e3133ec574f71613039",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
}
OLD_BASE_SHA = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
MODS = [2] * 4 + [4] * 6 + [8] * 4


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path):
    x = json.loads(path.read_text(encoding="utf-8"))
    b = dict(x); h = b.pop("canonical_sha256")
    assert h == LOCKS[path] == csha(b), path
    return x


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(x) for x in zip(*a)]


def rowmul(v, m):
    return [sum(v[k] * m[k][j] for k in range(len(v))) for j in range(len(m[0]))]


def invert(a):
    n = len(a)
    m = [[Fraction(a[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        p = next((r for r in range(col, n) if m[r][col]), None)
        assert p is not None
        m[col], m[p] = m[p], m[col]
        q = m[col][col]
        m[col] = [x / q for x in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                q = m[r][col]
                m[r] = [m[r][j] - q * m[col][j] for j in range(2*n)]
    return [r[n:] for r in m]


def determinant(a):
    m = [[Fraction(x) for x in r] for r in a]
    det = Fraction(1)
    for c in range(len(m)):
        p = next((r for r in range(c, len(m)) if m[r][c]), None)
        if p is None: return 0
        if p != c:
            m[c], m[p] = m[p], m[c]; det = -det
        q = m[c][c]; det *= q
        for j in range(c, len(m)): m[c][j] /= q
        for r in range(c+1, len(m)):
            q = m[r][c]
            if q:
                for j in range(c, len(m)): m[r][j] -= q * m[c][j]
    assert det.denominator == 1
    return int(det)


def rowmul_f2(v, m):
    return [sum((int(v[i]) & 1) * (int(m[i][j]) & 1) for i in range(len(v))) & 1 for j in range(len(m[0]))]


def solve10(basis, target):
    for bits in itertools.product((0, 1), repeat=10):
        v = [0] * 14
        for bit, row in zip(bits, basis):
            if bit:
                v = [a ^ (int(b) & 1) for a, b in zip(v, row)]
        if v == target:
            return list(bits)
    return None


semantic = locked(SEMANTIC)
kc2 = locked(KC2)
u1 = locked(U1)
u2 = locked(U2)
proper = locked(PROPER)
target = locked(TARGET)
old_base = runpy.run_path(str(OLD_BASE))["load"]()
assert old_base["canonical_sha256"] == OLD_BASE_SHA
Gs = [[int(x) for x in row] for row in old_base["picard_gram_64x64"]]
indlistK = [int(x) for x in semantic["upstream_source_lock"]["indlistK_1based"]]
assert len(indlistK) == 20

sys.path.insert(0, str(LEGACY))
from stoll_cuboid_source import load_pinned_source, run_magma  # noqa: E402
text, core, blob, source_attempt = load_pinned_source()
assert blob == SOURCE_BLOB
start = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
end = "// action of sign change of c"
kcore = text[text.index(start):text.index(end, text.index(start))]
targets_literal = "[" + ",".join(map(str, indlistK)) + "]"
extra = f'''
targets33 := {targets_literal};
D33,_,V33:=SmithForm(pmPic); ds33:=[Abs(Integers()!D33[j,j]):j in [1..64]];
pos33:=[j:j in [1..64]|ds33[j] gt 1]; mods33:=[ds33[j]:j in pos33];
assert mods33 eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
Vin33:=V33^-1; assert V33*Vin33 eq IdentityMatrix(Integers(),64);
printf "STAGE33_12_ADJOINT_BEGIN\\n"; printf "MODS=%o\\n",mods33;
for j in targets33 do printf "P_%o=%o\\n",j,Eltseq(preimsinPic[j]); end for;
for a in [1..14] do
  sc:=mods33[a] div 2;
  printf "ZB_%o=%o\\n",a,[sc*Integers()!Vin33[pos33[a],j]:j in [1..64]];
end for;
printf "STAGE33_12_ADJOINT_END\\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + kcore + "\n" + extra
stdout, magma_attempt = run_magma(code, 360, "Stage33-12 Picard adjoint proper Br2", "perfect-cuboid-stage33/4.5-picard-adjoint-br2")
if "STAGE33_12_ADJOINT_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout); raise SystemExit("adjoint extraction failed")


def grab(name, n=None):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    assert m, name
    v = [int(x) for x in ast.literal_eval(m.group(1))]
    if n is not None: assert len(v) == n
    return v


assert grab("MODS", 14) == MODS
P = [grab(f"P_{j}", 64) for j in indlistK]
ZB = [grab(f"ZB_{a}", 64) for a in range(1, 15)]
PGPt = mm(mm(P, Gs), transpose(P))
assert all(x % 2 == 0 for row in PGPt for x in row)
Gk = [[x // 2 for x in row] for row in PGPt]
assert determinant(Gk) == -32
invGk = invert(Gk)

u1_num = kc2["semantic_half_lattice_basis"][0]["numerator_mod2"]
u2_num = kc2["semantic_half_lattice_basis"][1]["numerator_mod2"]
zero20 = [0] * 20
combo = {
    tuple(zero20): [0, 0],
    tuple(u1_num): [1, 0],
    tuple(u2_num): [0, 1],
    tuple(a ^ b for a, b in zip(u1_num, u2_num)): [1, 1],
}
columns = []
for a, zS in enumerate(ZB, start=1):
    zK = [sum(zS[k] * P[j][k] for k in range(64)) for j in range(20)]
    xK = rowmul(zK, invGk)
    twice = [2 * x for x in xK]
    assert all(x.denominator == 1 for x in twice), f"target AT2 basis {a} did not land in source AT2"
    vmod2 = tuple(int(x) & 1 for x in twice)
    assert vmod2 in combo, (a, vmod2)
    columns.append({
        "target_basis_index_1based": a,
        "source_T_mod_2_coordinate_f2": combo[vmod2],
        "source_half_lattice_numerator_mod2": list(vmod2),
        "source_picard_dual_covector_zK": zK,
    })

beta1 = [c["source_T_mod_2_coordinate_f2"][0] for c in columns]
beta2 = [c["source_T_mod_2_coordinate_f2"][1] for c in columns]
assert rowmul_f2(beta1, proper["proper_Br2_cc_action_f2"]) == beta1
assert rowmul_f2(beta1, proper["proper_Br2_ct_action_f2"]) == beta1
assert rowmul_f2(beta2, proper["proper_Br2_cc_action_f2"]) == beta2
assert rowmul_f2(beta2, proper["proper_Br2_ct_action_f2"]) == beta2
basis10 = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
coord10_beta1 = solve10(basis10, beta1)
coord10_beta2 = solve10(basis10, beta2)
assert coord10_beta1 is not None and coord10_beta2 is not None
u1_at2 = u1["exact_normalization"]["full_surface_A_T_2_coordinates_f2"]
u2_at2 = u2["semantic_u2_pullback"]["full_surface_A_T_2_coordinates_f2"]
annihilation = [
    [sum(a*b for a,b in zip(beta1, u1_at2)) & 1, sum(a*b for a,b in zip(beta1, u2_at2)) & 1],
    [sum(a*b for a,b in zip(beta2, u1_at2)) & 1, sum(a*b for a,b in zip(beta2, u2_at2)) & 1],
]
assert annihilation == [[0,0],[0,0]]

out = {
    "schema": "STAGE33_12_J2_PICARD_ADJOINT_PROPER_BR2_V1",
    "stage": "33-12",
    "status": "PASS_EXACT_PICARD_ADJOINT_PROPER_BR2_MATERIALIZED",
    "source_locks": {
        "stoll_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "stoll_git_blob_sha1": blob,
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "semantic_picard_basis_sha256": LOCKS[SEMANTIC],
        "kc_discriminant_2torsion_sha256": LOCKS[KC2],
        "semantic_u1_full_surface_sha256": LOCKS[U1],
        "semantic_u2_full_surface_sha256": LOCKS[U2],
        "proper_brauer2_sha256": LOCKS[PROPER],
        "retained_10D_target_sha256": LOCKS[TARGET],
        "full_surface_picard_base_sha256": OLD_BASE_SHA,
    },
    "degree2_picard_adjoint": {
        "semantic_Kc_basis_BigK_indices_1based": indlistK,
        "picard_pullback_matrix_P_20x64": P,
        "source_picard_gram_Gk_equals_PGsPt_over_2_20x20": Gk,
        "source_picard_gram_determinant": determinant(Gk),
        "target_AT2_basis_picard_covectors_zS_14x64": ZB,
        "formula": "for x_S=z_S*G_S^-1, adjoint pushforward has source covector z_K=z_S*P^T; decode 2*(z_K*G_K^-1) mod 2 in semantic [u1,u2] basis",
        "decoded_target_basis_columns": columns,
        "degree2_mod2_annihilation_matrix_on_known_pullback_u1_u2": annihilation,
    },
    "proper_brauer2_pullback": {
        "corrected_named_Kc_functional_coordinate_f2": [1,0],
        "proper_Br2_14D_coordinate_f2": beta1,
        "proper_Br2_14D_weight": sum(beta1),
        "proper_Br2_cc_fixed": True,
        "proper_Br2_ct_fixed": True,
        "retained_10D_coordinate_f2": coord10_beta1,
        "retained_10D_weight": sum(coord10_beta1),
        "companion_beta2_proper_Br2_14D_coordinate_f2": beta2,
        "companion_beta2_retained_10D_coordinate_f2": coord10_beta2,
    },
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": magma_attempt,
        "planned_jobs": 1,
        "effective_heavy_concurrency": 1,
        "persisted_artifact": "none; compact certificate committed after verification",
        "projected_peak_storage_bytes_upper_bound": 1000000,
    },
    "promotion_firewall": {
        "proper_Br2_14D_coordinate_materialized": True,
        "retained_10D_coordinate_materialized": True,
        "first_75D_matrix_column_materialized": False,
        "finite_v4_kummer_columns_materialized": 0,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "Q_defined_descent_credit_restored": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "proper14": beta1,
    "retained10": coord10_beta1,
    "proper14_weight": sum(beta1),
    "retained10_weight": sum(coord10_beta1),
    "companion_beta2": beta2,
    "canonical_sha256": out["canonical_sha256"],
}, sort_keys=True))
