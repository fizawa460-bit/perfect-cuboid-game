#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
import re
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
S33_07 = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(S33_07))

from stoll_cuboid_source import load_pinned_source, run_magma  # type: ignore

OUT = ROOT / "stages/stage35-ex/35ex-35/goal4ae-c5-direct-pick-to-pics-indlist64.json"
GOAL4AD = ROOT / "stages/stage35-ex/35ex-35/goal4ad-c5-pair-marked-picard-adapter-preflight.json"
MARKED = ROOT / "stages/stage33/33-09/marked-picard-basis-source.json"
REC = S33_07 / "certify_two_coordinate_swap_picard_rows.py"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
GOAL4AD_BLOB = "6cedfed8d5944a3a93ddfe106f488c2a75670c92"
MARKED_SHA256 = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,
    93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,
    117,118,119,120,121,125,126,127,129,133,135,
]
K_START = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
K_END = "// action of sign change of c"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    x = json.loads(path.read_text())
    b = dict(x)
    got = b.pop("canonical_sha256", None)
    if got != expected or csha(b) != expected:
        raise SystemExit(f"canonical hash regression: {path}")
    return x


def parse_rows(stdout: str) -> list[dict]:
    rows = []
    pat = re.compile(r"^GOAL4AE_ROW=([-0-9]+)\|([-0-9]+)\|([-0-9]+)\|(.+?)\|(.+?)\|(.+)$")
    for line in stdout.splitlines():
        m = pat.match(line.strip())
        if not m:
            continue
        e1, e2, e3 = map(int, m.group(1, 2, 3))
        pick20 = [int(x) for x in ast.literal_eval(m.group(4))]
        pics64 = [int(x) for x in ast.literal_eval(m.group(5))]
        ind64 = [int(x) for x in ast.literal_eval(m.group(6))]
        rows.append({
            "sign_triple": [e1, e2, e3],
            "PicK_basis_coordinates_20": pick20,
            "PicS_historical_Magma_coordinates_64": pics64,
            "PicS_INDLIST_coordinates_64": ind64,
        })
    return rows


def add(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b)]


def scale(k: int, a: list[int]) -> list[int]:
    return [k * x for x in a]


def pair(u: list[int], v: list[int], gram: list[list[int]]) -> int:
    return sum(u[i] * gram[i][j] * v[j] for i in range(64) for j in range(64))


if git_blob(GOAL4AD) != GOAL4AD_BLOB:
    raise SystemExit("Goal4AD blob moved")
marked = load_canonical(MARKED, MARKED_SHA256)
if marked["indlist_1based"] != INDLIST:
    raise SystemExit("Stage33 marked INDLIST order moved")
if marked["source"]["git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("Stage33 marked source upstream blob moved")

full_source, surface_core, upstream_blob, source_attempt = load_pinned_source()
if upstream_blob != SOURCE_BLOB:
    raise SystemExit("pinned upstream source blob moved")
for needle in [
    "function imageinPicK(C)",
    "PicKtoPicS := hom<PicK -> Pic",
    "MatKtoS := Matrix(Integers()",
    "C5K := Curve(IrreducibleComponents(Scheme(K, B1+B2+B3))[1]);",
    "until #C5sK eq 8;",
    K_START,
    K_END,
]:
    if needle not in full_source:
        raise SystemExit(f"upstream C5/PicK route regression: {needle}")

# Generation 1 submitted all 42 kB of cuboids.magma to the public calculator
# and received an empty response before any mathematical assertion ran.  Reuse
# the established Stage33 source slicer for S, then append only the exact K/PicK
# setup through PicKtoPicS.  Aut/Gal, H-perp, low-degree enumeration and all
# later expensive source blocks are intentionally excluded.
k_start = full_source.index(K_START)
k_end = full_source.index(K_END, k_start)
k_core = full_source[k_start:k_end]
source_slice = surface_core + "\n" + k_core
for forbidden in ("CloseVectors(", "SmithForm(", "Setting up the action of Aut and Gal on Pic(K)"):
    if forbidden in source_slice:
        raise SystemExit(f"Goal4AE source slice unexpectedly contains heavy block: {forbidden}")
for required in (
    "function imageinPic(C)",
    "function imageinPicK(C)",
    "PicKtoPicS := hom<PicK -> Pic",
    "assert MatKtoS*MatStoK eq 2*IdentityMatrix(Integers(), 20);",
):
    if required not in source_slice:
        raise SystemExit(f"Goal4AE source slice lost required construction: {required}")

extra = r'''
// Stage35-EX Goal4AE: materialize the eight sign-labelled C5 pair pullbacks.
// For fixed (e1,e2,e3), the e4=+/- C5 curves have the same image on K.
// Pulling that K curve back by the pinned PicKtoPicS map gives the exact pair
// class on the minimal resolution, including exceptional total-transform terms.
indMat35 := Matrix(Rationals(), [Eltseq(qPic(Big.j)) : j in indlist]);
indInv35 := indMat35^-1;
for e1 in [1,-1] do
  for e2 in [1,-1] do
    for e3 in [1,-1] do
      Cp35 := Curve(ReducedSubscheme(Scheme(S, [
        a1+e2*a2+e3*a3+i*c,
        (e2*a2+e3*a3)*b1+e1*i*b2*b3
      ])));
      Cm35 := Curve(ReducedSubscheme(Scheme(S, [
        a1+e2*a2+e3*a3-i*c,
        (e2*a2+e3*a3)*b1+e1*i*b2*b3
      ])));
      Kp35 := proj(Cp35);
      Km35 := proj(Cm35);
      assert Kp35 eq Km35;
      vKL35 := imageinPicK(Kp35);
      vK35 := PicK!Eltseq(vKL35);
      vS35 := PicKtoPicS(vK35);
      vSL35 := PicL!vS35;
      assert (vSL35, HinPicL) eq 16;
      assert (vSL35, vSL35) eq -4;
      xq35 := Vector(Rationals(), Eltseq(vS35))*indInv35;
      assert forall{q : q in Eltseq(xq35) | Denominator(q) eq 1};
      xi35 := [Integers()!q : q in Eltseq(xq35)];
      assert &+[xi35[j]*qPic(Big.indlist[j]) : j in [1..64]] eq vS35;
      printf "GOAL4AE_ROW=%o|%o|%o|%o|%o|%o\n",
        e1,e2,e3,Eltseq(vK35),Eltseq(vS35),xi35;
    end for;
  end for;
end for;
printf "GOAL4AE_DONE\n";
'''
code = "SetColumns(0);\nquick := true;\n" + source_slice + "\n" + extra
stdout, magma_attempt = run_magma(
    code,
    300,
    "Stage35-EX Goal4AE sliced C5 PicK-to-PicS extraction",
    user_agent="perfect-cuboid-stage35ex/4ae-g2",
)
if "GOAL4AE_DONE" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout)
    raise SystemExit("Goal4AE Magma extraction failed")
rows = parse_rows(stdout)
if len(rows) != 8:
    print(stdout)
    raise SystemExit(f"expected 8 C5 pair rows, got {len(rows)}")
if sorted(tuple(r["sign_triple"]) for r in rows) != sorted((e1,e2,e3) for e1 in (1,-1) for e2 in (1,-1) for e3 in (1,-1)):
    raise SystemExit("C5 sign-triple coverage regression")
for r in rows:
    if len(r["PicK_basis_coordinates_20"]) != 20:
        raise SystemExit("PicK row width regression")
    if len(r["PicS_historical_Magma_coordinates_64"]) != 64 or len(r["PicS_INDLIST_coordinates_64"]) != 64:
        raise SystemExit("PicS row width regression")

# Independent local replay of the S-side lattice invariants in the retained
# primitive INDLIST basis.  Large retained payloads remain runner-side behind
# the established Stage33 adapter and are not copied into this certificate.
rec = runpy.run_path(str(REC))
gram = [[int(x) for x in row] for row in rec["gram"]]
hyperplane = [int(x) for x in rec["hyperplane"]]
by_sign = {tuple(r["sign_triple"]): r for r in rows}
for t, r in by_sign.items():
    v = r["PicS_INDLIST_coordinates_64"]
    if pair(v, hyperplane, gram) != 16:
        raise SystemExit(f"C5 pair degree regression at {t}")
    if pair(v, v, gram) != -4:
        raise SystemExit(f"C5 pair square regression at {t}")
    anti = tuple(-x for x in t)
    if add(v, by_sign[anti]["PicS_INDLIST_coordinates_64"]) != scale(2, hyperplane):
        raise SystemExit(f"antipodal quadratic-section relation regression at {t}")
if len({tuple(r["PicS_INDLIST_coordinates_64"]) for r in rows}) != 8:
    raise SystemExit("C5 pair Picard orbit collapsed")

# Goal4AC chose e1=+1 as each quadratic-section representative.  Its residual
# pair is the antipodal triple, hence exactly the four e1=-1 rows.
residual = []
for e2 in (1,-1):
    for e3 in (1,-1):
        chosen = (1,e2,e3)
        anti = (-1,-e2,-e3)
        residual.append({
            "chosen_section_representative": list(chosen),
            "residual_antipodal_pair": list(anti),
            "PicS_INDLIST_coordinates_64": by_sign[anti]["PicS_INDLIST_coordinates_64"],
        })
if len(residual) != 4:
    raise SystemExit("residual pair selection regression")

out = {
    "schema": "STAGE35_EX_35_GOAL4AE_C5_DIRECT_PICK_TO_PICS_INDLIST64_V1",
    "stage": "35-EX",
    "unit": "35EX-35_GOAL4AE_SECOND_CLASS_QI_CYCLIC_C5_DIRECT_PicK_TO_PicS_INDLIST64_EXTRACTION_PREFLIGHT",
    "status": "EXPLORATORY_EXACT_NUMERIC_SOURCE_EXTRACTION_PENDING_PROMOTION_AND_HOSTILE_AUDIT_NO_E1_CREDIT",
    "source_locks": {
        "goal4ad_blob_sha1": GOAL4AD_BLOB,
        "upstream_stoll_git_blob_sha1": SOURCE_BLOB,
        "stage33_marked_source_sha256": MARKED_SHA256,
        "stage33_INDLIST_1based": INDLIST,
        "stage33_source_helper_blob_sha1": git_blob(S33_07 / "stoll_cuboid_source.py"),
        "stage33_known140_reconstruction_blob_sha1": git_blob(REC),
        "surface_core_sha256": hashlib.sha256(surface_core.encode()).hexdigest(),
        "k_picard_core_sha256": hashlib.sha256(k_core.encode()).hexdigest(),
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    },
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": magma_attempt,
        "remote_cas_used": True,
        "remote_cas_role": "evaluate the pinned source C5 projection through imageinPicK and PicKtoPicS and emit exact integral coordinates",
        "source_slice_used": True,
        "submitted_magma_code_bytes": len(code.encode()),
        "excluded_heavy_source_blocks": ["AutGal_S", "AutGal_K", "Hperp_low_degree_enumeration", "SmithForm", "CloseVectors"],
        "bounded_single_job": True,
        "raw_large_artifact_persisted": False,
    },
    "c5_pair_rows": rows,
    "exact_checks": {
        "sign_label_count": 8,
        "all_rows_integral": True,
        "all_rows_distinct": True,
        "PicK_rank": 20,
        "PicS_rank": 64,
        "PicS_pair_degree": 16,
        "PicS_pair_self_intersection": -4,
        "antipodal_pair_sum_equals_2H_for_all_8_labels": True,
        "Goal4AC_residual_pair_count": 4,
    },
    "goal4ac_residual_pairs": residual,
    "semantic_firewall": {
        "target_span_with_C5_pairs_computed": False,
        "explicit_F_B_computed": False,
        "full_Br_a_U_computed": False,
        "local_evaluations_computed": False,
        "brauer_manin_obstruction_obtained": False,
        "E1_proved": False,
        "R29_PESCH_E1_closed": False,
        "R29_FIB2_closed": False,
        "stage35_closed": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print("PASS Stage35-EX Goal4AE probe: 8 labelled C5 pair PicK/PicS rows materialized; four Goal4AC residual pair INDLIST64 rows selected")
print("CERTIFICATE_SHA256=" + out["canonical_sha256"])
