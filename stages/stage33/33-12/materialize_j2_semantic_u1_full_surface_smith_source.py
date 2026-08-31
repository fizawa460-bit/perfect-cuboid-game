#!/usr/bin/env python3
"""Materialize the exact semantic-u1 full-surface Smith source coordinate.

One pinned Magma request computes only the six required Kc pullback rows and
the compact nontrivial part of the historical full-surface Smith transform.
Python then source-locks the result against the retained 140-curve marking,
the Stage33-09 marked basis, and the literal retained q256 Smith basis.

This certificate stops at the full-surface A_T[2] coordinate.  The proper-Br2
dual coordinate, retained 10D solve, and 75D column placement are performed by
a separate network-free producer.
"""
from __future__ import annotations

import ast
import hashlib
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
OLD_BASE = LEGACY / "picard_base_rows_retained.py"
OLD_SIGNS = LEGACY / "picard_coordinate_sign_rows_retained.py"
RETAINED = LEGACY / "retained-q256-geometric-sign-endpoint.json"
DISCRIMINANT = LEGACY / "picard-discriminant-compact.json"
OLD_CT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
OUT = HERE / "j2-semantic-u1-full-surface-smith-source.json"

SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
MARKED_SHA = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
STAGE32_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
OLD_BASE_SHA = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
OLD_SIGNS_SHA = "5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9"
RETAINED_SHA = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
DISCRIMINANT_SHA = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
OLD_CT_SHA = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
TARGETS = [2, 4, 9, 10, 47, 49]
MODS = [2] * 4 + [4] * 6 + [8] * 4
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,
    105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135,
]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path}")
    return obj


def invert(a: list[list[int]]) -> list[list[Fraction]]:
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


def integral(row, label):
    out = [Fraction(x) for x in row]
    if any(x.denominator != 1 for x in out): raise SystemExit(f"nonintegral row: {label}")
    return [int(x) for x in out]


def mm(a, b):
    return [[sum(int(a[i][k]) * int(b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a): return [list(x) for x in zip(*a)]


def retained_known_classes():
    marking = runpy.run_path(str(MARKING))["load"]()
    if marking["stage32_picard_core_sha256"] != STAGE32_CORE_SHA: raise SystemExit("Stage32 core moved")
    lines = [x.strip() for x in marking["hperp_text"].splitlines() if x.strip()]
    if lines[:3] != ["S32_D16_AUT_CANON_HPERP_V1", STAGE32_CORE_SHA, SOURCE_BLOB]:
        raise SystemExit("Stage32 Hperp header moved")
    if tuple(map(int, lines[4].split())) != (63, 140): raise SystemExit("Stage32 Hperp shape moved")
    off = 68
    pair = []
    for i in range(140):
        row = list(map(int, lines[off+i].split()))
        if len(row) != 65: raise SystemExit(f"bad known-class row {i+1}")
        pair.append([row[0]] + row[2:])
    inv = invert([pair[j-1] for j in INDLIST])
    known = [integral(rowmul(row, inv), f"known {i+1}") for i, row in enumerate(pair)]
    return known


sys.path.insert(0, str(LEGACY))
from stoll_cuboid_source import load_pinned_source, run_magma  # noqa: E402

text, core, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB: raise SystemExit("pinned Stoll blob moved")
start = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
end = "// action of sign change of c"
kcore = text[text.index(start):text.index(end, text.index(start))]
extra = r'''
targets33 := [2,4,9,10,47,49];
assert #Cs eq 92 and #pts eq 48 and bdim eq 140;
assert #CsK eq 62 and #ptsK eq 12 and bdimK eq 74;
D33,_,V33:=SmithForm(pmPic); ds33:=[Abs(Integers()!D33[j,j]):j in [1..64]];
pos33:=[j:j in [1..64]|ds33[j] gt 1]; mods33:=[ds33[j]:j in pos33];
assert mods33 eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
Vin33:=V33^-1; assert V33*Vin33 eq IdentityMatrix(Integers(),64);
Pinv33:=ChangeRing(pmPic,Rationals())^-1; Vq33:=ChangeRing(Vin33,Rationals());
B833:=8*Vq33*Pinv33*Transpose(Vq33);
n33:=&+[Vector(Integers(),Eltseq(preimsinPic[j])):j in targets33];
prod33:=n33*pmPic; assert &and[IsDivisibleBy(Integers()!x,2):x in Eltseq(prod33)];
z33:=Vector(Integers(),[Integers()!x div 2:x in Eltseq(prod33)]); y33:=z33*V33;
assert &and[(Integers()!y33[pos33[a]] mod mods33[a]) in {0,mods33[a] div 2}:a in [1..14]];
printf "STAGE33_12_J2_U1_SMITH_BEGIN\n"; printf "MODS=%o\n",mods33;
for j in targets33 do
  assert preimsinPic[j] eq qPic(Big![MatBigKtoBig[j,c]:c in [1..bdim]]);
  printf "PRE_IDX_%o=%o\n",j,[a[1]:a in preimages[j]];
  printf "PRE_MULT_%o=%o\n",j,[a[2]:a in preimages[j]];
  printf "PIC_ROW_%o=%o\n",j,Eltseq(preimsinPic[j]);
end for;
for a in [1..14] do printf "R_%o=%o\n",a,[Integers()!Vin33[pos33[a],j] mod 8:j in [1..64]]; end for;
for j in [1..64] do printf "C_%o=%o\n",j,[Integers()!V33[j,pos33[b]] mod 8:b in [1..14]]; end for;
for a in [1..14] do printf "B8_%o=%o\n",a,[Integers()!B833[pos33[a],pos33[b]] mod (a eq b select 16 else 8):b in [1..14]]; end for;
printf "N=%o\n",Eltseq(n33); printf "Z=%o\n",Eltseq(z33);
printf "Y=%o\n",[Integers()!y33[pos33[a]] mod mods33[a]:a in [1..14]];
printf "STAGE33_12_J2_U1_SMITH_END\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + kcore + "\n" + extra
stdout, magma_attempt = run_magma(code, 360, "Stage33-12 semantic u1 full-surface Smith source", "perfect-cuboid-stage33/4.3-j2-u1-smith")
if "STAGE33_12_J2_U1_SMITH_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout); raise SystemExit("semantic-u1 Smith extraction failed")


def grab(name, width=None):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m: raise SystemExit(f"missing Magma output {name}")
    row = ast.literal_eval(m.group(1))
    if not isinstance(row, list) or (width is not None and len(row) != width): raise SystemExit(f"bad Magma output {name}")
    return [int(x) for x in row]


mods = grab("MODS", 14)
if mods != MODS: raise SystemExit("Smith moduli moved")
R = [[x % 8 for x in grab(f"R_{a}", 64)] for a in range(1, 15)]
C = [[x % 8 for x in grab(f"C_{j}", 14)] for j in range(1, 65)]
b8 = [grab(f"B8_{a}", 14) for a in range(1, 15)]
if [[x % 8 for x in row] for row in mm(R, C)] != [[int(i == j) for j in range(14)] for i in range(14)]:
    raise SystemExit("compact Smith inverse regression")

marked = load_locked(MARKED, MARKED_SHA)
old = load_locked(OLD_CT, OLD_CT_SHA)
retained = load_locked(RETAINED, RETAINED_SHA)
disc = load_locked(DISCRIMINANT, DISCRIMINANT_SHA)
old_base = runpy.run_path(str(OLD_BASE))["load"]()
old_signs = runpy.run_path(str(OLD_SIGNS))["load"]()
if old_base["canonical_sha256"] != OLD_BASE_SHA or old_signs["canonical_sha256"] != OLD_SIGNS_SHA:
    raise SystemExit("retained Picard source moved")
if b8 != disc["discriminant_bilinear_numerator_over_8_reduced"]:
    raise SystemExit("literal retained Smith quadratic form mismatch")


def induced(g):
    raw = mm(mm(R, transpose(g)), C)
    return [[x % MODS[j] for j, x in enumerate(row)] for row in raw]


if induced(old_base["picard_action_cc_64x64"]) != retained["cc_action_mixed_moduli"]:
    raise SystemExit("literal retained cc mismatch")
if induced(old_base["picard_action_ct_64x64"]) != retained["ct_action_mixed_moduli"]:
    raise SystemExit("literal retained ct mismatch")
if [induced(old_signs["picard_actions_64x64"][x]) for x in ["a1","a2","a3","b1","b2","b3","c"]] != retained["sign_actions_mixed_moduli"]:
    raise SystemExit("literal retained sign mismatch")

B = [[int(x) for x in row] for row in marked["indlist_to_magma_picard_matrix_64x64"]]
known = retained_known_classes()
old_rows = {r["BigK_index_1based"]: r for r in old["pullbacks"]}
records = []; sum_ind = [0] * 64; sum_mag = [0] * 64
for j in TARGETS:
    idx, mult, mag = grab(f"PRE_IDX_{j}"), grab(f"PRE_MULT_{j}"), grab(f"PIC_ROW_{j}", 64)
    if not idx or len(idx) != len(mult) or len(set(idx)) != len(idx): raise SystemExit(f"bad preimage support {j}")
    ind = [sum(m * known[k-1][c] for k, m in zip(idx, mult)) for c in range(64)]
    if integral(rowmul(ind, B), f"BigK[{j}]") != mag: raise SystemExit(f"marked bridge mismatch {j}")
    if j in old_rows and old_rows[j]["fullPic64_historical_Magma_coordinates"] != mag: raise SystemExit(f"old pullback mismatch {j}")
    sum_ind = [a+b for a,b in zip(sum_ind, ind)]; sum_mag = [a+b for a,b in zip(sum_mag, mag)]
    records.append({"BigK_index_1based":j,"full_surface_known_preimage_indices_1based":idx,"full_surface_known_preimage_multiplicities":mult,"fullPic64_INDLIST_coordinates":ind,"fullPic64_historical_Magma_coordinates":mag})

n = grab("N", 64); z = grab("Z", 64); y = grab("Y", 14)
if n != sum_mag: raise SystemExit("semantic numerator sum mismatch")
gram = old_base["picard_gram_64x64"]
prod = integral(rowmul(n, gram), "n*pmPic")
if any(x & 1 for x in prod) or z != [x // 2 for x in prod]: raise SystemExit("exact half-lattice normalization mismatch")
bits = []
for value, modulus in zip(y, MODS):
    scale = modulus // 2
    if value not in (0, scale): raise SystemExit("Smith coordinate escaped A_T[2]")
    bits.append(value // scale)

out = {
    "schema":"STAGE33_12_J2_SEMANTIC_U1_FULL_SURFACE_SMITH_SOURCE_V1",
    "stage":"33-12",
    "status":"PASS_EXACT_FULL_SURFACE_A_T_2_COORDINATE_MATERIALIZED",
    "source_locks":{
        "stoll_commit":"51233ed5ef2bf228fac9416c66db9adc0ebcaadd","stoll_git_blob_sha1":blob,
        "submitted_magma_code_sha256":hashlib.sha256(code.encode()).hexdigest(),"stage32_picard_core_sha256":STAGE32_CORE_SHA,
        "stage33_09_marked_basis_sha256":MARKED_SHA,"retained_q256_endpoint_sha256":RETAINED_SHA,
        "picard_discriminant_compact_sha256":DISCRIMINANT_SHA,"prior_six_ct_pullbacks_sha256":OLD_CT_SHA,
    },
    "semantic_u1_pullback":{"BigK_support_1based":TARGETS,"pullbacks":records,"fullPic64_INDLIST_numerator":sum_ind,"fullPic64_historical_Magma_numerator":n},
    "retained_common_smith_source":{
        "discriminant_moduli":MODS,"vin_nontrivial_rows_mod8_14x64":R,"v_nontrivial_columns_mod8_64x14":C,
        "discriminant_bilinear_numerator_over_8_reduced":b8,
        "all_retained_cc_ct_and_seven_sign_actions_reproduced_literally":True,"retained_quadratic_form_reproduced_literally":True,
    },
    "exact_normalization":{
        "formula":"z=(n_S*pmPic)/2; y=z*V","integral_dual_quotient_representative_z":z,
        "nontrivial_smith_coordinates_mixed_moduli":y,"full_surface_A_T_2_coordinates_f2":bits,
        "A_T_2_coordinate_weight":sum(bits),"normalization_integral_exact":True,
    },
    "execution":{"source_fetch_attempt":source_attempt,"magma_request_attempt":magma_attempt,"planned_jobs":1,"effective_heavy_concurrency":1,"persisted_artifact":"one compact JSON","retention_days":1,"projected_peak_storage_bytes_upper_bound":1000000},
    "promotion_firewall":{"proper_Br2_14D_coordinate_materialized":False,"retained_10D_coordinate_materialized":False,"first_75D_matrix_column_materialized":False,"stage33_12_closed_exact":False,"stage33_13_released":False,"Q_defined_descent_credit_restored":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False},
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"success":True,"A_T_2_coordinate":bits,"weight":sum(bits),"certificate_sha256":out["canonical_sha256"]}, sort_keys=True))
