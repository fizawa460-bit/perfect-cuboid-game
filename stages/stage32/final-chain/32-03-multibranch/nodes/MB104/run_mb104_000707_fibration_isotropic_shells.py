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

from stoll_cuboid_source import load_pinned_source, run_magma  # noqa: E402

SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
PICARD_MARKING_BLOB = "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
PICARD_CORE_SHA256 = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"

SUPPORT = {
    "mask": "000707000f0f",
    "orbit_size": 768,
    "compact_indices_0based": [0, 1, 2, 3, 8, 9, 10, 11, 24, 25, 26, 32, 33, 34],
}

SHELLS = [
    {"degree": 10, "p_intersection": 30, "support_mass": 10, "scale_a": 8, "scale_b": 5, "hperp_norm": 400},
    {"degree": 10, "p_intersection": 34, "support_mass": 9, "scale_a": 8, "scale_b": 5, "hperp_norm": 400},
    {"degree": 10, "p_intersection": 38, "support_mass": 8, "scale_a": 8, "scale_b": 5, "hperp_norm": 400},
    {"degree": 12, "p_intersection": 36, "support_mass": 12, "scale_a": 4, "scale_b": 3, "hperp_norm": 144},
]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def build_extra() -> str:
    compact = [i + 1 for i in SUPPORT["compact_indices_0based"]]
    shell_records = "[" + ",".join(
        "<%d,%d,%d,%d,%d,%d>" % (
            sh["degree"],
            sh["p_intersection"],
            sh["support_mass"],
            sh["scale_a"],
            sh["scale_b"],
            sh["hperp_norm"],
        )
        for sh in SHELLS
    ) + "]"
    return f"""
assert #pts eq 48;
assert #Cs eq 92;
assert bdim eq 140;

// Rebuild the current compact 48-node ordering over the exact Stoll field.
compact := [];
for j in [1..3] do
  for sa in [1,-1] do
    for s1 in [1,-1] do
      for s2 in [1,-1] do
        x := [L!0 : k in [1..7]];
        x[j] := L!sa;
        q := [k : k in [1..3] | k ne j];
        x[3+q[1]] := L!s1;
        x[3+q[2]] := L!s2;
        x[7] := L!1;
        Append(~compact, Pr6!x);
      end for;
    end for;
  end for;
end for;
for j in [1..3] do
  q := [k : k in [1..3] | k ne j];
  aa := q[1]; bb := q[2];
  for sr in [1,-1] do
    for ep in [1,-1] do
      for eq in [1,-1] do
        x := [L!0 : k in [1..7]];
        x[aa] := L!1;
        x[bb] := i*sr;
        x[3+aa] := i*ep;
        x[3+bb] := -eq*sr;
        Append(~compact, Pr6!x);
      end for;
    end for;
  end for;
end for;
assert #compact eq 48;

compactToPts := [];
for cp in compact do
  hits := [j : j in [1..#pts] | pts[j] eq cp];
  assert #hits eq 1;
  Append(~compactToPts, hits[1]);
end for;
assert #Seqset(compactToPts) eq 48;
printf "FIBSHELL_MAP=%o\\n", compactToPts;

supportCompact := {compact};
supportPts := [compactToPts[j] : j in supportCompact];
assert #supportPts eq 14 and #Seqset(supportPts) eq 14;
printf "FIBSHELL_SUPPORT_PTS=%o\\n", supportPts;

EsumPic := &+[qPic(Big.(#Cs+j)) : j in supportPts];
PPic := 7*HinPic - 4*EsumPic;
PL := PicL!PPic;
EsumL := PicL!EsumPic;
assert (PL,HinPicL) eq 112;
assert (PL,PL) eq 336;
assert &and[(PL,gensinPicL[#Cs+j]) eq 8 : j in supportPts];

// H^perp positive-definite lattice and rank-62 kernel of pairing with P.
LH := LatticeWithGram(pospmHperp);
prow := [(PicL!HperptoPic(HperpMod.j), PL) : j in [1..63]];
KP := Kernel(Transpose(Matrix(Integers(),1,63,prow)));
assert Dimension(KP) eq 62;
BKP := BasisMatrix(KP);
pospmKP := BKP*pospmHperp*Transpose(BKP);
LKP := LatticeWithGram(pospmKP);
KPMod := RSpace(Integers(), 62);
KPtoH := hom<KPMod -> HperpMod | Basis(KP)>;
ARat := ChangeRing(pospmKP, Rationals());

function BezoutSolution(row, target)
  coeff := [Integers()!0 : j in [1..#row]];
  g := Integers()!0;
  for j in [1..#row] do
    a := Integers()!row[j];
    if a ne 0 then
      if g eq 0 then
        g := Abs(a);
        coeff[j] := a div g;
      else
        gg, s, t := Xgcd(g, a);
        coeff := [s*x : x in coeff];
        coeff[j] +:= t;
        g := gg;
      end if;
    end if;
  end for;
  assert g gt 0;
  assert target mod g eq 0;
  coeff := [(target div g)*x : x in coeff];
  assert &+[coeff[j]*row[j] : j in [1..#row]] eq target;
  return coeff, g;
end function;

shells := {shell_records};
for sh in shells do
  e := sh[1];
  pf := sh[2];
  expectedM := sh[3];
  aa := sh[4];
  bb := sh[5];
  nrm := sh[6];

  // x = aa*F - bb*H lies in H^perp.
  // Its P-pairing is fixed by P.F and P.H=112.
  pc := aa*pf - bb*112;
  vseq, pgcd := BezoutSolution(prow, pc);
  vH := HperpMod!vseq;
  vLH := LH!Eltseq(vH);

  cross := Vector(Rationals(), [
    Rationals()!(LH!Eltseq(KPtoH(KPMod.j)), vLH)
    : j in [1..62]
  ]);
  center := -cross*(ARat^-1);
  proj := -&+[cross[j]*center[j] : j in [1..62]];
  qmin := Rationals()!(vLH,vLH) - proj;
  distq := Rationals()!nrm - qmin;

  den := Integers()!1;
  for z in Eltseq(center) do
    den := LCM(den, Denominator(z));
  end for;
  den := LCM(den, Denominator(qmin));
  targetCoords := [Integers()!(den*center[j]) : j in [1..62]];
  targetL := LKP!targetCoords;

  rawCount := 0;
  integralCount := 0;
  nefCount := 0;
  cands := [];

  if distq ge 0 then
    scaledDistQ := den^2*distq;
    assert Denominator(scaledDistQ) eq 1;
    scaledDist := Integers()!scaledDistQ;
    clv := CloseVectors(den*LKP, targetL, scaledDist, scaledDist);
    rawCount := #clv;

    for cv in clv do
      zL := LKP!(1/den*cv[1]);
      zK := KPMod!Eltseq(zL);
      xH := vH + KPtoH(zK);
      xLH := LH!Eltseq(xH);
      assert (xLH,xLH) eq nrm;
      xPic := HperptoPic(xH);
      xPicL := PicL!xPic;
      assert (xPicL,HinPicL) eq 0;
      assert (xPicL,PL) eq pc;

      numL := PicL!(xPic + bb*HinPic);
      numseq := [Integers()!z : z in Eltseq(numL)];
      if forall{j : j in [1..#numseq] | numseq[j] mod aa eq 0} then
        integralCount +:= 1;
        F := PicL![numseq[j] div aa : j in [1..#numseq]];
        assert (F,HinPicL) eq e;
        assert (F,F) eq 0;
        assert (F,PL) eq pf;
        msum := (F,EsumL);
        assert msum eq expectedM;
        allpairs := [(F,gensinPicL[j]) : j in [1..bdim]];
        if Min(allpairs) ge 0 then
          nefCount +:= 1;
          fseq := [Integers()!z : z in Eltseq(F)];
          g := GCD([Abs(z) : z in fseq]);
          if g eq 1 and not F in cands then
            Append(~cands,F);
            zeros := [j : j in [1..bdim] | allpairs[j] eq 0];
            printf "FIBSHELL_KEEP|%o|%o|%o|%o|%o|%o\\n",
                   e,pf,expectedM,Min(allpairs),zeros,Eltseq(F);
          end if;
        end if;
      end if;
    end for;
  end if;

  printf "FIBSHELL_SHELL|%o|%o|%o|%o|%o|%o|%o|%o|%o|%o|%o\\n",
         e,pf,expectedM,aa,bb,nrm,pc,rawCount,integralCount,nefCount,#cands;
end for;
printf "FIBSHELL_KERNEL_RANK=62\\n";
printf "FIBSHELL_DONE\\n";
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
    if sorted(mapping) != list(range(1, 49)):
        raise SystemExit("compact-to-Stoll map is not a permutation of 1..48")

    rows: dict[tuple[int, int], dict] = {}
    shell_re = re.compile(
        r"^FIBSHELL_SHELL\\|(\\d+)\\|(\\d+)\\|(\\d+)\\|(\\d+)\\|(\\d+)\\|(\\d+)\\|(-?\\d+)\\|(\\d+)\\|(\\d+)\\|(\\d+)\\|(\\d+)$",
        re.M,
    )
    for m in shell_re.finditer(stdout):
        e, pf, sm, aa, bb, nrm, pc, raw, integral, nef, kept = map(int, m.groups())
        rows[(e, pf)] = {
            "degree": e,
            "p_intersection": pf,
            "support_mass": sm,
            "scale_a": aa,
            "scale_b": bb,
            "hperp_norm": nrm,
            "hperp_p_pairing": pc,
            "raw_affine_close_vector_count": raw,
            "integral_picard_class_count": integral,
            "nef_known140_count": nef,
            "primitive_nef_candidate_count": kept,
            "primitive_nef_candidates": [],
        }

    keep_re = re.compile(
        r"^FIBSHELL_KEEP\\|(\\d+)\\|(\\d+)\\|(\\d+)\\|(-?\\d+)\\|(\\[[^\\n]*\\])\\|(\\[[^\\n]*\\])$",
        re.M,
    )
    for m in keep_re.finditer(stdout):
        e, pf, sm, minpair, zeros_s, coords_s = m.groups()
        row = rows[(int(e), int(pf))]
        if row["support_mass"] != int(sm):
            raise SystemExit("support-mass mismatch in keep row")
        coords = [int(x) for x in ast.literal_eval(coords_s)]
        zeros = [int(x) for x in ast.literal_eval(zeros_s)]
        if len(coords) != 64:
            raise SystemExit("Picard coordinate length mismatch")
        row["primitive_nef_candidates"].append(
            {
                "picard_basis_coordinates": coords,
                "minimum_known140_pairing": int(minpair),
                "zero_known140_indices_1based": zeros,
            }
        )

    expected = {(sh["degree"], sh["p_intersection"]) for sh in SHELLS}
    if set(rows) != expected:
        raise SystemExit(f"shell coverage mismatch: {sorted(rows)}")
    for row in rows.values():
        if row["primitive_nef_candidate_count"] != len(row["primitive_nef_candidates"]):
            raise SystemExit("candidate count mismatch")
        if not (
            row["raw_affine_close_vector_count"]
            >= row["integral_picard_class_count"]
            >= row["nef_known140_count"]
            >= row["primitive_nef_candidate_count"]
        ):
            raise SystemExit("filter counts are not monotone")

    ordered = [rows[(sh["degree"], sh["p_intersection"])] for sh in SHELLS]
    return {
        "mask": SUPPORT["mask"],
        "orbit_size": SUPPORT["orbit_size"],
        "compact_indices_0based": SUPPORT["compact_indices_0based"],
        "compact_to_stoll_pts_1based": mapping,
        "support_stoll_pts_1based": support_pts,
        "kernel_rank": 62,
        "submitted_magma_code_sha256": code_sha,
        "magma_request_attempt": magma_attempt,
        "raw_stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "shells": ordered,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args()

    text, core, blob, source_attempt = load_pinned_source()
    if blob != SOURCE_BLOB:
        raise SystemExit(f"pinned Stoll blob moved: {blob}")

    code = "SetColumns(0);\\nquick := true;\\n" + core + "\\n" + build_extra()
    code_sha = hashlib.sha256(code.encode()).hexdigest()
    stdout, magma_attempt = run_magma(
        code,
        args.timeout,
        "Stage32 MB104 000707 degree10/12 fibration isotropic shells",
        user_agent="perfect-cuboid-stage32mb/1.0-000707-fibration-shells",
    )
    support_result = parse_run(stdout, code_sha, magma_attempt)

    total_candidates = sum(
        sh["primitive_nef_candidate_count"] for sh in support_result["shells"]
    )
    deg10_candidates = sum(
        sh["primitive_nef_candidate_count"]
        for sh in support_result["shells"]
        if sh["degree"] == 10
    )
    deg12_candidates = sum(
        sh["primitive_nef_candidate_count"]
        for sh in support_result["shells"]
        if sh["degree"] == 12
    )

    out = {
        "schema": "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_V1",
        "status": "PRE_AUDIT_EXACT_FINITE_PICARD64_NUMERICAL_CANDIDATES_NO_CREDIT",
        "source_locks": {
            "stoll_repository": "MichaelStollBayreuth/Verification",
            "stoll_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
            "stoll_cuboids_blob": blob,
            "stage33_stoll_helper_blob": "010db3767b8f932c71ac5722b50ccb64a8c79f9d",
            "stage33_picard_marking_blob": PICARD_MARKING_BLOB,
            "stage32_picard_core_sha256": PICARD_CORE_SHA256,
            "parent_engine": "run_mb104_z40_p_null_picard64_finite_enumeration.py",
        },
        "mathematical_scope": {
            "support_mask": SUPPORT["mask"],
            "P": "7H-4*sum_{i in support}E_i",
            "P2": 336,
            "H_dot_P": 112,
            "degree10": {
                "H_dot_F": 10,
                "F2": 0,
                "P_dot_F_values": [30, 34, 38],
                "support_mass_values": [10, 9, 8],
                "hperp_transform": "x=8F-5H",
                "minus_x2": 400,
            },
            "degree12": {
                "H_dot_F": 12,
                "F2": 0,
                "P_dot_F_values": [36],
                "support_mass_values": [12],
                "hperp_transform": "y=4F-3H",
                "minus_y2": 144,
            },
            "filters": [
                "Picard64 integrality of F",
                "nonnegative intersection with all known 140 curves",
                "primitive Picard class",
            ],
        },
        "execution": {
            "source_fetch_attempt": source_attempt,
            "support_request_count": 1,
            "shell_count": len(SHELLS),
            "rank_before_P_pairing_reduction": 63,
            "rank_after_P_pairing_reduction": 62,
            "max_hperp_norm": max(sh["hperp_norm"] for sh in SHELLS),
            "raw_artifact_persisted": False,
        },
        "support": support_result,
        "summary": {
            "degree10_primitive_nef_candidate_count": deg10_candidates,
            "degree12_primitive_nef_candidate_count": deg12_candidates,
            "total_primitive_nef_candidate_count": total_candidates,
            "fibration_improvement_shells_numerically_empty_candidate": total_candidates == 0,
            "geometric_effectivity_or_semiampleness_proved": False,
            "global_min_P_dot_F_40_proved": False,
        },
        "next_geometry_if_candidates_remain": {
            "degree10": "reducible sextic residual: quartic+conic or conic+conic+conic, plus exceptional components",
            "degree12": "QA+QB+degree4 residual singular-fiber geometry, plus exceptional components",
        },
        "credit_firewall": {
            "numerical_fibration_shell_credit": False,
            "effectivity_credit": False,
            "semiampleness_credit": False,
            "global_fibration_optimum_credit": False,
            "MB104_complete": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    Path(args.output).write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "success": True,
                "canonical": out["canonical_sha256_without_this_field"],
                "degree10_candidates": deg10_candidates,
                "degree12_candidates": deg12_candidates,
                "total_candidates": total_candidates,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
