#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

SINGULAR = r'''
option(redSB);
ring r=(0,t),(x,y,z),dp;
minpoly=t^4+1;
ideal rel=x*y-z^2;
qring q=std(rel);
LIB "modules.lib";

// A1 toy model. I=(x,z), J=(z,y). Test a nonfree rank-one Hom and
// require modules.lib to interpret an actual Hom generator as a concrete rule.
matrix gi[1][2]=x,z;
matrix gj[1][2]=z,y;
Matrix GI=gi;
Matrix GJ=gj;
Module MI=image(GI);
Module MJ=image(GJ);
Module HT=hom(MI,MJ);
matrix hgm=HT.generators.hom;
if (ncols(hgm)<=0) { ERROR("toy Hom has no generators"); }
Vector HV=makeVector([hgm[1..nrows(hgm),1]],HT);
def HF=interpret(HV);
if (typeof(HF)!="Homomorphism") { ERROR("toy Hom interpretation failed"); }
if (nrows(HF.rule)<=0 || ncols(HF.rule)<=0) { ERROR("toy Hom rule empty"); }
print("GOAL4AJ_TOY_HOM_INTERPRET=PASS");

ring rr=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
if (ii^2+1!=0) { ERROR("i relation failed"); }
if (ss^2-2!=0) { ERROR("sqrt2 relation failed"); }
ideal surf=
  a1^2+a2^2-b3^2,
  a2^2+a3^2-b1^2,
  a1^2+a3^2-b2^2,
  a1^2+a2^2+a3^2-c^2;
qring S=std(surf);

// Exact Stoll C1[1] strict curve ideal: [a1,a2+b3,a3+b2,b1+c].
matrix gc[1][4]=a1,a2+b3,a3+b2,b1+c;
Matrix GC=gc;
Module MC=image(GC);
Module HC=hom(MC,MC);
matrix hcm=HC.generators.hom;
if (ncols(hcm)<=0) { ERROR("cuboid C1 self-Hom has no generators"); }
Vector CV=makeVector([hcm[1..nrows(hcm),1]],HC);
def CF=interpret(CV);
if (typeof(CF)!="Homomorphism") { ERROR("cuboid C1 Hom interpretation failed"); }
if (nrows(CF.rule)<=0 || ncols(CF.rule)<=0) { ERROR("cuboid C1 Hom rule empty"); }
print("GOAL4AJ_CUBOID_C1_HOM_INTERPRET=PASS");
print("GOAL4AJ_SINGULAR_MODULE_HOM_PREFLIGHT=PASS");
quit;
'''

with tempfile.TemporaryDirectory() as td:
    p=Path(td)/"goal4aj.sing"
    p.write_text(SINGULAR)
    cp=subprocess.run(["Singular","-q",str(p)],text=True,capture_output=True,timeout=240)
    stdout=cp.stdout
    stderr=cp.stderr

print(stdout,end="")
if stderr:
    print("GOAL4AJ_SINGULAR_STDERR="+json.dumps(stderr[:12000]))

marker="GOAL4AJ_SINGULAR_MODULE_HOM_PREFLIGHT=PASS"
toy_marker="GOAL4AJ_TOY_HOM_INTERPRET=PASS"
cuboid_marker="GOAL4AJ_CUBOID_C1_HOM_INTERPRET=PASS"
error_text=("error occurred" in stdout.lower() or "? error" in stdout.lower() or "? cannot" in stdout.lower() or "? member" in stdout.lower() or "? assign" in stdout.lower())
out={
    "schema":"STAGE35_EX_GOAL4AJ_SINGULAR_MODULE_HOM_PREFLIGHT_DIAGNOSTIC_V2",
    "singular_returncode":cp.returncode,
    "singular_error_text_present":error_text,
    "completion_marker_present":marker in stdout,
    "toy_a1_rank1_hom_interpreted":toy_marker in stdout,
    "cuboid_c1_self_hom_interpreted":cuboid_marker in stdout,
    "literal_F_B_materialized":False,
    "local_evaluations_computed":False,
    "brauer_manin_obstruction_obtained":False,
    "E1_proved":False,
    "stage35_closed":False,
    "theorem_credit":False,
    "endpoint_credit":False,
}
print("GOAL4AJ_SINGULAR_PREFLIGHT_JSON="+json.dumps(out,sort_keys=True,separators=(",",":")))
if cp.returncode!=0 or error_text or marker not in stdout or toy_marker not in stdout or cuboid_marker not in stdout:
    raise SystemExit("Goal4AJ Singular module-Hom preflight failed closed")
