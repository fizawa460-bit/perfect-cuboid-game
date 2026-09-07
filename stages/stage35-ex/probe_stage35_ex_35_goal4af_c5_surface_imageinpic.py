#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
S33_07 = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(S33_07))

from stoll_cuboid_source import load_pinned_source, run_magma  # type: ignore

REC = S33_07 / "certify_two_coordinate_swap_picard_rows.py"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,
    93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,
    117,118,119,120,121,125,126,127,129,133,135,
]


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def add(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b)]


def scale(k: int, a: list[int]) -> list[int]:
    return [k * x for x in a]


def row_times_matrix(row: list[int], matrix: list[list[int]]) -> list[int]:
    return [sum(row[k] * matrix[k][j] for k in range(len(row))) for j in range(len(matrix[0]))]


def mm(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    bt = list(zip(*b))
    return [[sum(x*y for x,y in zip(r,c)) for c in bt] for r in a]


def pair(u: list[int], v: list[int], gram: list[list[int]]) -> int:
    return sum(u[i] * gram[i][j] * v[j] for i in range(64) for j in range(64))


def parse_rows(stdout: str) -> list[dict]:
    rows = []
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("GOAL4AF_C5_ROW="):
            continue
        payload = line.split("=", 1)[1]
        e1s,e2s,e3s,e4s,vecs = payload.split("|", 4)
        vec = [int(x) for x in ast.literal_eval(vecs)]
        rows.append({"sign_quadruple":[int(e1s),int(e2s),int(e3s),int(e4s)],"PicS_INDLIST_coordinates_64":vec})
    return rows


full_source, surface_core, upstream_blob, source_attempt = load_pinned_source()
if upstream_blob != SOURCE_BLOB:
    raise SystemExit("pinned upstream source blob moved")
for needle in (
    "Genus 3 nonhyperelliptic curves of degree 8",
    "function imageinPic(C)",
    "indlist := [",
):
    if needle not in full_source:
        raise SystemExit(f"pinned source semantic regression: {needle}")
if "function imageinPic(C)" not in surface_core:
    raise SystemExit("surface core lost direct imageinPic")
if "Now repeat this for the K3 quotient" in surface_core:
    raise SystemExit("Goal4AF surface core unexpectedly contains K3 quotient block")

extra = r'''
// Stage35-EX Goal4AF: direct S-side C5 -> imageinPic -> primitive indlist64.
indMat35 := Matrix(Rationals(), [Eltseq(qPic(Big.j)) : j in indlist]);
indInv35 := indMat35^-1;
for e1 in [1,-1] do
  for e2 in [1,-1] do
    for e3 in [1,-1] do
      for e4 in [1,-1] do
        C35 := Curve(ReducedSubscheme(Scheme(S, [
          a1+e2*a2+e3*a3+e4*i*c,
          (e2*a2+e3*a3)*b1+e1*i*b2*b3
        ])));
        assert Degree(C35) eq 8;
        v35 := Pic!imageinPic(C35);
        xq35 := Vector(Rationals(), Eltseq(v35))*indInv35;
        assert forall{q : q in Eltseq(xq35) | Denominator(q) eq 1};
        xi35 := [Integers()!q : q in Eltseq(xq35)];
        assert &+[xi35[j]*qPic(Big.indlist[j]) : j in [1..64]] eq v35;
        printf "GOAL4AF_C5_ROW=%o|%o|%o|%o|%o\n", e1,e2,e3,e4,xi35;
      end for;
    end for;
  end for;
end for;
printf "GOAL4AF_C5_DONE\n";
'''
code = "SetColumns(0);\nquick := true;\n" + surface_core + "\n" + extra
stdout, magma_attempt = run_magma(
    code,
    240,
    "Stage35-EX Goal4AF direct S C5 imageinPic extraction",
    user_agent="perfect-cuboid-stage35ex/4af-g1",
)
if "GOAL4AF_C5_DONE" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout)
    raise SystemExit("Goal4AF direct S imageinPic extraction failed")
rows = parse_rows(stdout)
if len(rows) != 16:
    print(stdout)
    raise SystemExit(f"expected 16 individual C5 rows, got {len(rows)}")
expected = {(e1,e2,e3,e4) for e1 in (1,-1) for e2 in (1,-1) for e3 in (1,-1) for e4 in (1,-1)}
by_sign = {tuple(r["sign_quadruple"]): r["PicS_INDLIST_coordinates_64"] for r in rows}
if set(by_sign) != expected or any(len(v) != 64 for v in by_sign.values()):
    raise SystemExit("C5 sign coverage/width regression")

# Independent exact runner-side replay in the retained primitive INDLIST basis.
rec = runpy.run_path(str(REC))
if list(rec["INDLIST"]) != INDLIST:
    raise SystemExit("Stage33 primitive INDLIST order moved")
gram = [[int(x) for x in r] for r in rec["gram"]]
hyperplane = [int(x) for x in rec["hyperplane"]]
known = [[int(x) for x in r] for r in rec["known"]]
actions = []
for p in rec["perms"]:
    actions.append([known[int(p[j-1])-1] for j in INDLIST])
I = [[int(i==j) for j in range(64)] for i in range(64)]
signc = I
for A in actions[3:9]:
    signc = mm(signc, A)
contracted = known[116:140]
if len(contracted) != 24:
    raise SystemExit("contracted exceptional packet regression")

individual_squares = set()
individual_exceptional_hist = {}
for t,v in by_sign.items():
    if pair(v, hyperplane, gram) != 8:
        raise SystemExit(f"individual C5 degree regression at {t}")
    individual_squares.add(pair(v,v,gram))
    mate = (t[0],t[1],t[2],-t[3])
    if row_times_matrix(v,signc) != by_sign[mate]:
        raise SystemExit(f"sigma_c/e4 sign transport regression at {t}")
    inc = tuple(pair(v,E,gram) for E in contracted)
    if any(x < 0 for x in inc):
        raise SystemExit(f"negative contracted-exceptional incidence at {t}")
    key = tuple(sorted(set(inc)))
    individual_exceptional_hist[str(t)] = {str(x):inc.count(x) for x in sorted(set(inc))}

pairs = []
pair_by_triple = {}
for e1 in (1,-1):
    for e2 in (1,-1):
        for e3 in (1,-1):
            triple = (e1,e2,e3)
            cp = by_sign[(e1,e2,e3,1)]
            cm = by_sign[(e1,e2,e3,-1)]
            strict = add(cp,cm)
            coeff = [pair(cp,E,gram) for E in contracted]
            correction = [0]*64
            for m,E in zip(coeff,contracted):
                if m:
                    correction = add(correction,scale(m,E))
            total = add(strict,correction)
            if row_times_matrix(total,signc) != total:
                raise SystemExit(f"total C5 pair is not sigma_c-fixed at {triple}")
            if any(pair(total,E,gram) != 0 for E in contracted):
                raise SystemExit(f"Lemma11 pullback orthogonality regression at {triple}")
            if pair(total,hyperplane,gram) != 16:
                raise SystemExit(f"total C5 pair degree regression at {triple}")
            row = {
                "sign_triple":list(triple),
                "strict_pair_INDLIST64":strict,
                "contracted_exceptional_coefficients_24":coeff,
                "total_pullback_pair_INDLIST64":total,
                "strict_pair_square":pair(strict,strict,gram),
                "total_pullback_pair_square":pair(total,total,gram),
            }
            pairs.append(row)
            pair_by_triple[triple] = total

# Goal4AC quadratic section: t and -t are the two sigma_c-pairs in the same
# scalar quadratic factor; total transforms must sum to the complete 2H divisor.
for t,total in pair_by_triple.items():
    anti = tuple(-x for x in t)
    if add(total,pair_by_triple[anti]) != scale(2,hyperplane):
        raise SystemExit(f"antipodal total-pair sum != 2H at {t}")

residual = []
for e2 in (1,-1):
    for e3 in (1,-1):
        chosen=(1,e2,e3)
        anti=(-1,-e2,-e3)
        residual.append({
            "chosen_section_representative":list(chosen),
            "residual_antipodal_pair":list(anti),
            "total_pullback_pair_INDLIST64":pair_by_triple[anti],
        })

summary = {
    "schema":"STAGE35_EX_GOAL4AF_DIRECT_SURFACE_C5_IMAGEINPIC_DIAGNOSTIC_V1",
    "source_blob_sha1":SOURCE_BLOB,
    "surface_core_sha256":hashlib.sha256(surface_core.encode()).hexdigest(),
    "submitted_magma_code_sha256":hashlib.sha256(code.encode()).hexdigest(),
    "submitted_magma_code_bytes":len(code.encode()),
    "source_fetch_attempt":source_attempt,
    "magma_request_attempt":magma_attempt,
    "individual_C5_count":16,
    "individual_C5_squares":sorted(individual_squares),
    "individual_contracted_exceptional_histograms":individual_exceptional_hist,
    "pair_count":8,
    "pair_rows":pairs,
    "goal4ac_residual_pair_count":4,
    "goal4ac_residual_pairs":residual,
    "antipodal_total_pair_sum_equals_2H":True,
    "remote_cas_used":True,
    "target_span_computed":False,
    "theorem_credit":False,
    "endpoint_credit":False,
}
print("GOAL4AF_DIAGNOSTIC_JSON=" + json.dumps(summary,sort_keys=True,separators=(",",":")))
