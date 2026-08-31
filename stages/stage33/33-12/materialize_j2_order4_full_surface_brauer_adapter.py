#!/usr/bin/env python3
"""Materialize the four missing order-4 pullback rows and corrected J2 proper-Br2 evaluations."""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import re
import runpy
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
LEGACY = S33 / "33-07"
MARKED = S33 / "33-09" / "marked-picard-basis-source.json"
MARKING = LEGACY / "stage32_picard_marking_retained.py"
U1_SOURCE = HERE / "j2-semantic-u1-full-surface-smith-source.json"
REDUCTION = HERE / "j2-order4-brauer-lift-reduction.json"
PROPER = LEGACY / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
OUT = HERE / "j2-order4-full-surface-brauer-adapter.json"

SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
MARKED_SHA = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
STAGE32_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
U1_SHA = "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec"
REDUCTION_SHA = "d1bb3b6f15019c7ea6b0b93db49df28155bfc4f97d665fecc2a31547910a73f9"
PROPER_SHA = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
TARGET_SHA = "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"
TERMS = [(2,1),(4,3),(9,3),(10,1),(20,2),(35,2),(39,2),(47,3),(49,3),(67,2)]
NEW_TARGETS = [20,35,39,67]
MODS = [2] * 4 + [4] * 6 + [8] * 4
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,
    105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135,
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path}")
    return obj


def invert(a):
    n = len(a)
    m = [[Fraction(x) for x in a[i]] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None: raise SystemExit("singular exact marking matrix")
        m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]; m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                f = m[r][col]; m[r] = [m[r][j] - f * m[col][j] for j in range(2*n)]
    return [row[n:] for row in m]


def rowmul(a, b):
    return [sum(a[k] * b[k][j] for k in range(len(a))) for j in range(len(b[0]))]


def rowmul_f2(a, b):
    return [sum((int(a[k]) & 1) * (int(b[k][j]) & 1) for k in range(len(a))) & 1 for j in range(len(b[0]))]


def integral(row, label):
    out = [Fraction(x) for x in row]
    if any(x.denominator != 1 for x in out): raise SystemExit(f"nonintegral row: {label}")
    return [int(x) for x in out]


def retained_known_classes():
    marking = runpy.run_path(str(MARKING))["load"]()
    if marking["stage32_picard_core_sha256"] != STAGE32_CORE_SHA: raise SystemExit("Stage32 core moved")
    lines = [x.strip() for x in marking["hperp_text"].splitlines() if x.strip()]
    if lines[:3] != ["S32_D16_AUT_CANON_HPERP_V1", STAGE32_CORE_SHA, SOURCE_BLOB]: raise SystemExit("Stage32 Hperp header moved")
    if tuple(map(int, lines[4].split())) != (63, 140): raise SystemExit("Stage32 Hperp shape moved")
    off = 68; pair = []
    for i in range(140):
        row = list(map(int, lines[off+i].split()))
        if len(row) != 65: raise SystemExit(f"bad known-class row {i+1}")
        pair.append([row[0]] + row[2:])
    inv = invert([pair[j-1] for j in INDLIST])
    return [integral(rowmul(row, inv), f"known {i+1}") for i, row in enumerate(pair)]


def solve_retained10(basis, target):
    for bits in itertools.product((0,1), repeat=len(basis)):
        v = [0] * len(target)
        for bit, row in zip(bits, basis):
            if bit: v = [a ^ (int(b) & 1) for a,b in zip(v,row)]
        if v == target: return list(bits)
    return None


u1 = load_locked(U1_SOURCE, U1_SHA)
reduction = load_locked(REDUCTION, REDUCTION_SHA)
proper = load_locked(PROPER, PROPER_SHA)
target = load_locked(TARGET, TARGET_SHA)
marked = load_locked(MARKED, MARKED_SHA)
assert reduction["schema"] == "STAGE33_12_J2_ORDER4_BRAUER_LIFT_REDUCTION_V2_BILINEAR_EVALUATION"
assert reduction["semantic_order4_generator"]["BigK_terms_row_and_coefficient_mod4"] == [list(x) for x in TERMS]
assert reduction["next_numeric_leaf"]["materialize_additional_BigK_pullback_rows_1based"] == NEW_TARGETS
assert u1["retained_common_smith_source"]["discriminant_moduli"] == MODS

sys.path.insert(0, str(LEGACY))
from stoll_cuboid_source import load_pinned_source, run_magma  # noqa: E402

text, core, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB: raise SystemExit("pinned Stoll blob moved")
start = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
end = "// action of sign change of c"
kcore = text[text.index(start):text.index(end, text.index(start))]
extra = r'''
termsJ33 := [2,4,9,10,20,35,39,47,49,67];
coeffsJ33 := [1,3,3,1,2,2,2,3,3,2];
newJ33 := [20,35,39,67];
assert #Cs eq 92 and #pts eq 48 and bdim eq 140;
assert #CsK eq 62 and #ptsK eq 12 and bdimK eq 74;
D33,_,V33:=SmithForm(pmPic); ds33:=[Abs(Integers()!D33[j,j]):j in [1..64]];
pos33:=[j:j in [1..64]|ds33[j] gt 1]; mods33:=[ds33[j]:j in pos33];
assert mods33 eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
n433:=&+[coeffsJ33[k]*Vector(Integers(),Eltseq(preimsinPic[termsJ33[k]])):k in [1..#termsJ33]];
prod433:=n433*pmPic;
printf "STAGE33_12_J2_ORDER4_BEGIN\n"; printf "MODS=%o\n",mods33;
for j in newJ33 do
  assert preimsinPic[j] eq qPic(Big![MatBigKtoBig[j,c]:c in [1..bdim]]);
  printf "PRE_IDX_%o=%o\n",j,[a[1]:a in preimages[j]];
  printf "PRE_MULT_%o=%o\n",j,[a[2]:a in preimages[j]];
  printf "PIC_ROW_%o=%o\n",j,Eltseq(preimsinPic[j]);
end for;
for j in [1..64] do printf "C_%o=%o\n",j,[Integers()!V33[j,pos33[b]] mod 8:b in [1..14]]; end for;
printf "N4=%o\n",Eltseq(n433); printf "PROD4=%o\n",Eltseq(prod433);
printf "STAGE33_12_J2_ORDER4_END\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + kcore + "\n" + extra
stdout, magma_attempt = run_magma(code, 360, "Stage33-12 J2 order4 four-row Brauer adapter", "perfect-cuboid-stage33/4.3-j2-order4-adapter")
if "STAGE33_12_J2_ORDER4_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout); raise SystemExit("order4 adapter extraction failed")


def grab(name, width=None):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m: raise SystemExit(f"missing Magma output {name}")
    row = ast.literal_eval(m.group(1))
    if not isinstance(row, list) or (width is not None and len(row) != width): raise SystemExit(f"bad Magma output {name}")
    return [int(x) for x in row]


mods = grab("MODS", 14)
if mods != MODS: raise SystemExit("Smith moduli moved")
C = [[x % 8 for x in grab(f"C_{j}", 14)] for j in range(1,65)]
expected_C = u1["retained_common_smith_source"]["v_nontrivial_columns_mod8_64x14"]
if C != expected_C: raise SystemExit("retained Magma Smith V nontrivial columns moved")

B = [[int(x) for x in row] for row in marked["indlist_to_magma_picard_matrix_64x64"]]
known = retained_known_classes()
new_records = []
for j in NEW_TARGETS:
    idx, mult, mag = grab(f"PRE_IDX_{j}"), grab(f"PRE_MULT_{j}"), grab(f"PIC_ROW_{j}",64)
    if not idx or len(idx) != len(mult) or len(set(idx)) != len(idx): raise SystemExit(f"bad preimage support {j}")
    ind = [sum(m * known[k-1][c] for k,m in zip(idx,mult)) for c in range(64)]
    if integral(rowmul(ind,B), f"BigK[{j}]") != mag: raise SystemExit(f"marked bridge mismatch {j}")
    new_records.append({
        "BigK_index_1based": j,
        "full_surface_known_preimage_indices_1based": idx,
        "full_surface_known_preimage_multiplicities": mult,
        "fullPic64_INDLIST_coordinates": ind,
        "fullPic64_historical_Magma_coordinates": mag,
    })

old_rows = {r["BigK_index_1based"]: r for r in u1["semantic_u1_pullback"]["pullbacks"]}
new_rows = {r["BigK_index_1based"]: r for r in new_records}
all_rows = dict(old_rows); all_rows.update(new_rows)
assert sorted(all_rows) == sorted(j for j,_ in TERMS)
weighted_mag = [0] * 64
weighted_ind = [0] * 64
for j,c in TERMS:
    weighted_mag = [a + c*b for a,b in zip(weighted_mag, all_rows[j]["fullPic64_historical_Magma_coordinates"])]
    weighted_ind = [a + c*b for a,b in zip(weighted_ind, all_rows[j]["fullPic64_INDLIST_coordinates"])]
n4 = grab("N4",64)
prod4 = grab("PROD4",64)
if n4 != weighted_mag: raise SystemExit("weighted order4 numerator mismatch")
if integral(rowmul(weighted_ind,B), "weighted order4 bridge") != n4: raise SystemExit("weighted marked bridge mismatch")

integral_z4 = all(x % 4 == 0 for x in prod4)
z4 = [x // 4 for x in prod4] if integral_z4 else None
y4 = None
doubling_matches = False
pairing_numerators = None
proper14 = None
cc_fixed = False
ct_fixed = False
retained10 = None
if integral_z4:
    y4 = [sum(z4[k] * C[k][j] for k in range(64)) % MODS[j] for j in range(14)]
    doubled = [(2*y4[j]) % MODS[j] for j in range(14)]
    expected_u1_y = u1["exact_normalization"]["nontrivial_smith_coordinates_mixed_moduli"]
    doubling_matches = doubled == expected_u1_y
    scales = [m // 2 for m in MODS]
    b8 = u1["retained_common_smith_source"]["discriminant_bilinear_numerator_over_8_reduced"]
    pairing_numerators = [sum(y4[i] * scales[j] * int(b8[i][j]) for i in range(14)) for j in range(14)]
    if doubling_matches and all(x % 4 == 0 for x in pairing_numerators):
        proper14 = [(x // 4) & 1 for x in pairing_numerators]
        cc_fixed = rowmul_f2(proper14, proper["proper_Br2_cc_action_f2"]) == proper14
        ct_fixed = rowmul_f2(proper14, proper["proper_Br2_ct_action_f2"]) == proper14
        basis10 = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
        retained10 = solve_retained10(basis10, proper14) if cc_fixed and ct_fixed else None

accepted = bool(integral_z4 and doubling_matches and pairing_numerators is not None and all(x % 4 == 0 for x in pairing_numerators) and proper14 is not None and cc_fixed and ct_fixed and retained10 is not None)
status = "PASS_EXACT_J2_PROPER14_AND_RETAINED10_MATERIALIZED" if accepted else "PASS_EXACT_ORDER4_REPLAY_MATERIALIZED_ADAPTER_NOT_PROMOTED"
out = {
    "schema": "STAGE33_12_J2_ORDER4_FULL_SURFACE_BRAUER_ADAPTER_V1",
    "stage": "33-12",
    "status": status,
    "source_locks": {
        "stoll_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "stoll_git_blob_sha1": blob,
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "stage32_picard_core_sha256": STAGE32_CORE_SHA,
        "stage33_09_marked_basis_sha256": MARKED_SHA,
        "semantic_u1_full_surface_smith_source_sha256": U1_SHA,
        "order4_lift_reduction_sha256": REDUCTION_SHA,
        "proper_brauer2_sha256": PROPER_SHA,
        "retained_10D_target_basis_sha256": TARGET_SHA,
    },
    "order4_pullback": {
        "terms_row_and_coefficient_mod4": [list(x) for x in TERMS],
        "new_rows": new_records,
        "weighted_fullPic64_INDLIST_numerator": weighted_ind,
        "weighted_fullPic64_historical_Magma_numerator": n4,
    },
    "exact_order4_normalization": {
        "prod4_equals_n4_pmPic": prod4,
        "z4_integral": integral_z4,
        "z4": z4,
        "y4_mixed_smith_coordinates": y4,
        "doubling_matches_locked_u1_mixed_smith_coordinate": doubling_matches,
    },
    "proper_brauer2_evaluation": {
        "formula": "f_j=2*b(w,(m_j/2)e_j)=(sum_i y4_i*(m_j/2)*B8[i][j])/4 mod2",
        "pairing_numerators_over_4": pairing_numerators,
        "all_pairing_numerators_divisible_by_4": bool(pairing_numerators is not None and all(x % 4 == 0 for x in pairing_numerators)),
        "proper_Br2_14D_coordinate_f2": proper14,
        "proper_Br2_cc_fixed": cc_fixed,
        "proper_Br2_ct_fixed": ct_fixed,
        "retained_10D_coordinate_f2": retained10,
        "adapter_accepted": accepted,
    },
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": magma_attempt,
        "planned_jobs": 1,
        "effective_heavy_concurrency": 1,
        "persisted_artifact": "one compact JSON",
        "retention_days": 1,
        "projected_peak_storage_bytes_upper_bound": 1000000,
    },
    "promotion_firewall": {
        "proper_Br2_14D_coordinate_materialized": accepted,
        "retained_10D_coordinate_materialized": accepted,
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
print(json.dumps({"success": True, "accepted": accepted, "proper14": proper14, "retained10": retained10, "canonical_sha256": out["canonical_sha256"]}, sort_keys=True))
