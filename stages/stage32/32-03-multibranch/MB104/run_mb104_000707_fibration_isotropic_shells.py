#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEGACY = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(LEGACY))

from stoll_cuboid_source import run_magma  # noqa: E402
from stage32_picard_marking_retained import load as load_marking  # noqa: E402
from picard_base_rows_retained import load as load_picard_base  # noqa: E402

SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
PICARD_MARKING_BLOB = "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
PICARD_BASE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
HPERP_ADAPTER_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
PICARD_CORE_SHA256 = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
HPERP_TEXT_SHA256 = "af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f"
PICARD_BASE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"

SUPPORT = {
    "mask": "000707000f0f",
    "orbit_size": 768,
    "compact_indices_0based": [0, 1, 2, 3, 8, 9, 10, 11, 24, 25, 26, 32, 33, 34],
}
COMPACT_TO_STOLL = [
    24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,
    25,32,26,31,30,27,29,28,33,40,34,39,38,35,37,36,41,48,42,47,46,43,45,44,
]
SUPPORT_STOLL = [COMPACT_TO_STOLL[i] for i in SUPPORT["compact_indices_0based"]]
RETAINED_BASIS_KNOWN_LABELS_1BASED = [
    1,33,12,16,7,90,87,92,51,40,77,44,20,55,19,56,
    123,118,73,117,119,122,120,121,94,96,79,95,99,75,24,98,
    132,26,125,126,128,127,129,130,108,107,52,18,11,102,3,106,
    136,137,134,139,140,133,6,135,112,110,113,115,116,114,109,111,
]
SHELLS = [
    {"degree": 10, "p_intersection": 30, "support_mass": 10, "scale_a": 8, "scale_b": 5, "hperp_norm": 400},
    {"degree": 10, "p_intersection": 34, "support_mass": 9, "scale_a": 8, "scale_b": 5, "hperp_norm": 400},
    {"degree": 10, "p_intersection": 38, "support_mass": 8, "scale_a": 8, "scale_b": 5, "hperp_norm": 400},
    {"degree": 12, "p_intersection": 36, "support_mass": 12, "scale_a": 4, "scale_b": 3, "hperp_norm": 144},
]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _magma_matrix(rows: list[list[int]]) -> str:
    n = len(rows)
    m = len(rows[0])
    assert all(len(r) == m for r in rows)
    flat = ",".join(str(v) for row in rows for v in row)
    return f"Matrix(Integers(),{n},{m},[{flat}])"


def load_retained_numeric() -> tuple[list[list[int]], list[int], list[list[int]], list[list[int]], dict]:
    marking = load_marking()
    assert marking["stage32_picard_core_sha256"] == PICARD_CORE_SHA256
    text = marking["hperp_text"]
    assert hashlib.sha256(text.encode()).hexdigest() == HPERP_TEXT_SHA256
    lines = text.splitlines()
    assert lines[0] == "S32_D16_AUT_CANON_HPERP_V1"
    assert lines[1] == PICARD_CORE_SHA256
    assert lines[2] == SOURCE_BLOB
    n, m = map(int, lines[4].split())
    assert (n, m) == (63, 140)
    q = [list(map(int, lines[5+i].split())) for i in range(63)]
    records = [list(map(int, lines[68+i].split())) for i in range(140)]
    assert all(len(r) == 65 for r in records)
    degree = [r[0] for r in records]
    linear = [r[2:] for r in records]

    base = load_picard_base()
    assert base["canonical_sha256"] == PICARD_BASE_CANONICAL
    assert base["upstream_git_blob_sha1"] == SOURCE_BLOB
    gram = [[int(v) for v in row] for row in base["picard_gram_64x64"]]
    assert len(gram) == 64 and all(len(r) == 64 for r in gram)
    assert len(RETAINED_BASIS_KNOWN_LABELS_1BASED) == 64
    assert len(set(RETAINED_BASIS_KNOWN_LABELS_1BASED)) == 64

    meta = {
        "hperp_text_sha256": HPERP_TEXT_SHA256,
        "picard_base_canonical": PICARD_BASE_CANONICAL,
        "compact_to_stoll_provenance_runs": [35501980795, 35502636705],
        "retained_basis_label_source_blob": HPERP_ADAPTER_BLOB,
    }
    return q, degree, linear, gram, meta


def build_fast_code() -> str:
    q, degree, linear, gram, _ = load_retained_numeric()
    shell_records = "[" + ",".join(
        "<%d,%d,%d,%d,%d,%d>" % (
            sh["degree"], sh["p_intersection"], sh["support_mass"],
            sh["scale_a"], sh["scale_b"], sh["hperp_norm"],
        )
        for sh in SHELLS
    ) + "]"
    support_rows = [92 + j for j in SUPPORT_STOLL]
    return f"""
SetColumns(0);
Q := {_magma_matrix(q)};
Lin := {_magma_matrix(linear)};
G := {_magma_matrix(gram)};
Deg := {degree};
basisLabels := {RETAINED_BASIS_KNOWN_LABELS_1BASED};
compactToPts := {COMPACT_TO_STOLL};
supportPts := {SUPPORT_STOLL};
supportRows := {support_rows};
assert Nrows(Q) eq 63 and Ncols(Q) eq 63;
assert Nrows(Lin) eq 140 and Ncols(Lin) eq 63;
assert Nrows(G) eq 64 and Ncols(G) eq 64;
assert #Deg eq 140;
assert #basisLabels eq 64 and #Seqset(basisLabels) eq 64;
assert #compactToPts eq 48 and Seqset(compactToPts) eq Seqset([1..48]);
assert #supportPts eq 14 and #Seqset(supportPts) eq 14;
printf "FIBSHELL_MAP=%o\n", compactToPts;
printf "FIBSHELL_SUPPORT_PTS=%o\n", supportPts;

HMod := RSpace(Integers(),63);
LH := LatticeWithGram(Q);
prow := [-4*&+[Lin[r,j] : r in supportRows] : j in [1..63]];
KP := Kernel(Transpose(Matrix(Integers(),1,63,prow)));
assert Dimension(KP) eq 62;
BKP := BasisMatrix(KP);
QKP := BKP*Q*Transpose(BKP);
LKP := LatticeWithGram(QKP);
KPMod := RSpace(Integers(),62);
KPtoH := hom<KPMod -> HMod | Basis(KP)>;
ARat := ChangeRing(QKP,Rationals());
Ginv := ChangeRing(G,Rationals())^-1;
pairingGcd := GCD([Abs(Integers()!z) : z in prow | z ne 0]);
assert pairingGcd gt 0;

function BezoutSolution(row,target)
  coeff := [Integers()!0 : j in [1..#row]];
  g := Integers()!0;
  for j in [1..#row] do
    a := Integers()!row[j];
    if a ne 0 then
      if g eq 0 then
        g := Abs(a);
        coeff[j] := a div g;
      else
        gg,s,t := Xgcd(g,a);
        coeff := [s*x : x in coeff];
        coeff[j] +:= t;
        g := gg;
      end if;
    end if;
  end for;
  assert g gt 0 and target mod g eq 0;
  coeff := [(target div g)*x : x in coeff];
  assert &+[coeff[j]*row[j] : j in [1..#row]] eq target;
  return coeff,g;
end function;

shells := {shell_records};
for sh in shells do
  e := sh[1]; pf := sh[2]; expectedM := sh[3];
  aa := sh[4]; bb := sh[5]; nrm := sh[6];
  pc := aa*pf - bb*112;
  if pc mod pairingGcd ne 0 then
    printf "FIBSHELL_SHELL|%o|%o|%o|%o|%o|%o|%o|0|0|0|0\n",
           e,pf,expectedM,aa,bb,nrm,pc;
    continue;
  end if;

  vseq,pgcd := BezoutSolution(prow,pc);
  assert pgcd eq pairingGcd;
  vH := HMod!vseq;
  vLH := LH!Eltseq(vH);
  cross := Vector(Rationals(),[
    Rationals()!(LH!Eltseq(KPtoH(KPMod.j)),vLH) : j in [1..62]
  ]);
  center := -cross*(ARat^-1);
  proj := -&+[cross[j]*center[j] : j in [1..62]];
  qmin := Rationals()!(vLH,vLH) - proj;
  distq := Rationals()!nrm - qmin;

  den := Integers()!1;
  for z in Eltseq(center) do den := LCM(den,Denominator(z)); end for;
  den := LCM(den,Denominator(qmin));
  targetCoords := [Integers()!(den*center[j]) : j in [1..62]];
  targetL := LKP!targetCoords;

  rawCount := 0; integralCount := 0; nonnegCount := 0;
  candSeqs := [];
  if distq ge 0 then
    scaledDistQ := den^2*distq;
    assert Denominator(scaledDistQ) eq 1;
    scaledDist := Integers()!scaledDistQ;
    clv := CloseVectors(den*LKP,targetL,scaledDist,scaledDist);
    rawCount := #clv;
    for cv in clv do
      zL := LKP!(1/den*cv[1]);
      zK := KPMod!Eltseq(zL);
      xH := vH + KPtoH(zK);
      xseq := [Integers()!z : z in Eltseq(xH)];
      xLH := LH!xseq;
      assert (xLH,xLH) eq nrm;
      assert &+[prow[j]*xseq[j] : j in [1..63]] eq pc;

      nums := [
        &+[Lin[r,j]*xseq[j] : j in [1..63]] + bb*Deg[r]
        : r in [1..140]
      ];
      if forall{{r : r in [1..140] | nums[r] mod aa eq 0}} then
        allpairs := [nums[r] div aa : r in [1..140]];
        bp := Vector(Rationals(),[allpairs[basisLabels[j]] : j in [1..64]]);
        fRat := bp*Ginv;
        if forall{{z : z in Eltseq(fRat) | Denominator(z) eq 1}} then
          integralCount +:= 1;
          fseq := [Integers()!z : z in Eltseq(fRat)];
          fsq := &+[fseq[a]*G[a,b]*fseq[b] : a,b in [1..64]];
          assert fsq eq 0;
          msum := &+[allpairs[92+j] : j in supportPts];
          assert msum eq expectedM;
          assert 7*e - 4*msum eq pf;
          if Min(allpairs) ge 0 then
            nonnegCount +:= 1;
            g := GCD([Abs(z) : z in fseq]);
            if g eq 1 and not fseq in candSeqs then
              Append(~candSeqs,fseq);
              zeros := [r : r in [1..140] | allpairs[r] eq 0];
              printf "FIBSHELL_KEEP|%o|%o|%o|%o|%o|%o\n",
                     e,pf,expectedM,Min(allpairs),zeros,fseq;
            end if;
          end if;
        end if;
      end if;
    end for;
  end if;
  printf "FIBSHELL_SHELL|%o|%o|%o|%o|%o|%o|%o|%o|%o|%o|%o\n",
         e,pf,expectedM,aa,bb,nrm,pc,rawCount,integralCount,nonnegCount,#candSeqs;
end for;
printf "FIBSHELL_KERNEL_RANK=62\n";
printf "FIBSHELL_DONE\n";
"""


def parse_run(stdout: str, code_sha: str, magma_attempt: int) -> dict:
    def grab(name: str):
        m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
        if not m:
            raise SystemExit(f"missing Magma output {name}")
        return ast.literal_eval(m.group(1))

    if "FIBSHELL_DONE" not in stdout:
        print(stdout)
        raise SystemExit("missing FIBSHELL_DONE")
    if any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
        print(stdout)
        raise SystemExit("Magma failure")

    mapping = [int(x) for x in grab("FIBSHELL_MAP")]
    support_pts = [int(x) for x in grab("FIBSHELL_SUPPORT_PTS")]
    if mapping != COMPACT_TO_STOLL:
        raise SystemExit("compact-to-Stoll retained map regression")
    if support_pts != SUPPORT_STOLL:
        raise SystemExit("support Stoll-point retained map regression")

    rows: dict[tuple[int, int], dict] = {}
    shell_re = re.compile(
        r"^FIBSHELL_SHELL\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(-?\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)$",
        re.M,
    )
    for m in shell_re.finditer(stdout):
        e,pf,sm,aa,bb,nrm,pc,raw,integral,nef,kept = map(int,m.groups())
        rows[(e,pf)] = {
            "degree":e, "p_intersection":pf, "support_mass":sm,
            "scale_a":aa, "scale_b":bb, "hperp_norm":nrm,
            "hperp_p_pairing":pc,
            "raw_affine_close_vector_count":raw,
            "integral_picard_class_count":integral,
            "known140_nonnegative_count":nef,
            "primitive_known140_nonnegative_candidate_count":kept,
            "primitive_known140_nonnegative_candidates":[],
        }

    keep_re = re.compile(
        r"^FIBSHELL_KEEP\|(\d+)\|(\d+)\|(\d+)\|(-?\d+)\|(\[[^\n]*\])\|(\[[^\n]*\])$",
        re.M,
    )
    for m in keep_re.finditer(stdout):
        e,pf,sm,minpair,zeros_s,coords_s = m.groups()
        row = rows[(int(e),int(pf))]
        if row["support_mass"] != int(sm):
            raise SystemExit("support-mass mismatch in keep row")
        coords = [int(x) for x in ast.literal_eval(coords_s)]
        zeros = [int(x) for x in ast.literal_eval(zeros_s)]
        if len(coords) != 64:
            raise SystemExit("Picard coordinate length mismatch")
        row["primitive_known140_nonnegative_candidates"].append({
            "picard_basis_coordinates":coords,
            "minimum_known140_pairing":int(minpair),
            "zero_known140_indices_1based":zeros,
        })

    expected = {(sh["degree"],sh["p_intersection"]) for sh in SHELLS}
    if set(rows) != expected:
        raise SystemExit(f"shell coverage mismatch: {sorted(rows)}")
    for row in rows.values():
        if row["primitive_known140_nonnegative_candidate_count"] != len(row["primitive_known140_nonnegative_candidates"]):
            raise SystemExit("candidate count mismatch")
        if not (
            row["raw_affine_close_vector_count"] >= row["integral_picard_class_count"]
            >= row["known140_nonnegative_count"]
            >= row["primitive_known140_nonnegative_candidate_count"]
        ):
            raise SystemExit("filter counts are not monotone")

    ordered = [rows[(sh["degree"],sh["p_intersection"])] for sh in SHELLS]
    return {
        "mask":SUPPORT["mask"],
        "orbit_size":SUPPORT["orbit_size"],
        "compact_indices_0based":SUPPORT["compact_indices_0based"],
        "compact_to_stoll_pts_1based":mapping,
        "support_stoll_pts_1based":support_pts,
        "kernel_rank":62,
        "submitted_magma_code_sha256":code_sha,
        "magma_request_attempt":magma_attempt,
        "raw_stdout_sha256":hashlib.sha256(stdout.encode()).hexdigest(),
        "shells":ordered,
    }


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    ap.add_argument("--timeout",type=int,default=1800)
    args=ap.parse_args()

    _,_,_,_,retained_meta = load_retained_numeric()
    code = build_fast_code()
    code_sha = hashlib.sha256(code.encode()).hexdigest()
    stdout,magma_attempt = run_magma(
        code,args.timeout,
        "Stage32 MB104 000707 retained-Hperp degree10/12 fibration shells",
        user_agent="perfect-cuboid-stage32mb/1.1-000707-retained-hperp-shells",
    )
    support_result = parse_run(stdout,code_sha,magma_attempt)

    total_candidates=sum(sh["primitive_known140_nonnegative_candidate_count"] for sh in support_result["shells"])
    deg10_candidates=sum(sh["primitive_known140_nonnegative_candidate_count"] for sh in support_result["shells"] if sh["degree"]==10)
    deg12_candidates=sum(sh["primitive_known140_nonnegative_candidate_count"] for sh in support_result["shells"] if sh["degree"]==12)

    out={
        "schema":"STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_V1",
        "status":"PRE_AUDIT_EXACT_FINITE_PICARD64_NUMERICAL_CANDIDATES_NO_CREDIT",
        "source_locks":{
            "stoll_repository":"MichaelStollBayreuth/Verification",
            "stoll_commit":"51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
            "stoll_cuboids_blob":SOURCE_BLOB,
            "stage33_stoll_helper_blob":"010db3767b8f932c71ac5722b50ccb64a8c79f9d",
            "stage33_picard_marking_blob":PICARD_MARKING_BLOB,
            "stage33_picard_base_rows_blob":PICARD_BASE_BLOB,
            "hperp_integral_adapter_blob":HPERP_ADAPTER_BLOB,
            "stage32_picard_core_sha256":PICARD_CORE_SHA256,
            "retained_hperp_text_sha256":HPERP_TEXT_SHA256,
            "retained_picard_base_canonical":PICARD_BASE_CANONICAL,
            "parent_engine":"retained Hperp affine-shell engine; no geometry reconstruction",
        },
        "mathematical_scope":{
            "support_mask":SUPPORT["mask"],
            "P":"7H-4*sum_{i in support}E_i",
            "P2":336,
            "H_dot_P":112,
            "degree10":{
                "H_dot_F":10,"F2":0,"P_dot_F_values":[30,34,38],
                "support_mass_values":[10,9,8],"hperp_transform":"x=8F-5H","minus_x2":400,
            },
            "degree12":{
                "H_dot_F":12,"F2":0,"P_dot_F_values":[36],
                "support_mass_values":[12],"hperp_transform":"y=4F-3H","minus_y2":144,
            },
            "filters":[
                "Picard64 integrality of F via retained basis Gram inverse",
                "nonnegative intersection with all known 140 curves via retained Hperp affine pairings",
                "primitive integral Picard class",
            ],
        },
        "execution":{
            "source_fetch_attempt":0,
            "support_request_count":1,
            "shell_count":len(SHELLS),
            "rank_before_P_pairing_reduction":63,
            "rank_after_P_pairing_reduction":62,
            "max_hperp_norm":max(sh["hperp_norm"] for sh in SHELLS),
            "raw_artifact_persisted":False,
            "geometry_reconstruction_skipped":True,
            "retained_numeric_input":retained_meta,
        },
        "support":support_result,
        "summary":{
            "degree10_primitive_known140_nonnegative_candidate_count":deg10_candidates,
            "degree12_primitive_known140_nonnegative_candidate_count":deg12_candidates,
            "total_primitive_known140_nonnegative_candidate_count":total_candidates,
            "fibration_improvement_shells_numerically_empty_candidate":total_candidates==0,
            "geometric_effectivity_or_semiampleness_proved":False,
            "global_min_P_dot_F_40_proved":False,
        },
        "next_geometry_if_candidates_remain":{
            "degree10":"reducible sextic residual: quartic+conic or conic+conic+conic, plus exceptional components",
            "degree12":"QA+QB+degree4 residual singular-fiber geometry, plus exceptional components",
        },
        "credit_firewall":{
            "numerical_fibration_shell_credit":False,
            "effectivity_credit":False,
            "semiampleness_credit":False,
            "global_fibration_optimum_credit":False,
            "MB104_complete":False,
            "receiver_credit":False,
            "theorem_credit":False,
            "endpoint_credit":False,
            "merge_authorized":False,
        },
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({
        "success":True,
        "canonical":out["canonical_sha256_without_this_field"],
        "degree10_candidates":deg10_candidates,
        "degree12_candidates":deg12_candidates,
        "total_candidates":total_candidates,
    },sort_keys=True))


if __name__=="__main__":
    main()
