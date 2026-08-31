#!/usr/bin/env python3
"""Materialize only the six full-surface Picard pullbacks needed by J2.

The historical 20x64 Kc-to-S matrix is deliberately not regenerated.  The
pinned Stoll construction already forms the raw known-curve preimage map
``MatBigKtoBig``.  This shard emits only rows 26,35,42,47,49,52 and their
images in the full-surface Magma Picard basis.  The result is then checked
locally against the retained Stage32 all-140 marking and the certified
Stage33-09 INDLIST-to-Magma basis bridge.

This is support transport only.  It does not assign the cc Cech parity, choose
the named CV/discriminant orientation, or materialize a Kummer column.
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
OUT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"

SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
MARKED_SHA = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
STAGE32_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
TARGETS = [26, 35, 42, 47, 49, 52]
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,
    105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135,
]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path}")
    return obj


def invert(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    m = [
        [Fraction(x) for x in a[i]]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None:
            raise SystemExit("singular exact marking matrix")
        m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r == col:
                continue
            f = m[r][col]
            if f:
                m[r] = [m[r][j] - f * m[col][j] for j in range(2*n)]
    return [row[n:] for row in m]


def rowmul(a: list[int], b: list[list[int | Fraction]]) -> list[int | Fraction]:
    return [sum(a[k] * b[k][j] for k in range(len(a))) for j in range(len(b[0]))]


def integral(row: list[int | Fraction], label: str) -> list[int]:
    out = [Fraction(x) for x in row]
    if any(x.denominator != 1 for x in out):
        raise SystemExit(f"nonintegral Picard row: {label}")
    return [int(x) for x in out]


def retained_known_classes() -> list[list[int]]:
    marking = runpy.run_path(str(MARKING))["load"]()
    if marking["stage32_picard_core_sha256"] != STAGE32_CORE_SHA:
        raise SystemExit("retained Stage32 Picard core moved")
    lines = [x.strip() for x in marking["hperp_text"].splitlines() if x.strip()]
    if lines[0] != "S32_D16_AUT_CANON_HPERP_V1" or lines[1] != STAGE32_CORE_SHA:
        raise SystemExit("retained Stage32 Hperp header moved")
    if lines[2] != SOURCE_BLOB:
        raise SystemExit("retained Stage32 source blob moved")
    if tuple(map(int, lines[4].split())) != (63, 140):
        raise SystemExit("retained Stage32 Hperp shape moved")
    off = 5 + 63
    pairing_rows = []
    for i in range(140):
        row = list(map(int, lines[off+i].split()))
        if len(row) != 65:
            raise SystemExit(f"bad retained known-class row {i+1}")
        pairing_rows.append([row[0]] + row[2:])
    basis = [pairing_rows[j-1] for j in INDLIST]
    inv = invert(basis)
    known = [integral(rowmul(row, inv), f"known class {i+1}")
             for i, row in enumerate(pairing_rows)]
    for k, j in enumerate(INDLIST):
        e = [0]*64
        e[k] = 1
        if known[j-1] != e:
            raise SystemExit("INDLIST standard-basis regression")
    return known


sys.path.insert(0, str(LEGACY))
from stoll_cuboid_source import load_pinned_source, run_magma  # noqa: E402

text, core, blob, source_attempt = load_pinned_source()
if blob != SOURCE_BLOB:
    raise SystemExit("pinned Stoll source blob moved")
start = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
end = "// action of sign change of c"
kcore = text[text.index(start):text.index(end, text.index(start))]
target_magma = str(TARGETS).replace("[", "[").replace("]", "]")
extra = f'''
targets33 := {target_magma};
assert #Cs eq 92 and #pts eq 48 and bdim eq 140;
assert #CsK eq 62 and #ptsK eq 12 and bdimK eq 74;
printf "STAGE33_12_J2_CT_SIX_PULLBACKS_BEGIN\\n";
for j in targets33 do
  assert &and[a[1] ge 1 and a[1] le bdim : a in preimages[j]];
  assert preimsinPic[j] eq qPic(Big![MatBigKtoBig[j,c] : c in [1..bdim]]);
  printf "PRE_IDX_%o=%o\\n",j,[a[1] : a in preimages[j]];
  printf "PRE_MULT_%o=%o\\n",j,[a[2] : a in preimages[j]];
  printf "PIC_ROW_%o=%o\\n",j,Eltseq(preimsinPic[j]);
end for;
printf "STAGE33_12_J2_CT_SIX_PULLBACKS_END\\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + kcore + "\n" + extra
stdout, magma_attempt = run_magma(
    code, 300, "Stage33-12 J2 six Kc support pullbacks",
    user_agent="perfect-cuboid-stage33/4.2-j2-six-pullbacks",
)
if "STAGE33_12_J2_CT_SIX_PULLBACKS_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("six-support pullback extraction failed")


def grab(name: str, width: int | None = None) -> list[int]:
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing Magma output {name}")
    row = ast.literal_eval(m.group(1))
    if not isinstance(row, list) or (width is not None and len(row) != width):
        raise SystemExit(f"bad Magma output {name}")
    return [int(x) for x in row]


marked = load_locked(MARKED, MARKED_SHA)
B = [[int(x) for x in row] for row in marked["indlist_to_magma_picard_matrix_64x64"]]
if len(B) != 64 or any(len(row) != 64 for row in B):
    raise SystemExit("marked basis bridge shape moved")
known = retained_known_classes()
records = []
sum_ind = [0]*64
sum_mag = [0]*64
for j in TARGETS:
    idx = grab(f"PRE_IDX_{j}")
    mult = grab(f"PRE_MULT_{j}")
    mag = grab(f"PIC_ROW_{j}", 64)
    if not idx or len(idx) != len(mult) or len(set(idx)) != len(idx):
        raise SystemExit(f"bad preimage support for BigK[{j}]")
    if any(not 1 <= x <= 140 for x in idx) or any(x <= 0 for x in mult):
        raise SystemExit(f"bad preimage index/multiplicity for BigK[{j}]")
    ind = [sum(m*known[k-1][c] for k, m in zip(idx, mult)) for c in range(64)]
    if integral(rowmul(ind, B), f"BigK[{j}] bridge") != mag:
        raise SystemExit(f"Stage32/Stage33-09 pullback bridge mismatch at BigK[{j}]")
    sum_ind = [a+b for a, b in zip(sum_ind, ind)]
    sum_mag = [a+b for a, b in zip(sum_mag, mag)]
    records.append({
        "BigK_index_1based": j,
        "full_surface_known_preimage_indices_1based": idx,
        "full_surface_known_preimage_multiplicities": mult,
        "fullPic64_INDLIST_coordinates": ind,
        "fullPic64_historical_Magma_coordinates": mag,
    })

out = {
    "schema": "STAGE33_12_J2_CT_SIX_KC_SUPPORT_FULLPIC64_PULLBACKS_V1",
    "source_locks": {
        "stoll_repository": "MichaelStollBayreuth/Verification",
        "stoll_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "stoll_path": "Cuboids/cuboids.magma",
        "stoll_git_blob_sha1": blob,
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "stage32_picard_core_sha256": STAGE32_CORE_SHA,
        "stage33_09_marked_basis_sha256": MARKED_SHA,
    },
    "target_BigK_support_1based": TARGETS,
    "pullbacks": records,
    "ct_sum_fullPic64_INDLIST_coordinates_mod2": [x & 1 for x in sum_ind],
    "ct_sum_fullPic64_historical_Magma_coordinates_mod2": [x & 1 for x in sum_mag],
    "exact_checks": {
        "only_six_required_support_rows_materialized": True,
        "all_preimages_are_full_surface_known_classes_1_to_140": True,
        "all_six_rows_reconstructed_from_retained_140_class_marking": True,
        "all_six_rows_transport_through_stage33_09_marked_basis_exactly": True,
        "historical_full_Kc20_to_fullPic64_matrix_regenerated": False,
    },
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": magma_attempt,
        "remote_cas_role": "emit six pinned raw preimage rows and their exact full-surface Picard quotient coordinates only",
        "smith_form_computed": False,
        "galois_action_computed": False,
        "artifact_persisted": False,
    },
    "remaining_interfaces": [
        "J2_CC_ACTUAL_CECH_PARITY",
        "NAMED_CV_d2_TO_SEMANTIC_DISCRIMINANT_ORIENTATION",
    ],
    "promotion_firewall": {
        "first_exact_75D_kummer_column_materialized": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "support": TARGETS,
    "certificate_sha256": out["canonical_sha256"],
    "ct_sum_weight_indlist_mod2": sum(out["ct_sum_fullPic64_INDLIST_coordinates_mod2"]),
}, indent=2, sort_keys=True))
