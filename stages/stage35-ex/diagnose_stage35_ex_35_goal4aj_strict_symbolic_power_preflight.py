#!/usr/bin/env python3
"""Goal4AJ diagnostic: certify a strict-curve symbolic-power constructor.

On the normal cuboid canonical surface the 92 retained strict curves are
height-one primes. Away from the finite A1 singular locus the surface is
regular, so their ordinary and symbolic powers agree. Hence the symbolic
power is obtained by saturating the ordinary power by the singular-locus
ideal. This preflight checks that mechanism exactly on the standard A1 model
and on the pinned Stoll C1[1] curve inside the four-quadric cuboid surface.

This is diagnostic only. It does not build the full 92-curve packet, solve a
degree-31 section system, or materialize F_B.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GOAL4AI = ROOT / "stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence.json"

GOAL4AI_CANONICAL_SHA256 = "b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a"
STOLL_CUBOIDS_BLOB_SHA1 = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
LOCATOR_RUN = 34090067335
LOCATOR_JOB = 101641601601

ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_CANONICAL_SHA256
facts = ai["source_locks"]["stoll_testa"]["facts"]
assert "normal_complete_intersection_four_quadrics_in_P6" in facts
assert "48_A1_rational_double_points" in facts
assert ai["homogeneous_realization"]["literal_numerator_coefficients_materialized"] is False
assert ai["homogeneous_realization"]["literal_denominator_coefficients_materialized"] is False

SINGULAR = r'''
option(redSB);
LIB "elim.lib";

proc contained(ideal A, ideal B)
{
  ideal G=std(B);
  int j;
  for (j=1; j<=size(A); j++)
  {
    if (reduce(A[j],G)!=0) { return(0); }
  }
  return(1);
}

// Standard A1 local model. P=(x,z) is one ruling prime. Since y is a unit
// at the generic point of P and xy=z^2, v_P(z)=1 and v_P(x)=2. Therefore
// P^(2)=(x), P^(3)=xP. Saturation by the singular maximal ideal must recover
// these symbolic powers from the ordinary powers.
ring rt=0,(x,y,z),dp;
ideal Ft=x*y-z^2;
ideal Pt=x,z;
ideal Mt=x,y,z;
ideal Ot2=Ft+Pt*Pt;
ideal Ot3=Ft+Pt*Pt*Pt;
list Lt2=sat(Ot2,Mt);
list Lt3=sat(Ot3,Mt);
ideal St2=Lt2[1];
ideal St3=Lt3[1];
ideal Et2=x*y-z^2,x;
ideal Et3=x*y-z^2,x^2,x*z;
if (contained(St2,Et2)!=1 || contained(Et2,St2)!=1) { ERROR("A1 symbolic square mismatch"); }
if (contained(St3,Et3)!=1 || contained(Et3,St3)!=1) { ERROR("A1 symbolic cube mismatch"); }
if (contained(St2,Ot2)==1) { ERROR("A1 symbolic square did not remove embedded singular contribution"); }
print("GOAL4AJ_A1_SYMBOLIC_POWER=PASS");

// Cuboid canonical surface over Q and pinned Stoll C1[1]:
//   [a1, a2+b3, a3+b2, b1+c].
// Its quotient is the irreducible conic b2^2+b3^2-c^2=0, hence this is a
// height-one prime on the normal surface. The 4x4 Jacobian minors define the
// singular locus on the complete-intersection surface. Saturating the
// ordinary square by that locus is therefore the reflexive/symbolic square.
ring r=0,(a1,a2,a3,b1,b2,b3,c),dp;
ideal surf=
  a1^2+a2^2-b3^2,
  a2^2+a3^2-b1^2,
  a1^2+a3^2-b2^2,
  a1^2+a2^2+a3^2-c^2;
matrix J=jacob(surf);
ideal Sing=minor(J,4);
ideal L=a1,a2+b3,a3+b2,b1+c;
ideal C=surf+L;
if (dim(std(surf))!=3) { ERROR("cuboid affine cone dimension mismatch"); }
if (dim(std(C))!=2) { ERROR("C1 affine cone dimension mismatch"); }
ideal O2=surf+L*L;
list LS2=sat(O2,Sing);
ideal S2=LS2[1];
list Lstable=sat(S2,Sing);
ideal S2stable=Lstable[1];
if (contained(O2,S2)!=1) { ERROR("ordinary square not contained in symbolic square"); }
if (contained(S2,S2stable)!=1 || contained(S2stable,S2)!=1) { ERROR("C1 symbolic square not saturation-stable"); }
if (contained(S2,O2)==1) { ERROR("C1 symbolic square shows no A1 correction"); }
print("GOAL4AJ_CUBOID_C1_SYMBOLIC_POWER=PASS");
print("GOAL4AJ_C1_ORDINARY_SQUARE_GENERATORS="+string(size(O2)));
print("GOAL4AJ_C1_SYMBOLIC_SQUARE_GENERATORS="+string(size(S2)));
print("GOAL4AJ_STRICT_SYMBOLIC_POWER_PREFLIGHT=PASS");
quit;
'''

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-symbolic.sing"
    src.write_text(SINGULAR, encoding="utf-8")
    cp = subprocess.run(["Singular", "-q", str(src)], text=True, capture_output=True, timeout=420)

stdout = cp.stdout
stderr = cp.stderr
print(stdout, end="")
if stderr:
    print("GOAL4AJ_STRICT_SYMBOLIC_STDERR=" + json.dumps(stderr[:12000]))

markers = {
    "a1_symbolic_square_cube_exact": "GOAL4AJ_A1_SYMBOLIC_POWER=PASS" in stdout,
    "cuboid_c1_symbolic_square_saturation_exact": "GOAL4AJ_CUBOID_C1_SYMBOLIC_POWER=PASS" in stdout,
    "completion_marker_present": "GOAL4AJ_STRICT_SYMBOLIC_POWER_PREFLIGHT=PASS" in stdout,
}
error_text = any(s in stdout.lower() for s in ("error occurred", "? error", "? cannot", "? member", "? assign", "? wrong"))
out = {
    "schema": "STAGE35_EX_GOAL4AJ_STRICT_SYMBOLIC_POWER_PREFLIGHT_DIAGNOSTIC_V2",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_CANONICAL_SHA256,
        "stoll_cuboids_magma_blob_sha1": STOLL_CUBOIDS_BLOB_SHA1,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "retained140_locator_run": LOCATOR_RUN,
        "retained140_locator_job": LOCATOR_JOB,
    },
    "singular_returncode": cp.returncode,
    "singular_error_text_present": error_text,
    **markers,
    "constructor": "P^(m)=saturation(surface_plus_ordinary_power(P,m), jacobian_singular_locus)",
    "normal_surface_height1_symbolic_equals_singular_locus_saturation": True,
    "representative_pinned_strict_curve": "Stoll C1[1]=[a1,a2+b3,a3+b2,b1+c]",
    "all_92_strict_curve_symbolic_powers_materialized": False,
    "degree31_numerator_section_solved": False,
    "degree19_denominator_residual_section_solved": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_STRICT_SYMBOLIC_POWER_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
if cp.returncode != 0 or error_text or not all(markers.values()):
    raise SystemExit("Goal4AJ strict symbolic-power preflight failed closed")
