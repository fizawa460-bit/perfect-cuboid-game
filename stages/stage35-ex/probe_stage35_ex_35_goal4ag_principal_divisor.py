#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNKEY = ROOT / "stages/stage35-ex/runkeys/goal4ag-principal-divisor-preflight.json"
GOAL4AA = ROOT / "stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json"
GOAL4Z = ROOT / "stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json"
PERMS = ROOT / "stages/stage33/33-07/galois-known-class-permutations.json"
HELPER = ROOT / "stages/stage33/33-07/stoll_cuboid_source.py"


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


key = json.loads(RUNKEY.read_text())
assert key["schema"] == "STAGE35_EX_GOAL4AG_PRINCIPAL_DIVISOR_PREFLIGHT_RUNKEY_V1"
assert key["armed"] is True
assert key["generation"] == 2
assert git_blob(Path(__file__)) == key["probe_blob_sha1"]
assert git_blob(HELPER) == key["stage33_source_helper_blob_sha1"] == "010db3767b8f932c71ac5722b50ccb64a8c79f9d"

aa = json.loads(GOAL4AA.read_text())
z = json.loads(GOAL4Z.read_text())
p = json.loads(PERMS.read_text())
assert aa["schema"] == "STAGE35_EX_35_GOAL4AA_QI_CYCLIC_LINEAR_HYPERPLANE_BLOCKER_V1"
assert z["schema"] == "STAGE35_EX_35_GOAL4Z_ONE_EXPLICIT_BIQUATERNION_SECOND_QI_PRINCIPALIZATION_V1"
assert p["canonical_sha256"] == "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"

formal = [0] * 140
cc = [int(x) for x in p["cc_permutation_1based"]]
for k, v in z["class_B"]["picard_lift_cc_indlist_coefficients"].items():
    i = int(k)
    c = int(v)
    formal[i - 1] += c
    formal[cc[i - 1] - 1] += c
for k, v in aa["class_B_principalization_target"]["simplified_boundary_divisor_E_B"].items():
    formal[int(k) - 1] -= int(v)

assert sum(x != 0 for x in formal) == 69
assert all(x == 0 for x in formal[40:92])
strict = formal[:92]
exceptional = formal[92:]
assert sum(x != 0 for x in strict) == 33
assert sum(x != 0 for x in exceptional) == 36


def hdeg(i1: int) -> int:
    return 2 if i1 <= 32 else 4


pos_hdeg = sum(c * hdeg(i + 1) for i, c in enumerate(strict) if c > 0)
neg_hdeg = sum((-c) * hdeg(i + 1) for i, c in enumerate(strict) if c < 0)
assert pos_hdeg == neg_hdeg == 396

sys.path.insert(0, str(HELPER.parent))
from stoll_cuboid_source import load_pinned_source, run_magma

full, _, source_blob, source_attempt = load_pinned_source()
assert source_blob == key["upstream_git_blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

stop = full.index("// Genus 3 hyperelliptic curves of degree 8")
geometry = full[:stop]
strict_literal = "[" + ",".join(str(int(x)) for x in strict) + "]"
exceptional_literal = "[" + ",".join(str(int(x)) for x in exceptional) + "]"

build = r'''
SetColumns(0);
targetStrict := __STRICT__;
assert #Cs eq 92;
assert #pts eq 48;
assert #targetStrict eq 92;
D := ZeroDivisor(S);
for j in [1..92] do
    if targetStrict[j] ne 0 then
        D +:= targetStrict[j] * Divisor(S, Cs[j] : CheckSaturated := true, CheckDimension := true);
    end if;
end for;
printf "GOAL4AG_STRICT_SUPPORT=%o\n", #[j : j in [1..92] | targetStrict[j] ne 0];
'''.replace("__STRICT__", strict_literal)

# Phase 1 is deliberately tiny.  It distinguishes transport/type failures from
# the mathematical Cartier/principal questions.
phase1 = geometry + build + r'''
printf "GOAL4AG_CARTIER=%o\n", IsCartier(D);
printf "GOAL4AG_PHASE1_DONE\n";
'''
out1, attempt1 = run_magma(
    phase1, 120, "Stage35-EX Goal4AG divisor construction/Cartier phase",
    user_agent="perfect-cuboid-stage35ex/4ag-cartier",
)
if "GOAL4AG_PHASE1_DONE" not in out1:
    print("GOAL4AG_PHASE1_RAW=" + repr(out1))
    raise SystemExit("Goal4AG phase1 returned no completion marker")


def grab(text: str, name: str) -> str:
    m = re.search(rf"^{re.escape(name)}=(.+)$", text, re.M)
    if not m:
        print(text)
        raise SystemExit(f"missing {name}")
    return m.group(1).strip()


cartier = grab(out1, "GOAL4AG_CARTIER").lower() == "true"
principal = False
exceptional_match = False
attempt2 = 0
attempt3 = 0

if cartier:
    phase2 = geometry + build + r'''
isp, f := IsPrincipal(D);
printf "GOAL4AG_STRICT_IS_PRINCIPAL=%o\n", isp;
if isp then
    assert Divisor(S, f) eq D;
end if;
printf "GOAL4AG_PHASE2_DONE\n";
'''
    out2, attempt2 = run_magma(
        phase2, 180, "Stage35-EX Goal4AG IsPrincipal phase",
        user_agent="perfect-cuboid-stage35ex/4ag-principal",
    )
    if "GOAL4AG_PHASE2_DONE" not in out2:
        print("GOAL4AG_PHASE2_RAW=" + repr(out2))
        raise SystemExit("Goal4AG phase2 returned no completion marker")
    principal = grab(out2, "GOAL4AG_STRICT_IS_PRINCIPAL").lower() == "true"

if principal:
    # Phase 3 recompiles the same exact divisor/function and only then invokes
    # the surface-resolution API.  This keeps a resolution API/type regression
    # from being misreported as failure of IsPrincipal.
    phase3 = geometry + build + r'''
isp, f := IsPrincipal(D);
assert isp;
Srf := Surface(Pr6, eqns);
Drf := Divisor(Srf, f);
dsds := ResolveSingularSurface(Srf);
mults := Multiplicities(Srf, Drf);
assert #dsds eq #mults;
assert #dsds eq 48;
ambpts := [Pr6![x : x in Eltseq(q)] : q in pts];
got := [0 : j in [1..48]];
for j in [1..#dsds] do
    assert #mults[j] eq 1;
    qp := Points(SingularPoint(dsds[j]));
    assert #qp eq 1;
    q := Rep(qp);
    qa := Pr6![x : x in Eltseq(q)];
    k := Position(ambpts, qa);
    assert k ne 0;
    got[k] := Integers()!mults[j][1];
end for;
targetExceptional := __EXCEPTIONAL__;
printf "GOAL4AG_EXCEPTIONAL_MULTS=%o\n", got;
printf "GOAL4AG_EXCEPTIONAL_MATCH=%o\n", got eq targetExceptional;
printf "GOAL4AG_PHASE3_DONE\n";
'''.replace("__EXCEPTIONAL__", exceptional_literal)
    out3, attempt3 = run_magma(
        phase3, 240, "Stage35-EX Goal4AG A1 exceptional pullback phase",
        user_agent="perfect-cuboid-stage35ex/4ag-resolution",
    )
    if "GOAL4AG_PHASE3_DONE" not in out3:
        print("GOAL4AG_PHASE3_RAW=" + repr(out3))
        raise SystemExit("Goal4AG phase3 returned no completion marker")
    exceptional_match = grab(out3, "GOAL4AG_EXCEPTIONAL_MATCH").lower() == "true"
    mults48 = [int(x) for x in re.findall(r"-?\d+", grab(out3, "GOAL4AG_EXCEPTIONAL_MULTS"))]
    assert len(mults48) == 48
else:
    mults48 = None

out = {
    "schema": "STAGE35_EX_GOAL4AG_PRINCIPAL_DIVISOR_PREFLIGHT_DIAGNOSTIC_V2",
    "upstream_git_blob_sha1": source_blob,
    "source_fetch_attempt": source_attempt,
    "magma_attempts": [attempt1, attempt2, attempt3],
    "formal_target_support_count": 69,
    "strict_support_count": 33,
    "exceptional_support_count": 36,
    "strict_positive_hyperplane_degree": pos_hdeg,
    "strict_negative_hyperplane_degree": neg_hdeg,
    "strict_divisor_cartier_on_singular_surface": cartier,
    "strict_divisor_principal_on_singular_surface": principal,
    "resolved_exceptional_multiplicities_match_target": exceptional_match,
    "exceptional_multiplicities_48": mults48,
    "explicit_F_B_materialized": False,
    "full_Br_a_U_computed": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
print("GOAL4AG_DIAGNOSTIC_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
