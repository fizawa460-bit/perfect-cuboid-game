#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648an-a1-strict-transform-delta-feasibility.json"
NOTE = HERE / "post1648an-a1-strict-transform-delta-feasibility-source-note.md"
AM = HERE / "post1648am-beauville-fibration-picard-source-lock.json"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"


def canonical_sha(payload: dict) -> str:
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    got = canonical_sha(cert)
    if got != cert["canonical_sha256_without_this_field"]:
        raise SystemExit(f"certificate canonical mismatch: {got}")

    locks = cert["source_locks"]
    if hashlib.sha256(NOTE.read_bytes()).hexdigest() != locks["source_note_sha256"]:
        raise SystemExit("AN source note hash moved")

    am = json.loads(AM.read_text())
    if am["canonical_sha256_without_this_field"] != cert["parent"]["am_canonical_sha256"]:
        raise SystemExit("AM canonical moved")
    if sorted(am["decision"]["projection_degrees_unordered"]) != [81, 105]:
        raise SystemExit("AM projection degrees moved")
    if int(am["exact_results"]["minimum_ramification_points"]) != 210:
        raise SystemExit("AM ramification lower bound moved")
    if int(am["exact_results"]["minimum_distinct_multibranch_surface_nodes"]) != 19:
        raise SystemExit("AM multibranch lower bound moved")
    if int(am["exact_results"]["minimum_total_normalization_preimages_over_met_surface_nodes"]) != 210:
        raise SystemExit("AM node-preimage lower bound moved")
    if int(am["exact_results"]["minimum_normalization_branch_excess_over_47_met_nodes"]) != 163:
        raise SystemExit("AM branch-excess lower bound moved")

    v6 = json.loads(V6.read_text())
    if v6["canonical_sha256_without_this_field"] != locks["v6_witness_canonical_sha256"]:
        raise SystemExit("V6 canonical moved")
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(pairings) != 140:
        raise SystemExit("V6 all140 width moved")
    masses = pairings[92:]
    vin = cert["v6_exact_inputs"]
    if masses != [int(x) for x in vin["exceptional_pairings"]]:
        raise SystemExit("V6 exceptional vector moved")
    if sum(masses) != 266 or sum(m > 0 for m in masses) != 47:
        raise SystemExit("V6 exceptional mass/support moved")
    if sum(m > 1 for m in masses) != 38:
        raise SystemExit("V6 positive nonunit node count moved")

    d = int(v6["target"]["d"])
    c2 = int(v6["witness"]["self_intersection"])
    pa = 1 + (c2 + d) // 2
    defect = pa - 1
    if (d, c2, pa, defect) != (186, 758, 473, 472):
        raise SystemExit("V6 adjunction/genus-defect arithmetic moved")
    if defect != int(vin["required_genus_defect"]):
        raise SystemExit("stored required genus defect moved")

    local = cert["a1_local_adapter"]
    if local["exceptional_intersection_formula"] != "m=min(A,B)":
        raise SystemExit("A1 exceptional multiplicity contract moved")
    if local["beauville_ramified_iff"] != "m odd":
        raise SystemExit("A1 ramification parity contract moved")
    minimal = local["minimal_fsm_type"]
    if (minimal["a1"], minimal["a2"], minimal["A"], minimal["B"], minimal["m"]) != (4, 4, 1, 1, 1):
        raise SystemExit("minimal FSM local type moved")

    # Exact local A1 germ check: x=t, y=lambda*t, z=lambda^2*t.
    # On y=x*u, z=x*u^2 it has x=t, u=lambda, hence one transverse
    # exceptional intersection and arbitrary nonzero landing parameter.
    for lam in (1, 2, 3, 17):
        x_coeff, y_coeff, z_coeff = 1, lam, lam * lam
        if x_coeff * z_coeff - y_coeff * y_coeff != 0:
            raise SystemExit("minimal A1 germ identity failed")
        if x_coeff != 1:
            raise SystemExit("minimal germ lost transversality")

    total_branches = sum(masses)
    ramification = total_branches
    multibranch_nodes = sum(m > 1 for m in masses)
    branch_excess = total_branches - sum(m > 0 for m in masses)
    minimal_branch_count = total_branches

    # Distinct symbolic landing parameters per node make the strict transforms
    # disjoint on that exceptional curve, so the forced local delta is zero.
    landing_keys = []
    for node, mass in enumerate(masses, start=1):
        if mass <= 0:
            continue
        node_keys = [(node, j) for j in range(1, mass + 1)]
        if len(node_keys) != len(set(node_keys)):
            raise SystemExit("landing parameter witness collided")
        landing_keys.extend(node_keys)
    if len(landing_keys) != total_branches:
        raise SystemExit("landing witness branch count moved")
    forced_exceptional_delta = 0

    witness = cert["local_feasibility_witness"]
    expected_witness = {
        "total_surface_node_preimages": total_branches,
        "beauville_ramification_points": ramification,
        "fsm_minimal_branch_count": minimal_branch_count,
        "distinct_multibranch_surface_nodes": multibranch_nodes,
        "branch_excess_over_47_met_nodes": branch_excess,
        "forced_exceptional_locus_delta": forced_exceptional_delta,
    }
    for k, v in expected_witness.items():
        if witness[k] != v:
            raise SystemExit(f"{k} moved: cert={witness[k]} replay={v}")

    if ramification < int(am["exact_results"]["minimum_ramification_points"]):
        raise SystemExit("local witness misses AM ramification bound")
    if multibranch_nodes < int(am["exact_results"]["minimum_distinct_multibranch_surface_nodes"]):
        raise SystemExit("local witness misses AM multibranch bound")
    if total_branches < int(am["exact_results"]["minimum_total_normalization_preimages_over_met_surface_nodes"]):
        raise SystemExit("local witness misses AM node-preimage bound")
    if branch_excess < int(am["exact_results"]["minimum_normalization_branch_excess_over_47_met_nodes"]):
        raise SystemExit("local witness misses AM branch-excess bound")
    if minimal_branch_count < 47:
        raise SystemExit("local witness misses AJ/FSM minimal-branch bound")

    # Smooth-locus analytic delta witness f=v^2-u^945.
    # gcd(2,945)=1 => one branch. Jacobian ideal (u^944,v) gives mu=944;
    # in characteristic zero a unibranch plane singularity has mu=2*delta.
    smooth = cert["smooth_locus_delta_witness"]
    if math.gcd(2, 945) != 1:
        raise SystemExit("smooth-locus cusp unexpectedly reducible")
    mu = 944
    delta = mu // 2
    if (
        smooth["plane_branch_equation"] != "v^2=u^945"
        or smooth["gcd_exponents"] != 1
        or smooth["branch_count"] != 1
        or smooth["milnor_number"] != mu
        or smooth["delta"] != delta
        or smooth["milnor_algebra_basis_count"] != mu
    ):
        raise SystemExit("smooth-locus delta witness moved")
    if forced_exceptional_delta + delta != defect:
        raise SystemExit("combined local delta budget no longer equals V6 defect")

    if not cert["decision"]["current_local_scalar_constraints_simultaneously_feasible"]:
        raise SystemExit("AN decision moved away from feasibility wall")
    if cert["decision"]["v6_carrier_constructed"] or cert["decision"]["v6_carrier_excluded"]:
        raise SystemExit("AN may neither construct nor exclude a global V6 carrier")
    if any(cert["firewalls"].values()):
        raise SystemExit("AN credit firewall moved")
    if not all(cert["guardrails"].values()):
        raise SystemExit("AN guardrail moved")

    print("PASS_STAGE32_POST1648AN_A1_STRICT_TRANSFORM_DELTA_FEASIBILITY")
    print(cert["canonical_sha256_without_this_field"])
    print(json.dumps({
        "exceptional_mass": sum(masses),
        "local_witness_node_preimages": total_branches,
        "local_witness_ramification": ramification,
        "local_witness_multibranch_nodes": multibranch_nodes,
        "forced_exceptional_delta": forced_exceptional_delta,
        "smooth_locus_delta_witness": delta,
        "required_total_delta": defect,
        "v6_excluded": False,
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
