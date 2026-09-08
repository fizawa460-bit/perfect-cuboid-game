#!/usr/bin/env python3
"""Goal4AJ gen10 diagnostic: degree-19-only strict divisor kernel over F_32009.

The older strict-intersection diagnostic started its polynomial-ring intersection
with ``surf`` even though every symbolic-power ideal already contains ``surf``.
Thus its first intersection is tautologically ``surf``.  This diagnostic fixes
that semantic initialization by starting from the unit ideal and, because only
degree 19 is needed, truncates every homogeneous standard basis to generators
of degree <=19 after each exact symbolic power/intersection.

For a homogeneous ideal I, standard-basis generators of degree >19 cannot affect
I_d for d<=19.  Hence this truncation preserves the degree-19 membership space
while discarding irrelevant high-degree Groebner growth.  The computation is
performed over F_32009, where both i and sqrt(2) split, so the exact 22 strict
components from the retained parent diagnostic can be imposed separately.

Any modular strict-kernel output is diagnostic only.  A1 exceptional jet
conditions are still not imposed, and no Q-literal section, F_B, local
Brauer evaluation, E1, Stage35, theorem, or endpoint credit is granted.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
import tempfile
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_strict_intersection.py"
GEN9 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_finite_field_generator_gen9.py"
PARENT_BLOB = "1b2d1079b39333aceb97fb52894a4fa4048d6d67"
GEN9_BLOB = "c21d98f4091b87996a5cb6e5d21d8df297558ba0"
ACTIVE_SHA = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
RIGIDITY_SHA = "e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc"
AUDITED_PR = 1659
AUDITED_REVIEW = 5134464420
MERGE_SHA = "1d7bfd98ef8eab7bd849fe7bfdbcdaf5c0b575e7"
GEN9_FAILED_RUN = 34127950514
GEN9_FAILED_JOB = 101761177630
FIELD_PRIME = 32009
I_ROOT = 10754
SQRT2_ROOT = 8047
DEGREE = 19


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(PARENT) == PARENT_BLOB
assert git_blob(GEN9) == GEN9_BLOB
assert pow(I_ROOT, 2, FIELD_PRIME) == FIELD_PRIME - 1
assert pow(SQRT2_ROOT, 2, FIELD_PRIME) == 2
assert FIELD_PRIME % 8 == 1

# Reuse the exact 22 split-curve formulas from the source-locked parent rather
# than recopying the retained Stoll formulas by hand.
tree = ast.parse(PARENT.read_text(encoding="utf-8"))
parent_singular = None
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1:
        t = node.targets[0]
        if isinstance(t, ast.Name) and t.id == "SINGULAR":
            parent_singular = ast.literal_eval(node.value)
            break
if not isinstance(parent_singular, str):
    raise SystemExit("source-locked parent SINGULAR program not found")

old_field = """ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;\nminpoly=u^4+1;\nnumber ii=u^2;\nnumber ss=u-u^3;\nnumber isv=ii*ss;"""
new_field = f"""ring r={FIELD_PRIME},(a1,a2,a3,b1,b2,b3,c),dp;\nnumber ii={I_ROOT};\nnumber ss={SQRT2_ROOT};\nnumber isv=ii*ss;\nif (ii^2+1!=0) {{ ERROR(\"finite-field i root mismatch\"); }}\nif (ss^2-2!=0) {{ ERROR(\"finite-field sqrt2 root mismatch\"); }}"""
if old_field not in parent_singular:
    raise SystemExit("parent coefficient-field block moved")
s = parent_singular.replace(old_field, new_field, 1)

# The old initialization is semantically tautological because every T contains
# surf.  Start instead from the unit ideal so the first intersection is T.
if "ideal Current=surf;" not in s:
    raise SystemExit("parent Current initialization moved")
s = s.replace("ideal Current=surf;", "ideal Current=ideal(1);", 1)

trunc_proc = r'''
proc trunc19(ideal A)
{
  ideal G=std(A);
  ideal T=0;
  int j;
  int k=0;
  for (j=1; j<=size(G); j++)
  {
    if (G[j]!=0 && deg(G[j])<=19)
    {
      k++;
      T[k]=G[j];
    }
  }
  return(std(T));
}

'''
if "proc sympow" not in s:
    raise SystemExit("parent sympow marker moved")
s = s.replace("proc sympow", trunc_proc + "proc sympow", 1)

# Each symbolic power is computed exactly first, then only its <=19 standard
# basis is retained.  Each subsequent exact ideal intersection is likewise
# truncated only after the intersection has been formed.
s, n_pow = re.subn(r"T=sympow\(P,(\d+)\);", r"T=trunc19(sympow(P,\1));", s)
s, n_int = re.subn(
    r"Current=intersect\(Current,T\);\nCurrent=std\(Current\);",
    "Current=trunc19(intersect(Current,T));",
    s,
)
if n_pow != 22 or n_int != 22:
    raise SystemExit(f"parent strict block count moved: sympow={n_pow}, intersect={n_int}")

# The parent tail checks full-ideal saturation, which is not the object here:
# this diagnostic intentionally retains only degree<=19 data.  Replace that
# tail by degree-19 Hilbert-space and candidate measurements.
cut = "list FinalSatL=sat(Current,Sing);"
if cut not in s:
    raise SystemExit("parent final tail marker moved")
s = s.split(cut, 1)[0]
s += r'''
// Semantic guard for the corrected initialization: if an ideal contains surf,
// intersecting it with surf returns surf and therefore imposes no divisor data.
ideal Dummy=surf+ideal(a1);
ideal OldInit=intersect(surf,Dummy);
if (equalideal(OldInit,surf)!=1) { ERROR("old-init containment guard failed"); }
print("GOAL4AJ_DEN_TRUNC_OLD_INIT_COLLAPSE=PASS");

ideal SurfStd=std(surf);
intvec HS=hilb(SurfStd,1);
intvec HF=hilb(Current,1);
print("GOAL4AJ_DEN_TRUNC_SURFACE_HILB1="+string(HS));
print("GOAL4AJ_DEN_TRUNC_FINAL_HILB1="+string(HF));
print("GOAL4AJ_DEN_TRUNC_FINAL_GENERATORS="+string(size(Current)));

int jj;
int cc=0;
int mindeg=999;
poly q;
for (jj=1; jj<=size(Current); jj++)
{
  q=reduce(Current[jj],SurfStd);
  if (q!=0)
  {
    if (deg(q)<mindeg) { mindeg=deg(q); }
    if (deg(q)==19 && cc<3)
    {
      cc++;
      print("GOAL4AJ_DEN_TRUNC_CANDIDATE_"+string(cc)+"="+string(q));
    }
  }
}
print("GOAL4AJ_DEN_TRUNC_MIN_NONSURFACE_GENERATOR_DEGREE="+string(mindeg));
print("GOAL4AJ_DEN_TRUNC_CANDIDATE_COUNT="+string(cc));
print("GOAL4AJ_DEN_TRUNC_STRICT_KERNEL=PASS");
quit;
'''

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-den-trunc-gen10.sing"
    src.write_text(s, encoding="utf-8")
    try:
        cp = subprocess.run(
            ["Singular", "-q", str(src)],
            text=True,
            capture_output=True,
            timeout=1200,
        )
        timed_out = False
        stdout, stderr, rc = cp.stdout, cp.stderr, cp.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        rc = None

print(stdout, end="")
if stderr:
    print("GOAL4AJ_DEN_TRUNC_STDERR=" + json.dumps(stderr[-12000:]))


def marker(prefix: str):
    return next((x.split("=", 1)[1] for x in stdout.splitlines() if x.startswith(prefix + "=")), None)


def parse_iv(text: str | None) -> list[int]:
    if text is None:
        return []
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def hf_from_first_hilb(v: list[int], d: int, nvars: int = 7) -> int:
    if not v:
        raise ValueError("empty Hilbert numerator")
    coeffs = v[:-1]
    return sum(
        a * comb(d - j + nvars - 1, nvars - 1)
        for j, a in enumerate(coeffs)
        if a and d >= j
    )

step_rows = []
for x in stdout.splitlines():
    if x.startswith("GOAL4AJ_DEN_STRICT_STEP="):
        payload = x.split("=", 1)[1]
        p = payload.split(":", 4)
        if len(p) == 5:
            step_rows.append(
                {
                    "step": int(p[0]),
                    "strict_index_1based": int(p[1]),
                    "multiplicity": int(p[2]),
                    "standard_basis_generator_count_after_truncation": int(p[3]),
                    "hilb1": parse_iv(p[4]),
                }
            )

hs = parse_iv(marker("GOAL4AJ_DEN_TRUNC_SURFACE_HILB1"))
hf = parse_iv(marker("GOAL4AJ_DEN_TRUNC_FINAL_HILB1"))
surface_hf19 = hf_from_first_hilb(hs, DEGREE) if hs else None
quotient_hf19 = hf_from_first_hilb(hf, DEGREE) if hf else None
strict_space_dim = (
    surface_hf19 - quotient_hf19
    if surface_hf19 is not None and quotient_hf19 is not None
    else None
)

candidates = []
for x in stdout.splitlines():
    if x.startswith("GOAL4AJ_DEN_TRUNC_CANDIDATE_") and not x.startswith("GOAL4AJ_DEN_TRUNC_CANDIDATE_COUNT"):
        candidates.append(x.split("=", 1)[1])
candidate_bytes = sum(len(x.encode()) for x in candidates)
error_text = any(
    t in stdout.lower()
    for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign")
)
completed = (
    not timed_out
    and rc == 0
    and not error_text
    and len(step_rows) == 22
    and marker("GOAL4AJ_DEN_TRUNC_OLD_INIT_COLLAPSE") == "PASS"
    and "GOAL4AJ_DEN_TRUNC_STRICT_KERNEL=PASS" in stdout
    and surface_hf19 == 2744
    and strict_space_dim is not None
    and strict_space_dim >= 0
)

out = {
    "schema": "STAGE35_EX_GOAL4AJ_DEGREE19_TRUNCATED_STRICT_KERNEL_GEN10_DIAGNOSTIC_V1",
    "source_locks": {
        "merged_goal4ai_pr": AUDITED_PR,
        "merged_goal4ai_hostile_review": AUDITED_REVIEW,
        "merged_goal4ai_merge_sha": MERGE_SHA,
        "parent_strict_intersection_blob_sha1": PARENT_BLOB,
        "gen9_finite_field_generator_blob_sha1": GEN9_BLOB,
        "gen9_failed_run": GEN9_FAILED_RUN,
        "gen9_failed_job": GEN9_FAILED_JOB,
        "active_divisor_condition_packet_canonical_sha256": ACTIVE_SHA,
        "denominator_residual_rigidity_canonical_sha256": RIGIDITY_SHA,
    },
    "coefficient_field": f"F_{FIELD_PRIME}",
    "field_prime": FIELD_PRIME,
    "i_root": I_ROOT,
    "sqrt2_root": SQRT2_ROOT,
    "degree_cap": DEGREE,
    "old_parent_initialization_intersect_surf_with_containing_ideal_collapses_to_surf": marker("GOAL4AJ_DEN_TRUNC_OLD_INIT_COLLAPSE") == "PASS",
    "corrected_initialization": "unit_ideal",
    "truncation_semantics": "after_each_exact_symbolic_power_and_exact_intersection_keep_homogeneous_standard_basis_generators_of_degree_le_19",
    "active_strict_curve_count": 22,
    "active_strict_total_multiplicity": 102,
    "completed_strict_curve_intersections": len(step_rows),
    "step_rows": step_rows,
    "singular_timed_out": timed_out,
    "singular_returncode": rc,
    "singular_error_text_present": error_text,
    "surface_degree19_dimension": surface_hf19,
    "quotient_by_strict_kernel_degree19_dimension": quotient_hf19,
    "strict_condition_section_space_degree19_dimension": strict_space_dim,
    "final_truncated_standard_basis_generator_count": int(marker("GOAL4AJ_DEN_TRUNC_FINAL_GENERATORS")) if marker("GOAL4AJ_DEN_TRUNC_FINAL_GENERATORS") else None,
    "minimum_nonsurface_generator_degree": int(marker("GOAL4AJ_DEN_TRUNC_MIN_NONSURFACE_GENERATOR_DEGREE")) if marker("GOAL4AJ_DEN_TRUNC_MIN_NONSURFACE_GENERATOR_DEGREE") else None,
    "degree19_candidate_standard_basis_count_capped3": len(candidates),
    "degree19_candidate_text_total_bytes": candidate_bytes,
    "degree19_candidates_capped3": candidates if candidate_bytes <= 60000 else [],
    "strict_degree19_kernel_completed": completed,
    "a1_exceptional_jet_conditions_imposed": False,
    "q_literal_degree19_denominator_materialized": False,
    "q_literal_degree31_denominator_materialized": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(
    json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
print("GOAL4AJ_DEN_TRUNC_GEN10_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_DEN_TRUNC_GEN10=" + ("PASS" if completed else "RESOURCE_OR_IMPLEMENTATION_WALL"), flush=True)
if not completed:
    raise SystemExit("Goal4AJ degree19 truncated strict kernel did not complete; no mathematical obstruction credit")
