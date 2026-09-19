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

SUPPORTS = [
    {
        "mask": "0000770000ff",
        "orbit_size": 48,
        "compact_indices_0based": [0,1,2,3,4,5,6,7,24,25,26,28,29,30],
        "expected_known_null_quartics": 4,
    },
    {
        "mask": "00007b0000ff",
        "orbit_size": 48,
        "compact_indices_0based": [0,1,2,3,4,5,6,7,24,25,27,28,29,30],
        "expected_known_null_quartics": 4,
    },
    {
        "mask": "000707000f0f",
        "orbit_size": 768,
        "compact_indices_0based": [0,1,2,3,8,9,10,11,24,25,26,32,33,34],
        "expected_known_null_quartics": 2,
    },
]

SHELLS = [
    (4,0,-6,84),(4,1,-4,52),(4,2,-2,20),
    (8,0,-10,112),(8,1,-8,80),(8,2,-6,48),(8,3,-4,16),
    (12,0,-14,116),(12,1,-12,84),(12,2,-10,52),(12,3,-8,20),
    (16,0,-18,96),(16,1,-16,64),(16,2,-14,32),(16,3,-12,0),
    (20,0,-22,52),(20,1,-20,20),
]

def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def build_extra(support: dict) -> str:
    compact = [i + 1 for i in support["compact_indices_0based"]]
    shells = "[" + ",".join(f"<{e},{pa},{r2},{n}>" for e,pa,r2,n in SHELLS) + "]"
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
printf "Z40_MAP=%o\n", compactToPts;

supportCompact := {compact};
supportPts := [compactToPts[j] : j in supportCompact];
assert #supportPts eq 14 and #Seqset(supportPts) eq 14;
printf "Z40_SUPPORT_PTS=%o\n", supportPts;

EsumPic := &+[qPic(Big.(#Cs+j)) : j in supportPts];
PPic := 7*HinPic - 4*EsumPic;
PL := PicL!PPic;
assert (PL,HinPicL) eq 112;
assert (PL,PL) eq 336;
assert &and[(PL,gensinPicL[#Cs+j]) eq 8 : j in supportPts];

nullq := [j : j in [1..#Cs] |
          (PL,gensinPicL[j]) eq 0 and
          (gensinPicL[j],HinPicL) eq 4 and
          (gensinPicL[j],gensinPicL[j]) eq -4];
assert #nullq eq {support["expected_known_null_quartics"]};
printf "Z40_NULLQ=%o\n", nullq;
qidx := nullq[1];
QPic := qPic(Big.qidx);
QL := PicL!QPic;

// Within H^perp, P-perp is rank 62.
prow := [(PicL!HperptoPic(HperpMod.j), PL) : j in [1..63]];
KP := Kernel(Transpose(Matrix(Integers(),1,63,prow)));
assert Dimension(KP) eq 62;
BKP := BasisMatrix(KP);
pospmKP := BKP*pospmHperp*Transpose(BKP);
LKP := LatticeWithGram(pospmKP);
KPMod := RSpace(Integers(), 62);
KPtoH := hom<KPMod -> HperpMod | Basis(KP)>;

// z0 = 4Q-H+sum(E_supported) is in H-perp and P-perp.
z0Pic := 4*QPic - HinPic + EsumPic;
z0H := z0Pic @@ HperptoPic;
z0K := z0H @@ KPtoH;
z0L := LKP!Eltseq(z0K);
assert (PicL!z0Pic,HinPicL) eq 0;
assert (PicL!z0Pic,PL) eq 0;
assert (z0L,z0L) eq 52;
printf "Z40_KERNEL_RANK=62\n";
printf "Z40_QIDX=%o\n", qidx;

shells := {shells};
for sh in shells do
  e := sh[1]; pa := sh[2]; r2 := sh[3]; nrm := sh[4];
  k := e div 4;
  base := k*z0L;
  clv := CloseVectors(4*LKP, base, nrm, nrm);
  cands := [];
  for cv in clv do
    uL := LKP!(1/4*cv[1]);
    uK := KPMod!Eltseq(uL);
    uH := KPtoH(uK);
    rPic := k*QPic - HperptoPic(uH);
    r := PicL!rPic;
    assert (r,HinPicL) eq e;
    assert (r,PL) eq 0;
    assert (r,r) eq r2;
    assert ((r,r)+(r,HinPicL)) div 2 + 1 eq pa;
    if not r in cands then
      Append(~cands,r);
    end if;
  end for;

  knownCount := 0;
  unknownKeepCount := 0;
  for r in cands do
    known := [j : j in [1..bdim] | r eq gensinPicL[j]];
    if #known gt 0 then
      knownCount +:= 1;
      printf "Z40_KEEP|%o|%o|%o|KNOWN|%o|%o\n",
             e,pa,r2,known,Eltseq(r);
    elif forall{{j : j in [1..bdim] | (r,gensinPicL[j]) ge 0}} then
      unknownKeepCount +:= 1;
      printf "Z40_KEEP|%o|%o|%o|UNKNOWN|%o|%o\n",
             e,pa,r2,[],Eltseq(r);
    end if;
  end for;
  printf "Z40_SHELL|%o|%o|%o|%o|%o|%o|%o\n",
         e,pa,r2,nrm,#clv,#cands,knownCount+unknownKeepCount;
end for;
printf "Z40_DONE\n";
"""

def parse_run(stdout: str, support: dict, code_sha: str, magma_attempt: int) -> dict:
    def grab(name: str):
        m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
        if not m:
            raise SystemExit(f"missing Magma output {name} for {support['mask']}")
        return ast.literal_eval(m.group(1))

    if "Z40_DONE" not in stdout:
        print(stdout)
        raise SystemExit(f"missing Z40_DONE for {support['mask']}")
    if any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
        print(stdout)
        raise SystemExit(f"Magma failure for {support['mask']}")

    mapping = [int(x) for x in grab("Z40_MAP")]
    support_pts = [int(x) for x in grab("Z40_SUPPORT_PTS")]
    nullq = [int(x) for x in grab("Z40_NULLQ")]
    qidx = int(re.search(r"^Z40_QIDX=(\d+)$", stdout, re.M).group(1))

    shell_rows = {}
    for m in re.finditer(r"^Z40_SHELL\|(\d+)\|(\d+)\|(-?\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)$", stdout, re.M):
        e,pa,r2,nrm,raw,uniq,kept = map(int,m.groups())
        shell_rows[(e,pa)] = {
            "degree": e,
            "arithmetic_genus": pa,
            "R2": r2,
            "reduced_norm": nrm,
            "raw_close_vector_count": raw,
            "unique_class_count": uniq,
            "kept_after_known_or_nonnegative_filter": kept,
            "known_kept": [],
            "unknown_nonnegative_kept": [],
        }

    for m in re.finditer(r"^Z40_KEEP\|(\d+)\|(\d+)\|(-?\d+)\|(KNOWN|UNKNOWN)\|(\[[^\n]*\])\|(\[[^\n]*\])$", stdout, re.M):
        e,pa,r2,kind,known_s,coords_s = m.groups()
        row = shell_rows[(int(e),int(pa))]
        assert row["R2"] == int(r2)
        rec = {
            "known_indices_1based": [int(x) for x in ast.literal_eval(known_s)],
            "picard_basis_coordinates": [int(x) for x in ast.literal_eval(coords_s)],
        }
        assert len(rec["picard_basis_coordinates"]) == 64
        if kind == "KNOWN":
            assert rec["known_indices_1based"]
            row["known_kept"].append(rec)
        else:
            assert not rec["known_indices_1based"]
            row["unknown_nonnegative_kept"].append(rec)

    expected_keys={(e,pa) for e,pa,_,_ in SHELLS}
    if set(shell_rows) != expected_keys:
        raise SystemExit(f"shell coverage mismatch for {support['mask']}: {sorted(shell_rows)}")

    return {
        "mask": support["mask"],
        "orbit_size": support["orbit_size"],
        "compact_indices_0based": support["compact_indices_0based"],
        "compact_to_stoll_pts_1based": mapping,
        "support_stoll_pts_1based": support_pts,
        "known_null_quartic_indices_1based": nullq,
        "reference_null_quartic_index_1based": qidx,
        "kernel_rank": 62,
        "submitted_magma_code_sha256": code_sha,
        "magma_request_attempt": magma_attempt,
        "raw_stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "shells": [shell_rows[(e,pa)] for e,pa,_,_ in SHELLS],
    }

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--timeout", type=int, default=900)
    args=ap.parse_args()

    text, core, blob, source_attempt = load_pinned_source()
    if blob != SOURCE_BLOB:
        raise SystemExit(f"pinned Stoll blob moved: {blob}")

    results=[]
    for support in SUPPORTS:
        code = "SetColumns(0);\nquick := true;\n" + core + "\n" + build_extra(support)
        code_sha=hashlib.sha256(code.encode()).hexdigest()
        stdout,magma_attempt=run_magma(
            code,args.timeout,
            f"Stage32 MB104 Z40 {support['mask']}",
            user_agent="perfect-cuboid-stage32mb/1.0-z40-pnull-picard64",
        )
        results.append(parse_run(stdout,support,code_sha,magma_attempt))

    mapping=results[0]["compact_to_stoll_pts_1based"]
    if any(r["compact_to_stoll_pts_1based"] != mapping for r in results[1:]):
        raise SystemExit("compact-to-Stoll point mapping changed between support requests")

    unknown_total=sum(
        len(sh["unknown_nonnegative_kept"])
        for r in results for sh in r["shells"]
    )
    known_total=sum(
        len(sh["known_kept"])
        for r in results for sh in r["shells"]
    )
    out={
        "schema":"STAGE32_MB104_Z40_P_NULL_PICARD64_FINITE_ENUMERATION_V1",
        "status":"PRE_AUDIT_EXACT_FINITE_PICARD64_ENUMERATION_NO_CREDIT",
        "source_locks":{
            "stoll_repository":"MichaelStollBayreuth/Verification",
            "stoll_commit":"51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
            "stoll_cuboids_blob":blob,
            "stage33_stoll_helper_blob":"010db3767b8f932c71ac5722b50ccb64a8c79f9d",
            "stage33_picard_marking_blob":PICARD_MARKING_BLOB,
            "stage32_picard_core_sha256":PICARD_CORE_SHA256,
        },
        "execution":{
            "source_fetch_attempt":source_attempt,
            "support_request_count":len(results),
            "shell_count_per_support":len(SHELLS),
            "total_shell_count":len(results)*len(SHELLS),
            "rank_before_P_null_reduction":63,
            "rank_after_P_null_reduction":62,
            "max_reduced_norm":max(n for _,_,_,n in SHELLS),
            "raw_artifact_persisted":False,
        },
        "supports":results,
        "summary":{
            "known_kept_class_occurrences":known_total,
            "unknown_nonnegative_class_occurrences":unknown_total,
            "numerical_null_locus_complete_candidate":unknown_total==0,
            "geometric_effectivity_of_unknowns_proved":False,
        },
        "credit_firewall":{
            "numerical_null_locus_credit":False,
            "semiampleness_credit":False,
            "effectivity_credit":False,
            "whole_uniform_ray_closed":False,
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
        "unknown_nonnegative_class_occurrences":unknown_total,
        "known_kept_class_occurrences":known_total,
        "total_shell_count":51,
    },sort_keys=True))

if __name__=="__main__":
    main()
