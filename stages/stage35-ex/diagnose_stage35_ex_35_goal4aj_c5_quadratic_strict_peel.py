#!/usr/bin/env python3
"""Goal4AJ diagnostic: C5 quadratic strict-support peel preflight.

Test whether any of the four exact Goal4AC C5 quadratic sections can be a
factor of the live numerator degree-31 divisor or the post-Q-linear-peel
denominator degree-19 residual.  Only strict retained140 components are tested
here.  Goal4AC proves each quadratic section has exactly four C5 strict
components, so a quadratic can only divide a target if all four of its C5
components occur in that target.  Exceptional A1 valuations are deliberately
left to a follow-up only when strict support admits a candidate.

Diagnostic only: no quadratic factor, literal section, F_B, or E1 credit is
awarded by this preflight alone.
"""
from __future__ import annotations

import ast
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"
NUM_PARENT = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_reflexive_generator_gen2.py"
DEN_PARENT = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_reflexive_generator_gen3.py"
GOAL4AC = ROOT / "stages/stage35-ex/35ex-35/goal4ac-c5-individual-quadratic-residual.json"

ACTIVE_SHA = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
NUM_PARENT_BLOB = "a6c4a4f6e1db1817149c09d02d440d612e4549b2"
DEN_PARENT_BLOB = "6ffb4f5127a1a300c9e9e9827de4a8b0b2ae7409"
GOAL4AC_BLOB = "ef451544bce4aaafc14d24081e22ce997977a861"
STOLL_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def literal_assignments(path: Path) -> tuple[dict[int, str], dict[int, list[int]]]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    vals: dict[str, object] = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id in {"IDEALS", "GROUPS"}
        ):
            vals[node.targets[0].id] = ast.literal_eval(node.value)
    ideals = {int(k): str(v) for k, v in dict(vals["IDEALS"]).items()}
    groups = {int(k): [int(x) for x in v] for k, v in dict(vals["GROUPS"]).items()}
    return ideals, groups


assert git_blob(NUM_PARENT) == NUM_PARENT_BLOB
assert git_blob(DEN_PARENT) == DEN_PARENT_BLOB
assert git_blob(GOAL4AC) == GOAL4AC_BLOB

goal4ac = json.loads(GOAL4AC.read_text(encoding="utf-8"))
assert goal4ac["schema"] == "STAGE35_EX_35_GOAL4AC_C5_INDIVIDUAL_QUADRATIC_RESIDUAL_V1"
assert goal4ac["source_locks"]["upstream_stoll"]["git_blob_sha1"] == STOLL_BLOB
assert goal4ac["c5_source"]["distinct_quadratic_section_count"] == 4
assert goal4ac["individual_section_decomposition"]["c5_curves_per_distinct_quadratic_section"] == 4
assert goal4ac["individual_section_decomposition"]["higher_generic_multiplicity_present"] is False
assert goal4ac["individual_section_decomposition"]["individual_C5_quadratic_strict_residuals_exhausted"] is True

num_ideals, num_groups = literal_assignments(NUM_PARENT)
den_ideals, den_groups = literal_assignments(DEN_PARENT)
num_mult = {idx: m for m, ids in num_groups.items() for idx in ids}
den_mult = {idx: m for m, ids in den_groups.items() for idx in ids}
assert len(num_mult) == 27 and sum(num_mult.values()) == 202
assert len(den_mult) == 22 and sum(den_mult.values()) == 102

ap = subprocess.run(["python", "-B", str(ACTIVE)], text=True, capture_output=True, timeout=60)
assert ap.returncode == 0
aline = next(x for x in ap.stdout.splitlines() if x.startswith("GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON="))
active = json.loads(aline.split("=", 1)[1])
assert active["canonical_sha256"] == ACTIVE_SHA
assert {int(k): int(v) for k, v in active["numerator"]["strict_multiplicities_1based"].items()} == num_mult
assert {int(k): int(v) for k, v in active["denominator_residual"]["strict_multiplicities_1based"].items()} == den_mult

reps = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]
all_ideals = dict(num_ideals)
all_ideals.update(den_ideals)

parts = [r'''
option(redSB);
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
ideal P; ideal J; poly q;
''']
for e1, e2, e3 in reps:
    label = f"{e1},{e2},{e3}"
    parts.append(f"q=({e2})*a2*b1+({e3})*a3*b1+({e1})*ii*b2*b3;\n")
    for idx in sorted(all_ideals):
        parts.append(f"P={all_ideals[idx]}; J=std(surf+P); if(reduce(q,J)==0){{print(\"GOAL4AJ_C5_STRICT_HIT={label}:{idx}\");}}\n")
parts.append('print("GOAL4AJ_C5_STRICT_MEMBERSHIP=PASS"); quit;\n')

with tempfile.TemporaryDirectory() as td:
    p = Path(td) / "goal4aj-c5-strict-peel.sing"
    p.write_text("".join(parts), encoding="utf-8")
    cp = subprocess.run(["Singular", "-q", str(p)], text=True, capture_output=True, timeout=120)

stdout = cp.stdout
error_text = any(s in stdout.lower() for s in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
if cp.returncode != 0 or error_text or "GOAL4AJ_C5_STRICT_MEMBERSHIP=PASS" not in stdout.splitlines():
    if cp.stderr:
        print("GOAL4AJ_C5_STRICT_STDERR=" + json.dumps(cp.stderr[-12000:]))
    raise SystemExit("Goal4AJ C5 strict-support membership failed closed")

hits = {str(rep): [] for rep in reps}
for line in stdout.splitlines():
    if not line.startswith("GOAL4AJ_C5_STRICT_HIT="):
        continue
    payload = line.split("=", 1)[1]
    triple, idx = payload.rsplit(":", 1)
    key = str(tuple(int(x) for x in triple.split(",")))
    hits[key].append(int(idx))

for key in hits:
    hits[key] = sorted(set(hits[key]))
    if len(hits[key]) > 4:
        raise SystemExit(f"Goal4AC four-component support regression at {key}: {hits[key]}")


def lane(mult: dict[int, int]) -> dict:
    per = {}
    total_degree_upper = 0
    for rep in reps:
        key = str(rep)
        hs = [i for i in hits[key] if i in mult]
        # Goal4AC proves the complete strict support has exactly four C5 curves.
        # Therefore all four must be present in this target before Q can divide it.
        peel = min((mult[i] for i in hs), default=0) if len(hs) == 4 else 0
        per[key] = {
            "active_c5_component_indices_1based": hs,
            "active_c5_component_count": len(hs),
            "all_four_goal4ac_components_present": len(hs) == 4,
            "strict_support_quadratic_peel_multiplicity_upper_bound": peel,
            "exceptional_a1_valuation_checked": False,
            "full_divisor_quadratic_factor_proved": False,
        }
        total_degree_upper += 2 * peel
    return {
        "quadratic_sections": per,
        "strict_support_total_quadratic_degree_peel_upper_bound": total_degree_upper,
        "any_strict_support_quadratic_candidate": any(v["strict_support_quadratic_peel_multiplicity_upper_bound"] > 0 for v in per.values()),
    }

out = {
    "schema": "STAGE35_EX_GOAL4AJ_C5_QUADRATIC_STRICT_SUPPORT_PEEL_DIAGNOSTIC_V1",
    "source_locks": {
        "active_divisor_condition_packet_canonical_sha256": ACTIVE_SHA,
        "numerator_parent_blob_sha1": NUM_PARENT_BLOB,
        "denominator_parent_blob_sha1": DEN_PARENT_BLOB,
        "goal4ac_artifact_blob_sha1": GOAL4AC_BLOB,
        "testa_stoll_cuboids_magma_blob_sha1": STOLL_BLOB,
    },
    "goal4ac_exact_fact": "each of four scalar classes Q(1,e2,e3) has exactly four C5 strict components, with no extra strict component or higher generic multiplicity",
    "quadratic_representatives": [list(x) for x in reps],
    "membership_test": "reduce(Q, std(surface + retained_strict_prime)) == 0 over Q(i,sqrt2)",
    "numerator": lane(num_mult),
    "denominator_residual": lane(den_mult),
    "exceptional_a1_valuation_checked": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_C5_STRICT_PEEL_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_C5_STRICT_PEEL=PASS")
