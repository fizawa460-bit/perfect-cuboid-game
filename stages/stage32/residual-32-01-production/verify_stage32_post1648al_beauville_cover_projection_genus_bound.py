#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648al-beauville-cover-projection-genus-bound.json"
NOTE = HERE / "post1648al-beauville-cover-projection-genus-bound-source-note.md"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
AJ = HERE / "post1648aj-v6-multibranch-node-fiber-lower-bounds.json"


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

    note_sha = hashlib.sha256(NOTE.read_bytes()).hexdigest()
    if note_sha != cert["source_locks"]["source_note_sha256"]:
        raise SystemExit(f"source note sha moved: {note_sha}")

    v6 = json.loads(V6.read_text())
    if v6["canonical_sha256_without_this_field"] != cert["source_locks"]["v6_witness_canonical_sha256"]:
        raise SystemExit("V6 witness canonical moved")
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(pairings) != 140:
        raise SystemExit("V6 all140 width moved")
    masses = pairings[92:]
    d = int(v6["target"]["d"])
    e = sum(masses)
    support = sum(m > 0 for m in masses)

    inp = cert["source_locked_inputs"]
    if (d, e, support) != (inp["v6_degree"], inp["v6_exceptional_mass"], inp["v6_positive_exceptional_support"]):
        raise SystemExit("V6 exact data moved")

    aj = json.loads(AJ.read_text())
    if aj["canonical_sha256_without_this_field"] != cert["parent"]["aj_canonical"]:
        raise SystemExit("AJ canonical moved")
    required_minimal = int(aj["fsm_minimal_branch_budget"]["minimal_branch_count_required"])
    if required_minimal != inp["aj_required_minimal_branches"]:
        raise SystemExit("AJ minimal-branch requirement moved")

    g_c8 = int(inp["C8_genus"])
    h_order = int(inp["H_order"])
    numerator = 2 * g_c8 - 2
    if numerator % h_order:
        raise SystemExit("free quotient genus is not integral")
    two_g_y_minus_2 = numerator // h_order
    if two_g_y_minus_2 % 2:
        raise SystemExit("quotient genus parity moved")
    g_y = (two_g_y_minus_2 + 2) // 2
    if g_y != cert["proof_adapter"]["factor_quotient_genus_Y"]:
        raise SystemExit("factor quotient genus moved")
    if g_y != 2:
        raise SystemExit("AL requires genus-two factor quotient")

    projection_sum = d
    min_max_projection = (projection_sum + 1) // 2
    min_r = 2 * min_max_projection
    max_r = e
    if min_r > max_r:
        raise SystemExit("Beauville adapter would already exclude V6; certificate is stale")

    if 2 * d <= max_r:
        raise SystemExit("constant-projection exclusion moved")

    max_each = max_r // 2
    min_each = projection_sum - max_each
    lift_genus_min = 1 + min_r // 2
    lift_genus_max = 1 + max_r // 2

    baseline_odd = sum(m & 1 for m in masses)
    increments = sorted((m - (m & 1) for m in masses if m > 1), reverse=True)

    cumulative = baseline_odd
    min_multibranch = 0
    for inc in increments:
        if cumulative >= min_r:
            break
        cumulative += inc
        min_multibranch += 1
    if cumulative < min_r:
        raise SystemExit("ramification capacity cannot reach AL lower bound")

    top14 = sum(increments[:14])
    top15 = sum(increments[:15])
    cap14 = baseline_odd + top14
    cap15 = baseline_odd + top15

    exp = cert["exact_results"]
    expected = {
        "projection_degree_sum": projection_sum,
        "minimum_max_projection_degree": min_max_projection,
        "minimum_ramification_points": min_r,
        "maximum_ramification_points_from_exceptional_mass": max_r,
        "lift_genus_minimum": lift_genus_min,
        "lift_genus_maximum": lift_genus_max,
        "projection_degree_minimum_each": min_each,
        "projection_degree_maximum_each": max_each,
        "minimum_total_normalization_preimages_over_met_surface_nodes": min_r,
        "minimum_normalization_branch_excess_over_47_met_nodes": min_r - support,
        "odd_mass_unibranch_ramification_capacity": baseline_odd,
        "largest_14_multibranch_capacity_increment_sum": top14,
        "ramification_capacity_with_at_most_14_multibranch_nodes": cap14,
        "largest_15_multibranch_capacity_increment_sum": top15,
        "ramification_capacity_with_15_multibranch_nodes": cap15,
        "minimum_distinct_multibranch_surface_nodes": min_multibranch,
    }
    for key, value in expected.items():
        if exp[key] != value:
            raise SystemExit(f"{key} moved: cert={exp[key]} replay={value}")

    if not (cap14 < min_r <= cap15 and min_multibranch == 15):
        raise SystemExit("parity-refined multibranch threshold moved")
    if exp["minimum_total_normalization_preimages_over_met_surface_nodes"] <= 72:
        raise SystemExit("AL failed to strengthen AJ preimage bound")
    if exp["minimum_distinct_multibranch_surface_nodes"] <= 3:
        raise SystemExit("AL failed to strengthen AJ multibranch-node bound")

    if any(cert["firewalls"].values()):
        raise SystemExit("AL firewall moved")

    print("PASS_STAGE32_POST1648AL_BEAUVILLE_COVER_PROJECTION_GENUS_BOUND")
    print(cert["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
